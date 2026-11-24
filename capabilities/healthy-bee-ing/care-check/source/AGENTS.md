# glee-fully-gpt06a-care-check

## Canonical guidance

This file is the canonical agent guide for this repository. `CLAUDE.md` contains
only `@AGENTS.md`, so Claude-specific work follows this guide too.

## Project identity and status

- Confirmed: this is the Git repository `OKHP3/glee-fully-gpt06a-care-check`.
- Confirmed: it is a single-project, documentation and agent-resource repository.
  No nested repository or separate application package was found.
- Confirmed: the project is identified as Glee-fully, Branch 06, 06a Care Check.
- Confirmed: the repository is licensed under MIT.
- Current status: implementation and deployment status for Care Check are unknown
  from this repository. Do not describe it as live, production-ready, or tested.
- GitHub: https://github.com/OKHP3/glee-fully-gpt06a-care-check
- Notion anchor recorded by the repository: https://app.notion.com/p/d5ec46203c30484fbe62bd869aac0735

## Purpose, mission, and vision

- Confirmed: the existing project description calls 06a Care Check a personal
  health check-in and symptom logging assistant.
- Inferred: its intended primary value is calm symptom logging, triage context,
  and urgency guidance within the wider Glee-fully wellness suite.
- Inferred from the suite pulsebook: the broader vision is a supportive wellness
  branch that reduces confusion around everyday health tasks and routes users to
  a more appropriate sibling tool when needed.
- Unknown: the current Care Check prompt or product behavior, target audience
  beyond the owner, data handling, deployment surface, and acceptance criteria.

## Scope and non-goals

This repository currently contains documentation and checked-in agent skills. It
does not contain an application runtime, source implementation, package
manifest, test suite, CI workflow, or deployment configuration.

Do not infer a medical diagnosis, clinical guarantee, production deployment, or
privacy property from the project name or the sibling pulsebook. Health-related
content must use appropriate safety boundaries and must not present the tool as
a substitute for professional medical care.

## Repository layout

- `README.md`: public orientation, current status, repository map, and
  boundaries. It is not an implementation guide.
- `docs/healthy-bee-ing-pulsebook-2025-09-01.md`: suite-level and sibling
  branch history. It lists Care Check as a sibling responsible for symptom
  triage and urgency guidance, but it is not a Care Check-specific
  implementation specification. Its referenced `dataLedger_*` files are not in
  this repository.
- `.agents/skills/`: checked-in agent skill resources, including skill
  instructions, references, assets, and some Python utilities. Read a skill's
  `SKILL.md` before using or changing that skill.
- `AGENTS.md`: this canonical guide.
- `CLAUDE.md`: pointer to this guide.
- `LICENSE`: MIT license.
- `.gitattributes`: automatic text detection and LF normalization.

No executable entry point or application data flow is currently documented.

## Technology and operating model

- Confirmed repository formats: Markdown, plain text, JSON, HTML, and Python
  files inside the checked-in skill resources.
- Confirmed repository tooling: Git. No project dependency manager or runtime
  setup is present.
- The `.agents/skills` resources are supporting agent capabilities, not evidence
  of a Care Check application runtime. Do not add project dependencies without
  an explicit implementation request.
- The GitHub remote is the only deployment-related configuration found. No CI,
  hosting, release, or external integration configuration is present.

The pulsebook documents a conceptual suite flow: accept a health-related prompt,
route it to an appropriate wellness twig, provide calm guidance, and defer to a
Toolbox when the request is ambiguous or outside scope. Treat this as historical
or inferred suite context, not as a verified Care Check workflow.

## Validation

The repository defines no build, test, lint, or deployment command. For
documentation-only changes, use:

```sh
git status --short --branch
git diff --check
git diff -- AGENTS.md CLAUDE.md README.md
```

Re-read every changed guidance file before finishing. If application code or a
runtime is added later, document its verified setup and validation commands here.

## Change conventions

- Preserve standalone punchy lines in generated content.
- Do not use em dashes in new generated content.
- Keep explanations proportional to the evidence and the task. The ROY
  principle is: understanding produced, explanation invested.
- Label facts as confirmed, inferences as inferred, and unresolved items as
  unknown when the distinction matters.
- Preserve historical documents unless the user explicitly asks for a content
  revision. Do not silently convert sibling or suite material into Care Check
  requirements.
- Do not add secrets, credentials, private personal information, or machine-only
  paths to this guide.
- Do not use destructive version-control commands. Preserve unrelated user
  changes.

## Safe change procedure

1. Check the working tree before editing.
2. Inspect the relevant Markdown, skill instructions, and repository history.
3. Make the smallest change that satisfies the request. Keep guidance changes in
   guidance files unless implementation work is explicitly requested.
4. Run `git diff --check` and any newly documented validation command.
5. Re-read changed files and report what is confirmed, inferred, and still
   unknown.

## Known gaps and risks

- `README.md` does not explain the project purpose, usage, or current status.
- There is no Care Check-specific prompt, implementation, data model, test
  fixture, safety review, or deployment record in this repository.
- The pulsebook is named for the broader Healthy Bee-ing branch and contains
  placeholders, including health disclaimer and data-ledger follow-ups.
- The repository does not establish a branch naming policy or release process.

Do not resolve these gaps by inventing product behavior. Ask the owner or use a
new authoritative project artifact when those details become necessary.

## Keeping this guide current

Update this file when the project gains an implementation, runtime, validation
workflow, deployment surface, or confirmed product status. Keep the evidence
labels accurate, remove stale TODOs, and retain short pointers instead of
duplicating long guidance in `CLAUDE.md` or other instruction files.

## Imported Claude Cowork project instructions
