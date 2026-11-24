# glee-fully-gpt05e-lifestyle-wallboard

## Project identity

- Suite: Glee-fully, Branch 05.
- Intended type: GPT tool-ette.
- Git remote: `https://github.com/OKHP3/glee-fully-gpt05e-lifestyle-wallboard.git`.
- License: MIT, as stated in `LICENSE`.
- Repository shape: standalone Git repository. No nested repository or monorepo package was found.
- Current status: scaffold only. No application source, runtime manifest, application tests, build configuration, or deployment configuration was found. Product maturity and production status are unknown. Some agent skill packages contain their own tests.

## Purpose, mission, and vision

- Purpose, inferred from the repository name, the former guide, and the knowledge bundle: a lifestyle wallboard or personal KPI visualization assistant.
- Mission, inferred: help an individual see and interpret selected life metrics in one place.
- Users, inferred: people tracking personal routines, goals, or other life indicators.
- Vision: unknown. Do not turn the inferred purpose into a roadmap or product promise without owner evidence.

The repository does not currently contain a wallboard UI, data model, integration, or executable assistant implementation. Treat the product description above as context, not as proof of implemented behavior.

## Scope and non-goals

This repository currently contains project context, agent skills, and a static knowledge bundle. It is not currently a runnable application.

Do not invent or imply any of the following until implementation evidence is added:

- KPI definitions, dashboards, persistence, authentication, or data sources.
- External integrations, production guarantees, or deployment targets.
- Build, test, lint, or release commands beyond those documented and verified here.

Keep changes scoped to the requested project-context or agent-material work. Preserve the knowledge-bundle contents byte-for-byte unless the user explicitly asks for content changes. Do not modify skill content, dependencies, CI behavior, or application code unless the user explicitly asks for that work.

## Repository structure

| Path | Role |
| --- | --- |
| `AGENTS.md` | Canonical agent guidance for this repository. |
| `CLAUDE.md` | Compatibility pointer to `AGENTS.md`; keep it short unless Claude-specific rules are needed. |
| `README.md` | Minimal project title only. |
| `knowledgebundle/ledgers/` | Eight static `dataLedger_*_v2.txt` source ledgers. |
| `knowledgebundle/archives/` | Static ZIP export containing the eight ledger files. |
| `.agents/skills/` | Local Agent Skill packages and their supporting references, assets, scripts, and evaluations. These are agent instructions, not wallboard runtime code. |
| `skills/` | Separate skill-distribution mirror containing the promotion package. |
| `LICENSE` | MIT license. |
| `.gitattributes` | LF normalization and text detection. |

The knowledge bundle is mostly empty ledger scaffolding. Its ideation ledger contains generic thread seeds, including `LifestyleWallboard` under `05_Glee-fully_Organized_Life`; this establishes historical intent but not an implemented feature or confirmed branch mapping. Ledger sources live under `knowledgebundle/ledgers/`; the ZIP is a derived archive under `knowledgebundle/archives/`.

The declared related repository is `glee-fully-gpt05-organized-life`. It has not been inspected in this repository task, and no integration with it is present here.

## Technology and entry points

- Confirmed file formats: Markdown, plain text, Python, JSON, HTML, and ZIP.
- The project-specific catalog helper is `.agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py`; additional Python files belong to the seeded `skill-creator` skill.
- No application language, package manager, dependency manifest, lockfile, service entry point, build system, test runner, or deployment model is currently established.
- The `SKILL.md` files under `.agents/skills/` describe reusable agent workflows. Read the relevant skill before changing the material it governs.

## Development and validation

Run commands from the repository root.

Verified repository checks:

```sh
git status --short --branch
git log -8 --oneline --decorate
unzip -t knowledgebundle/archives/gleefully_lifestylewallboard_knowledgebundle.zip
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --help
```

There is no application test or build command to run at present. The skill cataloger preview command is useful only for inspecting the seeded skills:

```sh
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --dry-run
```

The preview reports the currently discovered local skill count and does not write files in dry-run mode. Treat the generated catalog as a separate skill-library concern; do not refresh it as part of wallboard content organization unless that change is explicitly in scope.

For guidance-only changes, re-read every changed guidance file and run:

```sh
git diff --check
git status --short --branch
```

## Conventions and safe changes

- `AGENTS.md` is the canonical guide. `CLAUDE.md` currently delegates to it with `@AGENTS.md`.
- No branch strategy, commit convention, application naming convention, or release process is documented. Preserve the current branch and existing naming unless the owner provides a rule.
- Preserve standalone punchy lines in generated content.
- Do not use em dashes in generated content.
- Apply the ROY principle: explanation should earn its space.
- Do not add secrets, credentials, private personal data, or unnecessary machine-specific paths.
- Treat the ZIP archive as a tracked artifact. If it is ever changed, inspect its contents and verify it with `unzip -t`.
- Preserve unrelated user changes and do not use destructive version-control commands.

## Known gaps and open questions

Important gaps:

- There is no confirmed implementation of the Lifestyle Wallboard product.
- The owner has not confirmed current status, target users, KPI model, data sources, runtime, integrations, or deployment.
- The repository name says `gpt05e`, while the bundle's historical seed places `LifestyleWallboard` under `05_Glee-fully_Organized_Life`.
- The skill catalog exists at `.agents/skills/README.md`. A dry run on 2026-10-27 found 46 local skills and proposed an update; catalog freshness is a separate skill-library concern.

Before adding product code or operational instructions, confirm the product identity, scope, runtime, data handling expectations, and deployment target. Update this file when those facts become evidenced by repository changes or an explicit owner decision.

## Imported Claude Cowork project instructions
