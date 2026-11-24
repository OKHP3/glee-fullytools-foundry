# glee-fully-gpt01c-career-fitness

## Current state

This repository is an early Glee-fully 01c Career Fitness scaffold that now
also contains a migrated Agent Skill library and skill-promotion workspace.

The intended Career Fitness purpose is to evaluate candidate fit and gaps
against target roles. That capability is not implemented here. The repository
does not currently define its input contract, scoring method, role model,
interface, integrations, deployment target, or acceptance criteria.

## Contents

- `AGENTS.md` - canonical repository guidance and confirmed boundaries.
- `.agents/prompts/` - project bootstrap and migration prompts.
- `.agents/skills/` - 46 local Agent Skill packages, their resources, tests,
  evaluations, and generated catalog.
- `skills/okhp3-skill-promotion/` - the reviewed publication mirror for the
  skill-promotion package.

The skill library is repository tooling. It is not evidence that the Career
Fitness product exists or runs.

## Validation

There is no application runtime or deployment command. Useful checks include:

```sh
git status --short
git diff --check
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs --root .agents/skills
python3 -m unittest discover -s skills/okhp3-skill-promotion/tests -v
```

See `AGENTS.md` before making structural or product changes.
