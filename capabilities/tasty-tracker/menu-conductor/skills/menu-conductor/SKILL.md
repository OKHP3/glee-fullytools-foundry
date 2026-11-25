---
name: menu-conductor
description: "Build a day, week or event menu from available recipes, diners, prep windows and repeat meals. Use when timing, leftovers or a grocery handoff matters."
license: MIT
metadata:
  version: "0.2.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Menu Conductor

## Make the menu

Produce the day, week or event menu the person can use today. Take the meal slots, dates, diner counts, restrictions, prep windows and any favorites or recipes they supplied. A pasted prior menu can be the starting plan. With sparse inputs, make a partial plan now and ask only for details that affect feasibility. Mark new dish suggestions as suggestions.

1. Fill fixed events and recurring meals first. Match favorites to the time and diners for each slot. Flag uncertain ingredients when a restriction matters. If no dish fits, offer a workable alternative or leave the slot open.
2. Give every batch a short label. Record its cooking day, yield, portions served, portions reserved and intended later meal. Reserve portions only once. Schedule a cook ahead of a reheat-only evening. If no amount of the chosen dish can satisfy everyone in the available time, identify the shortage.
3. Build the shopping handoff from **batches actually cooked**. Scale quantities by planned yield divided by recipe yield. Deduct known pantry stock once after totaling demand. List ingredients with missing amounts under “Check”. Name a confirmed recurrence in the copyable plan.
4. When diners, timing or stock change, return the entire revised menu and handoff. Keep unaffected meals and restrictions. If an earlier meal has already happened, carry its actual remaining portions forward. If the cook is still planned, resize it when the recipe permits. Show what changed.

Use `menu-plan.md`, included under `references/`, for a reusable sheet or when the user asks about its columns. Fill in the menu and its grocery handoff, then give the cook/reheat sequence. If the sheet cannot be opened, use day, meal, diners, prep window, batch and portion allocation, followed by shopping amounts. If the person asks to reuse the plan, include the recurrence and editable quantities in the text. Calendar entries, shared lists and cross-plugin transfers require a host that actually performs those actions.

## Original guide

The Menu Conductor catalog entry is #03b in `governance/operators-cathedral-layout.md` and `inventory/inventory-of-toolbox-tools-and-tool-ettes.md`. Its migrated knowledge filename is `Operator’s Cathedral Layout 📐.md`. Consult that entry for questions about the original design and cite the source actually available. The menu and revisions can be produced from the supplied ingredients and schedule alone.
