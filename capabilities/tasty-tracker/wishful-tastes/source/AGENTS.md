# Agent Guidance

## Project identity

- **Repository:** `glee-fully-gpt03c-wishful-tastes`
- **Suite:** Glee-fully, Branch 03
- **Repository kind:** Git repository containing a reusable Agent Skill workbench and publication mirror
- **Public repository:** https://github.com/OKHP3/glee-fully-gpt03c-wishful-tastes
- **Current status:** Active Agent Skill workbench. No restaurant application implementation is present in this checkout.

## Purpose and product context

**Confirmed by the repository:** This project distributes skills under `.agents/skills/`. The tracked implementation is Markdown skill guidance, YAML frontmatter, reference material, assets, and Python helper scripts.

**Inferred context:** Earlier guidance describes “Wishful Tastes” as a restaurant wishlist and dining discovery assistant, but the underlying product metadata is not identified in this repository. That product is not implemented in this checkout.

**Mission and vision:** No owner-authored mission or vision is present in the current files. Treat the restaurant-assistant direction as an inferred product context, not as an implemented capability or roadmap commitment.

## Scope boundaries

- Keep repository-maintenance changes focused on agent guidance, skill definitions, skill references, skill assets, and their supporting scripts.
- Do not assume that a restaurant UI, API, database, recommendation engine, deployment, or production integration exists here.
- Do not invent commands, dependencies, deployment guarantees, product behavior, ownership, or roadmap items.
- Preserve existing user changes and avoid destructive version-control operations.
- Do not add secrets, private service anchors, credentials, or machine-specific filesystem paths to committed guidance.
- The repository’s brand conventions include no em dashes in generated content, preservation of standalone punchy lines, and verbosity that earns its space.

## Repository structure

```text
.
├── AGENTS.md                              Canonical agent guidance
├── CLAUDE.md                              Claude guidance pointer to AGENTS.md
├── README.md                              Repository orientation and status
├── LICENSE                                MIT license
├── .gitattributes                         Text normalization rules
├── .agents/prompts/                       Project onboarding and migration prompts
├── .agents/skills/                        46 local skill packages
└── skills/okhp3-skill-promotion/         Verified publication mirror
```

There are no nested `AGENTS.md`, `agents.md`, `CLAUDE.md`, or `CONTRIBUTING.md` files. No nested repositories were found. There is no application package manifest, application source tree, CI configuration, container configuration, or deployment configuration. Individual skill packages may contain their own package manifests and tests.

## Technology and runtime

- Skill content is Markdown with YAML frontmatter.
- Supporting utilities and tests include Python 3 and Node.js scripts.
- The documented catalog check uses Python 3; the Foundry suite validator uses Node.js. Individual skills may require additional dependencies.
- Skills may require a compatible agent host or external connectors, as stated in each skill’s frontmatter. They are instructions and tooling packages, not a standalone service.

## Development and validation

Run commands from the repository root.

Check the installed skill catalog without writing generated files:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --check --quiet
```

Validate the complete local skill suite:

```bash
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs \
  --skills-dir .agents/skills
```

There is no verified build, test, lint, local server, packaging, or deployment command for the repository as a whole. When changing a skill, validate its frontmatter, inspect referenced paths, run any relevant helper script in a non-writing mode when available, and review the resulting diff.

## Change conventions

- Keep each skill self-contained under `.agents/skills/<skill-name>/`.
- Keep the frontmatter `name` aligned with the skill directory name and use lowercase kebab case.
- Put reusable supporting material in the skill’s `references/`, `assets/`, or `scripts/` directories.
- Keep private Notion anchors and connector-only identifiers out of public skill files. Use runtime or local non-committed configuration when a skill requires them.
- Treat generated catalogs and reports as generated outputs. Do not create or refresh them unless the task explicitly requests it.
- Update this file when repository structure, runtime assumptions, validation commands, or project purpose materially changes.

## Known gaps and risks

- The skill catalog is generated in project mode from `.agents/skills/`; rerun it after package changes rather than hand-editing the generated section.
- The Foundry structural validator currently validates all 46 packages but emits non-blocking advisory warnings for some packages.
- Historical Foundry raw evaluation outputs under `okhp3-skill-foundry/workspace/` are retained because the historical benchmark references that path.
- Python bytecode and cache files are ignored by `.gitignore` and are not maintained source.
- The product status, owner-approved mission, vision, and implementation plan remain unknown from repository evidence.

## Guidance precedence

This file is the canonical project guide. `CLAUDE.md` currently points to it and should remain a short pointer unless Claude-specific instructions are genuinely required. Higher-level instructions supplied by the execution environment take precedence over this file.

*Last aligned from repository evidence: 2026-08-06.*

## Imported Claude Cowork project instructions
