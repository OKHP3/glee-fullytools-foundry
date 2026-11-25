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

    def test_workflow_packages_include_only_declared_knowledge_and_keep_native_identity(self):
        self.product["workflowRelease"] = {"skillVersion": "0.1.0", "version": "1.0.0"}
        relative = "references/worksheet.md"
        worksheet = self.skill.parent / relative
        worksheet.parent.mkdir()
        worksheet.write_bytes(b"field,quantity\r\n")
        source = self.license.parent / "vocabulary.csv"
        source.write_bytes(b"industry,term\n")
        fixture = self.directory / "evals/skill-v0.1.0.json"
        fixture.parent.mkdir()
        config = {"skill": "fixture", "version": "0.1.0", "knowledgeSources": ["vocabulary.csv"],
                  "skillKnowledgeSources": [relative]}
        fixture.write_text(json.dumps(config), encoding="utf-8")
        _, archive = PACK.package(self.root, self.product)
        with zipfile.ZipFile(io.BytesIO(archive)) as built:
            self.assertEqual(built.read("skills/fixture/" + relative), b"field,quantity\n")
            self.assertEqual(built.read("skills/fixture/references/workflow/vocabulary.csv"), source.read_bytes())
        manifest = {"name": "original-host-id", "version": "0.4.2"}
        lookup = "skills/instructions/lookup/knowledge-index.json"
        original = {"plugin.json": json.dumps(manifest), ".codex-plugin/plugin.json": json.dumps(manifest),
                    lookup: json.dumps({"files": [{"name": "suite.md", "path": "references/suite.md"}]})}
        native = PACK.workflow_overlay(self.root, self.product, original, "Existing handoff directory.")
        self.assertEqual(json.loads(native["plugin.json"]), {"name": "original-host-id", "version": "1.0.0"})
        self.assertEqual(len(json.loads(native[lookup])["files"]), 3)
        self.assertIn(b"Existing handoff directory.", native["skills/instructions/SKILL.md"])
        config["knowledgeSources"] = ["../product.json"]
        fixture.write_text(json.dumps(config), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "path"):
            PACK.package(self.root, self.product)

    def test_collision_never_replaces_existing_file(self):
        target = self.root / "sample.zip"
        PACK.write_new(target, b"first")
        PACK.write_new(target, b"first")
        with self.assertRaisesRegex(ValueError, "differs"):
            PACK.write_new(target, b"second")
        self.assertEqual(target.read_bytes(), b"first")
        self.assertFalse(list(self.root.glob(".plugin-*")))

    def make_former_gpt_fixture(self):
        directory = self.directory / "plugin"
        icon = "./assets/gpt-icon.png"
        native = {"name": "fixture", "version": "1.0.0", "description": "Fixture",
                  "author": {"name": "Example"}, "extensions": {"com.openai": {"interface": {
                      "displayName": "Fixture", "capabilities": ["skills"], "logo": icon, "composerIcon": icon}}}}
        files = {"plugin.json": json.dumps(native).encode(), "assets/gpt-icon.png": b"image",
                 "skills/instructions/agents/openai.yaml": b"interface: {}\n",
                 "skills/instructions/SKILL.md": b"---\nname: instructions\n---\nUse the template.\n"}
        records = []
        for path, data in files.items():
            (directory / path).parent.mkdir(parents=True, exist_ok=True)
            (directory / path).write_bytes(data)
            records.append({"path": path, "sha256": hashlib.sha256(data).hexdigest()})
        source = self.directory / "source/resources.zip"
        with zipfile.ZipFile(source, "w") as bundle:
            bundle.writestr("original/template.csv", b"title\r\n")
        knowledge = "skills/instructions/references/template.csv"
        records.append({"path": knowledge, "source": source.relative_to(self.root).as_posix(),
                        "member": "original/template.csv", "sha256": hashlib.sha256(b"title\n").hexdigest()})
        receipt = {"formatVersion": 1, "packageId": "fixture", "sourceVersion": "1.0.0", "files": records}
        (directory / "release.json").write_text(json.dumps(receipt), encoding="utf-8")
        starters = b'{ "starters": ["First", "Second", "Third", "Fourth"] }\n'
        (directory / "builder-starters.json").write_bytes(starters)
        product = PACK.former_gpt_registry(self.root)["fixture"]
        return product, source, knowledge, native, receipt, starters

    def test_native_release_uses_pinned_archive_member_and_regenerates_lookup(self):
        product, source, knowledge, native, receipt, starters = self.make_former_gpt_fixture()
        name, result = PACK.former_gpt_package(self.root, product)
        self.assertEqual(name, "fixture-former-gpt-1.0.0.zip")
        self.assertEqual((name, result), PACK.former_gpt_package(self.root, product))
        with zipfile.ZipFile(io.BytesIO(result)) as built:
            self.assertEqual(built.read(knowledge), b"title\n")
            lookup = json.loads(built.read("skills/instructions/lookup/knowledge-index.json"))
            self.assertEqual(lookup["files"], [{"name": "template.csv", "path": "references/template.csv"}])
            self.assertEqual(json.loads(built.read(".codex-plugin/plugin.json"))["interface"],
                             native["extensions"]["com.openai"]["interface"])
            self.assertEqual(json.loads(built.read("foundry-release.json")), receipt)
            self.assertEqual(built.read("foundry/builder-starters.json"), starters)
        with zipfile.ZipFile(source, "w") as bundle:
            bundle.writestr("original/template.csv", b"different data")
        with self.assertRaisesRegex(ValueError, "digest"):
            PACK.former_gpt_package(self.root, product)

    def make_workflow_fixture(self):
        self.make_former_gpt_fixture()
        registry = self.root / "products"
        sources = registry / "workflow-package-sources"
        sources.mkdir(parents=True)
        (registry / "migration-map.json").write_text(json.dumps({"products": [self.product]}), encoding="utf-8")
        row = {"productId": "fixture", "route": self.product["destination"],
               "privateHostedVersion": "1.0.2+bundle.abc", "result": "pass", "knowledge": {"indexedResources": 2}}
        report = registry / "remaining-workflow-acceptance.json"
        report.write_text(json.dumps({"products": [row]}), encoding="utf-8")
        (sources / "instructions.json").write_text(json.dumps({"fixture": [
            {"before": "Use the template.", "after": "Complete the revised template."}]}), encoding="utf-8")
        for name in ("replacement.csv", "new.md"):
            (sources / name).write_bytes(b"Reviewed public contents.\r\n")
        refs = {PACK.REFERENCE_PREFIX + "template.csv": "products/workflow-package-sources/replacement.csv",
                PACK.REFERENCE_PREFIX + "new.md": "products/workflow-package-sources/new.md"}
        (sources / "knowledge.json").write_text(json.dumps({"fixture": refs}), encoding="utf-8")
        return PACK.workflow_registry(self.root)["fixture"]

    def test_accepted_workflow_retains_native_files_and_applies_reviewed_public_edits(self):
        product = self.make_workflow_fixture()
        name, result = PACK.workflow_package(self.root, product)
        self.assertEqual(name, "fixture-workflow-1.0.2+bundle.abc.zip")
        self.assertEqual((name, result), PACK.workflow_package(self.root, product))
        with zipfile.ZipFile(io.BytesIO(result)) as built:
            self.assertIsNone(built.testzip())
            for path in ("plugin.json", ".codex-plugin/plugin.json"):
                self.assertEqual(json.loads(built.read(path))["version"], "1.0.2+bundle.abc")
            self.assertIn(b"Complete the revised template.", built.read("skills/instructions/SKILL.md"))
            self.assertEqual(built.read("LICENSE"), self.canonical_license)
            lookup = json.loads(built.read("skills/instructions/lookup/knowledge-index.json"))
            self.assertEqual(lookup["files"], [{"name": "template.csv", "path": "references/template.csv"},
                                              {"name": "new.md", "path": "references/new.md"}])
            for item in lookup["files"]:
                self.assertEqual(built.read("skills/instructions/" + item["path"]), b"Reviewed public contents.\n")
            self.assertEqual(len(json.loads(built.read("foundry/builder-starters.json"))["starters"]), 4)
            receipt = json.loads(built.read("foundry-release.json"))
            self.assertEqual(receipt["historicalSourceEdition"], "1.0.0")
            self.assertEqual({r["path"]: r["sha256"] for r in receipt["files"]},
                             {p: hashlib.sha256(built.read(p)).hexdigest()
                              for p in built.namelist() if p != "foundry-release.json"})

    def test_accepted_workflow_requires_correct_route_unique_anchor_and_reviewed_source(self):
        product = self.make_workflow_fixture()
        for before in ("Absent", "e"):
            with self.subTest(before=before), self.assertRaisesRegex(ValueError, "unique anchor"):
                PACK.workflow_package(self.root, dict(product, instructionEdits=[{"before": before, "after": ""}]))
        private_link = {"before": "Use the template.", "after": "Open https://chatgpt.com/c/fixture"}
        with self.assertRaisesRegex(ValueError, "destination in public instructions"):
            PACK.workflow_package(self.root, dict(product, instructionEdits=[private_link]))
        for target, source in ((PACK.REFERENCE_PREFIX + "new.md", ".git/config"),
                               ("skills/instructions/SKILL.md", "products/workflow-package-sources/new.md")):
            with self.subTest(target=target), self.assertRaisesRegex(ValueError, "knowledge override"):
                PACK.workflow_package(self.root, dict(product, knowledgeFiles={target: source}))
        report = self.root / "products/remaining-workflow-acceptance.json"
        rows = json.loads(report.read_text(encoding="utf-8"))
        rows["products"][0]["route"] = "capabilities/other"
        report.write_text(json.dumps(rows), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "accepted workflow"):
            PACK.workflow_registry(self.root)

    def test_hosted_only_workflow_preserves_historical_skill_and_owner_license(self):
        product = self.make_workflow_fixture()
        (self.root / "LICENSE.md").write_bytes(b"Original owner license.\r\n")
        empty = dict(product, instructionEdits=[], knowledgeFiles={}, indexedResources=1, repositorySource=False)
        _, result = PACK.workflow_package(self.root, empty)
        with zipfile.ZipFile(io.BytesIO(result)) as built:
            self.assertEqual(built.read("LICENSE"), b"Original owner license.\n")
            self.assertEqual(built.read("skills/instructions/SKILL.md"),
                             (self.directory / "plugin/skills/instructions/SKILL.md").read_bytes())

    def test_accepted_workflow_requires_knowledge_map_accepted_count_and_complete_index(self):
        product = self.make_workflow_fixture()
        with self.assertRaisesRegex(ValueError, "count or index membership"):
            PACK.workflow_package(self.root, dict(product, knowledgeFiles={}))
        index = "skills/instructions/lookup/knowledge-index.json"
        record = {"name": "missing.md", "path": "references/missing.md"}
        content = {index: json.dumps({"files": [record]}), PACK.REFERENCE_PREFIX + "other.md": b"Other"}
        with self.assertRaisesRegex(ValueError, "count or index membership"):
            PACK.accepted_knowledge(self.root, dict(product, indexedResources=1, knowledgeFiles={}), content)
        (self.root / "products/workflow-package-sources/knowledge.json").unlink()
        with self.assertRaises(FileNotFoundError):
            PACK.workflow_registry(self.root)
