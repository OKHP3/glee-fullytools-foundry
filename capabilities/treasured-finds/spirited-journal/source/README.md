# glee-fully-gpt02e-spirited-journal

## Current status

This repository is a pre-development Glee-fully Branch 02 scaffold. Its
declared product direction is a Spirited Journal for discovering spirits such
as whiskey and wine, recording tasting notes, and tracking a collection.

That product direction is not yet an implemented application or confirmed
product specification. The repository contains no verified runtime, deployment
configuration, application entry point, or product test suite.

The repository also contains a broad Agent Skills workbench and migration
surface under `.agents/`. That workbench is present in the current checkout,
but its long-term relationship to the Spirited Journal project has not been
decided.

## Start here

- `AGENTS.md` - canonical repository guidance and current evidence boundary
- `prompts/drafts/02e-glee-fully-spirited-journal_prompts_v1.yaml` - draft prompt record
- `.agents/prompts/` - project onboarding and migration prompts
- `.agents/skills/README.md` - generated catalog of bundled Agent Skills
- `.agents/skills/` - local Agent Skills, references, scripts, and evaluations
- `skills/okhp3-skill-promotion/` - exact publication mirror for the local
  `okhp3-skill-promotion` package

## Known boundaries

The intended deliverable remains unresolved: prompt library, Agent Skill, GPT
tool-ette, application, or another form. Target users, authoritative
requirements, runtime, integrations, deployment, and lifecycle are also TBD.

Do not treat the bundled Agent Skills as evidence that the Spirited Journal
product itself is implemented.
