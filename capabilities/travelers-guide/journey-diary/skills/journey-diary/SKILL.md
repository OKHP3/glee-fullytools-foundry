---
name: journey-diary
description: "Turn memories from a past trip into a journal entry, optional reflection and list of places suitable for a map. Use for travel recaps and visited-place logs."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Journey Diary

## Inputs

Ask for the destination, date or approximate period, optional companion labels and a few concrete memories. Let the traveler decide what is shareable.

## Workflow

1. Order known events using their dates or the user's sequence. Preserve approximate timing or uncertainty rather than assigning a precise day. Keep visited places separate from places the traveler only considered.
2. Shape the supplied sensory details, meals, surprises or lessons into a short journal in the traveler's chosen voice. Quote only words they supplied. Leave a reflection prompt if they gave no personal reaction.
3. Add trip type tags and a visited-places list. Link each named keepsake or media label to its event. Use location names for map-ready rows and include coordinates only when provided or independently verified.

## Output

Return a journal entry followed by visited places, optional media labels and a reflection. For example, a café stop remembered as 'sometime in June' stays dated June, day unknown.

## Limits

Use a text map index if there is no map tool. Skip unseen image descriptions and omit precise home locations or private companion details from public versions.

## Source

The catalog describes Journey Diary in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/travelers-guide/journey-diary/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
