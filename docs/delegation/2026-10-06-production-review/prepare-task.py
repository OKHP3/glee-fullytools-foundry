"""Validate the proposed series and print bounded agent arguments; never dispatch."""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys


def validate(plan):
    tasks = plan["tasks"]
    by_id = {task["id"]: task for task in tasks}
    if len(by_id) != len(tasks):
        raise ValueError("duplicate task ID")
    for task in tasks:
        if any(dep not in by_id or dep == task["id"] for dep in task["depends_on"]):
            raise ValueError("unknown or self dependency: " + task["id"])
        for path in task["owned_paths"]:
            if PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts or "\\" in path or ":" in path:
                raise ValueError("unsafe owned path: " + path)
        for field in ("objective", "acceptance", "output"):
            if not isinstance(task[field], str) or not task[field].strip():
                raise ValueError("missing " + field + ": " + task["id"])
    visited, active = set(), set()

    def visit(task_id):
        if task_id in active:
            raise ValueError("dependency cycle")
        if task_id in visited:
            return
        active.add(task_id)
        for dependency in by_id[task_id]["depends_on"]:
            visit(dependency)
        active.remove(task_id)
        visited.add(task_id)

    for task_id in by_id:
        visit(task_id)
    policy = plan["policy"]
    if not 0 < policy["per_delegate_token_ceiling"] <= 2_000_000:
        raise ValueError("invalid delegate ceiling")
    if not 0 < policy["maximum_concurrent_workers"] <= 3 or policy["recursive_spawning"]:
        raise ValueError("unsupported concurrency or recursive spawning")
    return by_id


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "list", "prepare"))
    parser.add_argument("task_id", nargs="?")
    parser.add_argument("--plan", type=Path, default=Path(__file__).with_name("next-series.json"))
    parser.add_argument("--state", type=Path, help="Private coordinator receipts; never written by this tool")
    parser.add_argument("--output-root", type=Path, help="Private report directory outside the source checkout")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--source-ref", help="Fresh coordinator-selected full commit SHA")
    for name in ("capability", "skill-name", "first-host", "second-host", "connector-host"):
        parser.add_argument("--" + name)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    tasks = validate(plan)
    if args.command == "validate":
        print(json.dumps({"validation": "pass", "tasks": len(tasks), "dispatch": "not-performed"}))
        return
    state = json.loads(args.state.read_text(encoding="utf-8")) if args.state else {}
    completed, gates = state.get("completed", {}), state.get("gates", {})
    if not isinstance(completed, dict) or not isinstance(gates, dict):
        raise ValueError("completed and gates must be receipt maps")
    if any(key not in tasks for key in completed):
        raise ValueError("unknown completed task")
    if any(not isinstance(value, str) or not value.strip() for value in [*completed.values(), *gates.values()]):
        raise ValueError("each receipt must be a nonempty evidence string")

    def missing(task):
        return [dep for dep in task["depends_on"] if dep not in completed] + [gate for gate in task["gates"] if gate not in gates]

    if args.command == "list":
        print(json.dumps([{ "id": task["id"], "title": task["title"], "missing": missing(task)} for task in tasks.values()], indent=2))
        return
    if args.task_id not in tasks:
        raise ValueError("select a known task ID")
    if args.task_id in completed:
        raise ValueError("task already has a completion receipt")
    task = tasks[args.task_id]
    if missing(task):
        raise ValueError("missing prerequisites: " + ", ".join(missing(task)))
    if not args.source_ref or not re.fullmatch(r"[0-9a-fA-F]{40}", args.source_ref):
        raise ValueError("provide a fresh full --source-ref; a moving branch name is insufficient")
    if args.output_root is None:
        raise ValueError("provide a private --output-root")
    repo, output = args.repo_root.resolve(), args.output_root.resolve()
    if output == repo or repo in output.parents:
        raise ValueError("private reports must be outside the source checkout")
    if not (repo / "AGENTS.md").is_file():
        raise ValueError("repo-root has no AGENTS.md")
    substitutions = {"capability": args.capability, "skill-name": args.skill_name, "first-host": args.first_host, "second-host": args.second_host, "connector-host": args.connector_host}
    paths = []
    for owned in task["owned_paths"]:
        for token in re.findall(r"<([^>]+)>", owned):
            value = substitutions.get(token)
            if not value or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
                raise ValueError("provide a lowercase ASCII slug for --" + token)
            owned = owned.replace("<" + token + ">", value)
        paths.append(owned)
    prompt = (
        f"Task {task['id']}: {task['title']}. Read {repo}/AGENTS.md and relevant guides first. "
        f"Verify the isolated checkout at exact source {args.source_ref}; do not use or switch another writer's checkout. "
        f"Create a goal for this duty with token_budget={plan['policy']['per_delegate_token_ceiling']}; "
        "verify its counter before substantive work and stop starting work at 80%, retaining closure capacity. "
        "No recursive spawning, purchases, silent budget reset, private-source disclosure, permission expansion or automatic release. "
        f"Objective: {task['objective']} Owned paths only: {json.dumps(paths)}. "
        f"Acceptance: {task['acceptance']} Deliverable: {task['output']}. "
        f"Save private result JSON/Markdown beneath {output}/{task['id']}; report exact source/artifact hashes, checks, blockers and usage. "
        f"Prerequisite receipt references: {json.dumps({key: completed[key] for key in task['depends_on']})}; "
        f"gate receipt references: {json.dumps({key: gates[key] for key in task['gates']})}. "
        "This formatter checks receipt presence only, not authority, freshness or evidence truth. "
        "Independently inspect every receipt before acting; return blocked if it is unsupported. "
        "For P15, verify an explicit owner request for the separate audit repair before editing; selection alone is insufficient. "
        "Return a reviewable scoped change or a precise no-change/blocker report."
    )
    print(json.dumps({"task_name": task["id"].lower(), "model": plan["policy"]["model"], "reasoning_effort": plan["policy"]["reasoning_effort"], "fork_turns": "none", "message": prompt}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        sys.exit(2)
