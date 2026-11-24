# Agent Guide: glee-fully-gpt06d-medi-minder

## Project identity

- Suite: Glee-fully, Branch 06
- Role: Tool-ette twig 06d, Medi Minder
- Repository: `https://github.com/OKHP3/glee-fully-gpt06d-medi-minder`
- License: MIT
- Repository status: documentation and agent-workbench scaffold. No Medi Minder executable implementation is present in the current Git history.
- Deployment status: unknown. The parent Healthy Bee-ing pulsebook describes the parent GPT as private and live, but does not prove a separate Medi Minder deployment.

## Purpose and product context

### Confirmed

The repository identifies Medi Minder as a medication tracking and reminder-management assistant. The parent Branch 06 pulsebook places it in a wellness branch and describes its twig scope as medication, refill, and appointment tracking.

The intended value is a focused health workflow within the larger Healthy Bee-ing branch. The parent branch is described as routing user health prompts to specialized twigs and returning calm, clear, supportive guidance.

### Inferred

The primary user is a private end user who wants help organizing medication-related information, reminders, refills, and appointments. A reasonable future vision is a calm, unified medication-support experience that reduces missed actions without presenting itself as a medical professional.

### Unknown

The repository does not define a target-specific mission statement, product requirements, interaction contract, data model, release plan, owner contact, or deployment mechanism. Do not turn the inferred vision into an implementation guarantee.

## Lifecycle assessment

- Current stage: documentation and agent-workbench scaffold with active guidance maintenance, not an active Medi Minder software implementation.
- Evidence: the latest commit is `f0772f4` on 2026-08-05. Recent commits add migration prompts, Agent Skill packages, catalog metadata, and promotion support rather than Medi Minder application code.
- Reboot status: implementation has not started in this checkout. The next meaningful step is to obtain the target instruction contract, safety policy, and implementation decisions before choosing a runtime.

## Scope and boundaries

In scope for this repository:

- Agent and project context documentation.
- The parent Branch 06 pulsebook reference.
- The local Agent Skills stored under `.agents/skills/`.
- The migration prompts stored under `.agents/prompts/`.
- The promotion mirror stored under `skills/okhp3-skill-promotion/`.

Not currently present:

- Application or GPT instruction source.
- Medi Minder runtime code, data storage, integrations, UI, tests, CI, or deployment configuration.

The Agent Skill packages under `.agents/skills/` contain their own package
manifests and validation files. Those package-level files do not constitute a
Medi Minder runtime.

For future health-related implementation, retain a clear not-medical-advice boundary, avoid diagnosis or prescribing, protect medication data, and define escalation behavior for urgent or ambiguous situations before adding features.

## Repository structure

The repository is a single Git repository. No nested Git repositories or independent application projects were found.

- `docs/healthy-bee-ing-pulsebook-2025-09-01.md`: parent Branch 06 identity, scope, sibling matrix, and historical operational notes.
- `.agents/skills/`: 46 local Agent Skill packages, including cataloging,
  migration, repository maintenance, evaluation, promotion, and general
  knowledge-operation capabilities. The generated catalog is the inventory
  authority for this directory.
- `.agents/prompts/`: project onboarding, context bootstrap, and GPT-to-skill
  migration prompts.
- `AGENTS.md`: canonical agent guidance for this repository.
- `CLAUDE.md`: short compatibility pointer to this guide.
- `README.md`: project orientation, current status, boundaries, and start-here links.
- `.gitattributes`: LF normalization and text detection.
- `LICENSE`: MIT license.

There are no application entry points or representative source files to describe yet.

## Architecture snapshot

- Parent context: `docs/healthy-bee-ing-pulsebook-2025-09-01.md` records the broader wellness branch and places Medi Minder in medication, refill, and appointment tracking.
- Repository guidance: `AGENTS.md` is canonical; `CLAUDE.md` points to it for Claude-compatible use.
- Local capabilities: `.agents/skills/` contains 46 reusable Agent Skills and
  their supporting references, assets, scripts, tests, and historical evidence.
- Migration support: `.agents/prompts/` contains three reusable project and
  GPT-to-skill migration prompts.
- Publication mirror: `skills/okhp3-skill-promotion/` mirrors the local
  promotion package and should be changed only through the promotion workflow.
- Medi Minder runtime surface: none is present. The repository does contain
  tests and validators inside Agent Skill packages, but there are no Medi
  Minder application modules, services, data stores, integrations, UI assets,
  CI workflows, or deployment files.

## Technology and operations

No Medi Minder programming language, framework, runtime, data store, build
system, test runner, or deployment target is declared. Do not invent setup or
run commands. The local Agent Skill packages may declare their own
package-level runtimes and validators, but those are not project runtime
instructions.

Verified repository checks:

- `git status --short --branch`
- `git log --oneline --decorate`
- `git ls-tree -r --name-only HEAD`
- `python3 .agents/skills/okhp3-repository-organizer/scripts/inventory_repo.py --root .`
- `python3 .agents/skills/okhp3-repl-repo-janitor/scripts/audit-repo.py --root . --base origin/main`
- `node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs --skills-dir .agents/skills`

These checks confirm the current documentation and agent-workbench shape. No
Medi Minder build, lint, or test command is available to run.

## Change conventions

- Keep this file as the single canonical guide. Update `CLAUDE.md` only for Claude-specific additions or to preserve the pointer.
- Preserve existing user changes and avoid destructive version-control commands.
- Keep repository guidance factual. Label conclusions as confirmed, inferred, or unknown when evidence is limited.
- Make guidance changes without modifying application code, dependencies, generated artifacts, secrets, CI behavior, or unrelated files unless the user explicitly expands scope.
- Preserve standalone punchy lines; do not consolidate them into paragraphs.
- Do not use em dashes in generated content.
- Apply the ROY principle: explanation should earn its space.
- Treat the pulsebook as historical parent-branch context. Re-check claims against newer repository evidence before relying on them.

## Validation and handoff

After changing guidance:

1. Re-read every changed guidance file.
2. Check referenced paths against the repository tree.
3. Run the available Git inspection commands when practical.
4. Report implementation and deployment uncertainty plainly.

When executable code is added, update this guide with verified setup, test, lint, build, and deployment instructions. When the project status or product scope changes, update the identity and evidence sections at the same time.

## Evidence and open questions

Primary evidence used for this guide:

- The current repository tree and Git history.
- `docs/healthy-bee-ing-pulsebook-2025-09-01.md`.
- The prior `AGENTS.md` and `CLAUDE.md` files.
- `.agents/skills/*/SKILL.md` metadata and instructions.

Open questions for the owner:

- Is Medi Minder a separately deployed GPT, or only a planned twig of the parent GPT?
- What exact user-facing instruction block, supported workflows, and safety policy should be implemented?
- What runtime, storage, integrations, validation approach, and release process should future code use?

## Imported Claude Cowork project instructions
