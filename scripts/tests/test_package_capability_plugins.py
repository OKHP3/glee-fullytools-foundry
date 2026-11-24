import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile


SCRIPT = Path(__file__).resolve().parents[1] / "package-capability-plugins.py"
SPEC = importlib.util.spec_from_file_location("package_capability_plugins", SCRIPT)
PACK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACK)


class PluginPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.product = {"productId": "fixture", "displayName": "A Fixture",
                        "destination": "capabilities/family/fixture"}
        self.directory = self.root / self.product["destination"]
        self.skill = self.directory / "skills/fixture/SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.skill.write_bytes(b'---\nname: fixture\ndescription: >-\n  A portable\n  example.\n'
                              b'license: MIT\nmetadata:\n  version: "0.1.0"\n---\n\n# Fixture\n')
        self.license = self.directory / "source/LICENSE"
        self.license.parent.mkdir()
        license_text = (PACK.ROOT / "capabilities/tasty-tracker/source/LICENSE").read_bytes()
        self.canonical_license = license_text.replace(b"\r\n", b"\n")
        self.license.write_bytes(self.canonical_license.replace(b"\n", b"\r\n"))
        record = {"path": "LICENSE", "sha256": hashlib.sha256(self.canonical_license).hexdigest()}
        (self.directory / "product.json").write_text(
            json.dumps({"sourceLicense": "MIT", "files": [record]}), encoding="utf-8")

    def test_roundtrip_reproducibility_manifest_and_exact_files(self):
        name, first = PACK.package(self.root, self.product)
        self.skill.write_bytes(self.skill.read_bytes().replace(b"\n", b"\r\n"))
        self.assertEqual((name, first), PACK.package(self.root, self.product))
        self.assertEqual(name, "fixture-0.1.0.zip")
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), {
                "skills/fixture/SKILL.md", ".codex-plugin/plugin.json", "LICENSE"})
            manifest = json.loads(archive.read(".codex-plugin/plugin.json"))
            self.assertEqual(manifest["skills"], "./skills/")
            self.assertEqual(manifest["interface"]["displayName"], "A Fixture")
            self.assertEqual(manifest["description"], "A portable example.")
            self.assertEqual(archive.read("LICENSE"), self.canonical_license)
            self.assertEqual(archive.read("skills/fixture/SKILL.md"),
                             self.skill.read_bytes().replace(b"\r\n", b"\n"))

    def test_rejects_traversal_and_duplicate_register_id(self):
        register = self.root / "products/migration-map.json"
        register.parent.mkdir()
        for entries in ([dict(self.product, destination="capabilities/../fixture")],
                        [self.product, self.product]):
            with self.subTest(entries=entries):
                register.write_text(json.dumps({"products": entries}), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "route"):
                    PACK.registry(self.root)

    def test_changed_license_and_extra_runtime_file_require_review(self):
        self.license.write_bytes(self.canonical_license + b"Additional conditions\n")
        with self.assertRaisesRegex(ValueError, "License"):
            PACK.package(self.root, self.product)
        self.license.write_bytes(self.canonical_license)
        (self.skill.parent / "helper.py").write_text("pass\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "additional runtime"):
            PACK.package(self.root, self.product)

    def test_collision_never_replaces_existing_file(self):
        target = self.root / "sample.zip"
        PACK.write_new(target, b"first")
        PACK.write_new(target, b"first")
        with self.assertRaisesRegex(ValueError, "differs"):
            PACK.write_new(target, b"second")
        self.assertEqual(target.read_bytes(), b"first")
        self.assertFalse(list(self.root.glob(".plugin-*")))
