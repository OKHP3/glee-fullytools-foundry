# Glee-fully Maven Wise

## Current state

This repository is a documentation and Agent Skills workbench for the
Glee-fully Branch 06 concept named Maven Wise. It is not an implemented
application. No runtime, user interface, model integration, health-data
store, deployment configuration, or product test suite is currently checked
in.

## What the evidence supports

- The repository identity and project guidance identify Maven Wise as a
  health and wellness knowledge-synthesis tool-ette.
- [`docs/healthy-bee-ing-pulsebook-2025-09-01.md`](docs/healthy-bee-ing-pulsebook-2025-09-01.md) is for Healthy Bee-ing, a related Branch 06
  wellness tool, and lists Maven Wise as a sibling focused on midlife and
  hormonal-change support.
- `.agents/prompts/` contains three reusable project and migration prompts.
- `.agents/skills/` contains the local 46-package Agent Skills workbench.
- `skills/okhp3-skill-promotion/` is a publication mirror for the local
  promotion skill.

The pulsebook is retained as lineage context. It is not implementation
documentation for Maven Wise and does not prove that Maven Wise is live.

## Start here

1. Read [`AGENTS.md`](AGENTS.md) for repository rules and evidence boundaries.
2. Read the [Healthy Bee-ing pulsebook](docs/healthy-bee-ing-pulsebook-2025-09-01.md)
   for the available Branch 06 lineage context.
3. Browse [`.agents/prompts/`](.agents/prompts/) and
   [`.agents/skills/`](.agents/skills/) for local agent support.
4. Treat product status, runtime, data sources, safety controls, and
   deployment as `TBD` until the owner supplies evidence.

## Non-goals

This repository must not present wellness material as diagnosis or treatment,
invent a clinical workflow, add credentials or private health data, or claim
that a planned tool is deployed merely because a pulsebook or skill exists.

## Validation

For documentation-only changes, reread the edited Markdown, check referenced
paths, run `git diff --check`, and inspect the complete diff. For skill-suite
changes, run the Foundry structural validator and regenerate the local skill
catalog with the checked-in cataloger.
