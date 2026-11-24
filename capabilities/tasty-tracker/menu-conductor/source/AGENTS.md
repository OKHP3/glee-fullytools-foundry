# glee-fully-gpt03b-menu-conductor

Canonical agent guidance for this repository. `CLAUDE.md` points here and should
not duplicate this file.

## Project identity

- Suite: Glee-fully, Branch 03
- Repository: https://github.com/OKHP3/glee-fully-gpt03b-menu-conductor
- Intended type: GPT Tool-ette
- Current repository state: early scaffold and project-local Agent Skills
  catalog. The repository contains 46 skill packages and guidance, but no
  menu-planning-specific implementation.
- Evidence snapshot: repository inspected on 2026-08-05.

## Lifecycle and current activity

- Lifecycle: reboot-in-progress for the intended product, with active
  maintenance limited to repository guidance and reusable agent skills.
- Recent commits through 2026-07-13 update `AGENTS.md`, `CLAUDE.md`, and the
  seeded skill packages; no product implementation has been added.
- The next product milestone is undefined until the owner confirms the runtime
  surface, authoritative prompt, workflow contract, and validation path listed
  under Safe next steps.

## Purpose, mission, and vision

### Confirmed

The prior project guide describes 03b as “Menu Conductor”, a weekly meal
planning and menu orchestration assistant. The repository name and its position
in the Glee-fully Branch 03 suite support that identity.

The current repository does not contain application code, a product prompt,
runtime configuration, or user-facing documentation that implements or further
specifies that purpose. Its present durable content is a catalog of project-local
Agent Skills and their supporting resources.

### Inferred

The intended mission is likely to help a person turn meal preferences,
constraints, and available food context into a coherent weekly menu. Treat this
as a product hypothesis, not as implemented behavior.

### Unknown

The longer-term vision, target user definition, supported inputs and outputs,
runtime surface, and integration plan are not established by repository
evidence.

## Scope and boundaries

This repository currently covers:

- Agent Skills stored under `.agents/skills/`.
- Project and migration prompts stored under `.agents/prompts/`.
- Shared guidance for agents working on the repository.
- Skill maintenance utilities and reference material included with those
  skills.

It currently does not provide:

- Meal-planning logic, recipes, menu data, or a user interface.
- A package manifest, application entry point, build system, test suite, or
  deployment configuration.
- A verified Notion integration or any committed private anchor configuration.

Do not infer production readiness, supported meal-planning workflows, or data
contracts until implementation evidence is added.

## Repository layout

- `AGENTS.md`: canonical agent guidance.
- `CLAUDE.md`: a short pointer to `AGENTS.md`.
- `README.md`: current-state orientation; it is not currently a product
  specification.
- `.agents/prompts/`: project onboarding, context bootstrap, and GPT-to-Agent-
  Skill migration prompts.
- `.agents/skills/`: 46 project-local Agent Skill packages, including their
  references, evaluations, fixtures, scripts, and tests where supplied.
- `.agents/skills/okhp3-skill-foundry/workspace/`: retained historical
  with-skill and without-skill evaluation outputs; treat these as versioned
  evidence, not as current release proof.
- `.agents/skills/README.md`: generated catalog of the 46 packages.
- `skills/okhp3-skill-promotion/`: publication mirror managed from its source
  package under `.agents/skills/`.
- `.gitattributes` and `LICENSE`: repository metadata.

There is one Git repository at the project root. No nested repository or
independent application was found.

## Technology and architecture

The confirmed implementation surface is Markdown instruction files, JSON
fixtures, HTML review assets, and Python utility scripts. The installed skills
are consumed by compatible agent clients. They are not a runtime for the Menu
Conductor product.

The Notion capture router declares that it requires access to a Notion
workspace connector, and GitHub reconciliation requires repository access.
Those are external capabilities of the skill workflow, not configured services
in this repository.

No application architecture or data flow can be confirmed yet. When product
implementation begins, document the entry point, input and output contracts,
state, external integrations, and error boundaries here.

## Validation and maintenance commands

Run commands from the repository root.

Verified during the 2026-08-05 inspection:

```bash
git status --short --branch
git log -8 --oneline --decorate
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --check
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --json
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs \
  --skills-dir .agents/skills
git diff --check
```

The catalog check found 46 skills. The Foundry structural validator validated
all 46 packages and reported advisory warnings about explicit scope sections or
obvious validation loops in some packages. These warnings do not establish
runtime quality or product behavior.

No build, test, lint, local-run, or deployment command is available to verify
because the repository has no corresponding configuration or application
implementation.

The cataloger documents a write-capable catalog command, but it was not run in
this maintenance pass because it would create or update generated catalog
artifacts:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills
```

Use that command when the project-local package inventory changes. Review its
generated changes before committing them.

## Change conventions

- Preserve user changes and avoid destructive version-control commands.
- Keep changes scoped to the requested guidance or skill work. Do not modify
  application code, dependencies, generated artifacts, CI behavior, or secrets
  unless the user explicitly requests that work.
- Keep `AGENTS.md` as the single canonical guide. Update `CLAUDE.md` only if it
  stops pointing to this file or gains genuinely Claude-specific instructions.
- The current branch is `main` and currently matches `origin/main`. No branch
  naming or commit-message convention is documented. Do not invent one.
- Keep public skill files free of private Notion URLs, database IDs, connector
  IDs, credentials, or other secrets. Obtain private anchors from runtime
  context or an explicitly private, uncommitted file when a supported workflow
  requires them.
- Keep employer-confidential or otherwise sensitive material out of public
  project artifacts.

## Brand and writing rules

- Do not use em dashes in generated content.
- Preserve standalone punchy lines. Do not fold them into surrounding
  paragraphs.
- Apply the ROY principle: explanation should earn its space and produce
  understanding.

The inherited AutoCAD R10 rule is not applicable to this repository and is not
treated as a project requirement.

## Safe next steps

Before implementing Menu Conductor behavior, confirm with the owner:

1. The intended runtime surface, such as a GPT configuration, prompt package,
   application, or another artifact.
2. The authoritative product prompt, user workflow, input schema, output
   format, and meal-planning constraints.
3. Whether Notion, GitHub, or another service is an actual runtime integration
   or only a knowledge-management workflow.
4. The intended status of this repository and the validation or deployment
   path.

When those answers are known, update this file with verified commands,
entrypoints, architecture, and operational boundaries. Replace hypotheses with
evidence as implementation lands.

## Related project

The prior guide names
[glee-fully-gpt03-tasty-tracker](https://github.com/OKHP3/glee-fully-gpt03-tasty-tracker)
as a related Branch 03 repository. Its local guide describes a broader food,
recipes, meal-planning, and culinary-tools branch, but this repository does not
currently document a concrete interface between the two projects.

## Imported Claude Cowork project instructions
