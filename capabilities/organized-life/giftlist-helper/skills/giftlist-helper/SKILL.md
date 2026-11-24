---
name: giftlist-helper
description: "Capture gift ideas or track purchases, stash locations, wrapping, delivery and giving by recipient and occasion. Use for gift timelines, wishlists or duplicate checks."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Giftlist Helper

## Inputs

Take an optional recipient, occasion or deadline, gift idea, source, budget and current state. Accept a quick idea without requiring a full profile.

## Workflow

1. Create an entry keyed to recipient, occasion and item. Store unsorted ideas in an inspiration list. Consult supplied gift history before suggesting a repeat. Similar items for different recipients remain separate.
2. Distinguish idea, bought, wrapped and given. Track shipped or stashed as separate facts when useful. Only advance a state the user reports. For a bought gift, offer a Present Hoarder handoff containing item, recipient alias and private location if wanted.
3. Work backward from the occasion using explicit order lead time and shipping buffer. Keep unknown arrival dates conditional. For a shared wishlist or printable view, leave out surprises, prices and hiding places when they would spoil the gift.

## Output

Return a recipient list with item, occasion, status, next action and optional private notes. For example, 'bought the puzzle' changes purchase status; it leaves wrapping and giving open.

## Limits

A copyable stash or reminder entry works without another tool. Sending a wishlist, writing to an external stash, or ordering a gift requires a distinct action.

## Source

The catalog describes Giftlist Helper in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/organized-life/giftlist-helper/source/README.md. Additional source material used here includes capabilities/organized-life/giftlist-helper/source/giftlist-helper-final.md. This version adapts the documented product instructions to a text workflow. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
