#!/usr/bin/env python3
"""Stable-release audit. Exit 0=current, 1=drift, 2=incomplete.
Only --prepare-mermaid changes source; major upgrades require --allow-major.
No packages are installed and no machine runtimes are changed.
"""
from __future__ import annotations
import argparse
import gzip
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import shutil
import sqlite3
import subprocess
import sys
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MERMAID_URL = "https://api.github.com/repos/mermaid-js/mermaid/releases?per_page=100"
PYTHON_URL = "https://www.python.org/downloads/"
NODE_URL = "https://nodejs.org/dist/index.json"
SQLITE_URL = "https://sqlite.org/changes.html"
MERMAID_PIN = re.compile(r'(?<=https://cdn\.jsdelivr\.net/npm/mermaid@)([^/\s"]+)(?=/dist/mermaid\.esm\.min\.mjs)')


def version(value: str) -> tuple[int, ...]:
    """Accept final numeric releases only, never a prerelease or mutable tag."""
    if not re.fullmatch(r"v?\d+(?:\.\d+){1,3}", value):
        raise ValueError(f"not a stable numeric release: {value!r}")
    return tuple(map(int, value.removeprefix("v").split(".")))


def get_text(url: str) -> str:
    headers = {"User-Agent": "Glee-fully-FoundRy-technology-audit"}
    if url.startswith("https://api.github.com/") and os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    with urlopen(Request(url, headers=headers), timeout=20) as response:
        data = response.read()
        if response.headers.get('Content-Encoding') == 'gzip' or data.startswith(b'\x1f\x8b'):
            data = gzip.decompress(data)
        return data.decode("utf-8")


def latest(kind: str, url: str) -> str:
    raw = get_text(url)
    if kind == "python":
        found = re.findall(r">Python (3\.\d+\.\d+)</a>", raw)
        return max(found, key=version)
    if kind == "sqlite":
        found = re.findall(r"<h3[^>]*>\s*\d{4}-\d{2}-\d{2}\s*\((\d+\.\d+\.\d+)\)", raw)
        if not found:
            raise ValueError("SQLite release headings not found")
        return found[0]
    data = json.loads(raw)
    if kind in {"node", "node-lts"}:
        releases = [x["version"] for x in data if kind == "node" or x.get("lts")]
        return max(releases, key=version).removeprefix("v")
    if kind == "pypi":
        releases = [v for v, files in data["releases"].items()
                    if re.fullmatch(r"\d+(?:\.\d+){1,3}", v)
                    and any(not f.get("yanked", False) for f in files)]
        return max(releases, key=version)
    if kind == "github":
        if data.get("draft") or data.get("prerelease"):
            raise ValueError("GitHub latest release is not stable")
        result = data["tag_name"].removeprefix("v")
    elif kind == "github-mermaid":
        if not isinstance(data, list):
            raise ValueError("expected Mermaid GitHub release list")
        prefix = "mermaid@"
        releases = [item["tag_name"][len(prefix):] for item in data
                    if isinstance(item, dict) and not item.get("draft")
                    and not item.get("prerelease")
                    and isinstance(item.get("tag_name"), str)
                    and item["tag_name"].startswith(prefix)
                    and re.fullmatch(r"\d+(?:\.\d+){1,3}", item["tag_name"][len(prefix):])]
        if not releases:
            raise ValueError("no stable Mermaid release in GitHub response")
        return max(releases, key=version)
    else:
        if data.get("deprecated"):
            raise ValueError("npm latest release is deprecated")
        result = data["version"]
    version(result)
    return result


def command_version(command: str, *args: str) -> str:
    executable = shutil.which(command)
    if not executable:
        return "not installed"
    result = subprocess.run([executable, *args], capture_output=True, text=True,
                            timeout=15, check=True)
    return result.stdout.strip().removeprefix("v")


def pins(path: Path) -> dict[str, str]:
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([\w.-]+)==([\d.]+)(?:\s|$)", line)
        if not match or match[1].lower() in result:
            raise ValueError(f"unsupported or duplicate pin in {path.name}: {line}")
        result[match[1].lower()] = match[2]
    if not result:
        raise ValueError(f"no pins in {path.name}")
    return result


def targets(root: Path) -> list[dict]:
    rows = []
    def add(name, current, kind, url, policy, evidence):
        rows.append(dict(name=name, current=current, kind=kind, source=url,
                         policy=policy, evidence=evidence))
    matches = MERMAID_PIN.findall((root / "web-templates/index.html").read_text(encoding="utf-8"))
    if len(matches) != 1:
        raise ValueError("expected exactly one Mermaid CDN pin")
    add("Mermaid", matches[0], "github-mermaid", MERMAID_URL, "pin", "web-templates/index.html")
    direct = pins(root / "requirements.txt")
    locked = pins(root / "requirements-lock.txt")
    for name, declared in direct.items():
        if locked.get(name) != declared:
            raise ValueError(f"requirement/lock mismatch: {name}")
    for name, current in locked.items():
        add(name, current, "pypi", f"https://pypi.org/pypi/{name}/json", "pin", "requirements-lock.txt")
    actions = set()
    for path in sorted((root / ".github/workflows").glob("*.y*ml")):
        for name, current in re.findall(r"uses:\s*([\w-]+/[\w-]+)@([\w.-]+)", path.read_text(encoding="utf-8")):
            if (name, current) not in actions:
                actions.add((name, current))
                add(name, current, "github", f"https://api.github.com/repos/{name}/releases/latest",
                    "action", path.relative_to(root).as_posix())
    add("Python (this host)", platform.python_version(), "python", PYTHON_URL, "host", "executing interpreter")
    add("SQLite (this host)", sqlite3.sqlite_version, "sqlite", SQLITE_URL, "host", "sqlite3.sqlite_version")
    node = command_version("node", "--version")
    add("Node.js (this host)", node, "node-host", NODE_URL, "host", "node --version")
    add("Node.js Current", node, "node", NODE_URL, "informational", "stable Current channel; LTS preferred")
    add("npm (this host)", command_version("npm", "--version"), "npm", "https://registry.npmjs.org/npm/latest", "host", "npm --version")
    add("pip (this interpreter)", importlib.metadata.version("pip"), "pypi", "https://pypi.org/pypi/pip/json", "host", "interpreter package metadata")
    add("Playwright (optional QA)", "not pinned", "npm", "https://registry.npmjs.org/playwright/latest", "informational", "scripts/foundry-error-recovery-qa.mjs")
    add("playwright-core (optional QA)", "not pinned", "npm", "https://registry.npmjs.org/playwright-core/latest", "informational", "scripts/foundry-authoring-qa.mjs")
    return rows


def compare(current: str, newest: str, policy: str) -> str:
    latest_parts = version(newest)
    if policy == "informational":
        return "informational"
    if policy == "action" and re.fullmatch(r"v\d+", current):
        major = int(current[1:])
        return "update available" if major < latest_parts[0] else ("tracks major" if major == latest_parts[0] else "source behind")
    current_parts = version(current)
    return "update available" if current_parts < latest_parts else ("current" if current_parts == latest_parts else "source behind")


def check(row: dict) -> dict:
    row = row.copy()
    try:
        if row["kind"] == "node-host":
            releases = json.loads(get_text(row["source"]))
            installed_major = version(row["current"])[0]
            is_lts = any(item.get("lts") and version(item["version"])[0] == installed_major
                         for item in releases)
            row["name"] = "Node.js LTS (this host)" if is_lts else "Node.js non-LTS (this host)"
            candidates = [item["version"] for item in releases if not is_lts or item.get("lts")]
            row["latest"] = max(candidates, key=version).removeprefix("v")
        else:
            row["latest"] = latest(row["kind"], row["source"])
        row["status"] = compare(row["current"], row["latest"], row["policy"])
    except (OSError, ValueError, KeyError, TypeError) as error:
        row["status"] = "unknown"
        row["error"] = str(error)
    return row


def exit_code(rows: list[dict], include_host: bool = False) -> int:
    if any(r["status"] in {"unknown", "source behind"} for r in rows):
        return 2
    if any(r["status"] == "update available" and
           (r["policy"] in {"pin", "action"} or include_host) for r in rows):
        return 1
    return 0


def prepare_mermaid(root: Path, newest: str, allow_major: bool = False) -> bool:
    path = root / "web-templates/index.html"
    raw = path.read_bytes()
    content = raw.decode("utf-8")
    matches = MERMAID_PIN.findall(content)
    if len(matches) != 1:
        raise ValueError("expected exactly one Mermaid CDN pin")
    current = matches[0]
    if version(newest) <= version(current):
        return False
    if version(newest)[0] != version(current)[0] and not allow_major:
        raise ValueError("major Mermaid update requires migration review and --allow-major")
    path.write_bytes(MERMAID_PIN.sub(newest, content).encode("utf-8"))
    return True


def markdown(report: dict) -> str:
    lines = ["# Technology version audit", "", f"Retrieved: {report['checked_at']}", "",
             "Host values describe only the interpreter/machine executing this audit.",
             "Standards, services and other-host evidence are in docs/technology-inventory.md.", "",
             "| Technology | In place | Latest stable | Status | Evidence |",
             "|---|---|---|---|---|"]
    for row in report["technologies"]:
        newest = row.get("latest", "unknown")
        lines.append(f"| {row['name']} | {row['current']} | [{newest}]({row['source']}) | {row['status']} | {row['evidence']} |")
    for row in report["technologies"]:
        if row.get("error"):
            lines.append(f"\n- {row['name']}: {row['error']}")
    lines.extend(["", "Repository pins require reviewed updates. Host updates are advisory unless --include-host is set.",
                  "An unavailable source is incomplete evidence, never an all-clear.", ""])
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--markdown-output", type=Path)
    parser.add_argument("--include-host", action="store_true")
    parser.add_argument("--prepare-mermaid", action="store_true")
    parser.add_argument("--allow-major", action="store_true")
    args = parser.parse_args(argv)
    if args.allow_major and not args.prepare_mermaid:
        parser.error("--allow-major requires --prepare-mermaid")
    try:
        if args.prepare_mermaid:
            newest = latest("github-mermaid", MERMAID_URL)
            changed = prepare_mermaid(args.root, newest, args.allow_major)
            print(f"Mermaid candidate {'updated' if changed else 'unchanged'}: {newest}; run compatibility checks before merging.")
            return 0
        with ThreadPoolExecutor(max_workers=6) as pool:
            rows = list(pool.map(check, targets(args.root)))
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        print(f"INCOMPLETE: {error}", file=sys.stderr)
        return 2
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "technologies": rows}
    output = markdown(report)
    print(output)
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if args.markdown_output:
        args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_output.write_text(output, encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a", encoding="utf-8") as summary:
            summary.write(output)
    return exit_code(rows, args.include_host)


if __name__ == "__main__":
    raise SystemExit(main())
