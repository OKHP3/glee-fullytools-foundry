---
name: supply-haus
description: >-
  Build and update a craft inventory by material, variant, location and project. Use to track consumables, checked-out equipment, reserved stock, actual use and shortages in compatible units.
license: MIT
metadata:
  version: "0.2.0"
---

# Supply Haus

## Scope

Produce a working ledger from the amounts supplied. Use the [craft stock ledger](references/craft-stock-ledger.md) to reconcile materials and tools or to give the user a copy-ready version of the result.

## Identify the stock

Give each material variant a stable label with color, dimensions, unit and location where known. Keep same-color ribbons of different widths separate. Record opened stock or low-stock thresholds when supplied. Track scissors, punches and other reusable equipment by unit, location and borrower or project. A tool still exists while checked out.

## Maintain a balance

1. Start with a known physical count or measured amount. Mark an estimate or unknown balance explicitly. Record each purchase received, usage, return, disposal or stocktake correction as a dated or sequential event. A change in location moves stock without changing the total.
2. Keep a separate reservation by project. Available stock equals on-hand quantity less all outstanding reservations. Reserving material changes availability only. Using stock from that reservation reduces both on-hand stock and that project's reservation by the amount used. Releasing the unused portion clears just that reservation. Distinguish it from returning material that was actually issued.
3. Recalculate the affected rows on follow-up and retain unrelated variants and tools. Keep the movement history with the reason, so a correction replaces an incorrect event and a repeated report is not counted again. Show discrepancies when units cannot be converted or use exceeds stock. Ask for the missing count or conversion without fabricating a balance.
4. For an upcoming project, compare its need to what can be issued to it, including any stock already reserved for that same project. Report the shortfall in the original unit. Round up to whole packs only if a pack size is known. A suggested purchase produces a shopping note; add stock only when the user reports receipt.

## Choose a view

For an inventory, show on hand, reserved, available and location with units. For a project, show its reservation, actual use, tool checkouts and shortfall. For a restock list, include the material, amount short and pack calculation. If a user asks about keeping the finished craft, identify the relevant documented specialist function and name the source actually used.

## Repository sources

`inventory/inventory-of-toolbox-tools-and-tool-ettes.md` documents quantities, project use, material and color tags, and status. `capabilities/treasured-finds/supply-haus/plugin/skills/instructions/SKILL.md` preserves the original hosted plan. The earlier metadata-only prompt survives at `capabilities/treasured-finds/supply-haus/source/prompts/02f-supply-haus-prompts-v1.yaml`. This workflow uses the quantities and events supplied in the conversation.
