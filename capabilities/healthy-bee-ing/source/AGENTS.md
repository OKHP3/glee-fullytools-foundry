# Agent Guidance: glee-fully-gpt06-healthy-bee-ing

This file is the canonical agent guide for this repository. `CLAUDE.md` points
to it. It applies to the repository root and its descendants unless a more
specific guidance file is added.

## Project identity and scope

- **Suite:** Glee-fully
- **Branch:** #06, Healthy Bee-ing
- **Repository type:** Documentation and prompt-design repository
- **Git state observed:** A single Git repository; no nested repositories or
  separate application packages were found.

The repository documents a wellness branch intended to organize health and
self-care guidance through six sibling twigs:

- Care Check: symptom triage and urgency guidance
- Calm Keep: stress, sleep, and micro-movement balance
- Snappy Count: nutrition awareness
- Medi Minder: medication, refill, and appointment tracking
- Moody Log: hydration, mood, and reflection timelines
- Maven Wise: midlife and hormonal-change support

These capabilities are documented design scope. This repository contains no
verified application implementation, service, database, or deployment
configuration.

## Mission and vision

The pulsebook describes the design intent as helping people approach everyday
health tasks with calm, clear, supportive guidance. Its stated vision is a
unified wellness space that reduces fragmentation and overwhelm.

Treat this as documented product intent, not as a verified production mission
or guarantee. The intended audience, owner workflow, runtime, and deployment
environment are not fully established in the repository.

## Scope boundaries and non-goals

Work in this repository is limited to project documentation, prompt artifacts,
and agent guidance unless the user explicitly expands the scope.

- Do not present health content as diagnosis, treatment, or medical advice.
- Do not invent clinical escalation rules, health claims, integrations, or
  production guarantees.
- Do not add real patient data, credentials, or other sensitive information.
- Treat the six sibling repositories as separate projects. Do not modify them
  as part of work in this repository.
- Do not treat references to absent `dataLedger_*` files as proof that those
  files exist or are authoritative.

## Repository structure

- `README.md`: minimal repository landing page.
- `docs/06-glee-fully-healthy-bee-ing_pulsebook_20250901.md`: the most detailed
  identity, design-intent, twig matrix, and historical deployment note.
- `docs/06-glee-fully-healthy-bee-ing_instructions.md`: older ecosystem directive
  with lifecycle, routing, and tone concepts. It references `dataLedger_*v2`
  files that are not present here.
- `docs/06-glee-fully-healthy-bee-ing_build.md`: build-design stub; no executable
  build prompt is currently supplied.
- `docs/06-glee-fully-healthy-bee-ing_ideation.md`: early ideation stub.
- `.agents/skills/`: bundled agent skills and supporting assets. These are
  repository tooling and reference material, not the Healthy Bee-ing runtime.
- `AGENTS.md`: canonical guidance for agents.
- `CLAUDE.md`: short pointer to `AGENTS.md`.

No package manifest, source directory, test suite, CI workflow, deployment
file, or application entry point was found.

## Technology and validation

The confirmed working format is Markdown with embedded YAML-like metadata and
prompt text. No language runtime or dependency manager is configured.

There is no verified build, test, lint, or run command. For documentation-only
changes, use repository inspection and Git checks as the validation baseline:

```sh
git status --short --branch
rg --files --hidden -g '!.git/**'
git diff --check
```

If a future change introduces executable tooling, document its verified setup
and commands here and add the corresponding project files.

## Safe editing conventions

- Preserve the existing filename and naming pattern for branch artifacts.
- Keep claims labeled by evidence level when status, deployment, ownership,
  or architecture is uncertain.
- Preserve standalone punchy lines when editing branded content.
- Do not use em dashes in generated content.
- Keep the Glee-fully tone warm, clear, and supportive, while allowing safety
  and uncertainty statements to remain direct.
- Preserve historical material when it is clearly labeled as historical.
- When editing the older ecosystem directive, do not silently upgrade its
  `dataLedger_v2` references. Resolve the source-of-truth question first.

Before changing files, inspect `git status` and preserve existing user edits.
Use non-destructive Git operations only. Keep changes narrowly scoped to the
requested documentation or guidance work.

## Current risks and known gaps

- The pulsebook records an as-deployed status of “Live” and private visibility
  as of 2025-08-31, but this repository has no deployment evidence. Current
  live status is therefore unknown.
- The instruction file names `dataLedger_*v2` as canonical, while the
  pulsebook names `dataLedger_*_v3`; neither set exists in this repository.
- The pulsebook marks health disclaimers, succession, reasoning annexes, and
  several function cards as placeholders or stubs.
- The build and ideation documents are scaffolds rather than operational
  specifications.
- The repository does not define a current status, runtime, release process,
  ownership channel, or acceptance criteria.

## Keeping this guide current

Update this file when repository structure, runtime, validation commands,
source-of-truth documents, or product status changes. Verify new claims from
files or executable checks. Record unresolved owner decisions as open questions
instead of converting them into instructions.

## Open questions for the owner

1. Is Healthy Bee-ing currently deployed, or is the pulsebook’s 2025 “Live”
   label historical only?
2. Which ledger files, if any, are authoritative, and where should they live?
3. Is this repository intended to remain documentation-only, or will an
   application or GPT configuration be added?
4. What health-safety disclaimer, escalation policy, and review process should
   govern future user-facing content?

## Imported Claude Cowork project instructions
