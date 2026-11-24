# glee-fully-gpt03d-pantry-shopper

## Project identity

- **Suite label:** Glee-fully / Branch 03.
- **Declared product label:** 03d: Pantry Shopper.
- **Repository:** `https://github.com/OKHP3/glee-fully-gpt03d-pantry-shopper`.
- **License:** MIT, copyright OverKill Hill P3, 2026.
- **Repository type, confirmed:** A Git repository containing Markdown-based Agent Skills and their supporting resources.
- **Product implementation status, confirmed:** No pantry, grocery, or inventory application code is present in this repository.
- **Status:** The skill bundle is present. The status of the Pantry Shopper product itself is unknown from repository evidence.

`CLAUDE.md` points to and imports `AGENTS.md`, so this file is the canonical guidance for both Codex and Claude work in this repository.

## Purpose and scope

The repository name and prior project notes describe a grocery list generation and pantry inventory assistant. That purpose is not implemented in the current tree. The current repository instead contains a small Agent Skills bundle for discovering, routing, cataloging, and creating skills.

### Confirmed current capabilities

- The repository contains 46 project-local Agent Skill packages under
  `.agents/skills/`.
- The bundle covers agent authoring, knowledge operations, process
  documentation, evaluation and governance, migration, Notion routing, and
  repository maintenance.
- `.agents/prompts/` contains three project onboarding and migration prompts.
- `okhp3-skill-cataloger` inventories `.agents/skills/` and validates or
  generates the catalog using Python standard-library code.
- `okhp3-skill-foundry` provides the package-quality and evaluation workflow;
  its durable historical benchmark records are separate from temporary raw
  evaluation workspaces.

### Scope boundaries

- Treat `.agents/skills/` as the primary project surface.
- Do not assume that the Pantry Shopper product has a UI, API, data model, runtime, deployment, or production behavior here.
- Do not add grocery-domain behavior merely because it is suggested by the repository name. Confirm the intended project boundary with the owner first.
- Do not modify external Notion pages, GitHub repositories, or connector-backed systems unless a task explicitly requests that work.

## Mission and vision

- **Confirmed mission:** No explicit mission statement is documented.
- **Inferred current mission:** Maintain reusable OverKill Hill P3 Agent Skills that can be loaded by compatible agent clients.
- **Vision:** Unknown. Do not turn the Pantry Shopper label or the related-repository links into a roadmap without owner confirmation.

## Repository structure

```text
AGENTS.md                         Canonical agent guidance
CLAUDE.md                         Pointer to AGENTS.md
README.md                         Public orientation and validation summary
LICENSE                           MIT license
.gitattributes                    Git text normalization
.agents/skills/<skill>/SKILL.md   Skill instructions and YAML frontmatter
.agents/skills/<skill>/assets/    Templates and schemas where needed
.agents/skills/<skill>/references/Supporting reference material where needed
.agents/skills/<skill>/scripts/   Executable helpers where needed
```

The 46 current skill directories are flat children of `.agents/skills/`. The
cataloger calls this **project mode**. There are no nested repositories in the
inspected tree. The top-level `skills/okhp3-skill-promotion/` directory is an
intentional publication mirror, not another runtime skill root.

## Runtime and validation

There is no application manifest, dependency lockfile, build configuration, test configuration, deployment configuration, or service entry point in the repository.

The cataloger documentation states that Python 3.9 or newer and no external dependencies are required. The available interpreter was Python 3.14.5 during this review.

Run commands from the repository root:

```bash
# Validate skill frontmatter, names, and descriptions without writing files.
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --check

# Print the discovered skill inventory as JSON without writing files.
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --json
```

`.agents/skills/README.md` and `.agents/skills/.catalog-meta.json` are
cataloger-owned generated outputs. Refresh them only when the skill inventory
changes or the task explicitly includes refreshing the catalog.

No repository-specific test, lint, build, run, or deployment command is currently documented or discoverable. When changing a skill, validate its Markdown/frontmatter shape and run any skill-specific checks described by that skill. If no check exists, report that limitation.

## Working conventions

- Keep each skill self-contained under its own directory.
- Keep the `name` frontmatter value equal to the skill directory name.
- Keep required skill metadata in YAML frontmatter, especially `name` and `description`.
- Put reusable templates, schemas, references, and scripts beside the skill that uses them.
- Follow progressive disclosure: keep the main `SKILL.md` operational and move large supporting material into `references/` or `assets/`.
- Preserve existing frontmatter, resource paths, output contracts, and compatibility requirements unless the task explicitly changes them.
- The cataloger is intended to run from the repository root and uses Python standard library code only.
- Preserve standalone punchy lines in generated content.
- Do not use em dashes in generated content.
- Apply the ROY principle: explanation should earn its space.
- The existing brand notes state that AutoCAD version R10 is locked. This repository has no AutoCAD files, so that rule is currently not operational here.

## Safe change procedure

1. Read the target skill's `SKILL.md` and only the referenced resources needed for the task.
2. Check `git status` before editing and preserve unrelated user changes.
3. Make the smallest scoped change. Keep application code, dependencies, generated artifacts, secrets, CI behavior, and unrelated skills out of scope unless explicitly requested.
4. Run the cataloger check and any relevant skill-specific validation.
5. Re-read every changed guidance or skill file and inspect the final diff.
6. Report confirmed behavior, warnings, and unresolved questions separately.

## External context and unresolved questions

The previous guidance listed a Notion anchor and `glee-fully-gpt03-tasty-tracker` as related context. Their relationship to this repository is not documented in the local files and was not verified during this review. Treat them as references only until the owner confirms their role.

Important unresolved questions:

- Is this repository intentionally a skill bundle, or was Agent Skill Seeding performed in the wrong Pantry Shopper repository?
- Should the Pantry Shopper assistant be implemented here, or should this repository be renamed or redirected to a separate skill project?
- What is the intended status, runtime, user interface, data source, and deployment model for the Pantry Shopper product?
- Should any of the 46 skills be removed or moved to a separate distribution
  repository?
- Which connector configuration, if any, is expected for the Notion capture workflow?

## Keeping this guide current

Update this file when the repository gains application code, new skills, manifests, tests, deployment configuration, or confirmed product decisions. Replace unknowns only with evidence from committed files or explicit owner input. Keep `CLAUDE.md` as a short pointer unless Claude-specific instructions are genuinely needed.

## Imported Claude Cowork project instructions
