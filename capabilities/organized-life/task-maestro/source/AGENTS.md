# glee-fully-gpt05a-task-maestro

## Project identity and status

- Suite: Glee-fully, Branch 05.
- Type: GPT Tool-ette scaffold and knowledge bundle.
- Repository: `https://github.com/OKHP3/glee-fully-gpt05a-task-maestro`.
- Current status: implementation is not present in this checkout. Treat the project as a documentation and agent-workbench scaffold with product status otherwise unknown.
- Scope: this file is the canonical agent guidance for the repository root. `CLAUDE.md` points here.

## Purpose, mission, and vision

- Confirmed from the existing project metadata: the intended subject is personal task management and prioritization.
- Inferred from the repository name and suite placement: the project is intended to be a focused Tool-ette within the broader Glee-fully Organized Life family.
- Mission and longer-term vision: unknown. Do not invent product behavior, users, roadmap, integrations, or production guarantees until repository evidence or owner direction provides them.
- Important distinction: the repository contains no registered Task Maestro entity, system ruleset, persona, narrative, or executable configuration. The knowledge bundle is not proof that those capabilities are implemented.

## Repository structure

This is a standalone Git repository, not a monorepo, package, service, or library based on the current tracked contents. No nested repository was found.

- `AGENTS.md`: canonical agent guidance.
- `CLAUDE.md`: short pointer to `AGENTS.md`.
- `README.md`: public orientation and current-status summary.
- `knowledgebundle/`: tracked v2.0.0 canonical ledger files.
  - `dataLedger_registry_v2.txt`
  - `dataLedger_system_v2.txt`
  - `dataLedger_parameters_v2.txt`
  - `dataLedger_narrative_v2.txt`
  - `dataLedger_processing_v2.txt`
  - `dataLedger_persona_v2.txt`
  - `dataLedger_archive_v2.txt`
  - `dataLedger_ideation_v2.txt`
- `knowledgebundle/exports/`: packaged ZIP export of the eight ledger files. Its internal filenames remain unchanged.
- `.agents/prompts/`: project-local onboarding, migration, and context-bootstrap prompts.
- `.agents/skills/`: 46 project-local Agent Skill packages and a generated catalog. These are agent workflow resources, not application runtime code.
- `skills/okhp3-skill-promotion/`: byte-identical publication mirror for the local promotion skill, maintained by its synchronization workflow.
- `LICENSE`: MIT license for the repository contents.

The bundle currently contains only a few control parameters and ideation-stage thread seeds. Its ideation ledger includes a `TaskTamer` seed under `05_Glee-fully_Organized_Life`, which does not establish that `TaskTamer` and this `Task Maestro` repository are the same project. The local Agent Skill workbench was added later for project migration and governance support, and should not be mistaken for Task Maestro product implementation.

## Technology and runtime

- No application language, framework, dependency manifest, build configuration, test configuration, deployment configuration, or runtime entry point was found.
- The repository uses Markdown, plain-text ledger records, YAML-like data fragments, JSON, Python and JavaScript skill tooling, and a ZIP archive.
- The code under `.agents/skills/` is skill tooling, not a verified project runtime.
- No local run command or deployment model is currently supported by repository evidence.

## Validation

The following checks are appropriate for the current repository shape and were verified during the context review:

```text
git status --short --branch
git log -8 --oneline --decorate
git ls-files
unzip -t knowledgebundle/exports/gleefully_taskmaestro_knowledgebundle.zip
git diff --check
```

There are no project tests, linter, build, or application smoke test to run at present. The skill cataloger documents a Python command that can generate `.agents/skills/README.md`; run it only when a skills catalog is explicitly requested because it writes a generated file.

## Safe change conventions

- Make changes from the repository root and preserve unrelated user work.
- Keep `AGENTS.md` as the single canonical guidance file. Keep `CLAUDE.md` as a short pointer unless Claude-specific guidance is genuinely needed.
- Do not treat ideation, archived ledger records, or thread seeds as implemented features.
- Do not add application code, dependencies, secrets, credentials, private Notion URLs, or generated catalogs unless the user explicitly requests that work.
- If the knowledge bundle is changed, preserve its ledger filenames, canonical v2.0.0 markers, and archive structure. Validate the resulting ZIP before handoff.
- No branch naming or release convention is documented. Do not invent one. The reviewed checkout is currently on `main`.

## Brand and writing rules

- No em dashes in generated content.
- Preserve standalone punchy lines. Do not consolidate them into paragraphs.
- ROY principle: understanding produced / explanation invested. Verbosity must earn its space.
- AutoCAD version is R10, locked and not negotiable.

## Known gaps and risks

- The actual GPT instructions, tool definition, interface, data model, integrations, and user workflow are absent.
- The generated skill catalog must be refreshed when the `.agents/skills/` package set changes. Do not hand-edit its generated section.
- Project status is not established beyond the presence of scaffolding and seed material.
- The relationship between this repository, `glee-fully-gpt05-organized-life`, and the `TaskTamer` ideation seed is unresolved.
- `README.md` provides orientation and validation guidance, but setup, usage, ownership, and the product contract remain undefined.
- The bundle records carry 2025 generation dates, while the repository has later commits. Their current ownership and update workflow are unknown.

## Keeping this guide current

Update this file when the repository gains an implementation, runtime or dependency manifest, verified commands, deployment configuration, a defined project status, or clarified product scope. Label new conclusions as confirmed or inferred when the evidence is not direct. Recheck `CLAUDE.md` whenever the canonical guidance filename changes.

## Imported Claude Cowork project instructions
