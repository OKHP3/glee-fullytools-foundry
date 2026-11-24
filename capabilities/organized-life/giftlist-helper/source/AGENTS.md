# glee-fully-gpt05c-giftlist-helper

## Project identity

- Suite: Glee-fully Personalizable Tools
- Tool-ette: Giftlist Helper, identified by the authored prompt as 05c
- Repository: https://github.com/OKHP3/glee-fully-gpt05c-giftlist-helper
- Project root in this workspace: `/Volumes/OKH-Local/04_GitHub_Mirrors/glee-fully-gpt05c-giftlist-helper`
- License: MIT
- Repository state: a small, documentation-and-bundle repository on `main`, tracking `origin/main`
- Product status: the prompt declares `PME_READY`; no runtime, deployment, or production evidence is present in this repository

## Purpose and users

Confirmed from `giftlist-helper-final.md`: Giftlist Helper is a cozy GPT Tool-ette for tracking, stashing, planning, and celebrating gifts for birthdays, holidays, surprises, and just-because occasions.

Primary users are people who want to manage gift ideas and gift status by person or occasion. The prompt supports wishlist capture, quick idea capture, gift timelines, status tracking, tagging, hiding-location notes, gift history lookup, reminders, and reusable CSV or Markdown formats.

Mission, inferred from the authored behavior: reduce gifting memory load and last-minute chaos by keeping ideas, purchases, wrapping, hiding places, occasions, and feedback organized in one conversational workflow.

Vision, inferred and not independently documented: make gifting feel personal and manageable while preserving surprise and delight.

## Scope and boundaries

In scope:

- Maintain conversational gift lists and wishlists.
- Capture ideas with names, notes, links, prices, people, occasions, sources, and tags.
- Track bought, wrapped, hidden, and given states.
- Record hiding locations and optionally coordinate with Present Hoarder, Tool-ette 02c.
- Summarize gift history and suggest reminders or gift ideas.
- Accept or produce lightweight CSV and Markdown formats described by the prompt.

Out of scope in this repository:

- Application code, APIs, databases, calendar adapters, notification services, or user data storage.
- A verified GPT deployment configuration or executable local service.
- Claims that the described calendar export, Present Hoarder sync, uploads, or reminders are implemented. They appear only as prompt behavior or format guidance.

## Repository structure and entry points

- `giftlist-helper-final.md`: canonical authored system prompt and behavior specification. Treat this as the primary product artifact.
- `knowledgebundle/giftlisthelper_builderbundle.zip`: distributable bundle containing a copy of the prompt and one PNG brand asset.
- `knowledgebundle/giftlisthelper_canonicaldataledgerbundle.zip`: canonical ledger bundle with narrative, parameters, processing, archive, system, registry, and persona files.
- `README.md`: public orientation, status, artifact map, and scope boundary.
- `LICENSE`: MIT license.
- `.agents/skills/`: seeded local agent skills and their supporting files. These are repository tooling assets, not the Giftlist Helper runtime.
- `CLAUDE.md`: Claude guidance pointer to this file. Keep it short and consistent with `AGENTS.md`.

There are no nested project roots or nested instruction files under this repository. The ZIP archives are artifacts to inspect, not source trees to edit in place.

## Technology and runtime

The tracked product artifacts are UTF-8 Markdown, plain text ledger files, a PNG, and ZIP archives. No language runtime, framework, package manifest, build system, test suite, deployment configuration, or service entry point was found.

The practical entry point is the prompt in `giftlist-helper-final.md`, or its copy inside the builder bundle. Ledger files provide scaffolding and metadata. External integrations named by the prompt are descriptive only unless a future repository change adds an implementation and validation evidence.

## Development and validation

No build, lint, or test command is currently defined. Do not invent one.

For documentation or bundle changes, use these checks as applicable:

```text
git status --short --branch
unzip -t knowledgebundle/giftlisthelper_builderbundle.zip
unzip -t knowledgebundle/giftlisthelper_canonicaldataledgerbundle.zip
diff -u giftlist-helper-final.md <(unzip -p knowledgebundle/giftlisthelper_builderbundle.zip 'Giftlist Helper Final.md')
```

The ZIP integrity checks currently pass. The root prompt and the bundled prompt currently match byte-for-byte. If an artifact is intentionally changed, explain whether the duplicate copy, the ZIP contents, or both were updated.

## Change conventions

- Keep changes limited to the requested guidance, prompt, ledger, or bundle artifact.
- Preserve existing user changes and do not use destructive version-control commands.
- Treat `giftlist-helper-final.md` as authored product content. Preserve its standalone punchy lines, emojis, and conversational voice unless the request explicitly changes them.
- Keep the root prompt and the builder-bundle copy synchronized when both are intended to represent the current prompt.
- Do not edit files inside ZIP archives without a clear request. Rebuild or replace an archive only when the requested change requires it, then run `unzip -t`.
- Do not add secrets, credentials, private personal information, generated runtime code, or unsupported production claims.
- No em dashes in generated content.
- ROY principle: understanding produced, explanation invested. Verbosity must earn its space.
- AutoCAD version is R10 when AutoCAD context is relevant.

## Guidance file precedence

`AGENTS.md` is the canonical repository guide. `CLAUDE.md` contains a short project summary and imports `AGENTS.md`; no separate Claude-specific rules are defined. If a future nested instruction file is added, apply the most specific applicable file and reconcile contradictions with this guide.

## Known gaps and open questions

Urgent before implementation or deployment:

- Confirm whether Giftlist Helper belongs to branch 05c under Organized Life or the `02_Glee-fully_Treasured_Finds` grouping. The authored prompt says 05c; the removed 2025 cross-suite scaffold had placed a thread seed under 02.
- Confirm the intended GPT platform, deployment process, persistence model, calendar integration, and Present Hoarder integration. None is represented by executable or configuration files here.

Optional documentation improvements:

- Expand `README.md` with artifact purpose, usage, and validation notes.
- Document the provenance and intended consumer of each canonical ledger file.
- The ZIP member timestamps remain 2025-07-13; refresh them only when the bundles are intentionally repackaged.
- The former cross-suite `dataLedger_ideation_v2.txt` scaffold was removed from this repository and both bundles as stale work-in-progress. Its prior bytes remain recoverable through Git history.

## Keeping this guide current

Update this file when the project gains a runtime, deployment path, new integration, authoritative product identity, or verified validation command. Base claims on repository evidence and label unresolved owner decisions as open questions. Re-read this file and any changed guidance file after each update.

---
*Reviewed 2026-08-05 from repository contents, Git history, and ZIP integrity checks.*

## Imported Claude Cowork project instructions
