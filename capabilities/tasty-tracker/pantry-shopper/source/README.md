# glee-fully-gpt03d-pantry-shopper

## What this repository is

This repository contains a project-local bundle of reusable Agent Skills for
the Glee-fully / Branch 03 workspace. It is a content and agent-tooling
repository, not a Pantry Shopper application.

The repository currently contains 46 skill packages under `.agents/skills/`,
three project prompts under `.agents/prompts/`, and the generated skill catalog
at `.agents/skills/README.md`.

## Current status

- Confirmed: the skill bundle, supporting scripts, references, fixtures, and
  evaluation records are present.
- Confirmed: the repository has no Pantry Shopper UI, API, inventory data
  model, application runtime, deployment configuration, or service entry point.
- Inferred: the bundle supports reusable agent authoring, knowledge operations,
  process documentation, evaluation, migration, and repository maintenance.
- Unknown: whether the Pantry Shopper product is intended to be implemented in
  this repository or maintained elsewhere.

## Start here

- [`AGENTS.md`](AGENTS.md): repository scope, evidence rules, and validation.
- [`.agents/skills/README.md`](.agents/skills/README.md): generated inventory of
  the local skills.
- [`.agents/prompts/`](.agents/prompts/): project onboarding and migration
  prompts.
- [`.agents/skills/okhp3-skill-cataloger/SKILL.md`](.agents/skills/okhp3-skill-cataloger/SKILL.md):
  catalog and validation workflow.

## Layout

```text
.agents/prompts/                  Project onboarding and migration prompts
.agents/skills/<skill>/           Runtime skill packages
.agents/skills/README.md          Generated skill catalog
skills/okhp3-skill-promotion/     Intentional publication mirror
```

The top-level `skills/okhp3-skill-promotion/` directory is an intentional
publication mirror of its `.agents/skills/` source package. It is not a
duplicate to delete.

## Validation

From the repository root:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --check

node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs \
  --skills-dir .agents/skills
```

The catalog check and Foundry validator are structural checks. They do not
prove that a Pantry Shopper product exists, runs, or is deployed.
