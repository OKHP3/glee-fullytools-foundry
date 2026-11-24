# glee-fully-gpt07g-self-fixer

## Project identity

- **Suite:** Glee-fully, Branch 07.
- **Recorded type:** GPT Tool-ette.
- **Repository:** `https://github.com/OKHP3/glee-fully-gpt07g-self-fixer`.
- **Recorded Notion anchor:** `https://app.notion.com/p/78f02efd129c414b8e3d1ddf9b3bab73`.
- **Current repository status:** Pre-implementation scaffold, re-confirmed by the 2026-07-24 audit. There is no application source, manifest, runtime configuration, test suite, build configuration, or deployment configuration in this repository.
- **License:** MIT, as recorded in [LICENSE](LICENSE).

## Purpose, users, and product intent

- **Recorded purpose:** 07g is intended to provide DIY repair guidance and troubleshooting assistance.
- **Primary users:** DIY users seeking repair or troubleshooting guidance. This is an inference from the recorded purpose, not a capability verified in code.
- **Mission:** Not stated in the repository.
- **Vision:** Not stated in the repository.
- Do not describe the product as implemented, deployed, production-ready, or safety-validated until repository evidence supports that claim.

## Lifecycle and recent activity

- **Lifecycle stage:** Pre-implementation and currently paused, inferred from the absence of application code and the recent history.
- **Recent activity:** The latest commit is dated 2026-07-13 and updates agent guidance. Earlier commits seeded the agent skills and created the repository documentation. No product implementation activity is recorded.
- **Next evidence needed:** An owner or product decision must define the intended implementation, supported repair domains, safety boundaries, and delivery workflow before this guide can describe a runnable product.

## Scope and boundaries

This repository currently holds project context and agent-facing skills. The contents of `.agents/skills/` are not evidence of a user-facing application runtime.

Do not infer a technology stack, interface, data flow, external integration, deployment model, or supported repair domain that is not documented by project files or verified by executable checks. Treat the Notion anchor and related repository below as reference links, not as local dependencies.

Related repository: [glee-fully-gpt07-identity-known](https://github.com/OKHP3/glee-fully-gpt07-identity-known).

## Repository layout

- `AGENTS.md`: canonical guidance for agents working in this repository.
- `CLAUDE.md`: short pointer to `AGENTS.md`.
- `README.md`: currently only the repository title; expand it when product behavior becomes available.
- `LICENSE`: MIT license.
- `.gitattributes`: enables automatic text detection and LF normalization.
- `.agents/skills/`: seeded agent skills and their supporting assets, references, scripts, and Claude command entry points.

Architecture snapshot: there is no runtime architecture yet. The repository is organized as agent-facing tooling: Notion capture and routing guidance, skill cataloging guidance with a generator script, and skill creation and evaluation guidance with helper scripts and supporting assets. These files are not evidence of a user-facing repair assistant.

There is one Git repository at the project root and no nested repository was found.

## Technology and commands

- **Languages, frameworks, dependencies, and runtime:** Unknown. No manifest or source files are present.
- **Entry points:** None identified.
- **Development, test, lint, build, and deployment commands:** None documented or verified.
- The only verified repository checks at alignment time were `git status --short --branch`, `git ls-files`, and inspection of the root tree and recent history. Do not add commands to this guide until they are confirmed in the repository.

The recent history is documentation and agent-skill seeding only. The current branch is `main`, tracking `origin/main`; no repository-specific branch or naming convention is documented.

## Safe change conventions

- Preserve existing user changes and avoid destructive version-control operations.
- Keep `AGENTS.md` as the single canonical project guide. Keep `CLAUDE.md` as a pointer unless Claude-specific instructions are genuinely needed.
- Make claims traceable to repository evidence. Label important conclusions as confirmed, inferred, or unknown when the distinction matters.
- Keep documentation current when implementation files, commands, integrations, or deployment behavior are added.
- For repair guidance content, include appropriate safety boundaries and escalation guidance once the product scope is defined. Do not invent technical safety claims now.

## Brand and content rules

- Do not use em dashes in generated content.
- Preserve standalone punchy lines. Do not consolidate them into paragraphs.
- Follow the ROY principle: understanding produced, explanation invested. Verbosity must earn its space.
- AutoCAD version is R10. Treat this as locked when AutoCAD content is introduced.
- No additional repository-specific coding or content constraints are currently evidenced.

## Known gaps and open questions

The following require owner or product documentation input:

- What implementation is intended, and which language, framework, model, or platform will host it?
- What are the supported repair domains, safety policy, user experience, and escalation rules?
- What are the development, validation, release, and deployment workflows?
- Is the Notion anchor the current product source of truth?
- What is the relationship to `glee-fully-gpt07-identity-known`?
- Does the AutoCAD R10 rule apply to this project specifically, or only to the wider suite?

## Keeping this guide current

Update this file when repository evidence changes, especially when source code, manifests, tests, runtime configuration, integrations, or deployment files are added. Re-check the README, recent history, and validation commands during each substantial context-alignment review. Keep unresolved questions explicit until they are answered by project evidence or the owner.

## Imported Claude Cowork project instructions
