from __future__ import annotations

import http.client
import json
import tempfile
import threading
import unittest
from pathlib import Path

from app.server import FoundryServer


class ImportContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(__file__).resolve().parents[2]
        self.server = FoundryServer(("127.0.0.1", 0), self.root, Path(self.tmp.name))
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.port = self.server.server_address[1]

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.tmp.cleanup()

    def request(self, method, path, body=None, headers=None):
        headers = headers or {}
        if body is not None:
            body = json.dumps(body).encode()
            headers = {"Content-Type": "application/json", "X-Foundry-Request": "1", **headers}
        conn = http.client.HTTPConnection("127.0.0.1", self.port)
        conn.request(method, path, body, headers)
        response = conn.getresponse()
        raw = response.read()
        conn.close()
        if response.getheader("Content-Type", "").startswith("application/json"):
            return response.status, dict(response.getheaders()), json.loads(raw)
        return response.status, dict(response.getheaders()), raw

    def project(self, **overrides):
        value = {
            "name": "Imported record",
            "kind": "web-tool",
            "description": "Source description",
            "audience": "Reviewers",
            "inputs": "Inputs",
            "outputs": "Outputs",
            "constraints": "Constraints",
            "instructions": "Instructions",
            "components": [{"id": "core", "name": "Core", "purpose": "Keep the record", "dependsOn": []}],
            "tests": [{"id": "case", "name": "Import evidence", "expected": "Resets on import", "actual": "Observed before export", "status": "pass"}],
            "skillIds": [],
        }
        value.update(overrides)
        return value

    def create(self, **overrides):
        status, _, item = self.request("POST", "/api/projects", self.project(**overrides))
        self.assertEqual(status, 201)
        return item

    def test_import_boundary_rejects_wrapper_and_resets_identity_and_evidence(self):
        original = self.create(
            tests=[
                {
                    "id": "case",
                    "name": "Import evidence",
                    "expected": "Resets on import",
                    "actual": "Observed before export",
                    "status": "pass",
                }
            ]
        )

        before = self.request("GET", "/api/projects")[2]["projects"]
        status, _, data = self.request("POST", "/api/import", {"project": original, "extra": True})
        self.assertEqual(status, 400)
        self.assertTrue(data["error"])
        self.assertEqual(self.request("GET", "/api/projects")[2]["projects"], before)

        status, _, data = self.request("POST", "/api/import", {"project": "not-an-object"})
        self.assertEqual(status, 400)
        self.assertTrue(data["error"])
        self.assertEqual(self.request("GET", "/api/projects")[2]["projects"], before)

        status, _, imported = self.request("POST", "/api/import", {"project": {**original, "schemaVersion": 1}})
        self.assertEqual(status, 201)
        self.assertNotEqual(imported["id"], original["id"])
        self.assertEqual(imported["revision"], 1)
        self.assertEqual(imported["status"], "draft")
        self.assertEqual(imported["tests"][0]["status"], "not-run")
        self.assertEqual(imported["tests"][0]["actual"], "")
        self.assertEqual(imported["tests"][0]["expected"], original["tests"][0]["expected"])

        history = self.request("GET", f"/api/projects/{imported['id']}/history")[2]["history"]
        self.assertIn(original["id"], history[0]["summary"])
        self.assertNotIn("Observed before export", json.dumps(imported))

    def test_import_retains_unavailable_skill_references_in_a_fresh_draft(self):
        skill_id = self.server.skills()[0]["id"]
        original = self.create(status="archived", skillIds=[skill_id])
        code, _, exported = self.request("GET", f"/api/projects/{original['id']}/export?format=json")
        self.assertEqual(code, 200)
        self.assertEqual(exported["status"], "archived")
        self.server.skills = lambda: []

        code, _, imported = self.request("POST", "/api/import", {"project": exported})
        self.assertEqual(code, 201, imported)
        self.assertNotEqual(imported["id"], original["id"])
        self.assertEqual(imported["status"], "draft")
        self.assertEqual(imported["skillIds"], [skill_id])
        self.assertEqual(imported["tests"], [{**original["tests"][0], "actual": "", "status": "not-run"}])

        code, _, report = self.request("GET", f"/api/projects/{imported['id']}/validation")
        self.assertEqual(code, 200)
        self.assertFalse(report["readyForReview"])
        skills_check = next(check for check in report["checks"] if check["id"] == "skills")
        self.assertEqual(skills_check["status"], "fail")
        self.assertIn(skill_id, skills_check["detail"])

        code, _, package = self.request("GET", f"/api/projects/{imported['id']}/package")
        self.assertEqual(code, 200)
        self.assertEqual(package["manifest"]["unavailableSkillIds"], [skill_id])
        self.assertEqual(self.request("GET", f"/api/projects/{original['id']}")[2], original)

    def test_import_rejects_malformed_and_duplicate_skill_references(self):
        for skill_ids, error in [
            (["invalid/skill"], "skillIds must be safe string identifiers"),
            (["retired-skill", "retired-skill"], "skillIds must be unique"),
        ]:
            with self.subTest(skill_ids=skill_ids):
                source = self.project(schemaVersion=1, skillIds=skill_ids)
                code, _, response = self.request("POST", "/api/import", {"project": source})
                self.assertEqual(code, 400)
                self.assertEqual(response["error"], error)

        self.assertEqual(self.request("GET", "/api/projects")[2]["projects"], [])


if __name__ == "__main__":
    unittest.main()
