---
name: present-hoarder
description: >-
  Create and reconcile a gift stash by recipient and occasion. Use to find hidden gifts, record wrapping or shipping, update assignments and produce an owner-only inventory or a spoiler-safe status message.
license: MIT
metadata:
  version: "0.2.0"
---

# Present Hoarder

## Scope

Build the requested gift record from the available details using the [gift stash template](references/gift-stash.md) if a reusable ledger would help. Use a private stash view for the owner and a separate, purpose-built message when the audience includes recipients. A typed update changes the working ledger in this conversation.

## Build the stash

Give each physical gift or distinct idea a short stable label. Record recipient or alias, occasion, item and quantity. Use separate fields for acquisition (idea, bought or otherwise obtained), wrapping (unknown, unwrapped, wrapped), and delivery (held, shipped, given). For an owner-facing record, include the last confirmed hiding spot and any useful attributes the owner supplies, such as size, wrapping instructions, a wishlist link or a gift note. Treat wishlist links as references. Count only acquired gifts as physical stock.

A bought and wrapped gift remains in the stash while held. A shipped gift has left the stash, even if its arrival is unknown. Preserve its wrapping history, mark the hiding place as previous, and wait for a receipt or explicit report before marking it given or delivered.

## Update and share

1. Apply an update to the matching recipient, occasion and gift label. Keep identical purchases as separate rows when their recipients, locations or delivery states differ. If a move cannot be tied to a row, ask for one distinguishing detail and leave both records intact.
2. Preserve the earlier event when an owner reassigns, ships or gives a gift. Update the current count and location only for the quantity that moved. A repeated report of the same shipment cannot reduce the count twice.
3. For a private reconciliation, show the updated rows, physical items still held, and the next action for each. Calculate “ready to give” from acquired, wrapped gifts still held. A shipped gift can remain in transit.
4. For a shared message, build a new view containing only the requested status and counts. Check the entire reply, including its heading and follow-up, for names, hiding places, item descriptions, wishlist links or hints that would reveal a surprise. When the user asks for a group message only, return just the safe message. If the audience is unclear, a count-only update can proceed while the private details stay out.

For questions about the documented behavior of a related gift tool, inspect the supplied suite guide or catalog. Identify the file used. A source's historical launch address does not establish a current destination.

## Repository sources

The Present Hoarder entry in `inventory/inventory-of-toolbox-tools-and-tool-ettes.md` defines recipient, event, hiding spot, wishlist references, gift stages and notes. `capabilities/treasured-finds/present-hoarder/plugin/skills/instructions/SKILL.md` preserves the original plan. Its earlier repository guide is `capabilities/treasured-finds/present-hoarder/source/README.md`. This workflow produces a working list or a shareable message directly in the conversation.
