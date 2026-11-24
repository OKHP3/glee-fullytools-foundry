---
name: treasured-finds
description: >-
  Choose the right collection helper for books, decor, gifts, scents, bottles, craft supplies or bags. Use when the goal is to record, locate, lend, enjoy or replenish something in a personal collection.
license: MIT
metadata:
  version: "0.1.0"
---

# Glee-fully Treasured Finds

## Scope

Ask what the person wants to remember about the item and what they need to do next. Use the intended record to select one helper.

| Record to keep | Helper | Useful details to carry forward |
| --- | --- | --- |
| Edition or reading progress | Personal Librarian | Title, author, format, reading status |
| Seasonal display or storage | Decor Detective | Item, occasion, bin, setup or care notes |
| Gifts already acquired or hidden | Present Hoarder | Gift, recipient alias, occasion, readiness |
| Candle, melt or diffuser oil | Scentinal Journal | Scent, format, open state, impressions |
| Wine or spirit bottle | Spirited Journal | Label, bottle status, occasion, tasting notes |
| Craft material or tool | Supply Haus | Material, quantity and unit, storage, project |
| Handbag or carry-all | Bag Nabbit | Bag identity, condition, location or loan |

## Route the request

A gift candle can belong in two records. If the next question is “Where did I hide it?”, route to Present Hoarder. If it is “Would I buy that scent again?”, route to Scentinal Journal. For a mixed inventory, group the supplied items by the relevant record and start with the group the user wants to act on.

Return the helper name, one reason and a copyable intake using the details already supplied. Withhold hiding spots or identifying details from a handoff intended for someone else. If a specialist cannot be launched here, the intake is still usable as a plain-text starting point.

## Verify the result

Check that every item in a mixed request appears in a suitable group and that the suggested first helper can answer the person's immediate question. Read a shareable handoff once for spoilers.

## Sources and limits

The original repository contains general tooling and collection-planning notes. The routing table reflects the seven named helpers in the catalog. Shared storage and automatic transfers depend on host support.

Repository records

- `capabilities/treasured-finds/source/README.md`
- `inventory/inventory-of-toolbox-tools-and-tool-ettes.md`
