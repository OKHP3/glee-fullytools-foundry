---
name: palatably-profiled
description: "Summarize taste patterns from attributed meal ratings and compare household preferences by ingredient, cuisine, mood or season."
license: MIT
metadata:
  version: "0.2.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Palatably Profiled

## Turn tastings into a profile

Produce a snapshot from the actual taste observations. Accept notes, a pasted rating table, or the prior sheet with a correction. Keep each observation keyed to person, dish and occasion. Record explicit restrictions separately so a highly rated ingredient can still be excluded from recommendations.

1. Record the original score, its scale, the person’s own words, and any known date, season or mood. Tag only supported attributes. A texture comment, a missing value and a numeric zero mean different things. Keep an unrated comment in the table and out of numeric counts.
2. Summarize supported ingredients, flavors or cuisines per person. Use counts alongside scores. Average only comparable scales or show a declared conversion alongside the raw ratings. A single high score supports a tentative observation. It does not establish a general preference.
3. To compare diners, use dishes both rated. If they tasted the same dish repeatedly, summarize the relevant period per person first and count that dish once in the overlap. Keep other dishes visible as unpaired. Show one agreement and difference when the evidence supports them. Name any “taste twin” resemblance only on the observed overlap.
4. To examine a trend, compare dated ratings within the same person using comparable tags, scales and periods. Report the observation count for each period. If no meaningful comparison is possible, show the missing evidence. Return a candidate tasting that respects exclusions, and explain which result would strengthen or challenge the hypothesis.
5. When someone corrects a score, update the specified observation and recalculate the affected profile. When they report a new tasting, append it. Return the revised snapshot and relevant evidence rows. If they want to turn a preference into a recipe, give **Flavor Meister** a copyable brief of confirmed preferences, exclusions and remaining questions. Use a launch URL only when furnished by the host's current directory.

Use `references/taste-profile.md` for a fillable observation sheet and household comparison. Supply a text table for a requested visual when a chart is unavailable. Keep the snapshot usable by someone who has only the exported table.

## Original guide

Palatably Profiled is entry #03e in `governance/operators-cathedral-layout.md` and `inventory/inventory-of-toolbox-tools-and-tool-ettes.md`. The migrated guide is `Operator’s Cathedral Layout 📐.md`. Use it to answer questions about the original design.
