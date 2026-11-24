# glee-fully-gpt03b-menu-conductor

## Current status

This repository is an early Glee-fully Branch 03b scaffold and local Agent
Skills catalog. It is not currently a working Menu Conductor application.

The intended product identity is “Menu Conductor”, a weekly meal-planning and
menu-orchestration assistant. The repository does not yet contain the
authoritative product prompt, meal-planning logic, recipes, runtime
configuration, user interface, package manifest, test suite, or deployment
configuration needed to implement that product.

## What is here

- `AGENTS.md`: canonical repository guidance and known product boundaries.
- `.agents/prompts/`: project and GPT-to-Agent-Skill onboarding prompts.
- `.agents/skills/`: project-local Agent Skill packages, evaluations, resources,
  and deterministic utilities.
- `.agents/skills/README.md`: generated catalog of the available skill packages.
- `skills/okhp3-skill-promotion/`: publication mirror for the promotion skill.
- `CLAUDE.md`: compatibility pointer to `AGENTS.md`.

## Important boundary

The installed skills support repository maintenance, knowledge operations, and
skill development. They are not evidence that Menu Conductor is implemented,
deployed, or production-ready.

Before product implementation begins, confirm the runtime surface, authoritative
prompt, workflow, inputs, outputs, constraints, integrations, and validation
path. Update `AGENTS.md` when those decisions become evidence-backed.
