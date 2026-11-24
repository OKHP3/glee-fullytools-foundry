---
name: itinerary-hacker
description: "Build or repair a day-by-day itinerary around reservations, transit, meals, rest and optional activities. Use for a mobile schedule or repeatable trip template."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Itinerary Hacker

## Inputs

Collect local dates and time zones, locations, fixed bookings, durations, travel estimates, accessibility needs and preferred pace. Mark an estimate where evidence is incomplete.

## Workflow

1. Place fixed bookings and necessary arrival buffers first. Work backward from each deadline using travel plus preparation time. Anchor the end of one block before sizing the next.
2. Fill flexible slots with categorized activities, meals and rest. Include transfers explicitly. If two anchors collide, show the size of the conflict and the smallest flexible change. Preserve fixed times until the traveler chooses otherwise.
3. Attach supplied map or booking references to the matching slot. Give alternatives for weather or low energy. For a recurring destination, provide an optional template that retains slot types while removing trip-specific booking details.

## Output

Return local day, start and end, place, activity category, transfer/buffer, and booking status. For example, a 14:00 appointment that needs 15 minutes for check-in and 25 minutes of travel means leaving by 13:20.

## Limits

Without live routing, treat travel durations and opening hours as provisional. The itinerary is a proposed schedule until the user confirms actual reservations.

## Source

The catalog describes Itinerary Hacker in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/travelers-guide/itinerary-hacker/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
