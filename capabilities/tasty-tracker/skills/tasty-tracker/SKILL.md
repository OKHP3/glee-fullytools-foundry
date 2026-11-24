---
name: tasty-tracker
description: "Organize a cooking request across recipe cards, menus, food wishlists, groceries and taste profiles. Use when a household wants several of these to fit together."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Tasty Tracker

## Inputs

Start with the outcome and the records available here. Capture diners, hard food restrictions, dates, portions and any pantry counts that affect this request.

## Workflow

1. Route a dish already cooked to Flavor Meister, a future meal slot to Menu Conductor, a food experience still to try to Wishful Tastes, inventory or purchasing to Pantry Shopper, and comparisons across ratings to Palatably Profiled. A simple request needs only its matching route.
2. For a mixed request, build only the records that feed the next decision. Give a recipe a short name and serving yield, place that name and the required portions in menu slots, then sum ingredients for those portions before subtracting available stock once.
3. Keep a wishlist idea distinct from a rated meal. Treat an allergy as a hard exclusion and a dislike as a preference. If an ingredient list is incomplete, flag that dish for checking before planning it for the affected diner.

## Output

Return the chosen route, the working records and any unfilled inputs. For example, a two-serving bean bowl scheduled twice creates four portions of demand. Two cups of beans on hand cover two of four required cups, leaving two cups to shop for.

## Limits

The user can carry these records between sessions. A missing recipe collection or pantry inventory stays unknown until supplied.

## Source

The catalog describes Tasty Tracker in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/tasty-tracker/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
