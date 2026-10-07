"""Regression contracts for the skills-first transition and historical backups."""
import json
import unittest
import zipfile
from io import BytesIO

from app.tests import test_server
from app.server import PORTABILITY_FIELDS


class PortableCapabilityTests(unittest.TestCase):
    setUp = test_server.ServiceTests.setUp
    tearDown = test_server.ServiceTests.tearDown
    request = test_server.ServiceTests.request
    project = test_server.ServiceTests.project
    create = test_server.ServiceTests.create

    def derive(self, source, kind):
        status, _, draft = self.request("POST", f"/api/projects/{source['id']}/derive",
                                        {"revision": source["revision"], "targetKind": kind})
        self.assertEqual(status, 201, draft)
        return draft

    def test_derivation_preserves_source_and_invalidates_all_evidence(self):
        source = self.create(kind="custom-gpt", tests=[{
            "id": "source-pass", "name": "Original", "expected": "Original outcome",
            "actual": "Original GPT observation", "status": "pass"}])
        skill = self.derive(source, "agent-skill")
        plugin = self.derive(skill, "plugin")
        connector = self.derive(skill, "connector")
        self.assertEqual(len({p["id"] for p in [source, skill, plugin, connector]}), 4)
        self.assertEqual(self.server.store.get(source["id"]), source)
        self.assertEqual(self.server.store.get(skill["id"]), skill)
        self.assertIn(source["id"], skill["sourceProvenance"])
        self.assertIn("revision 1", skill["sourceProvenance"])
        self.assertEqual(skill["instructions"], source["instructions"])
        self.assertEqual(len(skill["tests"]), 4)
        for draft in [skill, plugin, connector]:
            self.assertTrue(all(t["status"] == "not-run" and t["actual"] == "" for t in draft["tests"]))
            self.assertEqual(draft["revision"], 1)
            self.assertFalse(self.request("GET", f"/api/projects/{draft['id']}/validation")[2]["readyForReview"])
        self.assertEqual(self.server.store.history(skill["id"])[0]["action"], "derived")
        payload = {k: v for k, v in skill.items() if k not in {"id", "schemaVersion", "createdAt", "updatedAt"}}
        payload["sourceProvenance"] = ""
        self.assertEqual(self.request("PUT", f"/api/projects/{skill['id']}", payload)[0], 200)
        checks = self.request("GET", f"/api/projects/{skill['id']}/validation")[2]["checks"]
        self.assertEqual(next(c for c in checks if c["id"] == "sourceProvenance")["status"], "fail")

    def test_bad_route_stale_revision_and_bad_body_do_not_create_records(self):
        source = self.create(kind="custom-gpt")
        for body, expected in [
            ({"revision": 1, "targetKind": "plugin"}, 400),
            ({"revision": 2, "targetKind": "agent-skill"}, 409),
            ({"revision": True, "targetKind": "agent-skill"}, 400),
            ({"revision": 1, "targetKind": []}, 400),
            ({"revision": 1, "targetKind": "agent-skill", "extra": 1}, 400),
        ]:
            self.assertEqual(self.request("POST", f"/api/projects/{source['id']}/derive", body)[0], expected)
        self.assertEqual(len(self.server.store.list()), 1)
        self.assertEqual(self.server.store.get(source["id"]), source)

    def test_portability_edits_reset_passes_and_survive_backup_restore(self):
        item = self.create(kind="plugin", **{key: "Recorded contract" for key in PORTABILITY_FIELDS},
                           tests=[{"id": "case", "name": "Check", "expected": "Works", "actual": "Observed", "status": "pass"}])
        for field in sorted(PORTABILITY_FIELDS):
            # Re-establish a pass without changing the contract before each edit.
            payload = {k: v for k, v in item.items() if k not in {"id", "schemaVersion", "createdAt", "updatedAt"}}
            payload["tests"][0].update(status="pass", actual="Observed after contract review")
            code, _, item = self.request("PUT", f"/api/projects/{item['id']}", payload)
            self.assertEqual(code, 200)
            payload["revision"] = item["revision"]
            payload[field] = "Changed contract <script>"
            code, _, item = self.request("PUT", f"/api/projects/{item['id']}", payload)
            self.assertEqual(code, 200)
            self.assertEqual(item["tests"][0]["status"], "not-run", field)
        backup = self.request("GET", "/api/workspace/backup")[2]
        status, _, result = self.request("POST", "/api/workspace/restore", {"backup": backup, "confirm": True, "mode": "replace"})
        self.assertEqual(status, 200, result)
        self.assertEqual(self.server.store.get(item["id"]), item)
        self.assertTrue(all(h["restorable"] for h in self.server.store.history(item["id"])))

    def test_pre_transition_snapshot_bytes_remain_valid(self):
        source = self.create(kind="custom-gpt")
        self.assertTrue(PORTABILITY_FIELDS.isdisjoint(source))
        before = self.request("GET", "/api/workspace/backup")[2]
        status, _, result = self.request("POST", "/api/workspace/restore", {"backup": before, "confirm": True, "mode": "replace"})
        self.assertEqual(status, 200, result)
        after = self.request("GET", "/api/workspace/backup")[2]
        self.assertEqual(before["snapshots"], after["snapshots"])
        self.assertEqual(before["projects"], after["projects"])
        self.derive(self.server.store.get(source["id"]), "agent-skill")

    def test_adapter_packages_are_explicitly_non_installable_and_escape_html(self):
        hostile = '<img src=x onerror="alert(1)">'
        for kind in ["plugin", "connector"]:
            item = self.create(kind=kind, **{key: hostile for key in PORTABILITY_FIELDS})
            status, _, raw = self.request("GET", f"/api/projects/{item['id']}/export?format=zip")
            self.assertEqual(status, 200)
            with zipfile.ZipFile(BytesIO(raw)) as bundle:
                blueprint = json.loads(bundle.read("adapter-blueprint.json"))
                self.assertFalse(blueprint["installable"])
                self.assertEqual(blueprint["compatibilityStatus"], "not-verified-by-foundry")
                self.assertEqual(blueprint["integrationContract"], hostile)
                self.assertEqual(blueprint["kind"], kind)
                for name in bundle.namelist():
                    if name.endswith(".md"):
                        self.assertNotIn(hostile, bundle.read(name).decode())
                self.assertNotIn(".codex-plugin/plugin.json", bundle.namelist())
                self.assertEqual(set(json.loads(bundle.read("manifest.json"))["files"]), set(bundle.namelist()) - {"manifest.json"})

    def test_blueprint_review_checks_require_conversion_and_integration_contracts(self):
        item = self.create(kind="connector")
        checks = self.request("GET", f"/api/projects/{item['id']}/validation")[2]["checks"]
        for key in PORTABILITY_FIELDS:
            self.assertEqual(next(c for c in checks if c["id"] == key)["status"], "fail")
        for key in PORTABILITY_FIELDS:
            status, _, _ = self.request("POST", "/api/projects", self.project(**{key: {"invalid": True}}))
            self.assertEqual(status, 400)

    def test_skill_frontmatter_boundary_and_full_description_preservation(self):
        item = self.create(kind="agent-skill", name="a" * 63 + " space", description="d" * 1200)
        files = self.request("GET", f"/api/projects/{item['id']}/package")[2]["files"]
        files = {f["name"]: f["content"] for f in files}
        self.assertIn("name: " + "a" * 63 + "\n", files["SKILL.md"])
        self.assertEqual(len(json.loads(files["SKILL.md"].splitlines()[2].removeprefix("description: "))), 1024)
        self.assertIn("d" * 1200, files["specification.md"])
        self.assertIn("directory named `" + "a" * 63 + "`", files["build.md"])


if __name__ == "__main__":
    unittest.main()
