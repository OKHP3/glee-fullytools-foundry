# glee-fully-gpt04d-dreamland-journeys

## Project identity

- Suite: Glee-fully, Branch 04.
- Product name: Dreamland Journeys.
- Repository type: content-first GPT Tool-ette and prompt/reference pack.
- Git repository: standalone repository on `main`, tracking `origin/main`.
- Current implementation status: content scaffold. No executable application, package manifest, runtime configuration, or deployment configuration is present in the repository. Owner-confirmed release status is unknown.
- Related product named by the source documentation: Glee-fully Traveler's Guide. Its repository location is not established in this checkout.

## Purpose, mission, and vision

The purpose below is supported by `prompts/dreamland_journeys_instructions.md` and `docs/dreamland_journeys_toolette_summary.md`.

- Confirmed purpose: capture aspirational travel ideas, moods, themes, notes, budgets, seasons, and planning status.
- Inferred mission: help a user turn an emotional or aesthetic travel wish into a structured dream-trip entry that can be grouped and developed over time.
- Inferred vision: provide a voice-, image-, and context-aware travelboard experience that connects imaginative travel ideation with practical early planning.

These are ideation and planning aids. Nothing in the repository establishes live booking, current availability, authoritative pricing, itinerary execution, or external data access.

## Scope and boundaries

In scope:

- Dream destination and wishboard entry capture.
- Mood, motif, and theme organization.
- Reverse-dream prompts for discovering destinations from feelings or imagery.
- Early budget, timing, milestone, and status fields.
- Product voice and overlay guidance for the GPT Tool-ette.

Not established by repository evidence:

- A web, mobile, or desktop user interface.
- A persistence layer, database, API, or external integration.
- Booking, routing, map, weather, visa, or live travel research.
- A production deployment target or release process.

## Repository map

- `prompts/dreamland_journeys_instructions.md`: system/persona and tone instructions for the Tool-ette. It includes the GLEE-LITE default and BLEED GLEE MODE overlay.
- `prompts/reversedreampromptbank.md`: reverse-dream prompt starters.
- `specifications/dreamland_journeys_pme.yaml`: declared functions, triggers, and descriptions for wishboard creation, theme grouping, and budget/timing estimation.
- `docs/dreamland_journeys_toolette_summary.md`: short product summary and named cross-links.
- `references/dreammood_tags.csv`: small seed table mapping moods to example destinations and seasons.
- `references/wishboard_moodboards.md`: seed moodboard themes.
- `templates/status_snapshot_template.md`: example structure for a dream-trip status entry.
- `README.md`: public orientation, repository map, status, and boundaries.
- `.agents/skills/`: repository-local agent skills and supporting assets. These are guidance/tooling resources, not the product runtime.
- `CLAUDE.md`: pointer to this file for Claude-specific work.

No nested Git repositories or independent application projects were found.

## Technology and data flow

Confirmed file formats are Markdown, YAML, CSV, plain text, and Git metadata. No language runtime, framework, dependency manager, build tool, test runner, or deployment tool is configured.

The conceptual workflow, inferred from the files, is:

1. User expresses a destination wish, mood, motif, or sensory prompt.
2. The Tool-ette suggests or organizes destinations and themes.
3. The wish is recorded with notes, season, budget, timing, milestones, and status.
4. The user develops the entry toward a future trip, with realization and itinerary work named as downstream products rather than implemented integrations here.

The PME YAML describes intended capabilities, not verified callable behavior in this repository.

## Working conventions

- Preserve the product's playful, emotionally attentive voice when editing prompt content, while keeping instructions clear and usable.
- Preserve standalone punchy lines when they carry meaning. Do not merge them into paragraphs solely for compactness.
- Do not use em dashes in agent-authored or newly generated project content. Prefer sentence breaks, commas, or hyphens.
- Keep factual travel guidance separate from imaginative suggestions. If live or safety-sensitive information is ever added, identify its source and freshness requirements.
- Preserve the existing lowercase filename style and the current lightweight Markdown/YAML/CSV organization unless a broader schema change is requested.
- When changing a capability, update the relevant instruction, PME declaration, summary, and reference data together when applicable. Do not claim a live capability that has no implementation or integration evidence.
- Preserve existing user changes. Do not use destructive version-control commands.

## Validation

No automated tests, lint configuration, build command, or local application start command were found.

For content-only changes:

- Re-read every changed guidance or prompt file.
- Confirm referenced paths exist.
- Parse YAML and CSV when those files change.
- Review Markdown for clear headings, intact standalone lines, and consistency with the product voice.
- Use `git diff --check` and `git status --short` before handoff.

No deployment or publishing workflow is verified. Do not invent one. The GitHub remote documents source control only.

## Known gaps and open questions

- The runtime host, GPT configuration surface, persistence model, and deployment target are unknown.
- The product status is not owner-confirmed beyond the repository being a content scaffold.
- `README.md` does not explain usage, validation, or contribution workflow.
- The `...` marker in `prompts/dreamland_journeys_instructions.md` may be an intentional truncation or unfinished content; preserve it unless the owner requests prompt completion.
- The exact contract between this Tool-ette and the related Traveler's Guide repository is not documented here.

## Keeping this guide current

Update this file when the repository gains a runtime, integration, deployment path, test command, durable data schema, or a confirmed product-status decision. Keep claims evidence-based and label important inferences or unresolved owner decisions rather than turning them into facts.

## Imported Claude Cowork project instructions
