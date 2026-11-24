# glee-fully-gpt02-treasured-finds

Documentation-first Glee-fully Branch 02 repository with two connected purposes:

- an unresolved Treasured Finds planning concept;
- a local Agent Skill migration and publication workbench.

## Status

The Treasured Finds concept is still ambiguous. The repository does not define a
concrete user problem, audience, workflow, product runtime, or deployment target.
Do not describe it as a working product.

The Agent Skill workbench is the active, confirmed repository surface. It contains
local skill sources, migration prompts, validation material, and one maintained
publication mirror.

## Start here

- [`AGENTS.md`](AGENTS.md) for scope, evidence boundaries, and validation guidance.
- [Local skill catalog](.agents/skills/README.md) for the 46 repository-local skills.
- [Migration prompts](.agents/prompts/) for project onboarding and GPT-to-Agent-Skill work.
- [Publication mirror](skills/okhp3-skill-promotion/SKILL.md) for the promoted skill package.

## Repository map

| Path | Purpose |
| --- | --- |
| `.agents/prompts/` | Project onboarding and migration prompts. |
| `.agents/skills/` | Editable local Agent Skill sources and supporting resources. |
| `skills/` | Explicitly maintained publication mirror surface. |
| `AGENTS.md` | Canonical repository instructions. |
| `CLAUDE.md` | Compatibility pointer to `AGENTS.md`. |

There is no application source, dependency manifest, database, service boundary,
or deployment configuration in this repository.
