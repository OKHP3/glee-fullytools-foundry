---
name: snappy-count
description: "Record meals from a photo or description and estimate broad portions or nutrition ranges when evidence supports them. Use for a meal diary, snack log or weekly food overview."
license: MIT
metadata:
  version: "0.1.0"
---

# Snappy Count

## Workflow

1. List visible or reported foods and beverages, time if supplied and an optional energy or mood note. Label sauces, oils or ingredients hidden from view as unknown. For an inaccessible image ask for a short description of the plate.
2. Use a known serving, label, household measure or comparison supplied by the user. Ask for the portion or preparation detail that would most change the result. If numbers are useful, give a broad range with its assumptions or calculate from an actual label. Skip a numerical estimate when the inputs cannot support one.
3. Keep estimated intake separate from measured or labeled amounts. For a weekly recap, make a compact plate-by-day table with meals, snacks and drinks actually reported. Offer a neutral observation about variety. Avoid framing food as a reward or punishment.
4. If an estimate is requested for a medical dosing decision, direct the person to their prescribed plan and clinician or pharmacist. Decline extreme restriction targets and offer a non-numeric log or support. Do not infer allergies, ingredients or safe consumption from a photo.

## Deliverable

Give a meal card with food, portion and evidence, optional estimate and uncertainty. For a recap, state coverage and leave unlogged meals blank.

Verify portion arithmetic against the label and ensure the reported total excludes unmeasured additions or explicitly accounts for their uncertainty.

## Scope and provenance

The 06c entry in `inventory/inventory-of-toolbox-tools-and-tool-ettes.md` and `capabilities/healthy-bee-ing/snappy-count/source/docs/06-glee-fully-healthy-bee-ing_pulsebook_20250901.md` inform this version. The parent outline identifies photo-based food awareness. Estimates depend on the information provided and do not require camera or tracker access.
