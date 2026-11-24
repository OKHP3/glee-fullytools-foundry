# glee-fully-gpt02b-decor-detective

## Scope and precedence

This file is the canonical agent guide for the repository root. `CLAUDE.md` points here, so keep both files aligned. The `.agents/skills/` directory contains 46 skill packages with their own `SKILL.md` files. When working inside a skill package, follow that skill's instructions in addition to this root guide.

The repository is a single Git project. No nested repositories, worktrees, application packages, or service directories were found.

## Project identity and status

- Suite: Glee-fully, Branch 02
- Project label: 02b, Decor Detective
- Intended type: GPT Tool-ette
- Stated purpose: home decor identification and sourcing assistance
- Repository: https://github.com/OKHP3/glee-fully-gpt02b-decor-detective
- Related repository: https://github.com/OKHP3/glee-fully-gpt02-treasured-finds
- Current status: early product scaffold plus an Agent Skills distribution and migration workbench, confirmed by the current tree and recent history

The Decor Detective product has no implementation beyond its project identity and historical placeholder. The repository also contains a substantial, separately scoped Agent Skills collection and promotion mirror. Do not describe Decor Detective as working, deployed, or production-ready.

## Mission, vision, and boundaries

The stated mission is to help identify home decor and find sourcing leads. This is supported by the project identity, but no implementation currently demonstrates the workflow.

The longer-term vision is unknown from repository evidence. Do not invent product commitments, supported retailers, image-recognition behavior, pricing coverage, or deployment guarantees.

Current repository scope:

- Product orientation and governance files for Decor Detective
- Reusable Agent Skills under `.agents/skills/`
- The promotion mirror under `skills/okhp3-skill-promotion/`
- Agent Skill benchmarks, fixtures, and validation resources

Not currently present:

- Application or GPT runtime code
- Image-processing or retrieval integrations
- Retailer, catalog, or product data
- Dependency manifests or lockfiles for the product
- Product automated tests, CI configuration, or deployment configuration

Treat the bundled skills as repository tooling and reusable agent capabilities, not as proof that Decor Detective itself is implemented.

## Repository structure

- `README.md`: public orientation, current status, validation, and open decisions.
- `AGENTS.md`: canonical guidance for agents working at the repository root.
- `CLAUDE.md`: short pointer to this file.
- `.agents/skills/README.md`: generated catalog of the current 46 local skills.
- `.agents/skills/okhp3-skill-cataloger/`: skill inventory and catalog tooling.
- `.agents/skills/okhp3-skill-foundry/`: skill authoring, evaluation, and release guidance.
- `.agents/skills/okhp3-skill-promotion/`: promotion workflow and benchmarked synchronization support.
- `skills/okhp3-skill-promotion/`: promotion mirror used by the synchronization benchmarks.
- `LICENSE`: MIT license, copyright 2026 OverKill Hill P3.

## Technology and entry points

No product language, framework, runtime, dependency set, or executable entry point is declared. Python, JavaScript, YAML, JSON, and Markdown files are part of the bundled skill tooling and evidence, not a declared Decor Detective application.

The repository's executable entry points are skill-specific:

- Read a skill's `.agents/skills/<skill-name>/SKILL.md` before using or changing that skill.
- For a read-only catalog validation, use:
  `python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check`
- Catalog generation is an approved maintenance operation when the skill inventory changes. It updates the generated catalog files.

There is no verified local run command for a Decor Detective product. Do not add one until an implementation and its runtime instructions exist.

## Change and documentation conventions

- Make the smallest change that satisfies the request and preserve unrelated user work.
- Do not modify application code, dependencies, generated artifacts, secrets, CI behavior, or unrelated files when maintaining repository context.
- Do not use destructive version-control commands such as reset, checkout, or clean unless explicitly requested.
- The current branch is `main` and tracks `origin/main`. Preserve the active branch unless the user asks for branch work.
- Keep standalone punchy lines as standalone lines when editing project-facing content.
- Do not use em dashes in generated content. Use commas, colons, parentheses, or a simple hyphen instead.
- Apply the OverKill Hill P3 writing principle: explanation should earn its space.
- Avoid embedding credentials, private data, or machine-specific paths in committed files.

## Safe workflow for future changes

1. Read this file and any more specific `SKILL.md` that applies to the requested path.
2. Check `git status` and preserve existing user changes, including the pre-sync stash.
3. Confirm whether the request concerns product orientation, a bundled skill, or the promotion mirror.
4. Inspect the relevant files before editing. Do not infer runtime behavior from the project name.
5. Make the narrowest in-scope edit.
6. Validate the changed artifact and run `git diff --check`.
7. Re-read changed guidance or skill files and report any unresolved uncertainty.

## Validation and known limitations

The repository has no product test suite, build, lint, or deployment check. Available validation is limited to:

- Catalog validation for the 46 local Agent Skills
- Python syntax checks for bundled skill scripts
- Skill-specific fixtures and tests where packages provide them
- `git diff --check` for whitespace errors

The product implementation is absent. The Notion routing skill requires external Notion context for real writes and must remain report-only when its anchors or permissions are unavailable.

## Open questions

- What runtime or host will deliver the Decor Detective GPT Tool-ette?
- Is a new canonical product prompt still intended, now that the historical placeholder has been removed?
- What image, search, retailer, catalog, or sourcing integrations are in scope?
- What is the owner-confirmed project status and release/deployment model?
- What test and evaluation criteria should define a correct identification or sourcing response?

## Keeping this guide current

Update this file when the repository gains an implementation, runtime instructions, tests, integrations, deployment configuration, or an owner-confirmed status. Label conclusions as confirmed, inferred, or unknown when the evidence does not justify stronger wording. Keep `CLAUDE.md` as a pointer unless it needs genuinely Claude-specific instructions.

## Imported Claude Cowork project instructions
