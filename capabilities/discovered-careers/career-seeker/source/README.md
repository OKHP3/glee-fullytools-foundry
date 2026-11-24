# glee-fully-gpt01f-career-seeker

01f Career Seeker is an early Glee-fully project scaffold associated with
career-search strategy and opportunity discovery.

## Current scope

This repository currently functions as an Agent Skills workbench. It contains
reusable skills and their supporting references, assets, scripts, evaluation
cases, and project prompts. It does not contain a runnable career-search
application, search provider, ranking model, user interface, data store,
external API integration, or deployment configuration.

The current inventory contains 46 local skill packages. The included skills
support:

- project and repository organization
- Agent Skill discovery, authoring, evaluation, promotion, and cataloging
- ChatGPT, Claude, and project-context migration workflows
- Notion capture and knowledge-operations workflows
- process analysis, decision modeling, handoff, and evidence governance
- Glee-fully-specific repository, brand, and agent workflows

## Skill source and mirror surfaces

`.agents/skills/` is the local runtime source surface for the project. The
top-level `skills/` directory contains publication mirrors only when a package
has an explicit promotion workflow. The existing
`skills/okhp3-skill-promotion/` mirror is verified against its source with the
bundled synchronization checker. The mirror is not a second authoring location.

The generated catalog is [`.agents/skills/README.md`](.agents/skills/README.md),
and its metadata is [`.agents/skills/.catalog-meta.json`](.agents/skills/.catalog-meta.json).

## Validation

From the repository root, run:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check
```

The catalog check requires Python 3.9 or newer and standard-library
dependencies only. There is currently no application start command, build
command, unified test suite, lint configuration, CI workflow, or deployment
command.

See [AGENTS.md](AGENTS.md) for repository instructions, scope boundaries, and
open questions. The project is licensed under the [MIT License](LICENSE).
