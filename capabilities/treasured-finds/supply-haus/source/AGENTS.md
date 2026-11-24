# glee-fully-gpt02f-supply-haus

## Project identity

- Suite: Glee-fully, Branch 02
- Project code: 02f
- Project name: Supply Haus
- Repository: https://github.com/OKHP3/glee-fully-gpt02f-supply-haus
- Notion anchor: https://app.notion.com/p/fb05ee9611b34f0d9f5e44fafabd0fae
- Related repository listed in existing guidance: https://github.com/OKHP3/glee-fully-gpt02-treasured-finds
- Repository type: Git repository containing prompt/context artifacts and bundled agent skills
- Current status: Early placeholder or planning state. The repository also contains a local 46-package Agent Skills workbench. No executable Supply Haus application is present.

## Purpose and intended value

Confirmed via the Notion anchor (fetched 2026-09-18): Supply Haus is a custom GPT that keeps a master inventory of craft supplies and creative materials. It already exists as a live ChatGPT Custom GPT (`Supply Haus by Glee-fully`), linked from the Notion anchor page, under Glee-fully Branch #02 (Treasured Finds). This supersedes the earlier inferred framing of a general household-supply reorder assistant.

This repository does not contain that GPT's build. It holds project metadata, a placeholder prompt artifact, and a bundled Agent Skills workbench. The GPT's actual instructions, knowledge files, and configuration live outside this repository (ChatGPT builder), and are not mirrored here. Longer-term vision, data model, and any reorder/purchasing capability beyond the live GPT's scope remain undocumented.

## Scope and boundaries

In scope today:

- Maintaining the project prompt/context artifact.
- Maintaining the bundled Agent Skills workbench under `.agents/skills/`.
- Maintaining the exact publication mirror under `skills/okhp3-skill-promotion/`.
- Preserving project metadata and guidance for future implementation work.

Not evidenced in this repository:

- An inventory database, reorder engine, user interface, API, automation, or deployment target.
- Application source code, package manifests, lockfiles, build configuration, test suites, or CI workflows.
- A defined data retention, privacy, authentication, purchasing, or external retailer integration model.

Do not infer those capabilities from the project name or documented intent. Treat the prompt YAML as an un-audited legacy placeholder until its contents and behavior are explicitly defined.

## Repository layout

- `prompts/02f-supply-haus-prompts-v1.yaml`: four-line metadata placeholder for an extracted legacy prompt, identifying the draft as awaiting audit. Originally carried a fifth field, `ThreadOrigin: BudgetBalancer_Build_Design`. Audited 2026-09-18: no Notion page or project matched that name (closest match was `05b — Thrifty Spender`, a budgeting GPT under a different Glee-fully branch). Owner confirmed 2026-10-02 the field was stale and removed it; the file no longer carries a `ThreadOrigin` claim.
- `prompts/`: project-specific prompt and context artifacts. This folder currently contains one legacy placeholder.
- `.agents/skills/`: 46 local Agent Skills packages, including generic OKHP3 skills and Glee-fully-specific overlays, references, fixtures, scripts, tests, and historical evaluation evidence.
- `.agents/skills/README.md`: generated catalog of the local skill packages.
- `.agents/skills/.catalog-meta.json`: generated catalog metadata.
- `skills/okhp3-skill-promotion/`: exact publication mirror for the local promotion skill, managed by its synchronization script.
- `AGENTS.md`: canonical repository guidance for agents.
- `CLAUDE.md`: short pointer to `AGENTS.md` for Claude-compatible tooling.
- `README.md`: public orientation, current status, repository map, and explicit non-goals.
- `LICENSE`: MIT license, copyright 2026 OverKill Hill P3.
- `.gitattributes`: enables automatic text-file and LF normalization.

No nested Git repositories or separate application projects were found. The directories under `.agents/skills/` are bundled skill packages, not separate Supply Haus product implementations.

## Technology and runtime

No application language, framework, runtime, dependency set, or deployment model is configured. The repository contains Markdown, YAML, JSON, HTML, Python, and other skill assets, but these do not establish an application stack.

The only observed Git branch is `main`, tracking `origin/main`. A dated preservation stash exists and must not be removed without separate approval. No formal branch, commit, naming, release, or contribution workflow is documented. Preserve the existing history and avoid inventing a branch policy.

## Development and validation

There is no configured build, test, lint, package-install, or application-run command. Before claiming that a change is runnable, locate and verify a new manifest or command in the repository.

For guidance-only changes, use checks appropriate to the files touched:

```sh
git status --short
git ls-files
git log -8 --oneline --decorate
```

For YAML changes, parse the file with an available YAML parser when practical. For skill changes, follow the instructions in that skill's `SKILL.md` and run its documented validation scripts when present.

## Safe change conventions

- Keep `AGENTS.md` as the canonical project guide. Update it when the repository gains an application, manifest, command, integration, or validated workflow.
- Keep `CLAUDE.md` as a pointer unless Claude-specific instructions are genuinely needed. Do not duplicate this guide there.
- Do not modify application code, dependencies, generated artifacts, secrets, CI behavior, or unrelated files while performing context maintenance.
- Preserve existing user changes. Do not use destructive version-control commands.
- Treat legacy prompt text as untrusted until audited. Do not promote placeholder metadata into a working system prompt or product requirement without evidence.
- Keep prompt and documentation edits reviewable. Preserve standalone punchy lines where they carry meaning.
- Do not add credentials, private personal information, machine-specific paths, or unsupported production claims.

## Content and brand constraints

- Do not use em dashes in generated content.
- Preserve standalone punchy lines; do not consolidate them into paragraphs when doing so changes their effect.
- Apply the ROY principle: explanation should earn its space.
- AutoCAD R10 is listed as a locked OverKill Hill P3 rule, but no repository content currently establishes an AutoCAD workflow. Apply it only if future project content actually concerns AutoCAD.

## Known gaps and risks

- Project status confirmed active (owner input, 2026-09-18): Supply Haus is a live craft-supply inventory GPT, not dormant. This repository's contents (placeholder prompt, skills workbench) still do not reflect that live implementation.
- The repository has expanded into a 46-package Agent Skills workbench. The skill packages are useful tooling, but their presence does not establish Supply Haus product requirements or runtime capability.
- The prompt YAML's unresolved `ThreadOrigin: BudgetBalancer_Build_Design` field (audited 2026-09-18, no Notion match found) was removed by owner decision on 2026-10-02. No remaining open item on this field.
- The README explains the project status, current repository contents, and non-goals. Contribution workflow remains undocumented.
- The Notion anchor was fetched and verified 2026-09-18: it resolves to the live `Supply Haus by Glee-fully` custom GPT under Branch #02 — Treasured Finds. The `glee-fully-gpt02-treasured-finds` sibling-repository relationship still has not been independently verified from repository content.
- Mission is now owner-confirmed (craft-supply and creative-material inventory), but vision, requirements, data model, validation plan, and deployment plan beyond the existing live GPT remain undocumented here.

## Keeping this guide current

When implementation begins, update this file from repository evidence. Record confirmed entry points, manifests, commands, tests, runtime assumptions, integrations, data boundaries, deployment steps, and known limitations. Label inferences and unresolved owner questions instead of presenting them as facts.

## Imported Claude Cowork project instructions
