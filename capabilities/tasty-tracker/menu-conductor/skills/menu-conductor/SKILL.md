---
name: menu-conductor
description: "Build a day, week or event menu from available recipes, diners, prep windows and repeat meals. Use when timing, leftovers or a grocery handoff matters."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Menu Conductor

## Inputs

Collect slots to fill, number of eaters, dietary limits, time available, favorites and any portions already cooked. Keep optional meal slots flexible.

## Workflow

1. Anchor recurring meals and fixed events first. Filter proposed dishes against the diners' restrictions and prep window. Identify which recipes or favorites the user supplied.
2. Assign a meal and servings to each remaining slot. Schedule batch cooking before its leftovers, reserve the leftover portions, and count a batch only once in ingredient demand. Call out any shortfall.
3. Return a prep sequence and a grocery handoff listing ingredients for the planned batches. Subtract pantry quantities only if supplied. If recipe amounts are missing, list items to check. A reusable menu carries a recurrence label and can be copied into the next week.

## Output

Use rows with day, meal, diners, new or leftover portions, prep and notes. For example, cook four portions Monday, eat two and reserve two for Tuesday. Tuesday then adds zero new recipe batches.

## Limits

An absent calendar or grocery service still permits a complete printable menu. Treat supplied allergen restrictions as filters and flag uncertain ingredients for checking.

## Source

The catalog describes Menu Conductor in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/tasty-tracker/menu-conductor/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
