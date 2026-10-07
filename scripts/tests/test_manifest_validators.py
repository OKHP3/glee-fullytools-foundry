"""Regression tests for the repository manifest validators.

Run from the repository root with:

    python3 -m unittest discover -s scripts/tests -v
"""

from __future__ import annotations

import ast
import importlib.util
import re
import subprocess
import sys
import sysconfig
import tempfile
import unittest
from pathlib import Path
from typing import Callable
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "manifest.yaml"
VALIDATOR = ROOT / "scripts" / "validate-manifest.py"
AUDIT = ROOT / "scripts" / "manifest-audit.py"
LOCK_CHECK = ROOT / "scripts" / "check-validator-lock.py"
REQUIREMENTS = ROOT / "requirements.txt"
REQUIREMENTS_LOCK = ROOT / "requirements-lock.txt"
REQUIREMENTS_CONTRACT = ROOT / "scripts" / "check-requirements-contract.py"
MANIFEST_WORKFLOW = ROOT / ".github" / "workflows" / "manifest-validation.yml"
MANIFEST_VALIDATOR_DEPENDENCIES = {"pyyaml", "jsonschema"}
MANIFEST_VALIDATOR_FILENAME = "*manifest*.py"
MANIFEST_CHANGE_PATHS = (
    "manifest.yaml",
    "schemas/example.json",
    "scripts/example.py",
    "requirements.txt",
    "requirements-lock.txt",
    ".github/workflows/manifest-validation.yml",
)
UNRELATED_CHANGE_PATHS = (
    "README.md",
    "docs/example.md",
    "app/example.py",
    ".github/workflows/foundry-app.yml",
)
IMPORT_TO_REQUIREMENT = {"yaml": "pyyaml", "jsonschema": "jsonschema"}
LOCKED_MANIFEST_VALIDATOR_DEPENDENCIES = {
    "attrs",
    "jsonschema",
    "jsonschema-specifications",
    "pyyaml",
    "referencing",
    "rpds-py",
    "typing-extensions",
}


def load_lock_checker():
    """Load the hyphenated lock-check script for deterministic unit coverage."""

    spec = importlib.util.spec_from_file_location("check_validator_lock", LOCK_CHECK)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {LOCK_CHECK}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_requirements_contract():
    """Load the standard-library-only requirements contract checker."""

    spec = importlib.util.spec_from_file_location(
        "check_requirements_contract",
        REQUIREMENTS_CONTRACT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {REQUIREMENTS_CONTRACT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


REQUIREMENTS_CONTRACT_MODULE = load_requirements_contract()
canonical_requirement_name = REQUIREMENTS_CONTRACT_MODULE.canonical_requirement_name
IMPORT_TO_DISTRIBUTION_ALIASES = (
    REQUIREMENTS_CONTRACT_MODULE.IMPORT_TO_DISTRIBUTION_ALIASES
)
requirement_name_for_import = (
    REQUIREMENTS_CONTRACT_MODULE.requirement_name_for_import
)
parse_requirement_entries = REQUIREMENTS_CONTRACT_MODULE.parse_requirement_entries
requirements_contract_errors = REQUIREMENTS_CONTRACT_MODULE.requirements_contract_errors
EXACT_PIN = REQUIREMENTS_CONTRACT_MODULE.EXACT_PIN
HASH_OPTION = re.compile(r"^--hash=sha256:[0-9a-fA-F]{64}$")
HASH_OPTIONS = REQUIREMENTS_CONTRACT_MODULE.HASH_OPTIONS


def manifest_change_pattern(workflow: str) -> re.Pattern[str]:
    """Extract the file-routing regex from the workflow's change step."""

    match = re.search(r"grep -Eq \\\n\s+'([^']+)'", workflow)
    if match is None:
        raise AssertionError("manifest workflow must define a change-routing regex")
    return re.compile(match.group(1))


def workflow_step(workflow: str, name: str) -> str:
    """Return one named workflow step, including its conditions."""

    marker = f"      - name: {name}\n"
    start = workflow.find(marker)
    if start == -1:
        raise AssertionError(f"manifest workflow is missing step {name!r}")
    end = workflow.find("\n      - name:", start + len(marker))
    if end == -1:
        end = len(workflow)
    return workflow[start:end]


def discover_manifest_validator_scripts(scripts_dir: Path) -> tuple[Path, ...]:
    """Discover the manifest validators covered by the import contract.

    Manifest validation scripts use ``manifest`` in their filename and live
    directly in the scripts directory.  Restricting discovery to that
    convention keeps unrelated maintenance tooling outside this contract while
    ensuring a newly added manifest validator is reviewed automatically.
    """

    return tuple(sorted(scripts_dir.glob(MANIFEST_VALIDATOR_FILENAME)))


MANIFEST_VALIDATOR_SCRIPTS = discover_manifest_validator_scripts(ROOT / "scripts")


def validator_imports(path: Path) -> set[str]:
    """Return top-level imports, including imports nested inside functions."""

    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            imports.add(node.module.split(".", 1)[0])
    return imports


def standard_library_modules() -> set[str]:
    """Return top-level standard-library modules across supported interpreters.

    ``sys.stdlib_module_names`` was added after some supported Python versions.
    When it is unavailable, inspect the interpreter's stdlib directory rather
    than treating every import as third-party.
    """

    registry = getattr(sys, "stdlib_module_names", None)
    if registry is not None:
        return set(registry)

    modules = set(sys.builtin_module_names)
    stdlib_path = sysconfig.get_path("stdlib")
    if not stdlib_path:
        return modules

    try:
        entries = Path(stdlib_path).iterdir()
    except OSError:
        return modules

    for entry in entries:
        if entry.name == "__pycache__":
            continue
        if entry.is_dir():
            module_name = entry.name
        elif entry.suffix in {".py", ".pyc", ".so"}:
            module_name = entry.stem.split(".", 1)[0]
        else:
            continue
        if module_name.isidentifier():
            modules.add(module_name)
    return modules


def validator_import_contract_errors(
    scripts: tuple[Path, ...],
    declared_dependencies: set[str],
) -> list[str]:
    """Report third-party validator imports absent from declared dependencies."""

    errors: list[str] = []
    standard_library = standard_library_modules()
    for script in scripts:
        for imported_module in sorted(validator_imports(script)):
            if imported_module == "__future__" or imported_module in standard_library:
                continue
            dependency = requirement_name_for_import(imported_module)
            if dependency not in declared_dependencies:
                errors.append(
                    f"{script.name} imports undeclared third-party package "
                    f"'{imported_module}'; add '{dependency}==<version>' "
                    "to requirements.txt"
                )
    return errors


def lock_contract_errors(path: Path) -> list[str]:
    """Report lock entries that do not describe the reviewed validator graph."""

    entries, errors = parse_requirement_entries(path)
    names = [name for _, name, _ in entries]
    for name in sorted(set(names)):
        if names.count(name) > 1:
            errors.append(f"duplicate lock requirement name: {name}")

    if set(names) != LOCKED_MANIFEST_VALIDATOR_DEPENDENCIES:
        missing = LOCKED_MANIFEST_VALIDATOR_DEPENDENCIES - set(names)
        unexpected = set(names) - LOCKED_MANIFEST_VALIDATOR_DEPENDENCIES
        for dependency in sorted(missing):
            errors.append(f"missing locked dependency: {dependency}")
        for dependency in sorted(unexpected):
            errors.append(f"unexpected locked dependency: {dependency}")

    for line_number, name, specifier in entries:
        if not EXACT_PIN.fullmatch(specifier):
            errors.append(f"{name} on line {line_number} must use an exact == pin")

    lines = path.read_text(encoding="utf-8").splitlines()
    for line_number, name, _ in entries:
        line = lines[line_number - 1].split("#", 1)[0].strip()
        hash_options = [
            token for token in line.split() if token.startswith("--hash=")
        ]
        if not hash_options:
            errors.append(
                f"{name} on line {line_number} must include an approved "
                "sha256 hash (--hash=sha256:<64 hex digits>)"
            )
            continue
        for hash_option in hash_options:
            if not HASH_OPTION.fullmatch(hash_option):
                errors.append(
                    f"{name} on line {line_number} has malformed integrity "
                    f"data {hash_option!r}; use --hash=sha256:<64 hex digits>"
                )

    return errors


class ManifestValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tracked_manifest_before = MANIFEST.read_bytes()

    def tearDown(self) -> None:
        self.assertEqual(
            self.tracked_manifest_before,
            MANIFEST.read_bytes(),
            "manifest validator tests must not modify the tracked manifest",
        )

    def run_validator(self, manifest_path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(manifest_path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def run_audit(self, manifest_root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(AUDIT), str(manifest_root)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def run_lock_check(
        self,
        requirements_path: Path,
        lock_path: Path,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(LOCK_CHECK),
                "--requirements",
                str(requirements_path),
                "--lock",
                str(lock_path),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def run_requirements_contract(
        self,
        requirements_path: Path,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(REQUIREMENTS_CONTRACT),
                "--requirements",
                str(requirements_path),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def write_requirements_variant(self, directory: Path, contents: str) -> Path:
        path = directory / "requirements.txt"
        path.write_text(contents, encoding="utf-8")
        return path

    def write_manifest_variant(
        self,
        directory: Path,
        mutate: Callable[[dict], None] | None = None,
    ) -> Path:
        manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
        if mutate is not None:
            mutate(manifest)
        path = directory / "manifest.yaml"
        path.write_text(
            yaml.safe_dump(manifest, sort_keys=False),
            encoding="utf-8",
        )
        return path

    def test_manifest_validator_requirements_are_unique_and_exactly_pinned(self) -> None:
        self.assertEqual([], requirements_contract_errors(REQUIREMENTS))

    def test_requirements_contract_preflight_passes_without_validator_imports(self) -> None:
        result = self.run_requirements_contract(REQUIREMENTS)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("OK manifest validator requirements contract", result.stdout)
        imports = validator_imports(REQUIREMENTS_CONTRACT)
        self.assertNotIn("yaml", imports)
        self.assertNotIn("jsonschema", imports)

    def test_requirements_contract_preflight_reports_actionable_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "PyYAML==6.0.3\n"
                "pyyaml==6.0.3\n"
                "jsonschema>=4.26,<5\n"
                "-r constraints.txt\n",
            )

            result = self.run_requirements_contract(path)

        self.assertNotEqual(0, result.returncode)
        self.assertIn("duplicate requirement name: pyyaml", result.stdout)
        self.assertIn(
            "jsonschema on line 3 must use an exact == pin",
            result.stdout,
        )
        self.assertIn(
            "line 4 is not a supported package requirement: -r constraints.txt; "
            "use a package name with an exact == version pin",
            result.stdout,
        )

    def test_validator_lock_check_passes_current_graph(self) -> None:
        result = self.run_lock_check(REQUIREMENTS, REQUIREMENTS_LOCK)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("OK validator lock matches direct requirements", result.stdout)

    def test_validator_lock_check_reports_version_drift_without_rewriting_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            requirements = self.write_requirements_variant(
                root,
                "PyYAML==6.0.3\njsonschema==4.26.0\n",
            )
            lock = root / "requirements-lock.txt"
            lock.write_text(
                "PyYAML==6.0.2\njsonschema==4.26.0\n",
                encoding="utf-8",
            )
            before = lock.read_bytes()

            result = self.run_lock_check(requirements, lock)

            self.assertEqual(before, lock.read_bytes())

        self.assertNotEqual(0, result.returncode)
        self.assertIn("pyyaml declares 6.0.3", result.stdout)
        self.assertIn("locks 6.0.2", result.stdout)

    def test_validator_lock_check_reports_missing_direct_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            requirements = self.write_requirements_variant(
                root,
                "PyYAML==6.0.3\njsonschema==4.26.0\n",
            )
            lock = root / "requirements-lock.txt"
            lock.write_text("PyYAML==6.0.3\n", encoding="utf-8")

            result = self.run_lock_check(requirements, lock)

        self.assertNotEqual(0, result.returncode)
        self.assertIn("jsonschema is declared at 4.26.0", result.stdout)
        self.assertIn("missing from", result.stdout)

    def test_validator_lock_update_report_identifies_newer_versions(self) -> None:
        lock_checker = load_lock_checker()

        with patch.object(
            lock_checker,
            "latest_version",
            return_value=("99.0.0", None),
        ):
            updates, warnings = lock_checker.update_report(REQUIREMENTS_LOCK)

        self.assertEqual([], warnings)
        self.assertIn(
            "attrs: lock has 26.1.0; latest index version is 99.0.0",
            updates,
        )

    def test_manifest_validator_imports_are_declared(self) -> None:
        entries, _ = parse_requirement_entries(REQUIREMENTS)
        declared_dependencies = {
            name for _, name, _ in entries
        }
        self.assertEqual(
            [],
            validator_import_contract_errors(
                MANIFEST_VALIDATOR_SCRIPTS,
                declared_dependencies,
            ),
        )

    def test_import_to_distribution_aliases_are_centralized(self) -> None:
        self.assertEqual({"yaml": "pyyaml"}, IMPORT_TO_DISTRIBUTION_ALIASES)
        self.assertEqual("pyyaml", requirement_name_for_import("yaml"))
        self.assertEqual("jsonschema", requirement_name_for_import("jsonschema"))

        with tempfile.TemporaryDirectory() as directory:
            script = Path(directory) / "yaml-validator.py"
            script.write_text("import yaml\n", encoding="utf-8")

            errors = validator_import_contract_errors(
                (script,),
                {"pyyaml"},
            )

        self.assertEqual([], errors)

    def test_standard_library_fallback_works_without_module_registry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            stdlib = Path(directory)
            (stdlib / "legacy_module.py").write_text("", encoding="utf-8")
            (stdlib / "legacy_package").mkdir()
            script = stdlib / "legacy-validator.py"
            script.write_text(
                "import legacy_module\n"
                "import legacy_package\n"
                "import requests\n",
                encoding="utf-8",
            )

            with patch.object(sys, "stdlib_module_names", None), patch.object(
                sysconfig,
                "get_path",
                return_value=str(stdlib),
            ):
                errors = validator_import_contract_errors(
                    (script,),
                    MANIFEST_VALIDATOR_DEPENDENCIES,
                )

        self.assertEqual(
            [
                "legacy-validator.py imports undeclared third-party package "
                "'requests'; add 'requests==<version>' to requirements.txt"
            ],
            errors,
        )

    def test_manifest_validator_discovery_catches_new_validators_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            scripts_dir = Path(directory)
            (scripts_dir / "manifest-policy.py").write_text(
                "import requests\n",
                encoding="utf-8",
            )
            (scripts_dir / "backup-maintenance.py").write_text(
                "import requests\n",
                encoding="utf-8",
            )

            discovered = discover_manifest_validator_scripts(scripts_dir)
            errors = validator_import_contract_errors(
                discovered,
                MANIFEST_VALIDATOR_DEPENDENCIES,
            )

        self.assertEqual(
            (scripts_dir / "manifest-policy.py",),
            discovered,
        )
        self.assertEqual(
            [
                "manifest-policy.py imports undeclared third-party package "
                "'requests'; add 'requests==<version>' to requirements.txt"
            ],
            errors,
        )

    def test_undeclared_third_party_import_identifies_source_and_correction(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            script = Path(directory) / "drifted-validator.py"
            script.write_text(
                "import pathlib\n"
                "import requests\n"
                "from urllib.parse import urlparse\n",
                encoding="utf-8",
            )

            errors = validator_import_contract_errors(
                (script,),
                MANIFEST_VALIDATOR_DEPENDENCIES,
            )

        self.assertEqual(
            [
                "drifted-validator.py imports undeclared third-party package "
                "'requests'; add 'requests==<version>' to requirements.txt"
            ],
            errors,
        )

    def test_manifest_validator_lock_is_complete_and_exactly_pinned(self) -> None:
        self.assertEqual([], lock_contract_errors(REQUIREMENTS_LOCK))

        requirements, _ = parse_requirement_entries(REQUIREMENTS)
        locked_requirements, _ = parse_requirement_entries(REQUIREMENTS_LOCK)
        requirement_versions = {
            name: specifier for _, name, specifier in requirements
        }
        locked_versions = {
            name: specifier for _, name, specifier in locked_requirements
        }
        for dependency in MANIFEST_VALIDATOR_DEPENDENCIES:
            self.assertEqual(
                requirement_versions[dependency],
                locked_versions[dependency],
                f"{dependency} lock pin must match requirements.txt",
            )

    def test_manifest_validator_lock_target_matches_workflow(self) -> None:
        lock = REQUIREMENTS_LOCK.read_text(encoding="utf-8")
        workflow = MANIFEST_WORKFLOW.read_text(encoding="utf-8")

        self.assertIn(
            "# Approved CI target: GitHub Actions ubuntu-latest (Linux X64), "
            "CPython 3.11.",
            lock,
        )
        self.assertEqual(2, workflow.count("runs-on: ubuntu-latest"))
        self.assertEqual(2, workflow.count("python-version: '3.11'"))
        self.assertIn(
            "expected = (\"Linux\", \"X86_64\", \"CPython\", (3, 11))",
            workflow,
        )

    def test_manifest_workflow_installs_hashed_lock(self) -> None:
        workflow = MANIFEST_WORKFLOW.read_text(encoding="utf-8")

        self.assertIn(
            "python -m pip install --require-hashes -r requirements-lock.txt",
            workflow,
        )

    def test_manifest_workflow_reports_missing_selected_artifact_hashes(self) -> None:
        workflow = MANIFEST_WORKFLOW.read_text(encoding="utf-8")

        self.assertIn("title=Missing approved dependency hash", workflow)
        self.assertIn(
            "Add an approved sha256 hash for every selected artifact",
            workflow,
        )

    def test_manifest_workflow_checks_requirements_before_installing(self) -> None:
        workflow = MANIFEST_WORKFLOW.read_text(encoding="utf-8")
        preflight = "python scripts/check-requirements-contract.py"
        install = "python -m pip install --require-hashes -r requirements-lock.txt"

        self.assertIn(preflight, workflow)
        self.assertLess(workflow.index(preflight), workflow.index(install))

    def test_manifest_workflow_triggers_for_every_pull_request(self) -> None:
        workflow = MANIFEST_WORKFLOW.read_text(encoding="utf-8")

        self.assertRegex(workflow, r"(?m)^  pull_request:\s*\{\}\s*$")
        self.assertNotRegex(workflow, r"(?m)^\s+paths(?:-ignore)?:")

    def test_manifest_workflow_routes_every_manifest_related_path_to_validation(
        self,
    ) -> None:
        workflow = MANIFEST_WORKFLOW.read_text(encoding="utf-8")
        routing_pattern = manifest_change_pattern(workflow)

        for path in MANIFEST_CHANGE_PATHS:
            with self.subTest(path=path):
                self.assertRegex(path, routing_pattern)

    def test_manifest_workflow_gates_all_validation_steps_for_unrelated_pull_requests(
        self,
    ) -> None:
        workflow = MANIFEST_WORKFLOW.read_text(encoding="utf-8")
        routing_pattern = manifest_change_pattern(workflow)
        change_step = workflow_step(
            workflow, "Check whether manifest validation is required"
        )

        for path in UNRELATED_CHANGE_PATHS:
            with self.subTest(path=path):
                self.assertNotRegex(path, routing_pattern)
        self.assertIn('echo "manifest=false"', change_step)

        parsed = yaml.load(workflow, Loader=yaml.BaseLoader)
        steps = parsed["jobs"]["validate-manifest"]["steps"]
        initial_checkout_index = next(
            (
                index
                for index, step in enumerate(steps)
                if step.get("uses", "").partition("@")[0] == "actions/checkout"
            ),
            None,
        )
        validation_steps = [
            step
            for index, step in enumerate(steps)
            if step.get("id") != "changes"
            and index != initial_checkout_index
            and ("run" in step or "uses" in step)
        ]
        self.assertTrue(
            validation_steps,
            "manifest workflow must retain conditional validation steps",
        )

        for step in validation_steps:
            step_name = step.get("name") or "<unnamed>"
            with self.subTest(step=step_name):
                self.assertEqual(
                    step.get("if"),
                    "steps.changes.outputs.manifest == 'true'",
                    f"validation step {step_name!r} must use the changed-file condition",
                )

    def test_manifest_validator_lock_requires_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "attrs==26.1.0\n",
            )

            errors = lock_contract_errors(path)

        self.assertIn(
            "attrs on line 1 must include an approved sha256 hash "
            "(--hash=sha256:<64 hex digits>)",
            errors,
        )

    def test_manifest_validator_lock_rejects_malformed_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "attrs==26.1.0 --hash=sha256:not-a-digest\n",
            )

            errors = lock_contract_errors(path)

        self.assertIn(
            "attrs on line 1 has malformed integrity data "
            "'--hash=sha256:not-a-digest'; use --hash=sha256:<64 hex digits>",
            errors,
        )

    def test_duplicate_requirement_names_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "PyYAML==6.0.3\npyyaml==6.0.3\njsonschema==4.26.0\n",
            )

            errors = requirements_contract_errors(path)

        self.assertIn("duplicate requirement name: pyyaml", errors)

    def test_incomplete_validator_lock_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "jsonschema==4.26.0\n",
            )

            errors = lock_contract_errors(path)

        self.assertIn("missing locked dependency: attrs", errors)
        self.assertIn("missing locked dependency: pyyaml", errors)

    def test_non_exact_manifest_validator_pins_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "PyYAML>=6.0,<7\njsonschema==4.26.0\n",
            )

            errors = requirements_contract_errors(path)

        self.assertIn(
            "pyyaml on line 1 must use an exact == pin",
            errors,
        )

    def test_missing_manifest_validator_dependencies_are_named(self) -> None:
        variants = (
            (
                "PyYAML==6.0.3\n",
                "missing manifest validator dependency: jsonschema",
            ),
            (
                "jsonschema==4.26.0\n",
                "missing manifest validator dependency: pyyaml",
            ),
        )

        for contents, expected_error in variants:
            with self.subTest(expected_error=expected_error):
                with tempfile.TemporaryDirectory() as directory:
                    path = self.write_requirements_variant(Path(directory), contents)

                    errors = requirements_contract_errors(path)

                self.assertIn(expected_error, errors)

    def test_unsupported_requirement_syntax_identifies_line_and_correction(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "PyYAML==6.0.3\n"
                "jsonschema==4.26.0\n"
                "-r constraints.txt\n",
            )

            errors = requirements_contract_errors(path)

        self.assertIn(
            "line 3 is not a supported package requirement: -r constraints.txt; "
            "use a package name with an exact == version pin",
            errors,
        )

    def test_invalid_package_names_report_line_and_pin_correction(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "PyYAML-==6.0.3\n"
                "jsonschema==4.26.0\n",
            )

            errors = requirements_contract_errors(path)

        self.assertIn(
            "line 1 is not a supported package requirement: PyYAML-==6.0.3; "
            "use a package name with an exact == version pin",
            errors,
        )

    def test_malformed_extras_report_line_and_pin_correction(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "PyYAML[not valid]==6.0.3\n"
                "jsonschema==4.26.0\n",
            )

            errors = requirements_contract_errors(path)

        self.assertIn(
            "line 1 is not a supported package requirement: "
            "PyYAML[not valid]==6.0.3; "
            "use a package name with an exact == version pin",
            errors,
        )

    def test_unsupported_version_separator_is_not_reported_as_missing_dependency(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "PyYAML>=6.0.3\n"
                "jsonschema==4.26.0\n",
            )

            errors = requirements_contract_errors(path)

        self.assertIn("pyyaml on line 1 must use an exact == pin", errors)
        self.assertNotIn(
            "missing manifest validator dependency: pyyaml",
            errors,
        )

    def test_comments_after_exact_pins_are_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_requirements_variant(
                Path(directory),
                "PyYAML==6.0.3  # YAML parser\n"
                "jsonschema==4.26.0 # schema validator\n",
            )

            errors = requirements_contract_errors(path)

        self.assertEqual([], errors)

    def test_current_manifest_passes_strict_validator_and_legacy_audit(self) -> None:
        validator_result = self.run_validator(MANIFEST)
        self.assertEqual(0, validator_result.returncode, validator_result.stdout)
        self.assertIn("PASS", validator_result.stdout)

        audit_result = self.run_audit(ROOT)
        self.assertEqual(0, audit_result.returncode, audit_result.stdout)
        self.assertIn("OK manifest.yaml baseline fields present", audit_result.stdout)

    def test_missing_top_level_section_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_manifest_variant(
                Path(directory),
                lambda manifest: manifest.pop("application"),
            )

            result = self.run_validator(path)

        self.assertNotEqual(0, result.returncode, result.stdout)
        self.assertIn("'application' is a required property", result.stdout)

    def test_missing_brand_domain_is_rejected_by_both_audits(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.write_manifest_variant(
                root,
                lambda manifest: manifest["brand"].pop("domain"),
            )

            validator_result = self.run_validator(path)
            audit_result = self.run_audit(root)

        self.assertNotEqual(0, validator_result.returncode, validator_result.stdout)
        self.assertIn("'domain' is a required property", validator_result.stdout)
        self.assertNotEqual(0, audit_result.returncode, audit_result.stdout)
        self.assertIn("missing required manifest field: brand.domain", audit_result.stdout)

    def test_invalid_lifecycle_status_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_manifest_variant(
                Path(directory),
                lambda manifest: manifest["repo"].update(
                    lifecycle_status="not-a-real-status"
                ),
            )

            result = self.run_validator(path)

        self.assertNotEqual(0, result.returncode, result.stdout)
        self.assertIn("not-a-real-status", result.stdout)
        self.assertIn("is not one of", result.stdout)


if __name__ == "__main__":
    unittest.main()