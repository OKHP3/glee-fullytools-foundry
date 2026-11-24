---
name: supply-haus
description: >-
  Track craft materials, tools and project consumption. Use to reconcile quantities, locate stock by material or color, or make a restock list from actual project needs.
license: MIT
metadata:
  version: "0.1.0"
---

# Supply Haus

## Scope

Identify the supply, material or variant, unit and location. Keep consumables such as ribbon separate from reusable tools such as scissors. Accept an initial count, a stocktake or a movement log. Label estimates explicitly.

## Workflow

1. Give each supply variant a stable label with material, color, dimensions or size where useful. Two same-color ribbons of different widths can require separate balances. Record original units and pack size when known.
2. Log an event for receipt, use, return, disposal or count correction. Calculate the balance only when starting stock, units and event direction are compatible. Keep a stocktake correction separate from project use. A tool can be checked out or relocated without being consumed.
3. For planned work, compare required quantity with available unallocated stock. Reserved stock remains physically present. Calculate shortages in the same unit and round to whole packs only when the pack size is known. If an event implies negative stock, preserve the discrepancy and request a recount or missing receipt.
4. Return quantities with units, locations and a short movement history keyed to projects. Provide a restock list only for demonstrated shortages or a user-specified threshold. Treat purchases as a separate action.

## Verify the result

Verify each balance in its original unit. Check that reserved stock was deducted once from availability, that actual use is recorded once and that a reusable tool still appears in inventory.

## Sources and limits

The archived YAML holds draft metadata. The catalog describes quantity, project use, material tags and restock tracking. A text ledger supports the workflow without a shopping account or external inventory service.

Repository records

- `inventory/inventory-of-toolbox-tools-and-tool-ettes.md`
- `capabilities/treasured-finds/supply-haus/source/prompts/02f-supply-haus-prompts-v1.yaml`
