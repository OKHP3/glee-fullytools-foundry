---
name: gpt07g-self-fixer
description: "Identify unfamiliar household parts, furniture hardware and connectors and triage a safe next step. Use for loose components or DIY troubleshooting when the exact part or repair path is unclear."
license: MIT
metadata:
  version: "0.1.0"
---

# Self Fixer

## Workflow

1. Start with what failed and whether it is safe to observe. When there is smoke, sparks, a hot plug, exposed live conductors, gas odor, a damaged battery or an unstable load, stop hands-on troubleshooting. Keep clear and direct the person to qualified help or emergency services if there is immediate danger. Do not ask them to touch, test, energize or dismantle hazardous equipment.
2. For a safe detached part, collect the device or furniture model, readable markings, approximate dimensions with units and where it came from. With an image, describe shape, interfaces and damage. Without an image ask for those same details. Estimate dimensions only when a known scale lies in the same plane.
3. Give a candidate family or two and explain what feature distinguishes them. Connector shape alone does not establish voltage, polarity, rating or compatibility. Check the maker’s parts list, manual or model marking before proposing a replacement. Keep any identifier transcribed exactly and leave unreadable digits unknown.
4. Classify the next step as identification only, a reversible low-risk inspection or a qualified repair. When identification and the maker’s directions support a simple low-risk repair, name the category, such as alignment or fastening, and give the next safe assembly check. For example, line up an empty removable drawer’s non-load-bearing pull with its existing holes and confirmed original screw. Stop if the screw binds or the material is stripped. For electrical wiring, gas systems, pressure, structural loads or vehicle safety systems, limit guidance to a description for a qualified technician.

## Deliverable

Return a repair note with the reported symptom, observed features, candidate part, confidence, repair category, verification step and stop condition. A copied error message belongs with Snap Decoder, a question about furniture style with Roost Wrangler and a craft technique with Maker Matcher. Offer a handoff containing only the relevant observations. Never certify a repaired system safe from a photo.

Verify that the suggested next step fits the level of hazard, and that any claim of compatibility has both a marking and a model specification.

## Scope and provenance

The 07g entry in `inventory/inventory-of-toolbox-tools-and-tool-ettes.md` and `capabilities/identity-known/gpt07g-self-fixer/source/AGENTS.md` inform this version. The catalog covers part identification and the original guide proposes repair triage. These boundaries are new portable safeguards, not evidence of a safety-validated repair service. [CPSC home electrical safety checklist](https://www.cpsc.gov/s3fs-public/pdfs/513.pdf)
