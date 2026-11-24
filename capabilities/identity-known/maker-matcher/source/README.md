# Glee-fully GPT07F Maker Matcher

## Current state

This repository began as a Glee-fully Maker Matcher GPT Tool-ette scaffold.
The intended product direction was an assistant connecting crafts and styles
with makers and artisans.

The current tree is not a runnable Maker Matcher. It is a content-first Agent
Skills workspace and migration staging repository containing 46 project-local
skill packages under `.agents/skills/`, plus an explicit publication mirror for
`okhp3-skill-promotion` under `skills/`.

## What is here

- `.agents/skills/`: skill instructions, references, assets, scripts, tests,
  fixtures, and evaluation records.
- `.agents/skills/README.md`: generated catalog of project-local skills.
- `skills/okhp3-skill-promotion/`: publication-mirror example with provenance
  and synchronization evidence.
- `AGENTS.md`: canonical operating guidance.
- `CLAUDE.md`: compatibility pointer to `AGENTS.md`.

## What is not established

No matcher algorithm, maker catalog, user interface, API, runtime, database,
deployment target, authoritative maker source, or production status is
established by the current repository.

Neutral skill packages, Glee-fully overlays, and publication mirrors may be
related, but their canonical ownership must be confirmed before consolidation
or deletion.

## Validation

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --check
```

See `AGENTS.md` for the complete inventory, audit, and package-validation
workflow.
