---
name: palatably-profiled
description: "Summarize taste patterns from attributed meal ratings and compare household preferences by ingredient, cuisine, mood or season."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Palatably Profiled

## Inputs

Use ratings or comments keyed to person and dish. Ask for dates if the user wants a trend. Keep stated dietary restrictions in a separate field from learned preferences.

## Workflow

1. Normalize ratings to their stated scale, retaining source comments. Tag ingredients or flavor only when supported. Track count and values for each person and tag. An unrated dish contributes no numeric score.
2. Compare two people on shared rated dishes or comparable tags. Show the overlap and at least one difference if supported. For a seasonal trend compare dated observations and state how many support each side.
3. Suggest a dish or a small tasting experiment from supported preferences. Flag weak evidence explicitly. Apply stated exclusions before offering candidates. Keep a blank cell for a person who has never rated a dish.

## Output

Return a profile table with person, tag, observation count, rating or comment, and one testable suggestion. For example, two smoky dishes rated 5/5 by one person support a tentative smoky preference for that person.

## Limits

Give a text table if a chart is unavailable. Ratings do not establish a medical diagnosis or another household member's preferences.

## Source

The catalog describes Palatably Profiled in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/tasty-tracker/palatably-profiled/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
