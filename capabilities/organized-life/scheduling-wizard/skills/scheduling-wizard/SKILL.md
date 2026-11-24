---
name: scheduling-wizard
description: "Arrange tasks, bills, routines, focus work and protected Joy Anchors into a feasible calendar draft, including recurrence, buffers and overload recovery."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Scheduling Wizard

## Inputs

Collect the scheduling window, local time zone, immovable commitments, durations, deadlines, energy preferences and explicitly protected breaks or Joy Anchors.

## Workflow

1. Place fixed events, due-time reminders, transitions and protected personal time first. A due date alone is a deadline. Use a separate block for the work that must precede it.
2. Group compatible tasks into remaining windows. Prefer high-energy periods for focus work when the user identifies them. For a conflict, show the overlap, preserve fixed blocks and offer specific moves for flexible tasks. Mark unschedulable work for another window.
3. Represent recurrence with weekday or month rule, local time, time zone, exceptions and optional alerts. Ask about ambiguous local times or missing zones before cross-zone conversion. Distinguish reminder time from event time.

## Output

Return day, local start/end, activity, fixed/flexible, reminder and conflicts. For example, protect a 12:00–12:30 walk as a Joy Anchor even when a new 45-minute task arrives.

## Limits

A pasted agenda can stand in for a calendar. Return a copyable draft or adapter handoff. Calendar writes and notifications require separate evidence.

## Source

The catalog describes Scheduling Wizard in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/organized-life/scheduling-wizard/source/README.md. Additional source material used here includes capabilities/organized-life/scheduling-wizard/source/prompts/scheduling_wizard_gpt_system_instructions.md. This version adapts the documented product instructions to a text workflow. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
