# glee-fully-gpt02c-present-hoarder

## Project identity

- Suite: Glee-fully, Branch 02.
- Product label: 02c, Present Hoarder.
- Repository type: single-project Git repository. No nested repositories or monorepo packages were found.
- Remote: https://github.com/OKHP3/glee-fully-gpt02c-present-hoarder
- License: MIT, as declared in `LICENSE`.
- Current status: pre-implementation placeholder. The repository has no application runtime, service, UI, or deployment configuration.

## Purpose and direction

- Confirmed project brief: a GPT tool-ette for gift tracking, wish-list management, and occasion planning.
- Inferred mission: help a person organize present ideas, gifts, and relevant occasions through a conversational workflow.
- Vision: unknown. No longer-term product vision is documented in the repository.
- Intended users: unknown. Do not assume a target audience, production guarantee, or supported workflow until the owner documents it.

The project brief is not yet represented by executable product code. Treat it as product context, not as evidence that these capabilities currently work.

## Scope and boundaries

The repository currently contains:

- One draft YAML prompt/configuration artifact.
- Root documentation and agent guidance.
- Local Agent Skills under `.agents/skills/`, currently 46 catalogable packages.
- Project-local onboarding and migration prompts under `.agents/prompts/`.
- The `skills/` directory contains an intentional publication mirror for selected packages; it is not a second product source tree.

The repository currently does not contain:

- An application source tree or package manifest.
- A gift, wish-list, or occasion data model.
- A user interface, API, persistence layer, external integration, or deployment target.
- Automated tests, lint configuration, build configuration, or release automation.

Do not describe the project as a working assistant or implement product behavior here unless the owner explicitly asks for that work.

## Repository map

- `prompts/02c-glee–fully-present-hoarder_prompts_v1.yaml`: five-field YAML artifact. Its current values identify it as `!PROCESSING_DRAFT`, a placeholder awaiting audit, with origin `BudgetBalancer_Build_Design` and target phase `Anvil`. It is not a production configuration.
- `README.md`: title-only project README.
- `AGENTS.md`: canonical repository guidance for coding agents.
- `CLAUDE.md`: short pointer to `AGENTS.md`; keep it aligned if its role changes.
- `.agents/prompts/`: durable onboarding, context-bootstrap, and GPT-to-Agent-Skill migration prompts.
- `.agents/skills/`: repository-local agent tooling and its supporting references, assets, scripts, and evaluation records. This is agent metadata, not product runtime.
- `skills/`: selected publication mirrors generated from `.agents/skills/`; do not edit both copies independently.
- `.gitattributes`: text normalization settings.
- `LICENSE`: MIT license.

The YAML filename contains a Unicode punctuation character. Preserve the exact filename and its contents unless the owner requests a prompt-artifact change.

## Technology and architecture

- Confirmed file formats: YAML and Markdown, with Python scripts bundled inside the local skill tooling.
- No application framework, runtime dependency set, package manager, lockfile, service boundary, or deployment model is currently declared.
- The only executable-looking code in the repository belongs to local skill tooling, especially `.agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py`. That tooling should not be mistaken for an application entry point.

## Local Agent Skills

The repository contains 46 local `SKILL.md` packages under `.agents/skills/`. They support repository governance, skill authoring and promotion, migration, evaluation, process analysis, and related knowledge operations. They do not implement Present Hoarder product behavior.

The package catalog is generated at `.agents/skills/README.md` by `.agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py`. The editable/incubating source for a package is normally under `.agents/skills/`; a selected copy under `skills/` is a publication mirror.

When working inside one of these skill directories, follow its local `SKILL.md` instructions in addition to this root guide. Do not expose private connector URLs, IDs, credentials, or personal data in committed files.

## Development and validation

Run commands from the repository root.

Before making changes, check the worktree and preserve existing user changes:

```bash
git status --short --branch
```

The current YAML artifact parses successfully with both available validators:

```bash
yq eval '.' 'prompts/02c-glee–fully-present-hoarder_prompts_v1.yaml'
ruby -e 'require "yaml"; p YAML.load_file("prompts/02c-glee–fully-present-hoarder_prompts_v1.yaml")'
```

For changes to `.agents/skills/`, use the cataloger's read-only checks before generating anything:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --dry-run
```

No repository-defined test, lint, build, run, or deployment command exists at present. Do not invent one in project documentation. If product code is added, document its verified entry points and validation commands here.

## Change conventions

- Keep `AGENTS.md` as the canonical source for repository-wide agent guidance.
- Keep `CLAUDE.md` as a short pointer unless Claude-specific instructions are genuinely needed.
- Make the smallest scoped change that satisfies the request. Do not modify application code, dependencies, generated artifacts, secrets, CI behavior, or unrelated files during a context-maintenance task.
- Do not use destructive version-control commands.
- The observed branch state is `main` tracking `origin/main`. No broader branch strategy is documented, so follow an explicit owner request for branch naming.
- No em dashes in generated content.
- Preserve standalone punchy lines when present.
- Apply the ROY principle: understanding produced and explanation invested. Verbosity must earn its space.
- AutoCAD version R10 is a general brand rule and is not applicable to this repository's current contents.

## Known gaps and risks

- The product mission, target users, vision, acceptance criteria, and owner-approved roadmap are not documented beyond the brief above.
- The YAML prompt is still a processing draft and references an audit that has not been performed in this repository.
- The repository has no executable product implementation or automated validation.
- The catalog metadata and README must be regenerated when the `.agents/skills/` package inventory changes.
- The Foundry evaluation workspace under `.agents/skills/okhp3-skill-foundry/workspace/` was removed as obsolete checkpoint output; durable benchmarks and evaluation definitions remain in the package.
- The related repository `glee-fully-gpt02-treasured-finds` is context only. Do not copy assumptions or files from it without a direct request.

## Keeping this guide current

Update this file when the repository gains product code, a runtime, dependencies, tests, deployment configuration, integrations, or a confirmed product status. Label material as confirmed, inferred, or unknown when the evidence is not equally strong. Recheck commands and paths after structural changes.

Last reviewed: 2026-08-06.

## Imported Claude Cowork project instructions
