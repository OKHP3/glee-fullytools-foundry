---
name: decor-detective
description: >-
  Build and update a seasonal décor inventory from a description, stocktake or prior ledger. Use for display setup, takedown, storage-bin lookup, maintenance history and copy-ready packing or reminder lists.
license: MIT
metadata:
  version: "0.2.0"
---

# Decor Detective

For a stocktake, turn the details supplied into a usable inventory on the first reply. For a later move, repair or correction, revise the inventory already in the conversation. Use the [seasonal inventory template](references/seasonal-inventory.md) for a copy-ready table or use the same fields in CSV.

## Inventory and updates

1. Identify an item or set using a short stable label. Capture occasion or season, type or use, quantity and unit, normal storage spot, and current physical locations. Keep a user-supplied tag such as “winter mantel” or an item's personal story. If the maker or material is inferred from an image, record it as an observation. Request a label or distinguishing feature before merging similar items.
2. For a split set, give each current location its own quantity. If the owner supplies the total and one part, calculate the remainder only when the destinations cover the whole set. Record unknown quantities as unknown. Count a damaged piece once at its physical location and attach its condition there.
3. Apply each event to the named item, quantity, origin and destination. Preserve unaffected balances and the set’s normal storage location. Log the event and date or seasonal cue provided. A correction replaces the earlier assertion. A requested move stays planned until the owner confirms it occurred. Ask about an ambiguous origin or insufficient stock before subtracting from it.
4. Record cleaning, completed repair, damage awaiting repair and retirement distinctly. Include only the observed work in history. Put proposed work on a maintenance list. Check the current location totals against the known set count and identify discrepancies with the smallest useful question.

## Return the requested view

For a stocktake, show the label, occasion, current locations and quantities, normal storage, and any condition or next action. For setup, group items by display area. For takedown, group by destination bin and keep pieces awaiting care visible. For a follow-up, show what changed and the revised totals. If the owner asks for a reminder, draft the text with the supplied date or seasonal cue. Claim a calendar change only after an authorized calendar action succeeds.

Scentinal Journal handles fragrance performance, while this inventory tracks the candle or accessory as an item of décor. For a question about documented sibling functions, consult the supplied suite reference and identify the file actually used. A requested organizational handoff can be fulfilled with the verified destination supplied by the host.

## Repository sources

The Decor Detective catalog entry in `inventory/inventory-of-toolbox-tools-and-tool-ettes.md` documents holiday cataloging, tagging, storage, seasonal changes and maintenance. `capabilities/treasured-finds/decor-detective/source/README.md` describes the earlier identification concept. The historical hosted instructions are preserved in `capabilities/treasured-finds/decor-detective/plugin/skills/instructions/SKILL.md`. The inventory workflow can run from conversation context alone.
