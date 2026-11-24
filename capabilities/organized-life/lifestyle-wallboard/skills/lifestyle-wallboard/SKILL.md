---
name: lifestyle-wallboard
description: "Summarize household tasks, habits, bills and goals in a weekly or monthly status board. Use for cross-category progress and exceptions."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Lifestyle Wallboard

## Inputs

Request the review date or period, source lists, status definitions and any targets. Use the latest supplied update for each identifiable item and flag conflicting entries.

## Workflow

1. Group records into tasks, bills, goals and habits. Cross-reference duplicates such as one bill and its reminder. Keep counts and money in separate measures. Distinguish an unreported category from a category with a verified zero.
2. Compute completion fractions with the denominator shown. Report a current habit streak only across consecutive expected, observed occurrences. A missing observation makes continuity unknown. For goals, show actual against target and the period.
3. Surface the most time-sensitive exceptions, then choose a small next-action list from the supplied data. Use words for status even in a color-coded layout. For a shared version, remove private notes and individual financial details as requested.

## Output

Return an as-of date, category summaries, exceptions and next actions. For example, two of four tasks done shows 2/4, or 50%, while a missing bill list shows 'no data supplied'.

## Limits

A supplied snapshot supports a printable view. Live refresh, prior-period trends and notifications require actual observations or connected services.

## Source

The catalog describes Lifestyle Wallboard in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/organized-life/lifestyle-wallboard/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
