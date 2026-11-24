# Glee-fully GPT07c Sight Seeker

This repository currently contains a project-local Agent Skills bundle. It is not a visual-analysis application.

## Current purpose

The repository packages reusable guidance for Agent Skill discovery, authoring, evaluation, migration, repository organization, evidence handling, process work, and promotion. The active skill surface is under `.agents/skills/`, with onboarding prompts under `.agents/prompts/`.

The repository name and branch label suggest a future Sight Seeker direction for visual scene analysis and point-of-interest identification. No implementation evidence for that product exists in this checkout, so that direction remains unconfirmed.

## Repository map

- `.agents/skills/` contains the 46 local Agent Skill packages.
- `.agents/prompts/` contains project-onboarding and migration prompts.
- `.agents/skills/README.md` and `.agents/skills/.catalog-meta.json` are generated catalog outputs.
- `skills/okhp3-skill-promotion/` is the verified publication mirror for the local promotion skill.
- `AGENTS.md` contains the canonical repository guidance.
- `CLAUDE.md` points to `AGENTS.md`.

## Validation

Run from the repository root:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --check

node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs \
  --skills-dir .agents/skills

python3 skills/okhp3-skill-promotion/scripts/sync_skill_mirror.py \
  --source .agents/skills/okhp3-skill-promotion \
  --destination skills/okhp3-skill-promotion --check
```

The catalog command in ordinary write mode regenerates the marked catalog files. Do not edit their generated sections manually.

## Scope boundary

Do not infer a visual-analysis runtime, model provider, interface, deployment model, or production status from the repository name. Product implementation requires explicit owner direction and evidence for those decisions.
