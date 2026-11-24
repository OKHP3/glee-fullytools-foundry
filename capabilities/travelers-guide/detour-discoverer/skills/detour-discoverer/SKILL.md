---
name: detour-discoverer
description: "Evaluate a side trip or layover stop against the actual time and distance available, then provide a usable insertion or skip decision."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Detour Discoverer

## Inputs

Take the start, return or next stop, available window, immovable departure, required return buffer, transport mode and the traveler's interests.

## Workflow

1. Measure the incremental detour. On a layover include outbound travel, the visit, return travel and the required buffer. On a through-route subtract the original direct travel only when both direct and alternative durations are known.
2. Compare one or a few candidate stops. For each, list the evidence for duration, hours, fee, access and interest match. Label missing or time-sensitive facts as checks. Reject a stop that breaches the fixed buffer.
3. For a viable stop, propose a departure, latest turnaround and rejoin point. Provide a shorter option or staying on route when the margin is thin. Log optional, made or skipped with the traveler's reason.

## Output

Return a candidate comparison and a suggested itinerary insertion. For example, a 90-minute window minus 20 minutes each way and a 25-minute return buffer leaves 25 minutes for the visit.

## Limits

Without current transport or opening-hour data, give a conditional assessment. A planned stop stays optional until the traveler reports making it.

## Source

The catalog describes Detour Discoverer in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/travelers-guide/detour-discoverer/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
