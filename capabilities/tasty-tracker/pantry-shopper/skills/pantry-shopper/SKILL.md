---
name: pantry-shopper
description: "Build an aisle-grouped shopping list by reconciling recipe quantities with pantry stock, staple thresholds and use-first items."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Pantry Shopper

## Inputs

Take planned batch count or serving yields, ingredient quantities, pantry amounts, optional expiration dates and staple minimums. Keep the unit associated with each number.

## Workflow

1. Scale each recipe for the servings to cook, combine demand for equivalent ingredients in compatible units, and deduct inventory once per item. Distinguish a reserved leftover meal from a new batch.
2. For a specified end-of-plan minimum, buy max(0, recipe demand + target ending stock − usable stock). Show the arithmetic when the staple target changes the result. Keep incompatible units separate until the user supplies a conversion.
3. Flag soon-dated stock as a use-first candidate. Separate items to buy from quantities to check. Group purchases by aisle or store section. Convert to packs only if pack size is supplied and show surplus.

## Output

Return a phone-friendly checklist and a short use-first or check list. For example, demand of 3 cups plus a 1-cup ending target less 2 cups on hand yields 2 cups to buy.

## Limits

Unknown stock is not zero. Treat uncertain condition or storage as a check item. Leave mobile sync and restock alerts as copyable text until a separately authorized adapter is available.

## Source

The catalog describes Pantry Shopper in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/tasty-tracker/pantry-shopper/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
