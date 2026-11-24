# glee-fully-gpt03e-palatably-profiled

## Project identity

- Suite label: Glee-fully, Branch 03.
- Project label: 03e, Palatably Profiled.
- Git repository: `https://github.com/OKHP3/glee-fully-gpt03e-palatably-profiled`.
- License: MIT. See `LICENSE`.
- Current repository state: agent-skill and documentation scaffold. No product implementation is present.
- The checkout currently contains 46 repository-local Agent Skill packages and three project-context prompts under `.agents/`.

The existing project description calls for a personal taste profile builder and a preference-aware recipe recommender. That describes the intended product, not a capability verified in this repository.

## Mission and vision

- Inferred mission: help a person express food preferences and use them to find more suitable recipes.
- Inferred vision: make recipe discovery feel personal, explainable, and useful over time as preferences become clearer.
- Unknown: intended users beyond the project description, supported platforms, product owner, data sources, and launch criteria.

## Scope and boundaries

This repository currently contains reusable agent skills and project guidance. It does not currently contain a recipe UI, API, preference data model, recommendation engine, database, deployment configuration, package manifest, test suite, or application entry point.

Do not describe the product as working or deployed without new repository evidence. Do not invent commands, integrations, user requirements, roadmap commitments, or production guarantees.

The related repository named in prior guidance is `glee-fully-gpt03-tasty-tracker`. Treat it as external context unless it is separately inspected and explicitly brought into scope.

## Repository structure

- `README.md`: title only. It is not a product or development guide.
- `AGENTS.md`: canonical agent guidance for this repository.
- `CLAUDE.md`: Claude-specific pointer to this file. Keep it aligned with the canonical guide.
- `LICENSE`: MIT license text.
- `.gitattributes`: Git text normalization settings.
- `.agents/prompts/`: project-context, GPT onboarding, and GPT-to-Agent-Skill migration orchestration prompts.
- `.agents/skills/`: 46 independent local Agent Skill packages, cataloged by `.agents/skills/README.md` and `.agents/skills/.catalog-meta.json`.
- `.agents/skills/okhp3-skill-cataloger/`: the catalog generator and validation workflow for this local skill surface.

The `.agents/skills/` directories are independent skill packages within this repository. No nested Git repositories or independent application projects were found.

## Technology and entry points

No application language, framework, package manager, runtime manifest, build system, test runner, or deployment target is declared.

The observed implementation surface is:

- Markdown skill instructions with YAML frontmatter in each `SKILL.md`.
- Python, JavaScript, and CommonJS helper scripts under the relevant skill packages.
- Skill assets, references, and Claude command files where a skill package provides them.

Use the relevant skill's `SKILL.md` as its entry point. There is no verified product runtime entry point.

## Working conventions

- Keep skill directory names and `name` frontmatter values lowercase kebab-case unless the skill format requires otherwise.
- Preserve the existing skill package layout: `SKILL.md`, then only the assets, references, scripts, or command files needed by that skill.
- Keep public skill files free of private Notion URLs, database IDs, credentials, and connector-only resource identifiers. The Notion capture skill expects private anchors to come from runtime context or a non-committed private file.
- Follow the OverKill Hill P3 writing rules: no em dashes in generated content, preserve standalone punchy lines, and make verbosity earn its space.
- Do not apply unrelated brand guidance, such as AutoCAD version requirements, to this repository.
- No repository-specific branch or release strategy is documented. Preserve the current Git workflow and ask for direction before introducing a new release process.

## Safe change procedure

1. Read this file and the nearest applicable skill instructions before editing.
2. Confirm that the requested change is within repository scope. Keep product implementation work separate from guidance maintenance.
3. Preserve existing user changes and avoid destructive version-control operations.
4. Make the smallest focused change. Do not modify dependencies, generated artifacts, CI behavior, or secrets as part of guidance maintenance unless that generated artifact is the explicitly approved target of the change.
5. Re-read every changed guidance file and verify paths, commands, and claims against the repository.
6. Run the applicable validation below and report limitations clearly.

## Validation

There is no repository-wide build, test, lint, or deployment command because no corresponding configuration exists.

Useful checks are:

```sh
git status --short --branch
git diff --check
```

The bundled structural validator can be run for every skill package:

```sh
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs --skills-dir .agents/skills
```

The project skill catalog can be checked and regenerated with:

```sh
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills
```

The structural validator currently reports warnings for some packages, including missing explicit `Scope` sections or obvious validation-loop wording. Warnings are not proof of failure; resolve them only when a skill-maintenance request is in scope.

## Known gaps and open questions

Confirmed gaps:

- The product implementation and its architecture are absent.
- `README.md` does not explain the intended product or how to use the local skill packages.
- No verified development, test, deployment, or release commands exist.
- Project status remains unknown. Existing placeholder status text was not promoted to a claim.
- The relationship between the intended food-preference product and the broad local skill corpus remains unresolved.

Owner input is needed to establish the intended product users, supported platform, technology choices, data and recipe sources, privacy requirements, recommendation behavior, and implementation roadmap.

## Keeping this guide current

Update this file when repository evidence changes, especially when an application runtime, manifest, tests, deployment target, nested project, or new instruction scope is added. Record confirmed facts separately from inferences and unknowns. Keep `CLAUDE.md` as a short pointer unless it gains genuinely Claude-specific rules.

## Imported Claude Cowork project instructions
