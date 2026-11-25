---
name: flavor-meister
description: "Turn a recipe and tasting notes into a reusable recipe card. Use for personal tweaks, flavor tags, meal ratings, favorite dishes or retrieval by occasion."
license: MIT
metadata:
  version: "0.2.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Flavor Meister

## Build a recipe box

Use a pasted recipe, ingredient notes, or previously returned cards. Produce a filled recipe card during this turn. Start with what the cook supplies, even when the cooking method is incomplete. Give each distinct recipe a stable title or short ID and keep that ID through revisions.

1. Put title, yield, ingredients with original quantities and units, and ordered method on the base card. Preserve a measure such as “one handful”. Mark missing times, quantities or steps as unknown. Keep personal tweaks in a separate cook entry unless the user explicitly revises the base.
2. For a cook, record its date when known, actual substitutions, taster, rating on the stated scale, and the cook’s description. The regular star scale is 1–5. Keep comments when the user gives no score. If a score uses another scale, label it or ask before converting it into stars.
3. Append a later tasting to the same recipe. Several tasters can rate one cook independently. Correct only the matching taster and cook when the user revises a rating. Use the most recent known date for “last cooked”. Mark a recipe as a favorite or family go-to only on the user's instruction.
4. Tag the dish with supported flavor, cuisine, season, meal or occasion terms. To retrieve from a set of cards, apply the requested favorite, rating or tag filters and identify the matching evidence. If no card matches, show that result. A planned substitution belongs under ideas until the cook reports trying it.

Use the included `references/recipe-card.md` for a reusable card and tasting log. Keep its fields when filling or revising a sheet the user has already copied. Return the current card and the relevant log after an edit. If the user wants a file and the host cannot make one, give copyable Markdown or properly quoted CSV. Treat a card kept in this conversation as durable across sessions only if the user saves and supplies it again.

## Original guide

Flavor Meister is entry #03a in `governance/operators-cathedral-layout.md` and `inventory/inventory-of-toolbox-tools-and-tool-ettes.md`. The migrated guide is `Operator’s Cathedral Layout 📐.md`. Use it for questions about the original design. The editable sheet is part of this skill.
