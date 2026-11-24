# glee-fully-gpt01-discovered-careers

## Project identity and scope

- Suite: Glee-fully Personalizable Tools
- Branch: 01, Discovered Careers
- Repository: https://github.com/OKHP3/glee-fully-gpt01-discovered-careers
- Notion anchor recorded by the project: https://app.notion.com/p/aa83b49f2ac84274924eb97b8cdbb1b5
- Project type: single Git repository containing prompt and product-design documentation
- Repository status: early-stage draft. No executable application is present in this checkout.

## Current lifecycle and activity

- Repository lifecycle: documentation-stage prototype under active documentation maintenance.
- Product/runtime lifecycle: TBD. The repository provides no executable implementation or deployment evidence.
- Recent repository activity through 2026-07-13 consists of guidance, Claude pointer, and seeded-skill updates. This supports active documentation maintenance, not a claim that the GPT is currently deployed.

This guide is the canonical agent guidance for the repository root. `CLAUDE.md` delegates to this file.

## Purpose, mission, and vision

Confirmed by the pulsebook and supporting design files:

- The project defines a career-navigation branch for the Glee-fully suite.
- The intended branch behavior is to understand a user's career task and route them to a more specialized sibling Tool-ette.
- The documented Tool-ettes cover resume building, resume customization, career fitness, letter composition, LinkedIn optimization, and job-search tracking.

Reasonable inference:

- The user value is reducing the fragmentation and stress of a job search by giving users a clear next tool and an encouraging experience.

Planned vision, not current capability:

- The pulsebook describes a broader career companion with personalized coaching, job matching, learning recommendations, external job-board integrations, and wider accessibility. None of these capabilities is implemented or verified here.

## Scope boundaries

In scope:

- Prompt, persona, routing, lifecycle, and product-design documentation for Discovered Careers.
- Markdown and YAML design artifacts, their terminology, and their internal consistency.
- The seeded local agent skills under `.agents/skills/` when a task explicitly concerns those skills.

Out of scope for this repository as it currently exists:

- A web, mobile, desktop, or API application.
- Resume generation, LinkedIn editing, job-board search, application storage, or external service integrations.
- Claims that the GPT is live, deployed, production-ready, or connected to sibling repositories. The pulsebook contains those claims as design history, but the checkout does not verify them.

## Repository map

- `README.md`: minimal repository landing page.
- `docs/discovered-careers-pulsebook.md`: large product and prompt-design record. It contains identity, intended behavior, Tool-ette routing, future plans, governance notes, and historical metadata.
- `LICENSE`: MIT license.
- `.agents/prompts/`: reusable project-context and migration prompts.
- `.agents/skills/`: tracked local skills for skill discovery, Notion capture routing, skill cataloging, and skill creation.
- `skills/okhp3-skill-promotion/`: publication mirror for the project-local skill-promotion package, as defined by that skill's three-surface model.
- `CLAUDE.md`: short delegation file that points to this guide.

No nested Git repository or independent application project was found.

## Technology and runtime

- Confirmed formats: Markdown and YAML, plus plain-text Git metadata.
- No package manifest, dependency lockfile, source directory, build system, test runner, container configuration, deployment configuration, or runtime entry point was found.
- The documented career routing is conceptual. It is not implemented as code or an executable workflow in this repository.

## Working conventions

- Base factual statements on repository evidence. Label planned behavior and historical pulsebook claims as planned or historical.
- Preserve standalone punchy lines when editing product copy. Do not silently consolidate them into paragraphs.
- Do not use em dashes in generated content.
- Keep Glee-fully tone guidance distinct from technical guarantees. `GleeTone.A1`, `JoyWarden.Core`, BLEED GLEE MODE, lifecycle tags, and PME identifiers are draft product conventions, not verified runtime services.
- Do not add secrets, private credentials, or unverified deployment details.
- Preserve unrelated user changes. Do not use destructive version-control commands.
- AutoCAD R10 is an inherited brand rule only when AutoCAD content is in scope. No AutoCAD content is currently present in this repository.

## Safe change workflow

1. Read this file, `CLAUDE.md`, the relevant design artifact, and any applicable local skill instructions before editing.
2. Keep documentation changes focused on the requested scope. Do not create application code or dependencies unless the project is intentionally expanded.
3. When changing routing or terminology, check the pulsebook and any supporting design artifacts for contradictions.
4. Preserve historical material, but mark it clearly when it describes future plans, prior releases, or unverified deployment state.
5. Re-read every changed guidance file and inspect the diff before handing off.

## Validation

There are no repository-defined build, test, lint, or deployment commands at present. For documentation-only changes, use:

- `git status --short --branch`
- `git diff --check`
- `rg --files -g '!node_modules' -g '!vendor' -g '!dist' -g '!build'`

Validation cannot establish product behavior because no executable implementation exists.

## Known gaps and open questions

Important risks:

- The pulsebook describes a 2025 deployment and many future integrations, but the current repository contains no implementation or deployment evidence.
- The pulsebook repeats sections and includes extensive future-state material. Treat it as a design record until it is reconciled.

Owner input is still needed to determine the intended current status of the GPT itself, the authoritative ledger location, whether sibling repositories are active dependencies, and whether the Notion anchor remains current.

## Keeping this guide current

Update this file when the repository gains an executable runtime, new validation commands, a deployment path, authoritative ledgers, new repository boundaries, or a confirmed change in product status. Keep confirmed facts, inferences, historical claims, and unknowns visibly distinct.

## Related repositories

- https://github.com/OKHP3/glee-fully-gpt01a-resume-builder
- https://github.com/OKHP3/glee-fully-gpt01b-resume-customizer
- https://github.com/OKHP3/glee-fully-gpt01c-career-fitness
- https://github.com/OKHP3/glee-fully-gpt01d-letter-composer
- https://github.com/OKHP3/glee-fully-gpt01e-blinkin-tuner
- https://github.com/OKHP3/glee-fully-gpt01f-career-seeker

## Imported Claude Cowork project instructions
