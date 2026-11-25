#!/usr/bin/env python3
"""Build portable skill ZIPs or reviewed former-GPT plugin distributions.

See https://developers.openai.com/plugins/build/plugins for the manifest layout.
Run with --all or repeat --product ID, and specify --output DIR. Add
--former-gpt to build the historical plugin edition. Use --check
to compare existing packages without writing. No installation or upload occurs.
"""

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
NUMBER = r"(?:0|[1-9][0-9]*)"
PRERELEASE = rf"(?:{NUMBER}|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)"
VERSION = rf"{NUMBER}\.{NUMBER}\.{NUMBER}(?:-{PRERELEASE}(?:\.{PRERELEASE})*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"


def read_file(root, path):
    """Read a regular repository file without following a redirected route."""
    if path.resolve(strict=True) != path or not path.is_relative_to(root) or not path.is_file():
        raise ValueError(f"Expected a regular file in the canonical tree: {path}")
    return path.read_bytes()


def registry(root):
    document = json.loads(read_file(root, root / "products/migration-map.json"))
    products = {}
    for product in document["products"]:
        slug = product["productId"]
        route = product["destination"]
        if (not re.fullmatch(SLUG, slug) or len(slug) > 64 or slug in products
                or not re.fullmatch(rf"capabilities/{SLUG}(?:/{SLUG})?", route)
                or PurePosixPath(route).name != slug):
            raise ValueError(f"Invalid or duplicate capability route: {slug!r}, {route!r}")
        products[slug] = product
    if not products:
        raise ValueError("The migration register contains no capabilities")
    return products


def scalar(header, key, indent=""):
    """Read the plain, quoted and folded scalars used by FoundRy SKILL.md files."""
    lines = header.splitlines()
    prefix = f"{indent}{key}:"
    indices = [i for i, line in enumerate(lines) if re.match(re.escape(prefix) + r"(?:\s|$)", line)]
    if len(indices) != 1:
        raise ValueError(f"Expected one frontmatter value for {key}")
    index = indices[0]
    value = lines[index][len(prefix):].strip()
    if value in {">", ">-"}:
        parts = []
        for line in lines[index + 1:]:
            if not line.startswith(indent + "  "):
                break
            parts.append(line.strip())
        value = " ".join(parts)
    elif value.startswith('"'):
        value = json.loads(value)
    elif value.startswith("'") and value.endswith("'"):
        value = value[1:-1].replace("''", "'")
    elif value.startswith(("'", "|", ">", "[", "{", "&", "*", "!")):
        raise ValueError(f"Unsupported frontmatter syntax: {key}")
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Empty or unsupported frontmatter scalar: {key}")
    return value


def license_bytes(root, directory):
    receipt = json.loads(read_file(root, directory / "product.json"))
    licenses = [f for f in receipt["files"] if re.fullmatch(r"LICENSE(?:\.md|\.txt)?", f["path"], re.I)]
    if len(licenses) != 1 or receipt["sourceLicense"] != "MIT":
        raise ValueError(f"Expected one verified MIT license for {directory.name}")
    record = licenses[0]
    raw = read_file(root, directory / "source" / record["path"])
    # Windows Git checkouts may project LF source blobs into CRLF text.
    for candidate in (raw, raw.replace(b"\r\n", b"\n")):
        if hashlib.sha256(candidate).hexdigest() == record["sha256"]:
            if candidate.lstrip().startswith(b"MIT License") and b"Permission is hereby granted" in candidate:
                return candidate
    raise ValueError(f"License does not match the verified source receipt for {directory.name}")


def package(root, product):
    slug = product["productId"]
    directory = root / product["destination"]
    skill_path = f"skills/{slug}/SKILL.md"
    source = read_file(root, directory / skill_path).replace(b"\r\n", b"\n")
    if len(source) > 1024 * 1024:
        raise ValueError(f"Skill exceeds 1 MiB: {slug}")
    if any(p.name != "SKILL.md" for p in (directory / skill_path).parent.iterdir()):
        raise ValueError(f"Skill has additional runtime resources requiring packaging review: {slug}")
    front = re.match(r"\A---\n(.*?)\n---\n(?=\s*\S)", source.decode("utf-8"), re.S)
    if not front:
        raise ValueError(f"Missing skill header or body: {slug}")
    header = front.group(1)
    metadata = re.findall(r"(?m)^metadata:[ \t]*\n((?:[ \t]+[^\n]*\n?)+)", header)
    if len(metadata) != 1 or scalar(header, "name") != slug or scalar(header, "license") != "MIT":
        raise ValueError(f"Skill identity, license or metadata mismatch: {slug}")
    version = scalar(metadata[0], "version", "  ")
    description = scalar(header, "description")
    title = product["displayName"]
    if not re.fullmatch(VERSION, version) or not title.strip() or len(description) > 1024:
        raise ValueError(f"Invalid skill version, title or description: {slug}")
    manifest = {"name": slug, "version": version, "description": description,
                "license": "MIT", "skills": "./skills/", "interface": {"displayName": title}}
    contents = {".codex-plugin/plugin.json": (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode(),
                "LICENSE": license_bytes(root, directory), skill_path: source}
    return f"{slug}-{version}.zip", archive_bytes(contents)


def archive_bytes(contents):
    buffer = io.BytesIO()
    # Stored entries and fixed metadata give identical archives on different hosts.
    with zipfile.ZipFile(buffer, "w") as archive:
        for name, body in sorted(contents.items()):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, body)
    return buffer.getvalue()


def former_gpt_registry(root):
    products = {}
    for pattern in ("*/plugin/release.json", "*/*/plugin/release.json"):
        for path in sorted((root / "capabilities").glob(pattern)):
            receipt = json.loads(read_file(root, path))
            slug = receipt["packageId"]
            route = path.parents[1].relative_to(root).as_posix()
            if (not re.fullmatch(SLUG, slug) or slug in products or receipt["formatVersion"] != 1
                    or not re.fullmatch(rf"capabilities/{SLUG}(?:/{SLUG})?", route)):
                raise ValueError(f"Invalid former-GPT package at {route}")
            products[slug] = (path.parent, receipt)
    if not products:
        raise ValueError("No former-GPT release records")
    return products


def relative_path(value):
    if (not isinstance(value, str) or not value or "\\" in value or ":" in value
            or any(part in ("", ".", "..") for part in value.split("/"))):
        raise ValueError(f"Invalid package path: {value!r}")
    return value


def former_gpt_package(root, product):
    directory, receipt = product
    slug = receipt["packageId"]
    contents = {}
    references = []
    required = {"plugin.json", "assets/gpt-icon.png", "skills/instructions/SKILL.md",
                "skills/instructions/agents/openai.yaml"}
    resource_prefix = "skills/instructions/references/"
    seen = set()
    for record in receipt["files"]:
        name = relative_path(record["path"])
        if (name.casefold() in seen or (name not in required and
                (not name.startswith(resource_prefix) or "/" in name[len(resource_prefix):]))):
            raise ValueError(f"Unexpected or duplicate member in {slug}: {name}")
        seen.add(name.casefold())
        source = directory / name
        if "source" in record:
            public_source = relative_path(record["source"])
            if public_source.split("/", 1)[0] not in {
                    "capabilities", "canon", "docs", "evaluation", "governance", "inventory",
                    "products", "prompts", "snapshots", "templates", "vernacular"}:
                raise ValueError(f"Source outside the documented public asset directories: {public_source}")
            source = root / public_source
        data = read_file(root, source)
        if "member" in record:
            member = relative_path(record["member"])
            with zipfile.ZipFile(io.BytesIO(data)) as bundle:
                matches = [entry for entry in bundle.infolist() if entry.filename == member]
                if len(matches) != 1 or matches[0].is_dir() or matches[0].file_size > 64 * 1024 * 1024:
                    raise ValueError(f"Invalid archive reference for {slug}: {name}")
                data = bundle.read(matches[0])
        digest = record["sha256"]
        if hashlib.sha256(data).hexdigest() != digest:
            # Windows checkouts may project text to CRLF. Match the reviewed bytes.
            if PurePosixPath(name).suffix.lower() not in {".md", ".txt", ".json", ".yaml", ".yml", ".csv"}:
                raise ValueError(f"Source digest mismatch for {slug}: {name}")
            lf = data.replace(b"\r\n", b"\n")
            data = next((b for b in (lf, lf.replace(b"\n", b"\r\n"))
                         if hashlib.sha256(b).hexdigest() == digest), None)
            if data is None:
                raise ValueError(f"Source digest mismatch for {slug}: {name}")
        contents[name] = data
        if name.startswith(resource_prefix):
            original = relative_path(record.get("originalName", name[len(resource_prefix):]))
            if "/" in original:
                raise ValueError(f"Invalid native knowledge name in {slug}: {original}")
            references.append({"name": original,
                               "path": name.removeprefix("skills/instructions/")})
    if not required.issubset(contents):
        raise ValueError(f"Missing native plugin files for {slug}: {sorted(required - contents.keys())}")
    native = json.loads(contents["plugin.json"])
    version = native["version"]
    if not re.fullmatch(VERSION, version) or version != receipt["sourceVersion"]:
        raise ValueError(f"Native version does not match the release record for {slug}")
    interface = native["extensions"]["com.openai"]["interface"]
    if (interface["capabilities"] != ["skills"] or interface["logo"] != "./assets/gpt-icon.png"
            or interface["composerIcon"] != "./assets/gpt-icon.png"):
        raise ValueError(f"Unrecognized native interface for {slug}")
    compat = {"interface": interface, "name": native["name"], "version": version,
              "description": native["description"], "author": native["author"],
              "keywords": [], "skills": "./skills"}
    lookup = {"files": references, "guidelines":
              "Resolve each path relative to skills/instructions/. This list contains the knowledge files included in this distribution."}
    # Builder can retain more starters than the native interface displays. Keep
    # the reviewed export intact, including its order and original wording.
    starter_bytes = read_file(root, directory / "builder-starters.json").replace(b"\r\n", b"\n")
    starters = json.loads(starter_bytes)
    if (not isinstance(starters, dict) or set(starters) != {"starters"}
            or not isinstance(starters["starters"], list)
            or not all(isinstance(item, str) and item.strip() for item in starters["starters"])):
        raise ValueError(f"Invalid original Builder starter list for {slug}")
    contents["foundry/builder-starters.json"] = starter_bytes
    for name, document in ((".codex-plugin/plugin.json", compat),
                           ("skills/instructions/lookup/knowledge-index.json", lookup),
                           ("foundry-release.json", receipt)):
        contents[name] = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return f"{slug}-former-gpt-{version}.zip", archive_bytes(contents)


def write_new(path, body):
    # Publish completed bytes atomically without replacing a conflicting archive.
    handle = tempfile.NamedTemporaryFile(dir=path.parent, prefix=".plugin-", delete=False)
    temp = Path(handle.name)
    try:
        with handle:
            handle.write(body)
        try:
            if os.name == "nt":
                temp.rename(path)  # Windows refuses replacement of an existing path.
            else:
                os.link(temp, path)
        except FileExistsError:
            if not path.is_file() or path.is_symlink() or path.read_bytes() != body:
                raise ValueError(f"Existing archive differs: {path}") from None
    finally:
        temp.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--all", action="store_true", help="package every registered capability")
    selection.add_argument("--product", action="append", metavar="ID", help="select a product ID (repeatable)")
    parser.add_argument("--output", type=Path, required=True, help="directory for the versioned ZIPs")
    parser.add_argument("--check", action="store_true", help="verify existing ZIPs without writing")
    parser.add_argument("--former-gpt", action="store_true", help="use reviewed native former-GPT release records")
    args = parser.parse_args()
    try:
        products = former_gpt_registry(ROOT) if args.former_gpt else registry(ROOT)
        build = former_gpt_package if args.former_gpt else package
        selected = sorted(products if args.all else set(args.product))
        pending = []
        for slug in selected:
            if slug not in products:
                raise ValueError(f"Unknown capability: {slug}")
            name, body = build(ROOT, products[slug])
            path = args.output / name
            if path.exists() or path.is_symlink():
                if path.is_symlink() or not path.is_file() or path.read_bytes() != body:
                    raise ValueError(f"Existing archive differs: {path}")
            elif args.check:
                raise ValueError(f"Missing archive: {path}")
            else:
                pending.append((path, body))
        if pending:
            args.output.mkdir(parents=True, exist_ok=True)
            for path, body in pending:
                write_new(path, body)
        print(f"Verified {len(selected)} native Codex plugin package(s) in {args.output}")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
