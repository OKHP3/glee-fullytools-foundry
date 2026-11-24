# glee-fully-gpt03a-flavor-meister

## Project identity and status

- Suite: Glee-fully, Branch 03.
- Product name: 03a Flavor Meister.
- Declared purpose: flavor profiling, recipe suggestion, and ingredient pairing assistance.
- Repository: [OKHP3/glee-fully-gpt03a-flavor-meister](https://github.com/OKHP3/glee-fully-gpt03a-flavor-meister).
- Current state: scaffolded and skill-seeded. No product source code, runtime manifest, test suite, deployment configuration, or implemented user interface is present.
- This guide is the canonical repository guidance. `CLAUDE.md` points here.

## Mission, users, and scope

- Mission, inferred from the repository name and prior project description: help a person reason about flavors, pair ingredients, and suggest recipes.
- Primary users: unknown. No product requirements, user research, or interface specification is present.
- Vision: unknown. Do not invent roadmap, production status, integrations, or guarantees.
- Current repository scope is limited to project guidance and reusable agent skills. Do not treat the declared product purpose as implemented functionality.
- A related repository, `glee-fully-gpt03-tasty-tracker`, is named in the prior guide, but its relationship and current contract have not been verified here.

## Repository structure

The repository is a standalone Git repository with no nested repositories found.

- `README.md`: public orientation, current-state boundary, and repository map.
- `AGENTS.md`: canonical agent guidance.
- `CLAUDE.md`: short pointer to `AGENTS.md`.
- `LICENSE`: MIT license, copyright 2026 OverKill Hill P3.
- `.agents/skills/`: 46 local Agent Skill packages and their supporting files.
  This is a broad seeded workbench containing universal, process, evaluation,
  migration, repository, and Glee-fully-specific skills. It is not product
  implementation.
- `skills/okhp3-skill-promotion/`: a separate promotion mirror of one local
  skill. Its retention and repository boundary remain under review.

No application entry point, package, service, database, API, or data flow can currently be confirmed.

## Runtime and commands

No product runtime or dependency manager is defined. Python 3 is available and is used by the bundled skill helper scripts, not by a confirmed product runtime.

Useful read-only checks from the repository root:

```sh
git status --short --branch
git diff --check
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --mode project --check
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs --root .agents/skills
```

The catalog check must describe the current skill surface; it is not a product
build or runtime check. There is no verified product build, test, lint,
local-run, or deployment command. Do not claim that the Flavor Meister product
is runnable until source and configuration are added and a corresponding check
is verified.

## Change and content conventions

- Preserve existing user changes. Inspect status and diffs before editing.
- Do not use destructive version-control commands.
- Keep changes scoped to the requested files and preserve the repository's MIT license and skill assets.
- The current branch is `main` and tracks `origin/main`. No additional branch or commit naming convention is documented.
- Generated content must not use em dashes.
- Preserve standalone punchy lines when editing project content.
- Apply the OverKill Hill P3 ROY principle: explanation should earn its space.
- The prior guide listed AutoCAD R10 as a global rule. No AutoCAD content exists here, so it is not an active repository concern unless that scope is explicitly introduced later.
- Do not place secrets, credentials, private Notion URLs, or unnecessary machine-specific paths in tracked guidance.

## Safe workflow for future agents

1. Read this file and `README.md` before making changes.
2. Confirm whether the task concerns repository guidance, local skills, or future product implementation.
3. Keep product work separate from skill maintenance. Do not alter `.agents/skills/` while making unrelated product changes.
4. For skill changes, read the target skill's `SKILL.md` and run its available validation helper.
5. Re-read changed guidance, run applicable checks, and inspect `git diff --check` before handoff.
6. Update this file when verified repository structure, commands, runtime, or conventions change.

## Known gaps and open questions

- Product status is not formally recorded beyond the evidence that the repository is currently scaffolded.
- Language, framework, dependencies, product entry point, data model, integrations, deployment model, and test strategy are unknown.
- Intended users, product requirements, and the boundary with `glee-fully-gpt03-tasty-tracker` are unknown.
- The broad seeded skill library may exceed the intended scope of this product
  repository; no removal or relocation has been approved.
- Some packages contain historical benchmarks, evaluation workspaces, or
  deliberate generic/brand variants. Treat those as provenance-bearing until
  their lifecycle and canonical location are confirmed.

## Imported Claude Cowork project instructions
