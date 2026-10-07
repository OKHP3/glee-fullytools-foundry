from __future__ import annotations

import html
import json
import unittest
import zipfile
from io import BytesIO

from app.tests.test_server import ServiceTests


PACKAGE_CONTRACT_FIXTURES = {
    "custom-gpt": {
        "name": "Contract GPT <&>",
        "target_files": ("instructions.md", "starters.md"),
    },
    "agent-skill": {
        "name": "Contract Skill <&>",
        "target_files": ("SKILL.md",),
    },
    "workflow": {
        "name": "Contract Workflow <&>",
        "target_files": ("workflow.md", "workflow.json"),
    },
    "web-tool": {
        "name": "Contract Web Tool <&>",
        "target_files": ("index.html", "style.css", "app.js"),
    },
}

PACKAGE_CONTRACT_FIELDS = {
    "owner": "Contract owner <&>",
    "version": "2.0.0",
    "purpose": "Purpose text <&> remains authored.",
    "description": "Description text <&> remains authored.",
    "audience": "Reviewers <&>",
    "inputs": "Inputs <&>",
    "outputs": "Outputs <&>",
    "constraints": "Constraints <&>",
    "instructions": "Instructions <&>",
    "skillIds": ["gpt-readiness"],
}


def expected_markdown(fixture):
    esc = lambda value: html.escape(value.strip(), quote=False)
    lines = [
        f"# {esc(fixture['name'])}",
        "",
        "Status: `draft`",
        "Version: `2.0.0`",
        f"Owner: {esc(PACKAGE_CONTRACT_FIELDS['owner'])}",
        "",
        "## Purpose",
        esc(PACKAGE_CONTRACT_FIELDS["purpose"]),
        "",
        "## Description",
        esc(PACKAGE_CONTRACT_FIELDS["description"]),
        "",
        "## Audience",
        esc(PACKAGE_CONTRACT_FIELDS["audience"]),
        "",
        "## Inputs",
        esc(PACKAGE_CONTRACT_FIELDS["inputs"]),
        "",
        "## Outputs",
        esc(PACKAGE_CONTRACT_FIELDS["outputs"]),
        "",
        "## Constraints",
        esc(PACKAGE_CONTRACT_FIELDS["constraints"]),
        "",
        "## Instructions",
        esc(PACKAGE_CONTRACT_FIELDS["instructions"]),
        "",
        "## Components",
        "No components recorded.",
        "",
        "## Acceptance cases",
        "No acceptance cases recorded.",
    ]
    return "\n".join(lines) + "\n"


def expected_contract_files(item, fixture):
    esc = lambda value: html.escape(value.strip(), quote=False)
    readme = expected_markdown(fixture)
    checks = [
        ("purpose", "Purpose", "pass", "Recorded."),
        ("audience", "Audience", "pass", "Recorded."),
        ("inputs", "Inputs", "pass", "Recorded."),
        ("outputs", "Outputs", "pass", "Recorded."),
        ("constraints", "Constraints", "pass", "Recorded."),
        ("instructions", "Instructions", "pass", "Recorded."),
        ("components", "Components and dependencies", "fail", "Add at least one component before review."),
        (
            "evidence",
            "Acceptance evidence",
            "fail",
            "Add acceptance cases and record passing actual evidence for every case.",
        ),
        (
            "skills",
            "Attached skill provenance",
            "fail",
            "Unavailable skill references: gpt-readiness",
        ),
    ]
    report = {
        "readyForReview": False,
        "checks": [
            {"id": key, "label": label, "status": status, "detail": detail}
            for key, label, status, detail in checks
        ],
        "summary": "Complete failed checks and address warnings before review.",
    }
    check_lines = "\n".join(
        f"- {esc(label)}: `{status}`. {esc(detail)}"
        for _, label, status, detail in checks
    )
    evaluation = (
        f"# Evaluation for {esc(fixture['name'])}\n\n"
        "Project status: `draft`.\n\n"
        "## Observed acceptance evidence\n"
        "- No acceptance cases recorded.\n\n"
        "## Readiness observations\n"
        f"{check_lines}\n\n"
        f"{esc(report['summary'])}\n"
    )
    references = (
        "# Skill references\n\n"
        "No Skillz references attached.\n"
        "Unavailable references: gpt-readiness. Recover their recorded source before review.\n"
    )
    build = (
        f"# Build and handoff guidance for {esc(fixture['name'])}\n\n"
        f"This is a local Glee-fully FoundRy working package for a `{item['kind']}` target.\n"
        "The package is inspectable and portable; it is not a deployment, account, model\n"
        "provider integration, or PME/publication certification.\n\n"
        "## Build sequence\n\n"
        "1. Read `manifest.json`, `specification.md`, and the recorded evidence.\n"
        "2. Resolve any unavailable Skillz references before relying on them.\n"
        "3. Adapt the target-specific files to the declared inputs, outputs, constraints,\n"
        "   components, and acceptance cases.\n"
        "4. Re-run the acceptance cases and record observed evidence in the FoundRy project.\n"
        "5. Export a new revision after material changes.\n"
    )
    handoff = (
        f"# Handoff: {esc(fixture['name'])}\n\n"
        "This package is a `draft` working record at revision 1.\n"
        "It does not certify PME readiness, publication readiness, deployment, or automatic\n"
        "behavioral validation.\n\n"
        "## Continue from here\n\n"
        "1. Review `specification.md` and the recorded acceptance evidence.\n"
        "2. Add or revise observed evidence in the FoundRy application, then export a new revision.\n"
        "3. For a web-tool package, open `index.html` in a modern browser and exercise add, complete, reopen, and filters.\n"
        "4. Treat attached Skillz references as pinned provenance, not executable dependencies.\n"
    )
    manifest = {
        "manifestVersion": 1,
        "projectId": item["id"],
        "schemaVersion": 1,
        "revision": 1,
        "name": fixture["name"],
        "kind": item["kind"],
        "owner": PACKAGE_CONTRACT_FIELDS["owner"],
        "version": PACKAGE_CONTRACT_FIELDS["version"],
        "purpose": PACKAGE_CONTRACT_FIELDS["purpose"],
        "status": "draft",
        "readyForReview": False,
        "validation": report,
        "skillReferences": [],
        "unavailableSkillIds": ["gpt-readiness"],
        "files": [
            "project.json",
            "README.md",
            "specification.md",
            "evaluation.md",
            "skill-references.md",
            "build.md",
            "handoff.md",
            *fixture["target_files"],
        ],
        "limitations": [
            "Recorded evidence is not automatic behavioral validation.",
            "Review readiness is not PME or publication authorization.",
            "This local package does not publish, deploy, or call an AI provider.",
        ],
    }
    if item["kind"] == "agent-skill":
        build += "\nExtract this skill into a directory named `contract-skill` to match its frontmatter.\nThe discovery description is limited to 1024 characters; the full authored description remains in specification.md.\n"
    return {
        "manifest.json": manifest,
        "README.md": readme,
        "build.md": build,
        "evaluation.md": evaluation,
        "handoff.md": handoff,
        "skill-references.md": references,
    }


class ExportBoundaryTests(ServiceTests):
    def assert_inspection_matches_zip(self, kind, inspection, zipped):
        inspected_files = inspection["files"]
        inspected_names = [item["name"] for item in inspected_files]
        inspected_contents = {
            item["name"]: item["content"] for item in inspected_files
        }
        repeated_inspected_names = sorted(
            {name for name in inspected_names if inspected_names.count(name) > 1}
        )
        self.assertEqual(
            repeated_inspected_names,
            [],
            f"{kind} inspection repeats package files: {repeated_inspected_names}",
        )

        with zipfile.ZipFile(BytesIO(zipped)) as bundle:
            zip_names_list = bundle.namelist()
            zip_names = set(zip_names_list)
            inspection_names = set(inspected_contents)
            repeated_zip_names = sorted(
                {name for name in zip_names_list if zip_names_list.count(name) > 1}
            )
            self.assertEqual(
                repeated_zip_names,
                [],
                f"{kind} ZIP repeats package files: {repeated_zip_names}",
            )
            self.assertEqual(
                inspection_names,
                zip_names,
                f"{kind} package files differ: "
                f"inspection-only={sorted(inspection_names - zip_names)}; "
                f"zip-only={sorted(zip_names - inspection_names)}",
            )
            for filename, inspected_content in inspected_contents.items():
                with self.subTest(kind=kind, file=filename):
                    zipped_content = bundle.read(filename).decode("utf-8")
                    self.assertEqual(
                        zipped_content,
                        inspected_content,
                        f"{kind} package file {filename} differs between inspection and ZIP",
                    )

        manifest_file = json.loads(inspected_contents["manifest.json"])
        self.assertEqual(
            manifest_file,
            inspection["manifest"],
            f"{kind} package file manifest.json differs from the inspection manifest",
        )
        self.assertEqual(
            inspection["manifest"]["unavailableSkillIds"],
            ["gpt-readiness"],
            f"{kind} package file manifest.json lost unavailable skill provenance",
        )
        self.assertIn(
            "Unavailable references: gpt-readiness.",
            inspected_contents["skill-references.md"],
            f"{kind} package file skill-references.md lost unavailable skill provenance",
        )

    def test_package_zip_parity_for_all_targets_and_unavailable_skills(self):
        for kind, fixture in PACKAGE_CONTRACT_FIXTURES.items():
            with self.subTest(kind=kind):
                item = self.create(
                    kind=kind,
                    name=fixture["name"],
                    **PACKAGE_CONTRACT_FIELDS,
                )
                registered_skills = self.server.skills
                self.server.skills = lambda: []
                try:
                    status, _, inspection = self.request(
                        "GET", f"/api/projects/{item['id']}/package"
                    )
                    self.assertEqual(status, 200, f"{kind} package inspection failed")
                    status, _, zipped = self.request(
                        "GET", f"/api/projects/{item['id']}/export?format=zip"
                    )
                    self.assertEqual(status, 200, f"{kind} ZIP export failed")
                finally:
                    self.server.skills = registered_skills

                self.assert_inspection_matches_zip(kind, inspection, zipped)

    def test_each_target_has_golden_common_contract_after_zip_extraction(self):
        for kind, fixture in PACKAGE_CONTRACT_FIXTURES.items():
            with self.subTest(kind=kind):
                item = self.create(
                    kind=kind,
                    name=fixture["name"],
                    **PACKAGE_CONTRACT_FIELDS,
                )
                # Creation validates against the registered shelf. Export must
                # still preserve the provenance when that shelf entry is gone.
                registered_skills = self.server.skills
                self.server.skills = lambda: []

                status, _, zipped = self.request(
                    "GET", f"/api/projects/{item['id']}/export?format=zip"
                )
                self.assertEqual(status, 200)
                expected = expected_contract_files(item, fixture)
                self.server.skills = registered_skills

                with zipfile.ZipFile(BytesIO(zipped)) as bundle:
                    self.assertEqual(
                        set(bundle.namelist()),
                        {
                            "manifest.json",
                            "project.json",
                            "specification.md",
                            *expected.keys() - {"manifest.json"},
                            *fixture["target_files"],
                        },
                        f"{kind} package member list changed",
                    )
                    for filename, contract in expected.items():
                        with self.subTest(kind=kind, file=filename):
                            actual = bundle.read(filename).decode("utf-8")
                            if filename == "manifest.json":
                                self.assertEqual(
                                    json.loads(actual),
                                    contract,
                                    f"{kind} package file {filename} changed",
                                )
                            else:
                                self.assertEqual(
                                    actual,
                                    contract,
                                    f"{kind} package file {filename} changed",
                                )

                    self.assertEqual(
                        json.loads(bundle.read("project.json")),
                        item,
                        f"{kind} package file project.json changed",
                    )
                    if kind == "custom-gpt":
                        self.assertEqual(
                            bundle.read("instructions.md").decode("utf-8"),
                            html.escape(PACKAGE_CONTRACT_FIELDS["instructions"], quote=False) + "\n",
                            f"{kind} package file instructions.md changed",
                        )
                        self.assertIn(
                            "Conversation starters",
                            bundle.read("starters.md").decode("utf-8"),
                        )
                    elif kind == "agent-skill":
                        skill = bundle.read("SKILL.md").decode("utf-8")
                        self.assertIn("name: contract-skill", skill)
                        self.assertIn("Draft status only. Review recorded evidence before use.", skill)
                    elif kind == "workflow":
                        self.assertEqual(
                            json.loads(bundle.read("workflow.json")),
                            {"name": fixture["name"], "components": []},
                            f"{kind} package file workflow.json changed",
                        )
                    else:
                        index = bundle.read("index.html").decode("utf-8")
                        self.assertIn("<form id=\"record-form\">", index)
                        self.assertIn("Contract Web Tool &lt;&amp;&gt;", index)
                        self.assertIn("localStorage", bundle.read("app.js").decode("utf-8"))

    def test_unicode_long_text_and_archive_paths_survive_export(self):
        name = "Glee Δossier ../unsafe/🪴✨"
        long_description = "".join([
            "Line one with unicode: café, naïve, 影, and 🧪.\n",
            "Line two stays readable even when it is deliberately long: " + ("彩" * 120) + "\n",
            "Line three keeps punctuation intact: —but we do not rely on em dashes here—\n",
        ])
        hostile = "Folder-ish name ../nested/..\\escape? <record>"
        item = self.create(
            kind="web-tool",
            name=name,
            description=long_description,
            audience="Unicode-sensitive reviewers",
            inputs=hostile,
            outputs=long_description,
            constraints="No path traversal, no lossy encoding.",
            instructions=long_description,
            components=[{
                "id": "entry",
                "name": hostile,
                "purpose": long_description,
                "dependsOn": [],
            }],
            tests=[{
                "id": "case",
                "name": hostile,
                "expected": long_description,
                "actual": long_description,
                "status": "pass",
            }],
        )

        status, headers, raw = self.request("GET", f"/api/projects/{item['id']}/export?format=json")
        self.assertEqual(status, 200)
        self.assertIn("attachment", headers["Content-Disposition"])
        exported = raw
        self.assertEqual(exported["name"], name)
        self.assertEqual(exported["description"], long_description)
        self.assertEqual(exported["components"][0]["name"], hostile)

        status, _, markdown = self.request("GET", f"/api/projects/{item['id']}/export?format=markdown")
        self.assertEqual(status, 200)
        markdown_text = markdown.decode()
        self.assertIn(name, markdown_text)
        self.assertIn("café", markdown_text)
        self.assertIn("彩" * 40, markdown_text)
        self.assertIn("Folder-ish name ../nested/..\\escape? &lt;record&gt;", markdown_text)

        status, _, zipped = self.request("GET", f"/api/projects/{item['id']}/export?format=zip")
        self.assertEqual(status, 200)
        with zipfile.ZipFile(BytesIO(zipped)) as bundle:
            members = set(bundle.namelist())
            self.assertEqual(members & {"../x", "..\\x", "/x", "C:/x"}, set())
            self.assertTrue(all(".." not in member and not member.startswith("/") for member in members))
            self.assertIn("café", bundle.read("README.md").decode())
            self.assertIn(name, bundle.read("README.md").decode())
            self.assertIn("Folder-ish name ../nested/..\\escape? &lt;record&gt;", bundle.read("specification.md").decode())
            self.assertIn("彩" * 40, bundle.read("evaluation.md").decode())
            self.assertEqual(json.loads(bundle.read("project.json")), item)
            self.assertIn("Continue from here", bundle.read("handoff.md").decode())
