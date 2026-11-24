---
name: medi-minder
description: "Organize medication label instructions, appointments, refill counts and questions for a pharmacist. Use for a medication list or reminder draft."
license: MIT
metadata:
  version: "0.1.0"
---

# Medi Minder

## Workflow

1. Transcribe the medication name, strength, form, written directions and source exactly as supplied. Keep strength separate from amount per dose. Label unconfirmed instructions, conflicting lists and any timing the person supplied independently. Ask for clarification of illegible labels.
2. Build a schedule only from verified directions. Keep as-needed medicines separate from scheduled ones. Preserve appointment time zone when known. For a regular fixed regimen, calculate full days of supply from remaining units divided by units per day and show the arithmetic. An as-needed regimen has no fixed run-out date.
3. Log possible side effects with dates and observations without assigning cause. Send missed-dose, conflicting-strength or interaction questions to a pharmacist or prescriber. Never tell someone to double, stop or change a dose. If an overdose is suspected, direct them to local poison control or emergency care immediately.
4. Offer a patient-held list or draft reminder. Before sharing with a caregiver, identify the recipient and what the patient wants included. Only report a reminder as scheduled or information as shared when an authorized tool actually confirms the action.

## Deliverable

Return a medication or appointment table, a refill estimate if justified and unresolved questions. Keep written directions intact in the shareable list.

Verify every transcribed strength and direction against the supplied wording. If entries disagree, leave the schedule unresolved for that item.

## Scope and provenance

The 06d entry in `inventory/inventory-of-toolbox-tools-and-tool-ettes.md` and `capabilities/healthy-bee-ing/medi-minder/source/README.md` inform this version. The source and catalog identify medication, refill and appointment support. Reminder text and a patient-held list work on a host without scheduling or messaging. [FDA guide to medication lists](https://www.fda.gov/consumers/consumer-updates/create-and-keep-medication-list-your-health)
