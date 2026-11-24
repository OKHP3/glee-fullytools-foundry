# glee-fully-gpt03-tasty-tracker

## Project identity and status

- Suite: Glee-fully
- Branch: 03, Tasty Tracker
- Repository: `https://github.com/OKHP3/glee-fully-gpt03-tasty-tracker`
- Project root: this directory
- Current status: early-stage documentation and prompt scaffold

The repository is a planning workspace for a Glee-fully food and cooking capability, delivered as a GPT or custom-instructions product rather than a standalone app or service. It contains no application, service, package manifest, data model, deployment configuration, or executable product entry point, because none of those apply to this product form.

## Purpose, mission, and vision

### Confirmed

The available project evidence identifies food, recipes, meal planning, and culinary tools as the intended subject area.

The product form is a GPT or custom-instructions product: a configured prompt/persona running on an existing LLM platform (such as a Custom GPT or an equivalent instructions-plus-knowledge setup), not a hosted app, API, or service with its own runtime.

The former planning notes described an ideation-to-build-design flow and a possible PME-ready handoff, but those notes were placeholder templates rather than developed product specifications.

### Inferred

Given the GPT product form, the eventual deliverable is most likely a set of custom instructions, a persona/tone definition, and optionally a small knowledge base or file attachments, rather than any executable code.

### Unknown

The primary users, confirmed mission, longer-term vision, canonical source format for the instructions/knowledge base, target GPT platform, validation criteria, and production status are not established by repository evidence.

## Scope and boundaries

In scope today:

- Maintaining this project profile and future owner-supplied product decisions.
- Maintaining the four intentionally retained repository-maintenance skills under `.agents/skills/`.
- Drafting and refining GPT custom instructions, persona/tone definitions, and any supporting knowledge files for the culinary concept, once the owner supplies the missing decisions below.

Not established as in scope:

- A recipe database, meal-planning UI, API, mobile app, shopping workflow, or external service integration.
- Any hosted runtime, scheduled jobs, persistent storage, authentication, or user-data handling — the GPT product form does not require these.
- The former ledger system or any external source of truth not present in this repository.

## Repository map

- `README.md`: current public orientation and project status.
- `AGENTS.md`: canonical local operating guidance and evidence boundaries.
- `.agents/skills/okhp3-repl-repo-janitor/`: single-checkout branch, naming, and detritus audit skill.
- `.agents/skills/okhp3-repository-janitor/`: multi-checkout Git reconciliation and branch-lifecycle guidance.
- `.agents/skills/okhp3-repository-organizer/`: content-first repository profiling and approval-gated organization workflow.
- `.agents/skills/okhp3-skill-foundry/`: portable Agent Skill authoring, evaluation, and release guidance.
- `CLAUDE.md`: short compatibility pointer to this file.
- `LICENSE`: repository license.

The former root planning templates, generic migration prompts, duplicate skill-promotion mirror, unrelated imported skill packages, stale generated catalog, and tracked Python bytecode were removed during repository cleanup. Their prior contents remain recoverable through Git history.

## Development and validation

No application development, test, lint, build, or deployment command is defined or verified, and none is expected under the GPT product form. If the owner instead decides to wrap the instructions in tooling (for example an export script or a GPT-builder skill), add the relevant command here only once it exists.

For documentation-only changes, run from the repository root:

~~~sh
git status --short --branch
git diff --check
~~~

Also re-read every changed guidance file and verify that every path and command mentioned in it exists or is explicitly marked as unknown.

## Working conventions

- Make changes only within this repository and preserve unrelated user edits.
- Use Markdown for project guidance unless the owner establishes another format.
- Keep confirmed facts, inferences, proposals, and unknowns visibly separate.
- Do not claim that a prompt draft, integration, workflow, or product is implemented without direct evidence.
- Use portable lowercase kebab-case for new ordinary paths. Preserve required names such as `README.md`, `AGENTS.md`, `CLAUDE.md`, `LICENSE`, and `.agents/`.
- Do not add credentials, secrets, private personal information, or private Notion URLs.
- Do not use destructive version-control commands or rewrite `main`.

## Owner decisions needed before implementation

- Primary users and culinary problem to solve.
- Target GPT platform and canonical source-of-truth format for instructions and knowledge files.
- Required capabilities and any knowledge-base or file-attachment content.
- Validation and acceptance expectations.

## Keeping this guide current

Update this file when a confirmed product decision, canonical source, instructions draft, or knowledge-base content is added. Verify each update against repository evidence. Keep `CLAUDE.md` as a short pointer unless separate Claude-specific rules are genuinely required.

## Imported Claude Cowork project instructions
