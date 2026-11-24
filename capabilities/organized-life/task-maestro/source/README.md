# glee-fully-gpt05a-task-maestro

Documentation and agent-workbench scaffold for the Glee-fully Branch 05
personal task-management Tool-ette concept.

## Current status

This checkout does not contain an implemented GPT, runtime, executable
configuration, integrations, tests, or deployment configuration. The intended
subject is personal task management and prioritization, but the product
identity, workflow, audience, and implementation contract remain unresolved.

The knowledge bundle contains one relevant `TaskTamer` ideation seed among a
larger set of Glee-fully suite thread seeds. That seed is evidence of an idea,
not proof that TaskTamer and Task Maestro are the same product.

## Repository map

- `knowledgebundle/` contains the eight v2.0.0 canonical ledger files.
- `knowledgebundle/exports/` contains the packaged ZIP export of those ledgers.
- `.agents/prompts/` contains project-local onboarding and migration prompts.
- `.agents/skills/` contains the project-local Agent Skill workbench and its
  generated catalog.
- `skills/okhp3-skill-promotion/` is the byte-identical publication mirror for
  the promotion skill.
- `AGENTS.md` is the canonical repository guidance. `CLAUDE.md` points to it.

## Validation

There is no application start command or project test suite. Appropriate checks
include Git status and diff checks, ZIP integrity, skill-package validation, and
publication-mirror equality. Do not describe this repository as a running
product based on the presence of scaffolding or Agent Skills.

## Open decisions

- Confirm whether Task Maestro is the same concept as the `TaskTamer` seed.
- Define the intended user workflow, GPT behavior, audience, and target
  platform.
- Decide whether the local Agent Skill workbench remains part of this project or
  should later move to a dedicated workbench repository.
