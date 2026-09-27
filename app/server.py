"""Loopback-only, standard-library FoundRy application service."""
from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import re
import sqlite3
import threading
import uuid
import zipfile
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

MAX_BODY = 1024 * 1024
MAX_TEXT = 100_000
MAX_ITEMS = 1_000
MAX_DEPENDENCIES = 100
MAX_BACKUP_PROJECTS = 1_000
MAX_BACKUP_BYTES = 10 * 1024 * 1024
KINDS = {"custom-gpt", "agent-skill", "plugin", "connector", "workflow", "web-tool"}
PORTABILITY_FIELDS = {"sourceProvenance", "capabilityMap", "semanticLoss", "targetHosts", "integrationContract"}
STATUSES = {"draft", "archived"}
TEST_STATUSES = {"not-run", "pass", "fail"}
EDITABLE = {"name", "kind", "owner", "version", "purpose", "description",
            "audience", "inputs", "outputs", "constraints", "instructions",
            "components", "tests", "skillIds", "status"}
TEXT_FIELDS = EDITABLE - {"components", "tests", "skillIds", "kind", "status"}
SAFE_ID = re.compile(r"^[A-Za-z0-9._:-]{1,128}$")
UUID_ID = re.compile(r"^[0-9a-f-]{36}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")

SOURCES = {
    "portable-capabilities": ("Skills, plugins and conversion workflow", "docs/application/portable-capabilities.md"),
    "product-subtrees": ("Product subtree migration", "products/README.md"),
    "promptchain": ("Builder-Ready PromptChain", "prompts/glee-fully-builder-ready-promptchain-v2-0.md"),
    "gpt-scaffold": ("Custom GPT scaffold", "prompts/custom-gpt-scaffold.md"),
    "pulsebook": ("GPT PulseBook v1.7", "evaluation/gpt-pulsebook-evaluation-v1-7.md"),
    "vernacular": ("Glee-fully vernacular", "vernacular/glee-fully-vernacular-lite.md"),
    "canon-overview": ("Canon overview", "canon/README.md"),
}
UNIVERSE = [
    {"id": "askjamie", "name": "AskJamie", "region": "left", "role": "Personal guidance", "url": "https://askjamie.bot", "shared": False},
    {"id": "overkill", "name": "OverKill Hill", "region": "center", "role": "Connective center and common baseline", "url": "https://overkillhill.com", "shared": False},
    {"id": "gleefully", "name": "Glee-fully", "region": "right", "role": "Personalizable tools", "url": "https://glee-fully.tools", "shared": False},
    {"id": "skillz", "name": "Skillz", "region": "shared", "role": "Shared skills", "url": "https://github.com/OKHP3/skillz", "shared": True},
    {"id": "askjamie-foundry", "name": "AskJamie FoundRy", "region": "left", "role": "AskJamie-only foundry", "url": "https://github.com/OKHP3/AskJamie-FoundRy", "shared": False},
    {"id": "overkill-foundry", "name": "OverKill Hill Found-Ry", "region": "center", "role": "OverKill-owned builder and reciprocal mentoring pattern", "url": "https://github.com/OKHP3/OverKill-Hill-FoundRy", "shared": False},
    {"id": "gleefully-foundry", "name": "Glee-fully Tools FoundRy", "region": "right", "role": "Glee-fully-only foundry", "url": "https://github.com/OKHP3/Glee-fullyTools-FoundRy", "shared": False},
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def template(kind: str, name: str, description: str) -> dict:
    guidance = {
        "custom-gpt": ("Conversation", "Clarify the request, use the supplied context and produce the agreed output.",
                       "1. Establish the user's objective and available source material.\n2. Ask for essential missing inputs.\n3. Work within the declared constraints.\n4. Distinguish source facts, assumptions and unknowns.\n5. Return the specified output with a useful next step."),
        "agent-skill": ("Skill workflow", "Carry out a bounded reusable method and leave an inspectable artifact.",
                        "Trigger: describe when this skill applies.\nInputs: check the required material before acting.\nProcedure: perform the bounded task using the declared sources.\nVerification: check the acceptance cases.\nHandoff: report the artifact, evidence and remaining limitations."),
        "plugin": ("Skill composition", "Compose portable skills with separately verified host adapters.",
                   "1. Identify the versioned skills and their input/output contracts.\n2. Define composition order and failure handling.\n3. Declare the target host, tools and permissions.\n4. Build and validate the native adapter against that host's documented format.\n5. Record host-specific installation and behavior evidence. This draft does not install a plugin."),
        "connector": ("Integration contract", "Connect a capability to a declared service through a reviewed adapter.",
                      "1. Specify the API or MCP service and operations needed by the skill.\n2. Declare authentication, scopes, read/write boundaries and user consent.\n3. Define input/output schemas and error handling.\n4. Keep credentials outside the package.\n5. Implement and test each host adapter before claiming compatibility. This draft does not implement a connector."),
        "workflow": ("Process", "Transform a defined input into an output with an explicit completion check.",
                     "1. Confirm scope and prerequisites.\n2. Name the responsible role for each step.\n3. Record decisions and exception paths.\n4. Check the output against acceptance criteria.\n5. Package the result and any unresolved work."),
        "web-tool": ("Record workspace", "Add records, mark them complete, reopen them and filter the list.",
                     "Use the exported record-management starter as an editable baseline.\nDefine the domain-specific record and user needs in this brief.\nAdapt the starter code to the specification, then run the acceptance cases.\nDo not treat the generic starter as an implementation of every authored requirement.")
    }
    component_name, purpose, instructions = guidance[kind]
    return {"id": kind, "name": name, "description": description,
            "project": {"name": "Untitled " + name, "kind": kind,
                        "owner": "", "version": "0.1.0", "purpose": description,
                        "description": description, "audience": "", "inputs": "", "outputs": "",
                        "constraints": "Working draft. Preserve source provenance and label unknowns. Evaluate before publication.",
                        "instructions": instructions,
                        "components": [{"id": "core", "name": component_name, "purpose": purpose, "dependsOn": []}],
                        "tests": [{"id": "expected-use", "name": "Expected use", "expected": "The agreed output is produced from valid inputs.", "actual": "", "status": "not-run"},
                                  {"id": "missing-input", "name": "Missing input", "expected": "Missing essential input is identified without inventing its value.", "actual": "", "status": "not-run"}],
                        "skillIds": []}}


TEMPLATES = [
    template("agent-skill", "Agent Skill", "A portable, reviewable skill specification."),
    template("plugin", "Plugin blueprint", "Compose skills and tools for a specific host adapter."),
    template("connector", "Connector blueprint", "Define API or MCP integration requirements and permissions."),
    template("custom-gpt", "Legacy GPT source", "Preserve an existing GPT specification for conversion to skills."),
    template("workflow", "Workflow", "A repeatable process with evidence and checks."),
    template("web-tool", "Web tool", "A local record-management web-tool starter."),
]


class ValidationError(ValueError):
    pass


def validate_project(payload: object, *, creating: bool = False, importing: bool = False) -> dict:
    if not isinstance(payload, dict):
        raise ValidationError("project must be an object")
    allowed = EDITABLE | PORTABILITY_FIELDS | ({"revision"} if not creating else set())
    if importing:
        allowed |= {"id", "schemaVersion", "createdAt", "updatedAt"}
    unknown = set(payload) - allowed
    if unknown:
        raise ValidationError("unknown project fields: " + ", ".join(sorted(unknown)))
    result = {key: payload.get(key, "" if key in TEXT_FIELDS else []) for key in EDITABLE}
    # Optional extensions must stay absent in historical v1 snapshots so their
    # canonical bytes and backup digests remain valid.
    for key in PORTABILITY_FIELDS & payload.keys():
        if not isinstance(payload[key], str) or len(payload[key]) > MAX_TEXT:
            raise ValidationError(key + " must be text no longer than 100000 characters")
        result[key] = payload[key]
    if not isinstance(result["name"], str) or not result["name"].strip():
        raise ValidationError("name is required")
    if not isinstance(result["kind"], str) or result["kind"] not in KINDS:
        raise ValidationError("kind is invalid")
    if "status" not in payload:
        result["status"] = "draft"
    if not isinstance(result["status"], str) or result["status"] not in STATUSES:
        raise ValidationError("status is invalid")
    for field in TEXT_FIELDS:
        if not isinstance(result[field], str) or len(result[field]) > MAX_TEXT:
            raise ValidationError(field + " must be text no longer than 100000 characters")
    if not isinstance(result["skillIds"], list) or len(result["skillIds"]) > MAX_ITEMS or any(not isinstance(x, str) or not SAFE_ID.fullmatch(x) for x in result["skillIds"]):
        raise ValidationError("skillIds must be safe string identifiers")
    if len(set(result["skillIds"])) != len(result["skillIds"]):
        raise ValidationError("skillIds must be unique")
    components = result["components"]
    if not isinstance(components, list) or len(components) > MAX_ITEMS:
        raise ValidationError("components must be a list")
    ids = set()
    for component in components:
        if not isinstance(component, dict) or set(component) != {"id", "name", "purpose", "dependsOn"}:
            raise ValidationError("components must contain id, name, purpose, dependsOn only")
        if not isinstance(component["id"], str) or not SAFE_ID.fullmatch(component["id"]) or component["id"] in ids:
            raise ValidationError("component IDs must be unique safe identifiers")
        ids.add(component["id"])
        if any(not isinstance(component[x], str) or not component[x].strip() or len(component[x]) > MAX_TEXT for x in ("name", "purpose")):
            raise ValidationError("component name and purpose must be text")
        if not isinstance(component["dependsOn"], list) or len(component["dependsOn"]) > MAX_DEPENDENCIES or any(not isinstance(x, str) for x in component["dependsOn"]):
            raise ValidationError("component dependsOn must be a string list")
    for component in components:
        if any(dep not in ids for dep in component["dependsOn"]):
            raise ValidationError("component dependency does not exist")
    # Kahn's iterative traversal avoids recursion-limit denial of service.
    graph = {c["id"]: set(c["dependsOn"]) for c in components}
    resolved = set()
    while graph:
        ready = {node for node, deps in graph.items() if deps <= resolved}
        if not ready:
            raise ValidationError("component dependencies contain a cycle")
        resolved.update(ready)
        for node in ready:
            del graph[node]
    tests = result["tests"]
    if not isinstance(tests, list) or len(tests) > MAX_ITEMS: raise ValidationError("tests must be a list with at most 1000 entries")
    test_ids = set()
    for case in tests:
        if not isinstance(case, dict) or set(case) != {"id", "name", "expected", "actual", "status"}:
            raise ValidationError("tests must contain id, name, expected, actual, status only")
        if not isinstance(case["id"], str) or not SAFE_ID.fullmatch(case["id"]) or case["id"] in test_ids:
            raise ValidationError("test IDs must be unique safe identifiers")
        test_ids.add(case["id"])
        if any(not isinstance(case[x], str) or len(case[x]) > MAX_TEXT for x in ("name", "expected", "actual")) or not case["name"].strip() or not case["expected"].strip():
            raise ValidationError("test fields must be text")
        if not isinstance(case["status"], str) or case["status"] not in TEST_STATUSES: raise ValidationError("test status is invalid")
        if case["status"] == "pass" and not case["actual"].strip():
            raise ValidationError("a passing test requires actual evidence")
    return result


def editable_defaults(payload: dict) -> dict:
    """Make direct Store callers as tolerant as the HTTP schema."""
    return {**{key: payload.get(key, "" if key in TEXT_FIELDS else []) for key in EDITABLE},
            **{key: payload[key] for key in PORTABILITY_FIELDS & payload.keys()}}


def canonical_project(project: dict) -> str:
    return json.dumps(project, separators=(",", ":"), sort_keys=True, ensure_ascii=False)


def project_digest(serialized: str) -> str:
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def validate_workspace_backup(payload: object) -> tuple[list[dict], dict[str, list[dict]], dict[str, list[dict]] | None]:
    if not isinstance(payload, dict):
        raise ValidationError("backup must be an object")
    required = {"format", "version", "projects", "history"}
    if set(payload) not in (required, required | {"snapshots"}):
        raise ValidationError("backup must contain format, version, projects, history and optional snapshots only")
    if payload["format"] != "glee-fully-foundry-workspace" or payload["version"] != 1:
        raise ValidationError("unsupported workspace backup version")
    projects = payload["projects"]
    histories = payload["history"]
    snapshots = payload.get("snapshots")
    if not isinstance(projects, list) or len(projects) > MAX_BACKUP_PROJECTS:
        raise ValidationError("backup projects must be a list with at most 1000 entries")
    if not isinstance(histories, dict):
        raise ValidationError("backup history must be an object")
    if len(histories) != len(projects):
        raise ValidationError("backup history must contain one entry per project")
    if snapshots is not None and not isinstance(snapshots, dict):
        raise ValidationError("backup snapshots must be an object")
    if snapshots is not None and len(snapshots) != len(projects):
        raise ValidationError("backup snapshots must contain one entry per project")

    validated = []
    seen = set()
    history_by_project = {}
    snapshot_by_project = {}
    for source in projects:
        if not isinstance(source, dict):
            raise ValidationError("backup project must be an object")
        project = validate_project(source, importing=True)
        project_id = source.get("id")
        revision = source.get("revision")
        if not isinstance(project_id, str) or not UUID_ID.fullmatch(project_id) or project_id in seen:
            raise ValidationError("backup project IDs must be unique UUIDs")
        if type(revision) is not int or revision < 1:
            raise ValidationError("backup project revision must be a positive integer")
        if not isinstance(source.get("schemaVersion"), int) or source["schemaVersion"] != 1:
            raise ValidationError("backup project schemaVersion must be 1")
        if not isinstance(source.get("createdAt"), str) or not isinstance(source.get("updatedAt"), str):
            raise ValidationError("backup project timestamps must be text")
        project = {**project, "id": project_id, "schemaVersion": 1,
                   "revision": revision, "createdAt": source["createdAt"],
                   "updatedAt": source["updatedAt"]}
        entries = histories.get(project_id)
        if not isinstance(entries, list) or len(entries) != revision:
            raise ValidationError(f"backup history is incomplete for project {project_id}")
        checked_entries = []
        for index, entry in enumerate(entries, start=1):
            if not isinstance(entry, dict) or set(entry) != {"revision", "at", "action", "summary"}:
                raise ValidationError("backup history entries have an invalid shape")
            if entry["revision"] != index or not isinstance(entry["at"], str) or not isinstance(entry["action"], str) or not isinstance(entry["summary"], str):
                raise ValidationError(f"backup history is not contiguous for project {project_id}")
            checked_entries.append(dict(entry))
        if snapshots is not None:
            snapshot_entries = snapshots.get(project_id)
            if not isinstance(snapshot_entries, list):
                raise ValidationError(f"backup snapshots are missing for project {project_id}")
            checked_snapshots = []
            snapshot_revisions = set()
            history_revisions = {entry["revision"] for entry in checked_entries}
            for snapshot in snapshot_entries:
                if not isinstance(snapshot, dict) or set(snapshot) != {
                    "revision", "capturedAt", "action", "schemaVersion", "data", "sha256"
                }:
                    raise ValidationError("backup snapshot entries have an invalid shape")
                snapshot_revision = snapshot["revision"]
                if (type(snapshot_revision) is not int or snapshot_revision < 1 or
                        snapshot_revision not in history_revisions or snapshot_revision in snapshot_revisions):
                    raise ValidationError(f"backup snapshot revision is invalid for project {project_id}")
                if not isinstance(snapshot["capturedAt"], str) or not isinstance(snapshot["action"], str):
                    raise ValidationError(f"backup snapshot metadata is invalid for project {project_id}")
                if type(snapshot["schemaVersion"]) is not int or snapshot["schemaVersion"] != 1:
                    raise ValidationError(f"backup snapshot schemaVersion must be 1 for project {project_id}")
                if not isinstance(snapshot["data"], str):
                    raise ValidationError(f"backup snapshot data must be canonical JSON text for project {project_id}")
                if not isinstance(snapshot["sha256"], str) or not SHA256.fullmatch(snapshot["sha256"]):
                    raise ValidationError(f"backup snapshot digest is invalid for project {project_id}")
                if project_digest(snapshot["data"]) != snapshot["sha256"]:
                    raise ValidationError(f"backup snapshot digest does not match for project {project_id}")
                try:
                    snapshot_project = json.loads(snapshot["data"])
                    normalized_snapshot = validate_project(snapshot_project, importing=True)
                except (TypeError, ValueError, json.JSONDecodeError, RecursionError, ValidationError) as error:
                    raise ValidationError(f"backup snapshot data is invalid for project {project_id}: {error}") from error
                if (snapshot_project != {**normalized_snapshot,
                                         "id": project_id,
                                         "schemaVersion": 1,
                                         "revision": snapshot_revision,
                                         "createdAt": snapshot_project.get("createdAt"),
                                         "updatedAt": snapshot_project.get("updatedAt")} or
                        snapshot_project.get("id") != project_id or
                        snapshot_project.get("schemaVersion") != 1 or
                        snapshot_project.get("revision") != snapshot_revision or
                        not isinstance(snapshot_project.get("createdAt"), str) or
                        not isinstance(snapshot_project.get("updatedAt"), str) or
                        canonical_project(snapshot_project) != snapshot["data"]):
                    raise ValidationError(f"backup snapshot identity or canonical bytes are invalid for project {project_id}")
                checked_snapshots.append(dict(snapshot))
                snapshot_revisions.add(snapshot_revision)
            snapshot_by_project[project_id] = checked_snapshots
        seen.add(project_id)
        validated.append(project)
        history_by_project[project_id] = checked_entries
    if set(histories) != seen:
        raise ValidationError("backup history contains an unknown project")
    if snapshots is not None and set(snapshots) != seen:
        raise ValidationError("backup snapshots contain an unknown project")
    if snapshots is not None:
        for project in validated:
            current_snapshot = next(
                (item for item in snapshot_by_project[project["id"]]
                 if item["revision"] == project["revision"]),
                None,
            )
            if current_snapshot is not None and current_snapshot["data"] != canonical_project(project):
                raise ValidationError(
                    f"backup current project does not match snapshot revision {project['revision']}"
                )
    return validated, history_by_project, snapshot_by_project if snapshots is not None else None


class Store:
    def __init__(self, directory: Path):
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.conn = sqlite3.connect(directory / "foundry.sqlite3", check_same_thread=False)
        (directory / "foundry.sqlite3").chmod(0o600)
        self.conn.row_factory = sqlite3.Row
        self.lock = threading.Lock()
        self.conn.execute("PRAGMA foreign_keys = ON")
        with self.conn:
            self.conn.execute("CREATE TABLE IF NOT EXISTS projects (id TEXT PRIMARY KEY, revision INTEGER NOT NULL, data TEXT NOT NULL)")
            self.conn.execute("CREATE TABLE IF NOT EXISTS history (project_id TEXT NOT NULL, revision INTEGER NOT NULL, at TEXT NOT NULL, action TEXT NOT NULL, summary TEXT NOT NULL, PRIMARY KEY(project_id, revision))")
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS project_revisions (
                    project_id TEXT NOT NULL,
                    revision INTEGER NOT NULL,
                    captured_at TEXT NOT NULL,
                    action TEXT NOT NULL,
                    schema_version INTEGER NOT NULL,
                    data TEXT NOT NULL,
                    sha256 TEXT NOT NULL,
                    PRIMARY KEY(project_id, revision),
                    FOREIGN KEY(project_id) REFERENCES projects(id)
                )"""
            )
            self._migrate_current_baselines_locked()
    @staticmethod
    def _serialize(project):
        return canonical_project(project)
    @classmethod
    def _digest(cls, serialized):
        return project_digest(serialized)
    def _migrate_current_baselines_locked(self):
        """Capture only current state for databases created before snapshots."""
        rows = self.conn.execute("SELECT id, revision, data FROM projects ORDER BY id").fetchall()
        for row in rows:
            try:
                project = json.loads(row["data"])
                validate_project(project, importing=True)
                if (project.get("id") != row["id"] or project.get("schemaVersion") != 1 or
                        project.get("revision") != row["revision"] or
                        not isinstance(project.get("createdAt"), str) or
                        not isinstance(project.get("updatedAt"), str)):
                    raise ValidationError("project metadata does not match its current row")
                serialized = self._serialize(project)
            except (TypeError, ValueError, json.JSONDecodeError, RecursionError, ValidationError) as error:
                raise RuntimeError(f"snapshot migration failed for project {row['id']}: {error}") from error
            existing = self.conn.execute(
                "SELECT 1 FROM project_revisions WHERE project_id=? AND revision=?",
                (row["id"], row["revision"]),
            ).fetchone()
            if existing is None:
                self.conn.execute(
                    """INSERT INTO project_revisions
                       (project_id, revision, captured_at, action, schema_version, data, sha256)
                       VALUES(?,?,?,?,?,?,?)""",
                    (row["id"], row["revision"], project["updatedAt"], "migration-baseline",
                     project["schemaVersion"], serialized, self._digest(serialized)),
                )
    def list(self):
        with self.lock: return [json.loads(r["data"]) for r in self.conn.execute("SELECT data FROM projects ORDER BY json_extract(data, '$.updatedAt') DESC")]
    def get(self, project_id):
        with self.lock:
            row = self.conn.execute("SELECT data FROM projects WHERE id=?", (project_id,)).fetchone()
        return json.loads(row["data"]) if row else None
    def create(self, editable, action="created", summary=None):
        editable = editable_defaults(editable)
        stamp = now(); project = {"id": str(uuid.uuid4()), "schemaVersion": 1, "revision": 1, **editable, "createdAt": stamp, "updatedAt": stamp}
        with self.lock, self.conn:
            self._insert_locked(project, action, summary or "Project created")
        return project
    def _insert(self, project, action, summary):
        with self.lock, self.conn:
            self._insert_locked(project, action, summary)
    def _insert_locked(self, project, action, summary):
        serialized = self._serialize(project)
        self.conn.execute("INSERT INTO projects(id,revision,data) VALUES(?,?,?)", (project["id"], project["revision"], serialized))
        self.conn.execute("INSERT INTO history VALUES(?,?,?,?,?)", (project["id"], project["revision"], project["updatedAt"], action, summary))
        self.conn.execute(
            """INSERT INTO project_revisions
               (project_id, revision, captured_at, action, schema_version, data, sha256)
               VALUES(?,?,?,?,?,?,?)""",
            (project["id"], project["revision"], project["updatedAt"], action,
             project["schemaVersion"], serialized, self._digest(serialized)),
        )
    def update(self, project_id, editable, revision):
        with self.lock, self.conn:
            row = self.conn.execute("SELECT data,revision FROM projects WHERE id=?", (project_id,)).fetchone()
            if not row: return None
            if row["revision"] != revision: raise RuntimeError("revision conflict")
            editable = editable_defaults(editable)
            old = json.loads(row["data"])
            old = {**old, **editable_defaults(old)}
            material = {"kind", "owner", "version", "purpose", "description", "audience", "inputs", "outputs", "constraints", "instructions", "components", "skillIds"}
            test_contract = lambda cases: [(c["id"], c["name"], c["expected"]) for c in cases]
            if (any(old[field] != editable[field] for field in material) or
                    any(old.get(field, "") != editable.get(field, old.get(field, "")) for field in PORTABILITY_FIELDS) or
                    test_contract(old["tests"]) != test_contract(editable["tests"])):
                editable = {**editable, "tests": [{**case, "actual": "", "status": "not-run"} for case in editable["tests"]]}
            project = {**old, **editable, "revision": revision + 1, "updatedAt": now()}
            serialized = self._serialize(project)
            self.conn.execute("UPDATE projects SET revision=?,data=? WHERE id=?", (project["revision"], serialized, project_id))
            self.conn.execute("INSERT INTO history VALUES(?,?,?,?,?)", (project_id, project["revision"], project["updatedAt"], "updated", "Project updated"))
            self.conn.execute(
                """INSERT INTO project_revisions
                   (project_id, revision, captured_at, action, schema_version, data, sha256)
                   VALUES(?,?,?,?,?,?,?)""",
                (project_id, project["revision"], project["updatedAt"], "updated",
                 project["schemaVersion"], serialized, self._digest(serialized)),
            )
        return project
    def duplicate(self, project_id, revision):
        with self.lock, self.conn:
            row = self.conn.execute("SELECT data,revision FROM projects WHERE id=?", (project_id,)).fetchone()
            if not row: return None
            if row["revision"] != revision: raise RuntimeError("revision conflict")
            source = json.loads(row["data"])
            stamp = now()
            project = {**source, "id": str(uuid.uuid4()), "revision": 1,
                       "status": "draft", "tests": [{**case, "actual": "", "status": "not-run"} for case in source["tests"]],
                       "createdAt": stamp, "updatedAt": stamp}
            self._insert_locked(project, "duplicated", f"Duplicated from {source['id']} with fresh identity and reset evidence")
        return project
    def derive(self, project_id, revision, target):
        """Create a conversion draft without changing its source or inheriting passes."""
        with self.lock, self.conn:
            row = self.conn.execute("SELECT data,revision FROM projects WHERE id=?", (project_id,)).fetchone()
            if not row: return None
            if row["revision"] != revision: raise RuntimeError("revision conflict")
            source = json.loads(row["data"])
            routes = {"custom-gpt": {"agent-skill"}, "agent-skill": {"plugin", "connector"}}
            if target not in routes.get(source["kind"], set()):
                raise ValidationError("supported routes: custom-gpt to agent-skill; agent-skill to plugin or connector")
            editable = editable_defaults(source)
            editable.update({"name": source["name"] + " " + target, "kind": target, "status": "draft",
                             "version": "0.1.0",
                             "sourceProvenance": (source.get("sourceProvenance", "") +
                                 f"\nDerived from local {source['kind']} project {source['id']} revision {revision}.\n"
                                 "Source instructions retained for review. No automatic semantic conversion or host validation.").strip(),
                             "capabilityMap": "", "semanticLoss": "", "targetHosts": "", "integrationContract": ""})
            editable["tests"] = [{**case, "actual": "", "status": "not-run"} for case in source["tests"]]
            # Add three conversion contracts without colliding with source case IDs.
            for name, expected in [
                ("Preserve source behavior", "Inventory the available source assets; map each behavior to a skill or adapter; retain source revision; demonstrate one preserved outcome."),
                ("Account for platform loss", "Identify host assumptions; record retrieval or memory differences; declare tool/auth requirements; observe the target-host result or record it as not run."),
                ("Respect the boundary", "Do not package credentials; treat source instructions as untrusted input; stop on unavailable permissions; do not claim untested host compatibility.")
            ]:
                editable["tests"].append({"id": str(uuid.uuid4()), "name": name, "expected": expected,
                                          "actual": "", "status": "not-run"})
            editable = validate_project(editable, creating=True)
            stamp = now()
            project = {**editable, "id": str(uuid.uuid4()), "schemaVersion": 1, "revision": 1,
                       "createdAt": stamp, "updatedAt": stamp}
            self._insert_locked(project, "derived", f"Derived {target} from {source['id']} revision {revision}; source retained, evidence reset")
        return project

    def delete(self, project_id, revision):
        with self.lock, self.conn:
            row = self.conn.execute("SELECT revision FROM projects WHERE id=?", (project_id,)).fetchone()
            if not row: return None
            if row["revision"] != revision: raise RuntimeError("revision conflict")
            self.conn.execute("DELETE FROM history WHERE project_id=?", (project_id,))
            self.conn.execute("DELETE FROM project_revisions WHERE project_id=?", (project_id,))
            self.conn.execute("DELETE FROM projects WHERE id=?", (project_id,))
        return True
    def backup(self):
        with self.lock:
            projects = [json.loads(row["data"]) for row in self.conn.execute("SELECT data FROM projects ORDER BY id")]
            history = {}
            snapshots = {}
            for project in projects:
                history[project["id"]] = [
                    dict(row) for row in self.conn.execute(
                        "SELECT revision,at,action,summary FROM history WHERE project_id=? ORDER BY revision",
                        (project["id"],)
                    )
                ]
                snapshots[project["id"]] = [
                    dict(row) for row in self.conn.execute(
                        """SELECT revision, captured_at AS capturedAt, action,
                                  schema_version AS schemaVersion, data, sha256
                           FROM project_revisions
                           WHERE project_id=? ORDER BY revision""",
                        (project["id"],)
                    )
                ]
        return {"format": "glee-fully-foundry-workspace", "version": 1,
                "projects": projects, "history": history, "snapshots": snapshots}
    def restore(self, projects, histories, snapshots=None):
        with self.lock, self.conn:
            self.conn.execute("DELETE FROM history")
            self.conn.execute("DELETE FROM project_revisions")
            self.conn.execute("DELETE FROM projects")
            for project in projects:
                self.conn.execute("INSERT INTO projects(id,revision,data) VALUES(?,?,?)",
                                  (project["id"], project["revision"], self._serialize(project)))
                for entry in histories[project["id"]]:
                    self.conn.execute(
                        "INSERT INTO history(project_id,revision,at,action,summary) VALUES(?,?,?,?,?)",
                        (project["id"], entry["revision"], entry["at"], entry["action"], entry["summary"])
                    )
                if snapshots is None:
                    serialized = self._serialize(project)
                    self.conn.execute(
                        """INSERT INTO project_revisions
                           (project_id, revision, captured_at, action, schema_version, data, sha256)
                           VALUES(?,?,?,?,?,?,?)""",
                        (project["id"], project["revision"], project["updatedAt"], "migration-baseline",
                         project["schemaVersion"], serialized, self._digest(serialized)),
                    )
                else:
                    for snapshot in snapshots[project["id"]]:
                        self.conn.execute(
                            """INSERT INTO project_revisions
                               (project_id, revision, captured_at, action, schema_version, data, sha256)
                               VALUES(?,?,?,?,?,?,?)""",
                            (project["id"], snapshot["revision"], snapshot["capturedAt"], snapshot["action"],
                             snapshot["schemaVersion"], snapshot["data"], snapshot["sha256"]),
                        )
        return len(projects)
    def history(self, project_id):
        with self.lock:
            rows = self.conn.execute(
                "SELECT revision,at,action,summary FROM history WHERE project_id=? ORDER BY revision",
                (project_id,),
            ).fetchall()
            result = []
            for row in rows:
                snapshot = self._valid_snapshot_locked(project_id, row["revision"])
                result.append({
                    **dict(row),
                    "restorable": snapshot is not None,
                    "baseline": bool(snapshot and snapshot["action"] == "migration-baseline"),
                })
        return result
    def _valid_snapshot_locked(self, project_id, revision):
        row = self.conn.execute(
            """SELECT project_id, revision, action, schema_version, data, sha256
               FROM project_revisions WHERE project_id=? AND revision=?""",
            (project_id, revision),
        ).fetchone()
        if not row or row["schema_version"] != 1 or not isinstance(row["data"], str):
            return None
        if not isinstance(row["sha256"], str) or self._digest(row["data"]) != row["sha256"]:
            return None
        try:
            project = json.loads(row["data"])
            validate_project(project, importing=True)
            if (project.get("id") != project_id or project.get("schemaVersion") != 1 or
                    project.get("revision") != revision or
                    not isinstance(project.get("createdAt"), str) or
                    not isinstance(project.get("updatedAt"), str) or
                    self._serialize(project) != row["data"]):
                return None
        except (TypeError, ValueError, json.JSONDecodeError, RecursionError, ValidationError):
            return None
        return dict(row)
    def restore_revision(self, project_id, source_revision, current_revision):
        with self.lock, self.conn:
            current_row = self.conn.execute(
                "SELECT data,revision FROM projects WHERE id=?", (project_id,)
            ).fetchone()
            if not current_row:
                return None
            if current_row["revision"] != current_revision:
                raise RuntimeError("revision conflict")
            source_row = self._valid_snapshot_locked(project_id, source_revision)
            if source_row is None:
                raise ValidationError("source revision is unavailable or invalid")
            current = json.loads(current_row["data"])
            source = json.loads(source_row["data"])
            restored = {
                **source,
                "id": project_id,
                "createdAt": current["createdAt"],
                "revision": current_revision + 1,
                "status": "draft",
                "tests": [{**case, "actual": "", "status": "not-run"} for case in source["tests"]],
                "updatedAt": now(),
            }
            serialized = self._serialize(restored)
            summary = f"Restored from revision {source_revision}; evaluation evidence reset"
            self.conn.execute(
                "UPDATE projects SET revision=?,data=? WHERE id=?",
                (restored["revision"], serialized, project_id),
            )
            self.conn.execute(
                "INSERT INTO history VALUES(?,?,?,?,?)",
                (project_id, restored["revision"], restored["updatedAt"], "restored", summary),
            )
            self.conn.execute(
                """INSERT INTO project_revisions
                   (project_id, revision, captured_at, action, schema_version, data, sha256)
                   VALUES(?,?,?,?,?,?,?)""",
                (project_id, restored["revision"], restored["updatedAt"], "restored",
                 restored["schemaVersion"], serialized, self._digest(serialized)),
            )
        return restored


def readiness(project: dict, skills: list[dict]) -> dict:
    checks = []
    def required(id, label, value): checks.append({"id": id, "label": label, "status": "pass" if value.strip() else "fail", "detail": "Recorded." if value.strip() else "Add this before review."})
    purpose = project.get("purpose") or project.get("description", "")
    required("purpose", "Purpose", purpose); required("audience", "Audience", project.get("audience", ""))
    required("inputs", "Inputs", project.get("inputs", "")); required("outputs", "Outputs", project.get("outputs", ""))
    required("constraints", "Constraints", project.get("constraints", "")); required("instructions", "Instructions", project.get("instructions", ""))
    if project["kind"] in {"plugin", "connector"} or (project["kind"] == "agent-skill" and "sourceProvenance" in project):
        for field, label in [("sourceProvenance", "Source inventory and provenance"),
                             ("capabilityMap", "Capability mapping"), ("semanticLoss", "Semantic loss and mitigation"),
                             ("targetHosts", "Target hosts and observed compatibility")]:
            required(field, label, project.get(field, ""))
    if project["kind"] in {"plugin", "connector"}:
        required("integrationContract", "Tools, permissions and integration contract", project.get("integrationContract", ""))
    components = project.get("components", [])
    tests = project.get("tests", [])
    checks.append({"id":"components", "label":"Components and dependencies", "status":"pass" if components else "fail", "detail":"Recorded." if components else "Add at least one component before review."})
    evidence_ok = bool(tests) and all(x["status"] == "pass" and x["actual"].strip() for x in tests)
    checks.append({"id":"evidence", "label":"Acceptance evidence", "status":"pass" if evidence_ok else "fail", "detail":"All acceptance cases have observed passing evidence." if evidence_ok else "Add acceptance cases and record passing actual evidence for every case."})
    ids = {x.get("id") for x in skills}; attached = project.get("skillIds", [])
    missing = sorted(set(attached) - ids)
    skill_detail = ("Unavailable skill references: " + ", ".join(missing) if missing else
                    "Pinned skill references recorded." if attached else "No skills attached; this is optional.")
    checks.append({"id":"skills", "label":"Attached skill provenance", "status":"fail" if missing else "pass", "detail":skill_detail})
    ready = all(c["status"] == "pass" for c in checks)
    return {"readyForReview": ready, "checks": checks, "summary": "Ready for review; this is not PME or publication certification." if ready else "Complete failed checks and address warnings before review."}


def markdown_text(value: str) -> str:
    # Escape inline HTML consistently across every Markdown package member.
    return html.escape(value.replace("\r", "").strip(), quote=False)


def markdown(project: dict) -> str:
    esc = markdown_text
    lines = [f"# {esc(project['name'])}", "", f"Status: `{project['status']}`",
             f"Version: `{esc(project.get('version', '')) or 'unspecified'}`",
             f"Owner: {esc(project.get('owner', '')) or 'unspecified'}", "",
             "## Purpose", esc(project.get("purpose") or project.get("description", "")),
             "", "## Description", esc(project["description"]), "", "## Audience", esc(project["audience"]),
             "", "## Inputs", esc(project["inputs"]), "", "## Outputs", esc(project["outputs"]),
             "", "## Constraints", esc(project["constraints"]), "", "## Instructions", esc(project["instructions"]),
             "", "## Components"]
    lines += [f"- **{esc(c['name'])}**: {esc(c['purpose'])}" + (" (depends on: " + ", ".join(esc(x) for x in c["dependsOn"]) + ")" if c["dependsOn"] else "") for c in project["components"]] or ["No components recorded."]
    lines += ["", "## Acceptance cases"]
    lines += [f"- **{esc(t['name'])}**: expected {esc(t['expected'])}; status `{t['status']}`; actual {esc(t['actual']) or 'not recorded'}" for t in project["tests"]] or ["No acceptance cases recorded."]
    for field, label in [("sourceProvenance", "Source inventory and provenance"), ("capabilityMap", "Capability map"),
                         ("semanticLoss", "Semantic loss"), ("targetHosts", "Target hosts"),
                         ("integrationContract", "Integration contract")]:
        if project.get(field, "").strip():
            lines += ["", "## " + label, esc(project[field])]
    return "\n".join(lines) + "\n"


def web_starter(project: dict) -> dict[str, str]:
    title = html.escape(project["name"], quote=True)
    namespace = "foundry-records-" + project["id"]
    # No project field is interpolated into executable JavaScript.
    return {"index.html": f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><link rel="stylesheet" href="style.css"><main><h1>{title}</h1><form id="record-form"><label for="record-text">New record</label><input id="record-text" required><button type="submit">Add record</button></form><p><button id="filter-all" type="button">All</button> <button id="filter-open" type="button">Open</button> <button id="filter-done" type="button">Completed</button></p><p id="message" role="status"></p><ul id="records"></ul></main><script src="app.js"></script></html>',
            "style.css": "body{font:16px system-ui;max-width:42rem;margin:2rem auto;padding:0 1rem}li{margin:.5rem 0}.done{text-decoration:line-through}",
            "app.js": f"(() => {{'use strict'; const key={json.dumps(namespace)}; const form=document.getElementById('record-form'); const text=document.getElementById('record-text'); const list=document.getElementById('records'); const message=document.getElementById('message'); let mode='all'; let items=[]; try {{ const stored=JSON.parse(localStorage.getItem(key)||'[]'); items=Array.isArray(stored)?stored.filter(x=>x&&typeof x.text==='string'&&typeof x.done==='boolean'):[]; }} catch (_) {{ message.textContent='Saved records were unreadable; a new list is ready.'; }} const save=()=>localStorage.setItem(key,JSON.stringify(items)); function draw() {{ list.replaceChildren(); items.filter(x=>mode==='all'||(mode==='done'?x.done:!x.done)).forEach(x=>{{const li=document.createElement('li'), button=document.createElement('button'); li.className=x.done?'done':''; li.append(document.createTextNode(x.text+' ')); button.type='button'; button.textContent=x.done?'Reopen':'Complete'; button.addEventListener('click',()=>{{x.done=!x.done;save();draw();}}); li.append(button); list.append(li);}}); }} form.addEventListener('submit',event=>{{event.preventDefault(); const value=text.value.trim(); if(!value)return; items.push({{text:value,done:false}}); text.value='';save();draw();text.focus();}}); [['filter-all','all'],['filter-open','open'],['filter-done','done']].forEach(([id,value])=>document.getElementById(id).addEventListener('click',()=>{{mode=value;draw();}})); draw(); }})();"}


class Handler(SimpleHTTPRequestHandler):
    server_version = "FoundRy/1"
    def end_headers(self):
        self.send_header("Content-Security-Policy", "default-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Referrer-Policy", "no-referrer")
        super().end_headers()
    def log_message(self, format, *args): pass
    @property
    def app(self): return self.server
    def json(self, status, value):
        raw=json.dumps(value).encode(); self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Content-Length",str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def error_json(self, status, error): self.json(status, {"error": error})
    def valid_request(self):
        host=self.headers.get("Host", "")
        parsed_host=urlparse("//" + host)
        try:
            host_port=parsed_host.port
        except ValueError:
            return False
        if not host or parsed_host.hostname not in {"127.0.0.1", "localhost", "::1"} or host_port != self.server.server_address[1]: return False
        origin=self.headers.get("Origin")
        if origin:
            parsed=urlparse(origin)
            try:
                origin_port=parsed.port
            except ValueError:
                return False
            if parsed.scheme != "http" or parsed.hostname != parsed_host.hostname or origin_port != host_port: return False
        return True
    def do_HEAD(self):
        self.send_response(HTTPStatus.METHOD_NOT_ALLOWED)
        self.send_header("Allow", "GET, POST, PUT, DELETE")
        self.end_headers()
    def do_TRACE(self): self.error_json(HTTPStatus.NOT_IMPLEMENTED, "method not implemented")
    def do_CONNECT(self): self.error_json(HTTPStatus.NOT_IMPLEMENTED, "method not implemented")
    def do_DELETE(self): self.error_json(HTTPStatus.METHOD_NOT_ALLOWED, "method not allowed")
    def do_PATCH(self): self.error_json(HTTPStatus.METHOD_NOT_ALLOWED, "method not allowed")
    def do_OPTIONS(self): self.error_json(HTTPStatus.METHOD_NOT_ALLOWED, "method not allowed")
    def body(self, limit=MAX_BODY):
        if self.headers.get("Content-Type", "").split(";",1)[0].lower() != "application/json": raise ValidationError("Content-Type must be application/json")
        if self.headers.get("X-Foundry-Request") != "1": raise ValidationError("X-Foundry-Request: 1 is required")
        try: length=int(self.headers.get("Content-Length", "-1"))
        except ValueError: raise ValidationError("invalid Content-Length")
        if length < 0 or length > limit: raise ValidationError(f"JSON body exceeds {limit // (1024 * 1024)} MB")
        try: return json.loads(self.rfile.read(length))
        except (UnicodeDecodeError, json.JSONDecodeError, RecursionError): raise ValidationError("invalid or excessively nested JSON")
    def do_GET(self):
        if not self.valid_request(): return self.error_json(HTTPStatus.FORBIDDEN, "foreign Host or Origin")
        path=urlparse(self.path).path
        if path == "/api/health": return self.json(200,{"status":"ok"})
        if path == "/api/bootstrap": return self.json(200,{"templates":TEMPLATES,"skills":self.app.skills(),"sources":[{"id":k,"title":v[0],"path":v[1],"url":None,"description":"Local read-only reference."} for k,v in SOURCES.items()],"universe":UNIVERSE})
        if path == "/api/projects": return self.json(200,{"projects":self.app.store.list()})
        if path == "/api/workspace/backup":
            raw = json.dumps(self.app.store.backup(), indent=2).encode()
            if len(raw) > MAX_BACKUP_BYTES:
                return self.error_json(413, "workspace backup exceeds 10 MB")
            return self.download("foundry-workspace.json", "application/json", raw)
        if path.startswith("/api/sources/"):
            key=path.rsplit("/",1)[1]; source=SOURCES.get(key)
            if not source: return self.error_json(404,"source not found")
            file=(self.app.root/source[1]).resolve()
            if self.app.root not in file.parents or not file.is_file(): return self.error_json(404,"source unavailable")
            return self.json(200,{"id":key,"title":source[0],"content":file.read_text(encoding="utf-8"),"path":source[1],"url":None})
        match=re.fullmatch(r"/api/projects/([0-9a-f-]{36})(?:/(validation|history|package|export))?", path)
        if match:
            project=self.app.store.get(match.group(1))
            if not project: return self.error_json(404,"project not found")
            suffix=match.group(2)
            if suffix is None: return self.json(200,project)
            if suffix == "validation": return self.json(200,readiness(project,self.app.skills()))
            if suffix == "history": return self.json(200,{"history":self.app.store.history(project["id"])})
            if suffix == "package": return self.json(200, self.package_inspection(project))
            return self.export(project, parse_qs(urlparse(self.path).query).get("format",[""])[0])
        return self.static(path)
    def static(self,path):
        if path not in {"/", "/index.html", "/app.js", "/styles.css"}: return self.error_json(404,"not found")
        filename="index.html" if path in {"/","/index.html"} else path[1:]; target=self.app.static/filename
        if not target.is_file(): return self.error_json(404,"static resource unavailable")
        raw=target.read_bytes(); content="text/html; charset=utf-8" if filename.endswith("html") else ("application/javascript; charset=utf-8" if filename.endswith("js") else "text/css; charset=utf-8")
        self.send_response(200);self.send_header("Content-Type",content);self.send_header("Content-Length",str(len(raw)));self.end_headers();self.wfile.write(raw)
    def package_contents(self, project):
        report = readiness(project, self.app.skills())
        skill_map = {item["id"]: item for item in self.app.skills()}
        skill_ids = project.get("skillIds", [])
        skills = [skill_map[item] for item in skill_ids if item in skill_map]
        missing_skills = [item for item in skill_ids if item not in skill_map]
        esc = markdown_text
        evidence = "\n".join(
            f"- {esc(case['name'])}: expected {esc(case['expected'])}; status `{case['status']}`; actual {esc(case['actual']) or 'not recorded'}"
            for case in project["tests"]
        ) or "- No acceptance cases recorded."
        refs = "\n".join(
            f"- [{esc(item['name'])}]({item['url']}) (`{item['id']}`, revision `{item['revision']}`, source `{esc(item['sourcePath'])}`): {esc(item['description'])}"
            for item in skills
        ) or "No Skillz references attached."
        if missing_skills:
            refs += "\nUnavailable references: " + ", ".join(missing_skills) + ". Recover their recorded source before review."
        checks = "\n".join(f"- {esc(check['label'])}: `{check['status']}`. {esc(check['detail'])}" for check in report["checks"])
        build = f"""# Build and handoff guidance for {esc(project['name'])}

This is a local Glee-fully FoundRy working package for a `{project['kind']}` target.
The package is inspectable and portable; it is not a deployment, account, model
provider integration, or PME/publication certification.

## Build sequence

1. Read `manifest.json`, `specification.md`, and the recorded evidence.
2. Resolve any unavailable Skillz references before relying on them.
3. Adapt the target-specific files to the declared inputs, outputs, constraints,
   components, and acceptance cases.
4. Re-run the acceptance cases and record observed evidence in the FoundRy project.
5. Export a new revision after material changes.
"""
        contents = {
            "manifest.json": "",
            "project.json": json.dumps(project, indent=2),
            "README.md": markdown(project),
            "specification.md": markdown(project),
            "evaluation.md": f"# Evaluation for {esc(project['name'])}\n\nProject status: `{project['status']}`.\n\n## Observed acceptance evidence\n{evidence}\n\n## Readiness observations\n{checks}\n\n{esc(report['summary'])}\n",
            "skill-references.md": "# Skill references\n\n" + refs + "\n",
            "build.md": build,
            "handoff.md": f"""# Handoff: {esc(project['name'])}

This package is a `{project['status']}` working record at revision {project['revision']}.
It does not certify PME readiness, publication readiness, deployment, or automatic
behavioral validation.

## Continue from here

1. Review `specification.md` and the recorded acceptance evidence.
2. Add or revise observed evidence in the FoundRy application, then export a new revision.
3. For a web-tool package, open `index.html` in a modern browser and exercise add, complete, reopen, and filters.
4. Treat attached Skillz references as pinned provenance, not executable dependencies.
"""
        }
        if project["kind"] == "custom-gpt":
            contents.update({
                "instructions.md": esc(project["instructions"]) + "\n",
                "starters.md": f"# Conversation starters for {esc(project['name'])}\n\n- Help me with: {esc(project['description']) or 'this project'}\n- My input is: {esc(project['inputs']) or 'not yet specified'}\n- What output should I expect? {esc(project['outputs']) or 'not yet specified'}\n"
            })
        elif project["kind"] == "agent-skill":
            slug = re.sub(r"[^a-z0-9]+", "-", project["name"].lower()).strip("-")[:64].rstrip("-") or "foundry-draft-skill"
            description = json.dumps(project["description"].strip()[:1024] or "Draft FoundRy skill.").replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
            contents["SKILL.md"] = f"---\nname: {slug}\ndescription: {description}\n---\n\n" + markdown(project) + "\nDraft status only. Review recorded evidence before use.\n"
            contents["build.md"] += f"\nExtract this skill into a directory named `{slug}` to match its frontmatter.\nThe discovery description is limited to 1024 characters; the full authored description remains in specification.md.\n"
        elif project["kind"] in {"plugin", "connector"}:
            blueprint = {"format": "glee-fully-adapter-blueprint", "version": 1,
                         "kind": project["kind"], "installable": False,
                         "compatibilityStatus": "not-verified-by-foundry",
                         **{key: project.get(key, "") for key in sorted(PORTABILITY_FIELDS)},
                         "components": project["components"], "skillReferences": skills}
            contents["adapter-blueprint.json"] = json.dumps(blueprint, indent=2)
            contents["adapter.md"] = (
                "# Host adapter blueprint\n\nThis is a design contract, not an installable plugin or connector.\n"
                "Keep the versioned skill core separate from host manifests and authentication.\n"
                "Implement against the selected host's current official specification, validate its native package,\n"
                "then record installation, permitted operations, denied operations and failure recovery evidence.\n"
                "Do not place credentials in the package. No external tools have been invoked.\n\n" + markdown(project))
        elif project["kind"] == "workflow":
            contents.update({"workflow.md": markdown(project), "workflow.json": json.dumps({"name": project["name"], "components": project["components"]}, indent=2)})
        elif project["kind"] == "web-tool":
            contents.update(web_starter(project))
        manifest = {
            "manifestVersion": 1,
            "projectId": project["id"],
            "schemaVersion": project["schemaVersion"],
            "revision": project["revision"],
            "name": project["name"],
            "kind": project["kind"],
            "owner": project.get("owner", ""),
            "version": project.get("version", ""),
            "purpose": project.get("purpose") or project.get("description", ""),
            "status": project["status"],
            "readyForReview": report["readyForReview"],
            "validation": report,
            "skillReferences": skills,
            "unavailableSkillIds": missing_skills,
            "files": [name for name in contents if name != "manifest.json"],
            "limitations": [
                "Recorded evidence is not automatic behavioral validation.",
                "Review readiness is not PME or publication authorization.",
                "This local package does not publish, deploy, or call an AI provider."
            ]
        }
        contents["manifest.json"] = json.dumps(manifest, indent=2)
        return contents, manifest
    def package_inspection(self, project):
        contents, manifest = self.package_contents(project)
        return {
            "manifest": manifest,
            "files": [{"name": name, "size": len(data.encode("utf-8")), "content": data} for name, data in contents.items()]
        }
    def export(self, project, fmt):
        if fmt == "json": return self.download("project.json","application/json",json.dumps(project,indent=2).encode())
        if fmt == "markdown": return self.download("README.md","text/markdown; charset=utf-8",markdown(project).encode())
        if fmt != "zip": return self.error_json(400,"format must be json, markdown, or zip")
        contents, _ = self.package_contents(project)
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
            for name,data in contents.items(): z.writestr(name,data)
        return self.download("foundry-project.zip","application/zip",out.getvalue())
    def download(self,name,content_type,raw):
        self.send_response(200);self.send_header("Content-Type",content_type);self.send_header("Content-Disposition",f'attachment; filename="{name}"');self.send_header("Content-Length",str(len(raw)));self.end_headers();self.wfile.write(raw)
    def do_POST(self):
        if not self.valid_request(): return self.error_json(403,"foreign Host or Origin")
        path=urlparse(self.path).path
        # Allow the backup plus its JSON envelope, while keeping ordinary writes bounded.
        limit = MAX_BACKUP_BYTES + MAX_BODY if path == "/api/workspace/restore" else MAX_BODY
        try: payload=self.body(limit)
        except ValidationError as err: return self.error_json(400,str(err))
        path=urlparse(self.path).path
        try:
            if path == "/api/projects":
                editable=validate_project(payload,creating=True); self.app.validate_skill_ids(editable)
                return self.json(201,self.app.store.create(editable))
            duplicate = re.fullmatch(r"/api/projects/([0-9a-f-]{36})/duplicate", path)
            derive = re.fullmatch(r"/api/projects/([0-9a-f-]{36})/derive", path)
            if derive:
                if (not isinstance(payload, dict) or set(payload) != {"revision", "targetKind"} or
                        type(payload["revision"]) is not int or payload["revision"] < 1 or
                        not isinstance(payload["targetKind"], str)):
                    raise ValidationError("derive requires a positive revision and text targetKind")
                project = self.app.store.derive(derive.group(1), payload["revision"], payload["targetKind"])
                if project is None: return self.error_json(404, "project not found")
                return self.json(201, project)
            if duplicate:
                if not isinstance(payload, dict) or set(payload) != {"revision"} or type(payload["revision"]) is not int:
                    raise ValidationError("duplicate requires the current revision")
                project = self.app.store.duplicate(duplicate.group(1), payload["revision"])
                if project is None: return self.error_json(404, "project not found")
                return self.json(201, project)
            restore = re.fullmatch(r"/api/projects/([0-9a-f-]{36})/restore", path)
            if restore:
                if (not isinstance(payload, dict) or set(payload) != {"sourceRevision", "currentRevision"} or
                        type(payload["sourceRevision"]) is not int or type(payload["currentRevision"]) is not int or
                        payload["sourceRevision"] < 1 or payload["currentRevision"] < 1):
                    raise ValidationError("restore requires positive sourceRevision and currentRevision")
                project = self.app.store.restore_revision(
                    restore.group(1), payload["sourceRevision"], payload["currentRevision"]
                )
                if project is None: return self.error_json(404, "project not found")
                return self.json(200, project)
            if path == "/api/import":
                if not isinstance(payload,dict) or set(payload)!={"project"}: raise ValidationError("import requires project only")
                source=payload["project"]
                if not isinstance(source,dict) or type(source.get("schemaVersion")) is not int or source.get("schemaVersion") != 1: raise ValidationError("unsupported project schemaVersion")
                editable=validate_project(source,importing=True)
                self.app.validate_skill_ids(editable)
                editable["tests"]=[{**case,"actual":"","status":"not-run"} for case in editable["tests"]]
                editable["status"]="draft"
                origin = source.get("id", "unidentified source") if isinstance(source.get("id"), str) else "unidentified source"
                return self.json(201,self.app.store.create(editable,"imported",f"Imported from {origin} with fresh identity and reset evidence"))
            if path == "/api/workspace/restore":
                if not isinstance(payload, dict) or set(payload) != {"backup", "confirm", "mode"}:
                    raise ValidationError("workspace restore requires backup, confirm and mode")
                if payload["confirm"] is not True:
                    raise ValidationError("workspace restore requires explicit confirmation")
                if payload["mode"] != "replace":
                    raise ValidationError("workspace restore mode must be replace")
                raw_backup = json.dumps(payload["backup"], separators=(",", ":")).encode()
                if len(raw_backup) > MAX_BACKUP_BYTES:
                    raise ValidationError("workspace backup exceeds 10 MB")
                projects, histories, snapshots = validate_workspace_backup(payload["backup"])
                restored = self.app.store.restore(projects, histories, snapshots)
                return self.json(200, {"restored": restored, "mode": "replace"})
            return self.error_json(404,"not found")
        except RuntimeError: return self.error_json(409, "revision conflict")
        except ValidationError as err: return self.error_json(400,str(err))
        except sqlite3.Error: return self.error_json(500, "database write failed")
    def do_PUT(self):
        if not self.valid_request(): return self.error_json(403,"foreign Host or Origin")
        match=re.fullmatch(r"/api/projects/([0-9a-f-]{36})",urlparse(self.path).path)
        if not match:return self.error_json(404,"not found")
        try:
            payload=self.body()
            if not isinstance(payload,dict) or type(payload.get("revision")) is not int: raise ValidationError("current revision is required")
            editable=validate_project(payload)
            existing=self.app.store.get(match.group(1))
            if not existing: return self.error_json(404,"project not found")
            self.app.validate_skill_ids(editable, existing_ids=existing["skillIds"])
            project=self.app.store.update(match.group(1),editable,payload["revision"])
            if not project:return self.error_json(404,"project not found")
            return self.json(200,project)
        except RuntimeError: return self.error_json(409,"revision conflict")
        except ValidationError as err:return self.error_json(400,str(err))
        except sqlite3.Error: return self.error_json(500, "database write failed")
    def do_DELETE(self):
        if not self.valid_request(): return self.error_json(403, "foreign Host or Origin")
        match = re.fullmatch(r"/api/projects/([0-9a-f-]{36})", urlparse(self.path).path)
        if not match: return self.error_json(405, "method not allowed")
        try:
            payload = self.body()
            if not isinstance(payload, dict) or set(payload) != {"confirm", "revision"}:
                raise ValidationError("delete requires confirm and revision")
            if payload["confirm"] is not True or type(payload["revision"]) is not int:
                raise ValidationError("delete requires explicit confirmation and current revision")
            deleted = self.app.store.delete(match.group(1), payload["revision"])
            if deleted is None: return self.error_json(404, "project not found")
            return self.json(200, {"deleted": True, "id": match.group(1)})
        except RuntimeError: return self.error_json(409, "revision conflict")
        except ValidationError as err: return self.error_json(400, str(err))


class FoundryServer(ThreadingHTTPServer):
    daemon_threads=True
    def __init__(self,address,root,data_dir):
        super().__init__(address,Handler); self.root=Path(root).resolve();self.static=self.root/"app"/"static";self.data_dir=Path(data_dir);self.store=Store(self.data_dir)
    def server_close(self):
        super().server_close()
        if hasattr(self, "store"):
            self.store.conn.close()

    def skills(self):
        file=self.root/"app"/"data"/"skills.json"
        if not file.is_file(): return []
        try:
            result=json.loads(file.read_text(encoding="utf-8"))
            if not isinstance(result,list): return []
            required={"id","name","description","url","sourcePath","revision"}
            return [x for x in result if isinstance(x,dict) and set(x)==required and all(isinstance(x[k],str) for k in required) and x["url"].startswith("https://")]
        except (OSError,json.JSONDecodeError): return []
    def validate_skill_ids(self, project, *, existing_ids=()):
        allowed={skill["id"] for skill in self.skills()}
        unknown=set(project["skillIds"]) - allowed - set(existing_ids)
        if unknown:
            raise ValidationError("unknown registered skill IDs: " + ", ".join(sorted(unknown)))


def main(argv=None):
    parser=argparse.ArgumentParser();parser.add_argument("--port",type=int,default=8765);parser.add_argument("--data-dir",default=None);args=parser.parse_args(argv)
    if not 1 <= args.port <= 65535: parser.error("port must be between 1 and 65535")
    root=Path(__file__).resolve().parents[1]; data=Path(args.data_dir) if args.data_dir else root/".foundry-data"
    server=FoundryServer(("127.0.0.1",args.port),root,data)
    print(f"FoundRy serving http://127.0.0.1:{args.port}")
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()

if __name__ == "__main__": main()
