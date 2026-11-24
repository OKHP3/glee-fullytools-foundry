# glee-fully-gpt03c-wishful-tastes

Reusable Agent Skills for the Glee-fully Branch 03 workbench.

## What this repository is

This repository is a skill-library workbench, not a restaurant application. It
contains portable `SKILL.md` packages, supporting references, assets, scripts,
tests, evaluation designs, benchmark records, and project orchestration prompts.

The repository name and earlier project context suggest an intended “Wishful
Tastes” restaurant wishlist and dining-discovery assistant. That product is
not implemented in this checkout. No UI, API, database, recommendation engine,
deployment, or production integration is present here.

## Start here

- [`AGENTS.md`](AGENTS.md): repository operating rules and verified boundaries
- [Installed Agent Skills](.agents/skills/README.md): generated inventory of local packages
- [Project prompts](.agents/prompts/): onboarding, migration, and context-bootstrap workflows
- [`skills/okhp3-skill-promotion/`](skills/okhp3-skill-promotion/): verified publication mirror

## Structure

| Path | Role |
|---|---|
| `.agents/skills/` | Editable local skill packages and their supporting evidence |
| `.agents/prompts/` | Project-level orchestration prompts, not standalone skills |
| `skills/` | Explicit publication mirrors; currently contains the promotion package |
| `AGENTS.md` | Canonical repository guidance |

Historical benchmark and raw run artifacts remain inside the relevant skill
package when retained records reference them. They are evidence, not proof of
current production readiness.

## Status

Active skill-library assembly. The product mission, owner-approved audience,
and implementation roadmap remain `TBD` from repository evidence.
