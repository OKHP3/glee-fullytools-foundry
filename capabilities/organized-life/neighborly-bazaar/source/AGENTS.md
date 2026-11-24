# Agent Guide: glee-fully-gpt05f-neighborly-bazaar

## Project identity

- **Suite:** Glee-fully, Branch 05
- **Project:** 05f Neighborly Bazaar
- **Repository type:** Single Git repository containing Custom GPT specifications, knowledge documents, and reusable agent skills. No nested repository was found.
- **Primary purpose:** Documentation and configuration support for a seller-facing local resale assistant. This repository is not an executable marketplace application.
- **Related context:** [GitHub repository](https://github.com/OKHP3/glee-fully-gpt05f-neighborly-bazaar) and [Notion anchor](https://app.notion.com/p/3c7d7432dafb442da75dd63fc030e5d5).

The Pulsebook records a public ChatGPT Custom GPT deployment dated 2025-10-14. That is historical deployment evidence, not proof that the deployment is currently live or healthy.

## Mission, vision, and scope

**Mission, confirmed by the product brief:** Help people in the United States sell pre-loved tangible goods locally by identifying items, estimating fair prices, improving listings, handling negotiation, and reducing scam and meetup risk. The assistant serves sellers only.

**Vision, inferred from the Pulsebook:** A friendly, safety-forward resale copilot that increases local reuse and confidence while reducing hassle and risk.

### In scope

- U.S. local markets and digital marketplaces intended for in-person exchanges.
- Legal, tangible, non-hazardous goods.
- Item identification and condition review from user-provided details or photos.
- Local comparable research and transparent price ranges.
- Listing copy, venue selection, negotiation coaching, safety guidance, garage-sale batch pricing, and user-reported sale reflection.

### Out of scope or restricted

- Buyers, brokers, shippers, payment processors, or marketplace impersonation.
- Services, weapons, animals, recalled goods, pharmaceuticals, counterfeit goods, and other restricted items.
- Legal, tax, or financial advice. Provide educational guidance and recommend qualified professionals when needed.
- Retaining addresses, IDs, or other personally identifying information.

When legality, intent, value, or safety is unclear, ask for clarification. Flag unusually valuable heirlooms or artwork for professional appraisal. Safety topics use the calm Watchkeeper tone and take priority over playful persona styling.

## Core workflow and boundaries

The intended user flow is:

1. Confirm that the user is a seller and establish a general U.S. location.
2. Gather item photos, brand or model, condition, dimensions, defects, and context.
3. Identify the item and assess confidence, category, condition, and risk flags.
4. Research local comparables, normally starting within 25 miles, then explain the price range and assumptions.
5. Produce a platform-appropriate listing kit and recommend a venue.
6. Coach friendly negotiation and safe public hand-off and payment practices.
7. Summarize user-reported outcomes, including value and space reclaimed when the inputs support it.

Do not claim that a price is current, a marketplace rule is unchanged, or a comparable was observed unless the relevant source was actually checked. Treat platform details and legal thresholds in the knowledge corpus as material that may need current verification.

## Repository map

- `specifications/05f-organized-life-neighborly-bazaar.md`: concise operating brief covering role, boundaries, persona, functions, workflow, safety, and output format.
- `specifications/gpt-pulsebook-v1.md`: detailed Pulsebook with deployment metadata, instruction versions, function cards, governance notes, placeholders, and change history.
- `specifications/gpt-pulsebook-v1.docx` and `specifications/gpt-pulsebook-v1.pdf`: companion document exports of the Pulsebook.
- `knowledge/`: 15 numbered DOCX and PDF knowledge pairs covering local comparables, listing craft, negotiation, safety, scams, regional logic, condition, bulk pricing, tax and legal considerations, UX, case studies, corpus integration, behavior, and trust governance.
- `.agents/skills/find-skills/`: guidance for finding or recommending skills.
- `.agents/skills/okhp3-notion-capture-router/`: workflow for routing AI conversations into Notion and reconciling them with GitHub.
- `.agents/skills/okhp3-skill-cataloger/`: skill inventory and catalog generation workflow.
- `.agents/skills/skill-creator/`: instructions and scripts for creating and evaluating agent skills.
- `CLAUDE.md`: pointer to this file, so `AGENTS.md` is the canonical local guide for both agents.
- `README.md`: public orientation and repository map. Keep it concise and factual.
- `LICENSE`: MIT license, copyright 2026 OverKill Hill P³.

The knowledge files are reference material, not executable code. Preserve DOCX and PDF pairs when updating a knowledge article unless the owner explicitly requests a format change. Do not add extracted text, caches, or generated conversions to the repository as part of routine inspection.

## Technology and architecture

No application language, framework, package manager, runtime manifest, service entry point, database, deployment configuration, or test framework is present. No build or application runtime command is currently verified.

The documented product architecture is behavioral rather than implemented here:

`user item details and location` -> `identify and normalize` -> `local comparables and price rationale` -> `listing and venue recommendation` -> `negotiation and safety guidance` -> `user-reported reflection`

The Pulsebook historically lists Web Search, Canvas, Image Generation, and Code Interpreter or Data Analysis as Custom GPT capabilities. These are deployment metadata only. Do not assume they are available in this repository or that they remain enabled without checking the current product configuration.

## Working conventions

- Keep `AGENTS.md` as the canonical repository guide. Keep `CLAUDE.md` as a short pointer unless Claude-specific instructions are genuinely needed.
- Preserve existing user changes and use non-destructive Git operations. The repository currently uses `main`; branch strategy and naming policy are not documented, so do not invent one or change branches without owner direction.
- Make guidance factual and label conclusions as confirmed, inferred, or unknown when the distinction matters.
- Keep the OverKill Hill P3 style rules: no em dashes in generated content, preserve standalone punchy lines, and make verbosity earn its space.
- Keep seller privacy and safety ahead of tone. Never add secrets, credentials, personal addresses, IDs, or PII to documentation, examples, logs, or tests.
- Do not expose hidden chain-of-thought. Give concise, user-facing rationale, source names, assumptions, and uncertainty instead.
- If editing product behavior, reconcile the concise operating brief and Pulsebook, then note which one is authoritative for the change. Do not silently turn Pulsebook placeholders or assumptions into guarantees.

## Validation

Because this is a documentation and configuration repository, validate changes proportionally:

- Re-read every changed Markdown or guidance file.
- Confirm referenced paths with `git ls-files` or filesystem inspection.
- Run `git diff --check` before handing off changes.
- Use `git status --short --branch` to confirm scope and preserve unrelated work.
- For DOCX inspection on macOS, `textutil -convert txt -stdout <file.docx>` is available in the current environment. This is an inspection aid, not a repository build step.

There is no verified test, lint, build, package-install, or deployment command. Do not report one as passing. If a future executable project is added, document its commands here and in the README after verifying them.

## Known gaps and risks

- The repository contains no executable implementation, so behavior described in the briefs cannot be integration-tested here.
- `README.md` is empty and does not explain the project to a new contributor.
- The concise brief describes 15 knowledge articles, two deep research papers, and four system documents, while the Pulsebook describes 12 knowledge articles and two deep research papers. The repository visibly contains 15 numbered knowledge DOCX/PDF pairs, but the claimed system documents are not clearly identified.
- The Pulsebook contains explicit assumptions, placeholders, pending checksum data, and `TBA` sections. Treat those as unresolved rather than current truth.
- The product brief says to keep data transient and avoid PII, but also says to log session metadata. No logging implementation exists. Do not add logging without owner direction, and never log PII.
- Several knowledge documents discuss platforms outside the local U.S. scope or include time-sensitive platform and legal claims. Verify current policy and law before presenting them as current advice.
- Generated local metadata such as `.DS_Store`, Python bytecode, and evaluation workspaces should remain untracked and are excluded by `.gitignore`.

## Keeping this guide current

Update this file when the repository gains an executable implementation, changes its deployment model, adds or removes knowledge sources, or settles one of the open questions above. Record evidence from the relevant files or verified commands. Keep historical deployment details in the Pulsebook, and keep this guide focused on what an agent needs to work safely in the current repository.

## Imported Claude Cowork project instructions
