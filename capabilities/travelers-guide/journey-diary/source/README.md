# glee-fully-gpt04a-journey-diary

## Current status

This repository is a Glee-fully and OKHP3 Agent Skills workbench. It contains
reusable skills, evaluation evidence, migration prompts, and publication
support. It does not currently contain a Journey Diary application, travel
journal corpus, user interface, API, deployment configuration, or runtime.

The Journey Diary identity is retained as the repository's declared product
role, but its implementation is not present in this checkout.

## What is here

- `.agents/prompts/`: project-context, onboarding, and GPT-to-skill migration
  orchestration prompts.
- `.agents/skills/`: the active local Agent Skills collection, including
  authoring, migration, process, evaluation, repository, and publication
  workflows.
- `.agents/skills/README.md`: generated catalog of the active local skills.
- `.agents/skills/okhp3-skill-foundry/benchmarks/`: historical and analytical
  evidence for the Foundry package.
- `skills/`: approved local publication mirrors. These are generated mirrors,
  not independent authoring locations.

## Operating model

An Agent Skills-compatible client reads the packages under `.agents/skills/`.
Some workflows require optional capabilities such as GitHub or Notion access.
The repository contains helper scripts and package-level tests, but it is not
an application project and has no single start command.

## Validation

From the repository root:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs
```

The catalog check validates catalog structure. The Foundry validator performs
structural package checks and may report non-blocking warnings. Neither proves
runtime behavior, deployment, or production readiness.

## Boundaries and open questions

- Do not describe this checkout as a working Journey Diary product.
- Do not treat historical benchmarks as current release evidence.
- Do not delete evaluation or migration material solely because it looks like
  a checkpoint; confirm its provenance and value first.
- The intended long-term relationship between this workbench and the Journey
  Diary product remains to be established.
