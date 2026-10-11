import io
import importlib.util
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "check-markdown-links.py"
SPEC = importlib.util.spec_from_file_location("check_markdown_links", SCRIPT)
CHECKER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CHECKER
SPEC.loader.exec_module(CHECKER)


class CheckMarkdownLinksTests(unittest.TestCase):
    def test_default_documents_cover_active_governed_indexes(self):
        self.assertEqual(
            (
                "README.md",
                "docs/README.md",
                "docs/application/README.md",
                "docs/adr/README.md",
                "prompts/README.md",
                "canon/README.md",
                "evaluation/README.md",
                "governance/README.md",
                "inventory/README.md",
                "templates/README.md",
                "vernacular/README.md",
                "web-templates/README.md",
                "scripts/tests/README.md",
            ),
            CHECKER.DEFAULT_DOCUMENTS,
        )
        self.assertNotIn("snapshots/README.md", CHECKER.DEFAULT_DOCUMENTS)
        self.assertNotIn(
            "docs/application/pilots/custom-gpt/README.md",
            CHECKER.DEFAULT_DOCUMENTS,
        )
        self.assertNotIn(
            "docs/delegation/2026-09-07-coop-pertition/README.md",
            CHECKER.DEFAULT_DOCUMENTS,
        )

    def test_pilot_discovery_covers_complete_packages_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pilots = root / CHECKER.PILOT_DOCUMENT_ROOT
            for package_name in ("alpha", "beta"):
                package = pilots / package_name
                package.mkdir(parents=True)
                (package / "project.json").write_text("{}\n", encoding="utf-8")
                (package / "README.md").write_text("# Package\n", encoding="utf-8")

            nested = pilots / "alpha" / "docs"
            nested.mkdir()
            (nested / "README.md").write_text("# Nested\n", encoding="utf-8")

            generated = pilots / "generated"
            generated.mkdir()
            (generated / "project.json").write_text("{}\n", encoding="utf-8")
            (generated / "README.md").write_text("# Generated\n", encoding="utf-8")

            no_manifest = pilots / "notes"
            no_manifest.mkdir()
            (no_manifest / "README.md").write_text("# Notes\n", encoding="utf-8")

            self.assertEqual(
                (
                    "docs/application/pilots/alpha/README.md",
                    "docs/application/pilots/beta/README.md",
                ),
                CHECKER.discover_pilot_documents(root),
            )

    def test_pilot_discovery_reports_one_missing_handoff_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pilots = root / CHECKER.PILOT_DOCUMENT_ROOT

            readme_only = pilots / "readme-only"
            readme_only.mkdir(parents=True)
            (readme_only / "README.md").write_text("# Notes\n", encoding="utf-8")

            manifest_only = pilots / "manifest-only"
            manifest_only.mkdir()
            (manifest_only / "project.json").write_text("{}\n", encoding="utf-8")

            complete = pilots / "complete"
            complete.mkdir()
            (complete / "project.json").write_text("{}\n", encoding="utf-8")
            (complete / "README.md").write_text("# Complete\n", encoding="utf-8")

            self.assertEqual(
                (
                    CHECKER.LinkIssue(
                        Path("docs/application/pilots/manifest-only"),
                        0,
                        "README.md",
                        "pilot package missing handoff file",
                    ),
                    CHECKER.LinkIssue(
                        Path("docs/application/pilots/readme-only"),
                        0,
                        "project.json",
                        "pilot package missing handoff file",
                    ),
                ),
                CHECKER.discover_pilot_package_issues(root),
            )
            self.assertEqual(
                ("docs/application/pilots/complete/README.md",),
                CHECKER.discover_pilot_documents(root),
            )

    def test_pilot_discovery_excludes_hidden_and_reserved_directories_from_warnings(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pilots = root / CHECKER.PILOT_DOCUMENT_ROOT
            for package_name in (
                ".hidden",
                "archive",
                "archives",
                "generated",
                "historical",
                "snapshots",
            ):
                package = pilots / package_name
                package.mkdir(parents=True)
                (package / "README.md").write_text("# Excluded\n", encoding="utf-8")

            self.assertEqual((), CHECKER.discover_pilot_package_issues(root))
            self.assertEqual((), CHECKER.discover_pilot_documents(root))

    def test_pilot_scan_reports_broken_link_without_broadening_default_scope(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# Repository\n", encoding="utf-8")
            package = root / "docs/application/pilots/example"
            package.mkdir(parents=True)
            (package / "project.json").write_text("{}\n", encoding="utf-8")
            (package / "README.md").write_text(
                "# Pilot\n\n[missing](missing.md)\n",
                encoding="utf-8",
            )

            pilot_result = CHECKER.scan(
                root,
                CHECKER.discover_pilot_documents(root),
            )
            default_result = CHECKER.scan(root, ("README.md",))

            self.assertEqual(1, len(pilot_result.issues))
            self.assertEqual(
                Path("docs/application/pilots/example/README.md"),
                pilot_result.issues[0].source,
            )
            self.assertEqual(3, pilot_result.issues[0].line)
            self.assertEqual("missing.md", pilot_result.issues[0].destination)
            self.assertEqual("target does not exist", pilot_result.issues[0].reason)
            self.assertEqual([], default_result.issues)

    def test_pilot_cli_reports_source_line_destination_and_reason(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            package = root / "docs/application/pilots/example"
            package.mkdir(parents=True)
            (package / "project.json").write_text("{}\n", encoding="utf-8")
            (package / "README.md").write_text(
                "# Pilot\n\n[handoff](missing.md)\n",
                encoding="utf-8",
            )

            output = io.StringIO()
            with redirect_stdout(output):
                status = CHECKER.main([str(root), "--pilots"])

            self.assertEqual(1, status)
            self.assertIn(
                f"{(package / 'README.md').relative_to(root)}:3", output.getvalue()
            )
            self.assertIn("'missing.md'", output.getvalue())
            self.assertIn("target does not exist", output.getvalue())

    def test_pilot_cli_reports_missing_handoff_file_with_package_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            package = root / "docs/application/pilots/incomplete"
            package.mkdir(parents=True)
            (package / "README.md").write_text("# Incomplete\n", encoding="utf-8")

            output = io.StringIO()
            with redirect_stdout(output):
                status = CHECKER.main([str(root), "--pilots"])

            self.assertEqual(1, status)
            self.assertIn("FAIL pilot package validation:", output.getvalue())
            self.assertIn(
                str(package.relative_to(root)), output.getvalue()
            )
            self.assertIn("'project.json'", output.getvalue())
            self.assertIn("pilot package missing handoff file", output.getvalue())

    def test_workflow_filters_cover_every_default_document(self):
        root = Path(__file__).parents[2]

        self.assertEqual([], CHECKER.check_workflow_document_coverage(root))

    def test_workflow_filters_support_quotes_and_inline_comments(self):
        workflow = """\
on:
  pull_request:
    paths:
      - "**/*.md" # Covers every maintained index.
      - scripts/** # Unquoted path filter.
  push:
    paths:
      - "**/*.md" # Covers every maintained index.
      - scripts/**
"""

        self.assertEqual(
            ("**/*.md", "scripts/**"),
            CHECKER.workflow_path_filters(workflow, "pull_request"),
        )
        self.assertEqual(
            [],
            CHECKER.check_workflow_document_coverage(
                Path("/repository"),
                workflow_text=workflow,
            ),
        )

    def test_workflow_filter_comments_inside_quotes_are_not_stripped(self):
        workflow = """\
on:
  pull_request:
    paths:
      - "docs/#guide" # Comment follows the quoted value.
  push:
    paths:
      - "docs/#guide"
"""

        self.assertEqual(
            ("docs/#guide",),
            CHECKER.workflow_path_filters(workflow, "pull_request"),
        )

    def test_malformed_workflow_path_structure_is_reported(self):
        workflow = """\
on:
  pull_request:
    paths:
      - "**/*.md"
       - "README.md"
  push:
    paths:
      - "**/*.md"
"""

        issues = CHECKER.check_workflow_document_coverage(
            Path("/repository"),
            workflow_text=workflow,
        )

        self.assertTrue(
            any(
                "pull_request paths are malformed" in issue
                and "line 5" in issue
                and "six-space list item" in issue
                for issue in issues
            ),
            issues,
        )

    def test_workflow_single_star_does_not_cover_nested_documents(self):
        root = Path(__file__).parents[2]
        workflow = (root / CHECKER.WORKFLOW_PATH).read_text(encoding="utf-8")
        workflow = workflow.replace("'docs/**'", "'docs/*'")

        issues = CHECKER.check_workflow_document_coverage(root, workflow)

        self.assertEqual(4, len(issues), issues)
        self.assertTrue(
            all(
                "docs/application/README.md" in item
                or "docs/adr/README.md" in item
                for item in issues
            )
        )

    def test_workflow_globs_match_github_documented_examples(self):
        cases = [
            ("docs/README.md", "docs/*", True),
            ("docs/application/README.md", "docs/*", False),
            ("docs/application/README.md", "docs/**", True),
            ("README.md", "**/README.md", True),
            ("docs/application/README.md", "**/README.md", True),
            ("docs/README.md", "*.md", False),
            ("docs/README.md", "**.md", True),
            ("page.js", "*.jsx?", True),
            ("page.jsx", "*.jsx?", True),
            ("page.jsxx", "*.jsx?", False),
            ("v1.10.1", "v[12].[0-9]+.[0-9]+", True),
        ]
        for document, pattern, expected in cases:
            with self.subTest(document=document, pattern=pattern):
                self.assertEqual(
                    expected,
                    CHECKER.workflow_path_matches(document, pattern),
                )

    def test_workflow_exclusions_and_reinclusions_are_ordered(self):
        path = "docs/application/README.md"

        self.assertFalse(
            CHECKER.workflow_covers_path(
                path, ("docs/**", "!docs/application/**")
            )
        )
        self.assertTrue(
            CHECKER.workflow_covers_path(
                path, ("docs/**", "!docs/application/**", path)
            )
        )

    def test_workflow_filter_drift_names_document_and_missing_filter(self):
        workflow = """\
on:
  pull_request:
    paths:
      - 'README.md'
  push:
    paths:
      - 'README.md'
"""

        issues = CHECKER.check_workflow_document_coverage(
            Path("/repository"),
            workflow_text=workflow,
        )

        self.assertTrue(
            any(
                "pull_request" in issue
                and "docs/README.md" in issue
                and "matching filter" in issue
                for issue in issues
            ),
            issues,
        )
        self.assertTrue(
            any(
                "push" in issue
                and "docs/README.md" in issue
                and "matching filter" in issue
                for issue in issues
            ),
            issues,
        )

    def test_workflow_coverage_cli_reports_drift(self):
        workflow = """\
on:
  pull_request:
    paths:
      - 'README.md'
  push:
    paths:
      - 'README.md'
"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow_path = root / CHECKER.WORKFLOW_PATH
            workflow_path.parent.mkdir(parents=True)
            workflow_path.write_text(workflow, encoding="utf-8")

            output = io.StringIO()
            with redirect_stdout(output):
                status = CHECKER.main([str(root), "--check-workflow-coverage"])

        self.assertEqual(1, status)
        self.assertIn("FAIL workflow/document coverage drift", output.getvalue())
        self.assertIn("pull_request", output.getvalue())
        self.assertIn("docs/README.md", output.getvalue())
        self.assertIn("add a matching filter", output.getvalue())

    def test_supported_non_repository_links_are_skipped(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs/guide.md").write_text("# Heading\n", encoding="utf-8")
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "# Index",
                        "[local](docs/guide.md)",
                        "[with anchor](docs/guide.md#heading)",
                        "[anchor](#index)",
                        "[external](https://example.invalid/missing)",
                        "[template]({{generated-path}})",
                        "[environment](${generated_path})",
                        "```markdown",
                        "[example](missing.md)",
                        "```",
                    ]
                ),
                encoding="utf-8",
            )

            result = CHECKER.scan(root, ("README.md",))

            self.assertEqual([], result.issues)
            self.assertEqual(6, result.links)
            self.assertEqual(1, result.external)
            self.assertEqual(1, result.anchors)
            self.assertEqual(2, result.placeholders)

    def test_missing_relative_link_is_reported_with_line_number(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "# Index\n\n[missing](docs/not-here.md)\n",
                encoding="utf-8",
            )

            result = CHECKER.scan(root, ("README.md",))

            self.assertEqual(1, len(result.issues))
            self.assertEqual(Path("README.md"), result.issues[0].source)
            self.assertEqual(3, result.issues[0].line)
            self.assertEqual("target does not exist", result.issues[0].reason)

    def test_missing_heading_fragment_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "# Index\n\n[missing](README.md#not-there)\n",
                encoding="utf-8",
            )

            result = CHECKER.scan(root, ("README.md",))

            self.assertEqual(1, len(result.issues))
            self.assertEqual(3, result.issues[0].line)
            self.assertEqual("heading does not exist", result.issues[0].reason)

    def test_heading_fragments_use_github_normalization_and_duplicate_suffixes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "\n".join(
                    [
                        "# Repeated Heading",
                        "# Repeated Heading",
                        "# Punctuation: and `markup`",
                        "Setext Heading",
                        "----------------",
                        "[first](README.md#repeated-heading)",
                        "[second](README.md#repeated-heading-1)",
                        "[punctuation](README.md#punctuation-and-markup)",
                        "[setext](#setext-heading)",
                    ]
                ),
                encoding="utf-8",
            )

            result = CHECKER.scan(root, ("README.md",))

            self.assertEqual([], result.issues)

    def test_percent_encoded_fragment_is_decoded_before_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs/guide.md").write_text("# A Heading\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[guide](docs/guide.md#a%2Dheading)\n",
                encoding="utf-8",
            )

            result = CHECKER.scan(root, ("README.md",))

            self.assertEqual([], result.issues)

    def test_external_fragment_is_not_validated(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "[external](https://example.invalid/missing#not-there)\n",
                encoding="utf-8",
            )

            result = CHECKER.scan(root, ("README.md",))

            self.assertEqual([], result.issues)
            self.assertEqual(1, result.external)


if __name__ == "__main__":
    unittest.main()
