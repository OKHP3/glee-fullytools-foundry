---
name: career-seeker
description: >-
  Maintain a job application log, reconcile new events and find the next follow-up. Use for tracking opportunities, interviews, deadlines, statuses or search progress.
license: MIT
metadata:
  version: "0.1.0"
---

# Career Seeker

## Scope

Request the current log or the events to record. Accept sparse notes and identify each opportunity by employer plus role and, when available, requisition ID or posting URL. Two openings at one employer may need separate records.

## Workflow

1. Keep a row per opportunity with employer, role, identifier or link, current stage, latest event date, next action, due date and notes. Capture the version of application materials where useful. Distinguish saved, applied, interviewing, offer, declined, withdrawn and closed. Preserve the user's original labels where they carry finer detail.
2. Reconcile events in chronological order. A scheduled interview is a future action until it occurs. A later status does not erase earlier evidence. On a possible duplicate or a contradictory event, show the candidate records and ask which applies.
3. Return the updated table plus a short next-action list sorted by known due dates. Clarify the date or timezone behind relative phrases when it affects priority. If reporting progress, give numerator, denominator and time window. Mark missing dates or states as unknown.
4. Provide an exportable table or CSV on request. A generated follow-up date is a draft reminder until an authorized calendar records it. Keep recruiter messages, application submission and personal contact details separate from routine tracking.

## Verify the result

Reconcile the row count to distinct opportunities and check that each next action belongs to the right opening. Recompute progress figures after resolving a duplicate.

## Sources and limits

The catalog calls for a log, stage tracking, reminders and progress views. The portable skill uses the table supplied in the session as its working record. It has no implicit access to job sites or calendars.

Repository records

- `capabilities/discovered-careers/career-seeker/source/README.md`
- `inventory/inventory-of-toolbox-tools-and-tool-ettes.md`
