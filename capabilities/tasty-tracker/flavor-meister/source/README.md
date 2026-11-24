# Glee-fully 03a Flavor Meister

03a Flavor Meister is an early Glee-fully concept for flavor profiling,
ingredient pairing, and recipe suggestion.

## Current state

This repository is a scaffold and Agent Skills workbench. No product runtime,
application source, user interface, dependency manifest, test suite, API,
database, or deployment configuration is currently confirmed.

The product concept is inferred from the repository identity and project
guidance. Product requirements, intended users, flavor model, recipe sources,
data boundaries, and the relationship to Tasty Tracker remain TBD.

## Repository map

- `AGENTS.md` — canonical repository guidance and evidence boundaries.
- `CLAUDE.md` — compatibility pointer to `AGENTS.md`.
- `.agents/prompts/` — project-onboarding and migration prompts.
- `.agents/skills/` — repository-local Agent Skills and their resources.
- `skills/okhp3-skill-promotion/` — a separately maintained promotion mirror;
  its relationship to this repository remains under review.

The local skill library is reusable agent tooling, not proof that Flavor Meister
implements any of the capabilities described by those skills.

## Start here

Read `AGENTS.md` before changing the repository. Use the applicable local skill
for repository organization, skill maintenance, or validation, and preserve
historical evaluation evidence unless its retention decision changes.
