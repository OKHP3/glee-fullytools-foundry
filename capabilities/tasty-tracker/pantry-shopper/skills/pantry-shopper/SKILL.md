---
name: pantry-shopper
description: "Build an aisle-grouped shopping list by reconciling recipe quantities with pantry stock, staple thresholds and use-first items."
license: MIT
metadata:
  version: "0.2.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Pantry Shopper

## Reconcile the pantry and the menu

Turn the actual recipe quantities and the user's shelf count into a shopping slip for the next shop. Accept pasted rows, dictated quantities, dated lots, a prior slip or a partial inventory. Make useful progress for the measured ingredients even when others need checking.

1. Scale each recipe to the portions that will be cooked. Sum demand once per fresh batch and once per ingredient. A meal served from reserved leftovers adds no new ingredients. Keep dried and cooked weights, different preparations and incompatible units separate unless a reliable conversion is supplied.
2. Total eligible on-hand stock after excluding quantities already reserved, discarded or explicitly unavailable. Keep separate lots when their date or storage matters. Distinguish “unknown” from zero. Suggest using earlier-dated stock first where its condition and storage are suitable. A date label alone cannot establish food safety.
3. For a known stock and a requested ending reserve, compute **max(0, recipe need + ending reserve − usable stock)**. Use zero reserve unless specified. If a pack size is supplied, round the shortfall up to whole packs and show expected inventory after the plan. Otherwise list the exact quantity and unit. Show each term where a threshold or pack rounding changes the result.
4. Return an aisle-grouped checklist plus a separate “Use first / Check” list. Distinguish definite purchases from items the shopper must measure. For a staple, show the restock trigger as a note. If asked for a meal from the pantry, suggest one supported by the listed stock, identifying any missing ingredient.
5. On a recount, correction, purchase or changed menu, update the right quantity and recompute the whole slip. A corrected count replaces the old count. A purchase adds only what was actually brought home. Planning to buy or cook does not change current stock.

Fill the included `references/pantry-balance.md` to show the ingredient arithmetic and a mobile-friendly slip. Keep the same units in the follow-up so the shopper can reconcile it. A plain-text checkbox list is usable without mobile synchronization or automatic alerts.

## Original guide

Pantry Shopper is entry #03d in `governance/operators-cathedral-layout.md` and `inventory/inventory-of-toolbox-tools-and-tool-ettes.md`. The migrated guide is `Operator’s Cathedral Layout 📐.md`. Use the guide for original design questions and the editable balance sheet for calculations.
