import json
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[2]
SCRIPT = ROOT / "scripts" / "check-inventory-catalog.py"
SPEC = importlib.util.spec_from_file_location("check_inventory_catalog", SCRIPT)
CHECKER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(CHECKER)


CATALOG_TEXT = """\
\ufeff# TOOLBOX 🧰 (Trunk🌳) \\#00 – Example Toolbox

### Full Description:
An example toolbox used by the regression check.

### Primary Functions:
🧰FUNCTION⚙️ (🌳Branch): Perform the example action

### Elevator Pitch:
📒 A complete example toolbox for exercising catalog imports.
"""

TOOL_CATALOG_TEXT = """\
# TOOL 🪚 (Branch🌵): \\#01 – Example Tool

🌐 [https://chatgpt.com/g/example-tool](https://chatgpt.com/g/example-tool)

**🧰 Parent Toolbox (Trunk🌳):** [*Example Toolbox*](https://chatgpt.com/g/example-toolbox)

### Full Description:
An example tool used by the regression check.

### Primary Functions:
🪚FUNCTION⚙️ (🌵Branch): Route an example request
🧭FUNCTION⚙️ (🌵Branch): Compare example options

### Elevator Pitch:
📒 **Example Tool** is a focused category guide for the regression check.

---
"""

TOOLETTE_CATALOG_TEXT = """\
# TOOL-ETTE 🔩 (Twig🌿): \\#01a – Example Tool-ette

🌐 [https://chatgpt.com/g/example-toolette](https://chatgpt.com/g/example-toolette)

**🪚 Parent Tool (Branch🌵):** [*Example Tool*](https://chatgpt.com/g/example-tool)

### Full Description:
An example Tool-ette used by the regression check.

### Primary Functions:
🔩FUNCTION⚙️ (🌿Twig): Process an example input
🧩FUNCTION⚙️ (🌿Twig): Export an example result

### Elevator Pitch:
📒 **Example Tool-ette** is a focused task assistant for the regression check.

---
"""

EXECUTED_LEDGER = """\
| ID | Legacy path | Signals | Classification | Candidate target | Disposition |
|---|---|---|---|---|---|
| X-01 | `legacy/example.md` | underscore | ordinary documentation | `docs/example.md` | **Executed 2026-09-09** |
"""


class CheckInventoryCatalogTests(unittest.TestCase):
    def _make_repository(self, catalog_text: str = CATALOG_TEXT) -> Path:
        directory = Path(tempfile.mkdtemp())
        catalog = directory / CHECKER.CATALOG_PATH
        catalog.parent.mkdir(parents=True)
        catalog.write_text(catalog_text, encoding="utf-8")

        for relative_path, count in CHECKER.DOCUMENTED_REFERENCES.items():
            document = directory / relative_path
            document.parent.mkdir(parents=True, exist_ok=True)
            document.write_text(
                "\n".join([count[0]] * count[1]),
                encoding="utf-8",
            )

        scaffold = directory / CHECKER.SCAFFOLD_PATH
        scaffold.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(
            ROOT
            / ".agents/skills/glee-fully-repo-standardizer/scripts/scaffold.py",
            scaffold,
        )
        self._set_ledger(
            directory,
            f"{CHECKER.CATALOG_PATH.as_posix()}\n\n"
            + self._mapping_ledger(
                "| X-00 | `legacy/example.md` | underscore | "
                "ordinary documentation | `docs/example.md` | **Retain** |\n"
            ),
        )
        return directory

    def _set_ledger(self, directory: Path, text: str = EXECUTED_LEDGER) -> None:
        ledger = directory / CHECKER.MIGRATION_LEDGER_PATH
        ledger.parent.mkdir(parents=True, exist_ok=True)
        ledger.write_text(text, encoding="utf-8")

    def _mapping_ledger(self, row: str) -> str:
        return (
            "| ID | Legacy path | Signals | Classification | Candidate target | "
            "Disposition |\n"
            "|---|---|---|---|---|---|\n"
            f"{row}"
        )

    def _run_scaffold(
        self, directory: Path, *arguments: str
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(directory / CHECKER.SCAFFOLD_PATH),
                "--tier",
                "toolbox",
                "--name",
                "Example Toolbox",
                "--id",
                "00",
                "--dry-run",
                *arguments,
            ],
            cwd=directory,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_current_contract_passes(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        self.assertEqual([], CHECKER.check(directory))

    def test_toolbox_entry_imports_by_id_with_leading_bom(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        scaffold = CHECKER._load_scaffold(directory / CHECKER.SCAFFOLD_PATH)
        entry = scaffold.parse_inventory(
            directory / CHECKER.CATALOG_PATH,
            target_id="00",
        )

        self.assertIsNotNone(entry)
        assert entry is not None
        self.assertEqual("00", entry.entity_id)
        self.assertEqual("Example Toolbox", entry.name)

    def test_duplicate_inventory_id_fails_before_import(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        duplicate_catalog = CATALOG_TEXT + """\

# TOOLBOX 🧰 (Trunk🌳) \\#00 – Conflicting Toolbox

### Full Description:
A conflicting catalog entry that must not be imported.
"""
        (directory / CHECKER.CATALOG_PATH).write_text(
            duplicate_catalog,
            encoding="utf-8",
        )
        scaffold = CHECKER._load_scaffold(directory / CHECKER.SCAFFOLD_PATH)

        with self.assertRaisesRegex(
            scaffold.DuplicateInventoryIDError,
            r"duplicate inventory entity ID '#00'.*"
            r"Example Toolbox \(line 1\).*Conflicting Toolbox \(line 12\)",
        ) as raised:
            scaffold.parse_inventory(
                directory / CHECKER.CATALOG_PATH,
                target_id="00",
            )

        self.assertEqual(
            [
                ("Example Toolbox", 1),
                ("Conflicting Toolbox", 12),
            ],
            raised.exception.entries,
        )

        result = subprocess.run(
            [
                sys.executable,
                str(directory / CHECKER.SCAFFOLD_PATH),
                "--tier",
                "toolbox",
                "--name",
                "Example Toolbox",
                "--id",
                "00",
            ],
            cwd=directory,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("duplicate inventory entity ID '#00'", result.stderr)
        self.assertIn(str(raised.exception), result.stderr)
        self.assertIn("Example Toolbox (line 1)", result.stderr)
        self.assertIn("Conflicting Toolbox (line 12)", result.stderr)

    def test_duplicate_inventory_name_fails_case_insensitively_before_name_import(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        duplicate_catalog = CATALOG_TEXT.replace(
            "Example Toolbox",
            "example toolbox",
            1,
        ) + """\

# TOOLBOX 🧰 (Trunk🌳) \#99 – EXAMPLE TOOLBOX

### Full Description:
A second entry with the same display name.
"""
        (directory / CHECKER.CATALOG_PATH).write_text(
            duplicate_catalog,
            encoding="utf-8",
        )
        scaffold = CHECKER._load_scaffold(directory / CHECKER.SCAFFOLD_PATH)

        with self.assertRaisesRegex(
            scaffold.DuplicateInventoryNameError,
            r"duplicate inventory display name 'example toolbox'.*"
            r"#00 \(line 1\).*#99 \(line 12\)",
        ) as raised:
            scaffold.parse_inventory(
                directory / CHECKER.CATALOG_PATH,
                target_name="Example Toolbox",
            )

        self.assertEqual(
            [("00", 1), ("99", 12)],
            raised.exception.entries,
        )

        result = self._run_scaffold(
            directory,
            "--name",
            "Example Toolbox",
            "--id",
            "missing-id",
        )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("duplicate inventory display name", result.stderr)
        self.assertIn("#00 (line 1)", result.stderr)
        self.assertIn("#99 (line 12)", result.stderr)

    def test_id_import_remains_valid_when_display_names_are_unique(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        scaffold = CHECKER._load_scaffold(directory / CHECKER.SCAFFOLD_PATH)
        entry = scaffold.parse_inventory(
            directory / CHECKER.CATALOG_PATH,
            target_id="00",
            target_name="A different name",
        )

        self.assertIsNotNone(entry)
        assert entry is not None
        self.assertEqual("00", entry.entity_id)
        self.assertEqual("Example Toolbox", entry.name)

    def test_scaffold_preserves_bom_catalog_metadata_in_generated_files(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        result = subprocess.run(
            [
                sys.executable,
                str(directory / CHECKER.SCAFFOLD_PATH),
                "--tier",
                "toolbox",
                "--name",
                "Example Toolbox",
                "--id",
                "00",
            ],
            cwd=directory,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(0, result.returncode, result.stderr)
        description = (directory / "gpt/description.md").read_text(
            encoding="utf-8"
        )
        instructions = (directory / "gpt/instructions.md").read_text(
            encoding="utf-8"
        )
        overview = (directory / "docs/overview.md").read_text(encoding="utf-8")
        functions = (directory / "docs/functions.md").read_text(encoding="utf-8")

        # Imported descriptions retain catalog prose without adding the entity name.
        self.assertTrue(description.startswith(
            "An example toolbox used by the regression check.\n"
        ))
        self.assertIn("Example Toolbox", instructions)
        self.assertIn("Example Toolbox", overview)
        self.assertIn("Example Toolbox", functions)
        self.assertIn("An example toolbox used by the regression check.", description)
        self.assertIn(
            "A complete example toolbox for exercising catalog imports.", overview
        )
        self.assertIn("Perform the example action", functions)

    def test_scaffold_preserves_tool_and_toolette_catalog_metadata_in_generated_files(self):
        cases = (
            (
                "tool",
                "Example Tool",
                "01",
                TOOL_CATALOG_TEXT,
                "An example tool used by the regression check.",
                ("Route an example request", "Compare example options"),
                "is a focused category guide for the regression check.",
            ),
            (
                "toolette",
                "Example Tool-ette",
                "01a",
                TOOLETTE_CATALOG_TEXT,
                "An example Tool-ette used by the regression check.",
                ("Process an example input", "Export an example result"),
                "is a focused task assistant for the regression check.",
            ),
        )

        for (
            tier,
            name,
            entity_id,
            catalog_text,
            description_text,
            functions_text,
            pitch_text,
        ) in cases:
            with self.subTest(tier=tier):
                directory = self._make_repository(catalog_text)
                self.addCleanup(shutil.rmtree, directory)

                result = subprocess.run(
                    [
                        sys.executable,
                        str(directory / CHECKER.SCAFFOLD_PATH),
                        "--tier",
                        tier,
                        "--name",
                        name,
                        "--id",
                        entity_id,
                    ],
                    cwd=directory,
                    capture_output=True,
                    text=True,
                    check=False,
                )

                self.assertEqual(0, result.returncode, result.stderr)
                self.assertIn(
                    f"Inventory match: #{entity_id} — {name}",
                    result.stdout,
                )
                generated = {
                    relative_path: (directory / relative_path).read_text(
                        encoding="utf-8"
                    )
                    for relative_path in (
                        "gpt/description.md",
                        "gpt/instructions.md",
                        "docs/overview.md",
                        "docs/functions.md",
                    )
                }

                self.assertIn(name, generated["gpt/instructions.md"])
                self.assertIn(name, generated["docs/overview.md"])
                self.assertIn(name, generated["docs/functions.md"])
                self.assertIn(description_text, generated["gpt/description.md"])
                self.assertIn(pitch_text, generated["docs/overview.md"])
                for function_text in functions_text:
                    self.assertIn(function_text, generated["docs/functions.md"])

                if tier == "toolette":
                    self.assertIn(
                        description_text, generated["gpt/instructions.md"]
                    )
                    for function_text in functions_text:
                        self.assertIn(function_text, generated["gpt/instructions.md"])

    def test_matching_name_and_id_do_not_warn(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        result = self._run_scaffold(directory)

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertNotIn("does not match catalog entry", result.stdout)
        self.assertIn("Inventory match: #00 — Example Toolbox", result.stdout)

    def test_mismatching_name_and_id_warn_but_still_import_catalog_metadata(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        result = self._run_scaffold(directory, "--name", "Different Toolbox")

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn(
            "WARNING: supplied name 'Different Toolbox' does not match "
            "catalog entry #00 named 'Example Toolbox'; using catalog metadata "
            "selected by ID.",
            result.stdout,
        )
        self.assertIn("Inventory match: #00 — Example Toolbox", result.stdout)
        self.assertIn("Pre-filling: description, overview, functions, instructions", result.stdout)

    def test_mismatching_name_keeps_quiet_and_json_output_contracts(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        for mode in ("--quiet", "--json"):
            with self.subTest(mode=mode):
                result = self._run_scaffold(
                    directory, "--name", "Different Toolbox", mode
                )

                self.assertEqual(0, result.returncode, result.stderr)
                self.assertNotIn("does not match catalog entry", result.stdout)
                self.assertEqual("", result.stderr)
                if mode == "--json":
                    data = json.loads(result.stdout)
                    self.assertEqual("Different Toolbox", data["name"])

    def test_scaffold_defaults_to_catalog_in_its_repository(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        scaffold = CHECKER._load_scaffold(directory / CHECKER.SCAFFOLD_PATH)

        self.assertEqual(
            directory / CHECKER.CATALOG_PATH,
            scaffold.default_inventory_path(),
        )

    def test_output_modes_preserve_inventory_metadata(self):
        outputs = []
        for mode in ([], ["--quiet"], ["--json"]):
            with self.subTest(mode=mode):
                directory = self._make_repository()
                self.addCleanup(shutil.rmtree, directory)
                catalog = CATALOG_TEXT.replace("### Full Description:",
                    "🌐 [Open](https://chatgpt.com/g/example-toolbox)\n"
                    "**Parent Tool:** [Example Parent](https://chatgpt.com/g/example-parent)\n\n"
                    "### Full Description:")
                (directory / CHECKER.CATALOG_PATH).write_text(catalog, encoding="utf-8")
                result = subprocess.run([sys.executable, str(directory / CHECKER.SCAFFOLD_PATH),
                    "--tier", "toolbox", "--name", "Example Toolbox", "--id", "00",
                    "--overwrite", *mode], cwd=directory, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                files = {name: (directory / name).read_text(encoding="utf-8") for name in
                         ("AGENTS.md", "README.md", "manifest.yaml", "canon/registry-entry.md")}
                self.assertIn("https://chatgpt.com/g/example-toolbox", files["manifest.yaml"])
                outputs.append({name: content.replace(directory.name, "fixture-repository")
                                for name, content in files.items()})
        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual(outputs[0], outputs[2])

    def test_explicit_inventory_path_overrides_catalog_default(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        explicit = directory / "alternate-catalog.md"
        explicit.write_text(CATALOG_TEXT, encoding="utf-8")

        scaffold = CHECKER._load_scaffold(directory / CHECKER.SCAFFOLD_PATH)

        self.assertEqual(explicit, scaffold.resolve_inventory_path(str(explicit)))

    def test_missing_default_catalog_warns_with_recovery_action(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        (directory / CHECKER.CATALOG_PATH).unlink()

        result = self._run_scaffold(directory)

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("WARNING: canonical inventory catalog", result.stdout)
        self.assertIn(str(directory / CHECKER.CATALOG_PATH), result.stdout)
        self.assertIn("catalog enrichment skipped", result.stdout)
        self.assertIn("pass --inventory PATH", result.stdout)
        self.assertNotIn("no matching entity", result.stdout)

    def test_readable_default_catalog_without_match_explains_stub_fallback(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        result = self._run_scaffold(
            directory, "--id", "99", "--name", "Unknown Toolbox"
        )

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("WARNING: canonical inventory catalog", result.stdout)
        self.assertIn(str(directory / CHECKER.CATALOG_PATH), result.stdout)
        self.assertIn("is available but has no matching entity", result.stdout)
        self.assertIn("id='99' or name='Unknown Toolbox'", result.stdout)
        self.assertIn("catalog enrichment skipped — using stubs", result.stdout)
        self.assertNotIn("is unavailable", result.stdout)

    def test_readable_override_without_match_names_path_and_requested_entity(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        explicit = directory / "alternate-catalog.md"
        explicit.write_text(CATALOG_TEXT, encoding="utf-8")

        result = self._run_scaffold(
            directory, "--inventory", str(explicit),
            "--id", "99", "--name", "Unknown Toolbox",
        )

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn(f"inventory override '{explicit}'", result.stdout)
        self.assertIn(
            "no matching entity for id='99' or name='Unknown Toolbox'",
            result.stdout,
        )
        self.assertIn("Check the supplied catalog", result.stdout)
        self.assertNotIn("is unavailable", result.stdout)

    def test_unreadable_explicit_catalog_warns_with_supplied_path(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        explicit = directory / "unreadable-catalog"
        explicit.write_bytes(b"\xff")

        result = self._run_scaffold(directory, "--inventory", str(explicit))

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn(f"inventory override '{explicit}'", result.stdout)
        self.assertIn("file is not valid UTF-8", result.stdout)
        self.assertIn("catalog enrichment skipped", result.stdout)
        self.assertNotIn("no matching entity", result.stdout)

    def test_quiet_mode_keeps_catalog_warning_suppressed(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        (directory / CHECKER.CATALOG_PATH).unlink()

        result = self._run_scaffold(directory, "--quiet")

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertNotIn("WARNING:", result.stdout)
        self.assertNotIn("WARNING:", result.stderr)
        self.assertIn("DRY RUN COMPLETE", result.stdout)

    def test_json_mode_keeps_catalog_warning_out_of_json_stdout(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        (directory / CHECKER.CATALOG_PATH).unlink()

        result = self._run_scaffold(directory, "--json")

        self.assertEqual(0, result.returncode, result.stderr)
        self.assertNotIn("WARNING:", result.stdout)
        self.assertIsInstance(json.loads(result.stdout), dict)

    def test_no_match_keeps_quiet_and_json_output_contracts(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        for mode in ("--quiet", "--json"):
            with self.subTest(mode=mode):
                result = self._run_scaffold(
                    directory, "--id", "99", "--name", "Unknown Toolbox", mode
                )
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertNotIn("no matching entity", result.stdout)
                self.assertNotIn("WARNING:", result.stdout)
                self.assertEqual("", result.stderr)
                if mode == "--quiet":
                    self.assertIn("DRY RUN COMPLETE", result.stdout)
                else:
                    data = json.loads(result.stdout)
                    self.assertEqual("Unknown Toolbox", data["name"])
                    self.assertNotIn("inventory_warning", data)

    def test_catalog_health_is_opt_in_and_preserves_plain_json_bytes(self):
        cases = (
            ("usable", None, (), True, "canonical", None),
            ("missing", "missing", (), False, "canonical", "file does not exist"),
            ("unreadable", "unreadable", (), False, "canonical", "file is not valid UTF-8"),
            ("no_match", None, ("--id", "99", "--name", "Unknown Toolbox"),
             True, "canonical", "no matching entity"),
            ("override", None, ("--inventory", "alternate-catalog.md"),
             True, "override", None),
        )
        for label, catalog_state, extra, available, source_kind, reason in cases:
            with self.subTest(label=label):
                directory = self._make_repository()
                self.addCleanup(shutil.rmtree, directory)
                catalog = directory / CHECKER.CATALOG_PATH
                if catalog_state == "missing":
                    catalog.unlink()
                elif catalog_state == "unreadable":
                    catalog.write_bytes(b"\xffsecret catalog text")
                if label == "override":
                    (directory / "alternate-catalog.md").write_text(
                        CATALOG_TEXT, encoding="utf-8"
                    )

                plain = self._run_scaffold(directory, *extra, "--json")
                opted = self._run_scaffold(
                    directory, *extra, "--json", "--catalog-health"
                )
                self.assertEqual(0, plain.returncode, plain.stderr)
                self.assertEqual(0, opted.returncode, opted.stderr)
                self.assertEqual("", plain.stderr)
                self.assertEqual("", opted.stderr)
                baseline = json.loads(plain.stdout)
                enriched = json.loads(opted.stdout)
                self.assertNotIn("catalog_health", baseline)
                health = enriched.pop("catalog_health")
                self.assertEqual(
                    {"available": available, "source_kind": source_kind,
                     "path": "alternate-catalog.md"
                     if source_kind == "override" else str(catalog),
                     "reason": reason},
                    health,
                )
                self.assertEqual(plain.stdout, json.dumps(enriched, indent=2) + "\n")
                self.assertNotIn("secret catalog text", opted.stdout)

    def test_catalog_health_requires_json(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        result = self._run_scaffold(directory, "--catalog-health")

        self.assertNotEqual(0, result.returncode)
        self.assertIn("--catalog-health requires --json", result.stderr)
        self.assertEqual("", result.stdout)

    def test_missing_documented_reference_is_reported(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        document = directory / "prompts/README.md"
        document.write_text("the catalog moved\n", encoding="utf-8")

        issues = CHECKER.check(directory)

        self.assertTrue(any("prompts/README.md" in issue for issue in issues))

    def test_importer_without_catalog_data_is_reported(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        (directory / CHECKER.CATALOG_PATH).write_text(
            "# TOOLBOX 🧰 #00 – Example Toolbox\n", encoding="utf-8"
        )

        issues = CHECKER.check(directory)

        self.assertTrue(any("pre-populate" in issue for issue in issues))

    def test_executed_move_passes_when_target_exists_and_legacy_is_absent(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(directory)
        (directory / "docs/example.md").parent.mkdir(parents=True, exist_ok=True)
        (directory / "docs/example.md").write_text("moved\n", encoding="utf-8")

        self.assertEqual([], CHECKER.check_filename_migration_ledger(directory))

    def test_executed_move_reports_missing_candidate(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(directory)

        issues = CHECKER.check_filename_migration_ledger(directory)

        self.assertTrue(any("candidate path to exist" in issue for issue in issues))

    def test_executed_move_reports_each_malformed_path_field(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)

        cases = (
            ("legacy", "legacy/example.md", "`docs/example.md`"),
            ("candidate", "`legacy/example.md`", "docs/example.md"),
        )
        for index, (field_name, legacy_path, candidate_path) in enumerate(
            cases,
            start=1,
        ):
            with self.subTest(field_name=field_name):
                self._set_ledger(
                    directory,
                    self._mapping_ledger(
                        f"| X-{index:02d} | {legacy_path} | underscore | "
                        f"ordinary documentation | {candidate_path} | "
                        "**Executed 2026-09-09** |\n"
                    ),
                )

                issues = CHECKER.check_filename_migration_ledger(directory)

                self.assertTrue(
                    any(
                        f"row X-{index:02d}" in issue
                        and field_name.capitalize() in issue
                        and "malformed" in issue
                        for issue in issues
                    ),
                    issues,
                )

    def test_short_executed_row_reports_missing_fields(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            self._mapping_ledger(
                "| X-02 | `legacy/example.md` | underscore | **Executed** |\n"
            ),
        )

        issues = CHECKER.check_filename_migration_ledger(directory)

        self.assertTrue(
            any(
                "row X-02" in issue
                and "malformed table row" in issue
                and "Candidate target" in issue
                and "Disposition" in issue
                for issue in issues
            ),
            issues,
        )

    def test_short_rows_in_other_tables_are_ignored(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            "| Batch | Rows | Recommended order | Required approval and checks |\n"
            "|---|---|---|---|\n"
            "| B0 | X-01 | First | Confirm |\n",
        )

        issues = CHECKER.check_filename_migration_ledger(directory)

        self.assertTrue(
            any(
                "missing a recognizable migration mapping-table header" in issue
                for issue in issues
            ),
            issues,
        )
        self.assertFalse(
            any("malformed table row" in issue for issue in issues),
            issues,
        )

    def test_missing_mapping_table_reports_expected_fields(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(directory, "The mapping table was removed.\n")

        issues = CHECKER.check_filename_migration_ledger(directory)

        self.assertEqual(1, len(issues), issues)
        self.assertIn(
            "missing a recognizable migration mapping-table header",
            issues[0],
        )
        for field in CHECKER.LEDGER_FIELDS:
            self.assertIn(field, issues[0])

    def test_renamed_mapping_table_header_reports_contract_failure(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            self._mapping_ledger(
                "| X-03 | `legacy/example.md` | underscore | "
                "ordinary documentation | `docs/example.md` | **Retain** |\n"
            ).replace("| ID | Legacy path |", "| ID | Legacy file |"),
        )

        issues = CHECKER.check_filename_migration_ledger(directory)

        self.assertTrue(
            any(
                "missing a recognizable migration mapping-table header" in issue
                for issue in issues
            ),
            issues,
        )
        self.assertFalse(
            any("row X-03" in issue for issue in issues),
            issues,
        )
        header_issue = next(
            issue
            for issue in issues
            if "missing a recognizable migration mapping-table header" in issue
        )
        for field in CHECKER.LEDGER_FIELDS:
            self.assertIn(field, header_issue)

    def test_ambiguous_execution_disposition_is_reported(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            self._mapping_ledger(
                "| X-03 | `legacy/example.md` | underscore | "
                "ordinary documentation | `docs/example.md` | "
                "**Execution pending** |\n"
            ),
        )

        issues = CHECKER.check_filename_migration_ledger(directory)

        self.assertTrue(
            any(
                "row X-03" in issue
                and "Disposition field" in issue
                and "ambiguous" in issue
                for issue in issues
            ),
            issues,
        )

    def test_duplicate_mapping_row_id_reports_all_affected_lines(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            self._mapping_ledger(
                "| X-04 | `legacy/first.md` | underscore | ordinary documentation | "
                "`docs/first.md` | **Retain** |\n"
                "| X-04 | `legacy/second.md` | underscore | ordinary documentation | "
                "`docs/second.md` | **Not executed** — awaiting approval |\n"
            ),
        )

        issues = CHECKER.check_filename_migration_ledger(directory)

        self.assertTrue(
            any(
                "duplicate mapping row ID 'X-04'" in issue
                and "line 3" in issue
                and "line 4" in issue
                for issue in issues
            ),
            issues,
        )

    def test_unique_mapping_ids_and_approval_tables_are_ignored(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            self._mapping_ledger(
                "| X-05 | `legacy/first.md` | underscore | ordinary documentation | "
                "`docs/first.md` | **Retain** |\n"
                "| X-06 | `legacy/second.md` | underscore | ordinary documentation | "
                "`docs/second.md` | **Retain** |\n"
                "\n"
                "| ID | Batch | Approval owner | Decision | Evidence | Notes |\n"
                "|---|---|---|---|---|---|\n"
                "| X-05 | B0 | Owner | Confirm | Review | Duplicate approval ID |\n"
                "| X-05 | B1 | Owner | Confirm | Review | Duplicate approval ID |\n"
            ),
        )

        self.assertEqual([], CHECKER.check_filename_migration_ledger(directory))

    def test_executed_move_rejects_paths_outside_repository(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        (directory / "docs/example.md").parent.mkdir(parents=True, exist_ok=True)
        (directory / "docs/example.md").write_text("moved\n", encoding="utf-8")

        cases = (
            ("legacy", "/tmp/legacy/example.md", "docs/example.md", "absolute"),
            ("legacy", "C:/outside/legacy.md", "docs/example.md", "absolute"),
            ("legacy", "C:legacy.md", "docs/example.md", "absolute"),
            ("legacy", r"\outside\legacy.md", "docs/example.md", "absolute"),
            ("legacy", "../outside/legacy.md", "docs/example.md", "outside"),
            ("candidate", "legacy/example.md", "/tmp/candidate.md", "absolute"),
            ("candidate", "legacy/example.md", "../outside/candidate.md", "outside"),
        )
        for index, (field_name, legacy_path, candidate_path, reason) in enumerate(
            cases,
            start=1,
        ):
            with self.subTest(field_name=field_name, reason=reason):
                self._set_ledger(
                    directory,
                    self._mapping_ledger(
                        f"| X-{index:02d} | `{legacy_path}` | underscore | "
                        f"ordinary documentation | `{candidate_path}` | "
                        "**Executed 2026-09-09** |\n"
                    ),
                )

                issues = CHECKER.check_filename_migration_ledger(directory)

                self.assertTrue(
                    any(
                        field_name in issue
                        and "line 3" in issue
                        and (
                            "absolute paths are not allowed" in issue
                            if reason == "absolute"
                            else "resolves outside the repository root" in issue
                        )
                        for issue in issues
                    ),
                    issues,
                )

    def test_executed_move_rejects_symlinked_paths_outside_repository(self):
        cases = (
            ("legacy", "legacy", "legacy/example.md", "docs/example.md"),
            ("candidate", "candidate", "legacy/example.md", "candidate/example.md"),
        )
        for field_name, link_name, legacy_path, candidate_path in cases:
            with self.subTest(field_name=field_name):
                directory = self._make_repository()
                self.addCleanup(shutil.rmtree, directory)
                outside = Path(tempfile.mkdtemp())
                self.addCleanup(shutil.rmtree, outside)

                try:
                    (directory / link_name).symlink_to(
                        outside,
                        target_is_directory=True,
                    )
                except (NotImplementedError, OSError) as error:
                    self.skipTest(f"symlinks are unavailable: {error}")

                if field_name == "legacy":
                    candidate = directory / candidate_path
                    candidate.parent.mkdir(parents=True, exist_ok=True)
                    candidate.write_text("moved\n", encoding="utf-8")

                self._set_ledger(
                    directory,
                    self._mapping_ledger(
                        f"| X-01 | `{legacy_path}` | underscore | "
                        f"ordinary documentation | `{candidate_path}` | "
                        "**Executed 2026-09-09** |\n"
                    ),
                )

                issues = CHECKER.check_filename_migration_ledger(directory)

                self.assertTrue(
                    any(
                        field_name in issue
                        and "line 3" in issue
                        and "resolves outside the repository root" in issue
                        for issue in issues
                    ),
                    issues,
                )
                self.assertFalse(
                    any(
                        (
                            "candidate path to exist" in issue
                            if field_name == "candidate"
                            else "still has the legacy path" in issue
                        )
                        for issue in issues
                    ),
                    issues,
                )

    def test_executed_move_reports_legacy_path_that_remains(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(directory)
        (directory / "docs/example.md").parent.mkdir(parents=True, exist_ok=True)
        (directory / "docs/example.md").write_text("moved\n", encoding="utf-8")
        (directory / "legacy/example.md").parent.mkdir(parents=True)
        (directory / "legacy/example.md").write_text("old\n", encoding="utf-8")

        issues = CHECKER.check_filename_migration_ledger(directory)

        self.assertTrue(any("still has the legacy path" in issue for issue in issues))

    def test_intentional_legacy_retention_is_allowed(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            EXECUTED_LEDGER.replace(
                "**Executed 2026-09-09**",
                "**Executed 2026-09-09** — intentional retention",
            ),
        )
        (directory / "docs/example.md").parent.mkdir(parents=True, exist_ok=True)
        (directory / "docs/example.md").write_text("moved\n", encoding="utf-8")
        (directory / "legacy/example.md").parent.mkdir(parents=True)
        (directory / "legacy/example.md").write_text("retained source\n", encoding="utf-8")

        self.assertEqual([], CHECKER.check_filename_migration_ledger(directory))

    def test_not_executed_disposition_is_ignored(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            EXECUTED_LEDGER.replace(
                "**Executed 2026-09-09**",
                "**Not executed** — awaiting approval",
            ),
        )

        self.assertEqual([], CHECKER.check_filename_migration_ledger(directory))

    def test_non_executed_source_retention_is_ignored(self):
        directory = self._make_repository()
        self.addCleanup(shutil.rmtree, directory)
        self._set_ledger(
            directory,
            EXECUTED_LEDGER.replace(
                "`legacy/example.md`",
                "`docs/source-material/original.md`",
            ).replace(
                "`docs/example.md`",
                "`docs/source-material/renamed.md`",
            ).replace(
                "**Executed 2026-09-09**",
                "**Retain by default** — provenance rename requires approval",
            ),
        )
        (directory / "docs/source-material/original.md").parent.mkdir(
            parents=True
        )
        (directory / "docs/source-material/original.md").write_text(
            "source\n", encoding="utf-8"
        )

        self.assertEqual([], CHECKER.check_filename_migration_ledger(directory))


if __name__ == "__main__":
    unittest.main()
