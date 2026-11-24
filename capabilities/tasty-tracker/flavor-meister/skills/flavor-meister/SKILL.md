---
name: flavor-meister
description: "Turn a recipe and tasting notes into a reusable recipe card. Use for personal tweaks, flavor tags, meal ratings, favorite dishes or retrieval by occasion."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Flavor Meister

## Inputs

Accept the dish, ingredients and method as supplied. Capture yield, cook date and taster if known. Distinguish original instructions from what happened on the last cook.

## Workflow

1. Record ingredients with amounts and units. Preserve ambiguous descriptions such as a handful. Number the cooking steps, marking omitted steps or temperatures as unknown.
2. Add cuisine, meal type, season or occasion tags only when supported. Add flavor tags from tasting notes. Attribute each 1–5 star rating to its taster and date. A rating and a favorite flag are separate choices.
3. On a repeat cook, keep the base recipe and append a dated variation with the changed ingredient, method and observed result. For retrieval, match the requested tags against supplied cards and identify the matching notes.

## Output

Return a recipe card plus a short cook log. For example, keep lime in the original dressing and log the cook's lemon substitution as a variation. Include a favorite flag only when the cook designates it.

## Limits

No stored cookbook is assumed. If the recipe is absent, produce a partial card with the supplied notes and ask for the missing method or ingredient list.

## Source

The catalog describes Flavor Meister in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/tasty-tracker/flavor-meister/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
