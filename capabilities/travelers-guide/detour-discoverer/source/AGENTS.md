# glee-fully-gpt04c-detour-discoverer

## Project identity

- Suite: Glee-fully, Branch 04.
- Intended product: 04c, Detour Discoverer.
- Intended role: help travelers find off-the-beaten-path attractions and hidden gems.
- Repository type: standalone Git repository. No nested application or second project was found.
- License: MIT.
- Current repository state: pre-implementation product concept plus a project-local Agent Skills workspace. The tree contains project guidance, 46 Agent Skill packages under `.agents/skills/`, one documented publication mirror under `skills/`, a README, and a license, but no product source code.

The product description above is declared by the prior project guidance and repository name. The current repository does not yet demonstrate a working product, user interface, data source, integration, or deployment.

## Mission and vision

- Intended mission, inferred: make unusual, personally relevant travel discoveries easier to find and act on.
- Intended users, inferred: travelers seeking alternatives to standard tourist recommendations.
- Longer-term vision: unknown. Do not turn the inferred mission into a roadmap without owner direction.

## Scope and non-goals

This repository is the context and future implementation home for the Detour Discoverer concept. Keep changes within this project unless the user explicitly expands scope.

Do not infer or add a technology stack, live data provider, model provider, production guarantee, or deployment target from the product name alone. Do not modify the related Travelers Guide repository as part of work here.

## Repository layout

- `README.md`: public orientation for the concept, current status, repository map, and open decisions.
- `AGENTS.md`: canonical agent guidance for this repository.
- `CLAUDE.md`: points to `AGENTS.md`; preserve this relationship.
- `.agents/skills/`: repository-local Agent Skills and supporting assets, evaluations, references, and scripts. The generated catalog is `.agents/skills/README.md`, with metadata in `.agents/skills/.catalog-meta.json`.
- `skills/okhp3-skill-promotion/`: documented publication mirror of the matching project-local package. Do not edit or remove it as if it were an unrelated duplicate.
- `LICENSE`: MIT license.
- `.gitattributes`: enables automatic text detection and LF normalization.

The repository also contains a Foundry evaluation workspace under
`.agents/skills/okhp3-skill-foundry/workspace/`. Treat its files as retained
evaluation evidence unless an explicit future review classifies them as
disposable checkpoints.

There are no verified application entry points, runtime manifests, dependency lockfiles, test suites, build scripts, lint configuration, CI workflows, or deployment configuration in the current tree.

## Technology and runtime

No product language, framework, runtime, dependency set, or execution environment is established by repository evidence. Code and manifests under `.agents/skills/` belong to Agent Skill tooling and are not evidence of the Detour Discoverer product runtime.

## Development and validation

No product development, build, lint, or deployment commands are currently available to verify. Some individual Agent Skill packages contain their own deterministic scripts and tests; validate those only when that package is in scope.

For documentation or guidance changes, use checks such as:

```text
git status --short --branch
git diff --check
git diff -- AGENTS.md CLAUDE.md README.md
```

Before claiming a product change is validated, first document or discover the relevant implementation command and test coverage.

## Change safety and conventions

- Read this file and any more-specific guidance before editing.
- Preserve existing user changes. Do not use destructive version-control commands.
- Keep the root `AGENTS.md` factual and concise. Label confirmed facts, inferences, and unknowns rather than filling gaps with assumptions.
- Do not add secrets, credentials, private personal information, generated artifacts, or machine-specific paths.
- Do not commit Python bytecode or other local build artifacts. The root `.gitignore` covers Python cache files.
- No repository-specific branch naming strategy is documented. The current checkout is `main`; confirm the desired branch and publication scope before making branch or remote changes.
- Keep `CLAUDE.md` as a short pointer unless genuinely Claude-specific instructions are needed.
- Follow the project brand rules below for generated content: no em dashes, preserve standalone punchy lines, and make verbosity earn its space under the ROY principle.
- AutoCAD version is R10 when AutoCAD content is in scope. This constraint is retained from the existing project guidance and is not evidence of a current product dependency.

## Declared project metadata

These links were present in the prior project guidance and were not independently verified from the repository contents:

- GitHub: https://github.com/OKHP3/glee-fully-gpt04c-detour-discoverer
- Notion anchor: https://app.notion.com/p/e80f1102e6b141e8a5ee2a8f7fedd6f5
- Related repository: https://github.com/OKHP3/glee-fully-gpt04-travelers-guide

Treat those links as routing hints, not as proof of current product or organizational state.

## Known gaps and open questions

- What is the actual end-user workflow and interface?
- Which attraction, map, travel, or other data sources are allowed and required?
- Is this intended to be a GPT configuration, a service, a web application, or another form of tool?
- What runtime, dependencies, integrations, deployment environment, and security requirements should be used?
- What is the project owner-approved status, roadmap, and branch/release convention?
- Should the current Agent Skills workspace remain in this product repository, or should its ownership be separated later?

Resolve these from repository evidence or owner input before encoding them as project facts.

## Keeping this guide current

Update this file when the repository gains an implementation, runtime, commands, deployment behavior, or durable conventions. Re-check every referenced path and command, regenerate the skill catalog when the package set changes, remove stale claims, and keep `CLAUDE.md` aligned with this file. Record unresolved uncertainty instead of inventing project details.

## Imported Claude Cowork project instructions
