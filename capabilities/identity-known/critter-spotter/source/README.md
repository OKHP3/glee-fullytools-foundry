# glee-fully-gpt07a-critter-spotter

This repository is the current skill-seeding scaffold for Glee-fully Branch
07a, whose intended product label is Critter Spotter. Its tracked product
surface is an Agent Skills collection, not a wildlife-identification
application.

## Current surface

The `.agents/skills/` directory contains four skills:

- `find-skills`: discover and evaluate installable agent skills.
- `okhp3-notion-capture-router`: route AI conversation material into Notion
  and reconcile reusable extracts with OKHP3 repositories.
- `okhp3-skill-cataloger`: inventory skills and generate a maintained catalog.
- `skill-creator`: create, evaluate, and improve Agent Skills.

There is currently no application runtime, wildlife-identification logic,
package manifest, dependency lockfile, test suite, CI configuration, or
deployment configuration. The repository therefore reads as scaffolded and
dormant rather than production-ready. The intended user experience, model or
vision provider, data sources, runtime, deployment target, ownership, and
confirmed product mission remain TBD.

## Validation

Run the cataloger's read-only check from the repository root:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --check --json
```

For repository-level documentation or skill edits, also run:

```bash
git diff --check
git status --short --branch
```

See [`AGENTS.md`](AGENTS.md) for the full project map, boundaries, conventions,
known gaps, and maintenance guidance. `CLAUDE.md` is the short Claude pointer.
