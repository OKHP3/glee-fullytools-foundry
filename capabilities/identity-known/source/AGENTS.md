# glee-fully-gpt07-identity-known

Canonical agent guidance for the Glee-fully GPT Branch #07 repository.

## Project identity

- Suite: Glee-fully
- Branch: #07, Identity Known
- Repository: https://github.com/OKHP3/glee-fully-gpt07-identity-known
- Notion anchor: https://app.notion.com/p/95a027dc2ae54f3fa1d194ec284e424b
- License: MIT
- Current status: early-stage and incomplete. No executable product has been identified in this repository.

## Current understanding

### Confirmed

This repository is a small Git project containing a Markdown-based project directive and agent-skill assets. Its stated branch theme is nature identification, wildlife, and personal identity tools.

The repository currently contains no application source tree, package manifest, dependency lockfile, test suite, build configuration, deployment configuration, or runtime entry point. `README.md` provides public orientation only. The `dataLedger_*v2.txt` files named by the project directive are not present.

The `.agents/skills/` directory contains reusable agent guidance and supporting scripts for Notion capture, skill cataloging, skill discovery, and skill creation. Treat those assets as repository tooling and reference material, not as the implementation of the branch product.

### Inferred

The likely purpose is to incubate and organize prompts or future tools for recognizing nature, wildlife, and identity-related subjects. The surviving project directive describes an exploratory workflow toward a PME-ready design, but it does not establish a delivered product, user interface, data model, or production workflow.

### Unknown

- The intended end-user experience and first deliverable are not defined.
- The technology stack, runtime, owner, deployment model, and production status are not documented.
- The meaning and operational requirements of PME readiness are not defined in this repository.
- The related repositories may contain implementation context, but they were not treated as part of this project root.

Do not turn these unknowns into assumptions in code, documentation, or plans.

## Scope and boundaries

In scope:

- Maintaining the branch context, project directive, and future project documents.
- Adding future implementation only when the project owner establishes the product scope and technology choices.
- Maintaining the checked-in `.agents/skills/` assets when a skill-specific change is requested.

Out of scope until explicitly defined:

- Claiming that the branch identifies species, people, or other subjects reliably.
- Treating prompt tags such as `!IDEA_STAGE` or `!PME_READY` as validated system behavior.
- Treating absent ledger files as available sources of truth.
- Adding dependencies, services, secrets, CI workflows, or deployment guarantees without a documented requirement.

## Repository map

- `README.md`: public orientation, status, and repository map.
- `docs/07-glee-fully-identity-known_instructions.md`: broad Glee-fully directive and intended ledger, routing, tone, and tagging rules. Several referenced files are absent.
- `.agents/skills/`: local agent skills, references, assets, and supporting scripts.
- `AGENTS.md`: canonical guidance for agents working in this repository.
- `CLAUDE.md`: short pointer to `AGENTS.md`.
- `LICENSE`: MIT license.

No nested Git repositories or separate project roots were found.

## Technology and workflow

The confirmed project format is Markdown documentation with embedded prompt text. The repository has no declared application runtime. Python files under `.agents/skills/` belong to the bundled skill tooling and should be changed only when the relevant skill workflow requires it.

The intended documentation flow described by the branch directive is:

`ideation_v2.txt` to `processing_v2.txt` to registry, persona, and parameters records to narrative, then archive.

This is documented intent only. The named ledger files and a system implementation for that flow are absent.

## Validation

No project-specific build, test, lint, or deployment command is currently defined. Before making a change:

1. Read this file and the relevant project document.
2. Confirm that the target is a guidance or metadata change, unless the owner has defined implementation scope.
3. Preserve unrelated working-tree changes.
4. After editing, run `git diff --check` and inspect the complete diff.
5. Re-read every changed guidance file and verify that referenced paths and commands exist.

For future implementation work, document the chosen runtime and add verified validation commands here at the same time as the implementation.

## Change conventions

- Use `AGENTS.md` as the canonical source for repository-wide agent guidance.
- Keep `CLAUDE.md` short and aligned with this file unless Claude-specific instructions are genuinely needed.
- Prefer small, factual documentation changes. Label facts, inferences, and unknowns.
- Do not invent ledger records, product behavior, roadmap commitments, ownership, or deployment status.
- Preserve standalone punchy lines when editing branded content.
- Use a warm, whimsical, precise tone where the project documents call for it, without sacrificing factual clarity.
- Generated content must not use em dashes.
- The brand materials state that AutoCAD R10 is locked. No AutoCAD artifacts or workflow are currently present here.

## Related repositories

These are related references, not nested projects in this checkout:

- [glee-fully-gpt07a-critter-spotter](https://github.com/OKHP3/glee-fully-gpt07a-critter-spotter)
- [glee-fully-gpt07b-roost-wrangler](https://github.com/OKHP3/glee-fully-gpt07b-roost-wrangler)
- [glee-fully-gpt07c-sight-seeker](https://github.com/OKHP3/glee-fully-gpt07c-sight-seeker)
- [glee-fully-gpt07d-snap-decoder](https://github.com/OKHP3/glee-fully-gpt07d-snap-decoder)
- [glee-fully-gpt07e-motif-muse](https://github.com/OKHP3/glee-fully-gpt07e-motif-muse)
- [glee-fully-gpt07f-maker-matcher](https://github.com/OKHP3/glee-fully-gpt07f-maker-matcher)
- [glee-fully-gpt07g-self-fixer](https://github.com/OKHP3/glee-fully-gpt07g-self-fixer)

## Keeping this guide current

Update this file when the repository gains an implementation, a defined runtime, verified commands, a new project boundary, or a materially changed workflow. Keep historical or aspirational material in the project documents and label it clearly rather than presenting it as current capability.

## Imported Claude Cowork project instructions
