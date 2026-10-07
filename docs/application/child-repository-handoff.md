# Child Repository Handoff

## September 27, 2026 destination update

New product consolidation targets [product subtrees](../../products/README.md). Use the [portable capability workflow](portable-capabilities.md) for skill conversion and adapter blueprints. The four-kind child-repository notes below are historical source guidance; they do not require creating another repository. Plugin/connector exports add adapter-blueprint.json and adapter.md and are non-installable design contracts.

This note maps the four export package types to a reviewable child-repository handoff using the current FoundRy application export shape and local governance.

Base revision for this handoff: `32b89159293bba2edc0c9b308b716ab20e234b5d` from `origin/main`.

## What Was Verified

The ZIP export members are defined in `app/server.py` and are covered by the service tests in `app/tests/test_server.py`.

Shared ZIP members across all kinds:

- `project.json`
- `README.md`
- `specification.md`
- `evaluation.md`
- `skill-references.md`
- `handoff.md`

Type-specific ZIP members:

- `custom-gpt`: `instructions.md`, `starters.md`
- `agent-skill`: `SKILL.md`
- `workflow`: `workflow.md`, `workflow.json`
- `web-tool`: `index.html`, `style.css`, `app.js`

## Handoff Mapping

| Package type | What the ZIP is for | Required review | Target validation | Public-data exclusions |
|---|---|---|---|---|
| `custom-gpt` | Reviewable authored GPT brief with exportable instructions and starters. | Check that the authored behavior is complete, the inputs and outputs are explicit, and the package does not claim PME or publication readiness. | Confirm the shared members plus `instructions.md` and `starters.md` exist, and confirm `evaluation.md` records actual observed evidence rather than invented passes. | Do not include secrets, personal records, private prompts, or deployment claims. Preserve canon in the ledgers only. |
| `agent-skill` | Portable skill package with a structurally valid `SKILL.md`. | Check trigger scope, inputs, procedure, verification, and handoff language. | Confirm the shared members plus `SKILL.md` exist, and confirm the description and Markdown body remain safely encoded. | Do not include credentials, private source links, or unverified installation claims. |
| `workflow` | Repeatable process package with structure and evidence. | Check step order, roles, exception paths, and acceptance evidence. | Confirm the shared members plus `workflow.md` and `workflow.json` exist, and confirm the JSON mirrors the recorded components. | Do not include private operational data, external system secrets, or claims that the workflow is already deployed. |
| `web-tool` | Runnable local starter for record entry, completion, reopening, and filtering. | Check that the starter works on loopback, the record flow is usable, and the exported files remain self-contained. | Confirm the shared members plus `index.html`, `style.css`, and `app.js` exist, then open the ZIP contents in a browser and exercise add, complete, reopen, and filter behavior. | Do not include live account data, network credentials, public hosting instructions, or any repository-root serving path. |

## Review Expectations

The child repository reviewer should verify three things for any received package:

1. The package contents match the export kind.
2. The package evidence is observed, not fabricated.
3. The handoff stays inside the public, reviewable boundary.

That means:

- Review `project.json` for the authored record state.
- Review `README.md`, `specification.md`, `evaluation.md`, `skill-references.md`, and `handoff.md` together.
- Review the type-specific file set for the chosen package kind.
- Reject any package that asserts readiness, deployment, or automatic validation without recorded evidence.

## Public-Data Boundary

The package is meant to be shared as a review artifact, not as a data dump.

Keep these out of the handoff:

- passwords, tokens, API keys, or secrets
- private operational data or personal records
- live deployment URLs that imply publication
- copied canon or repository-root instructions
- unverified claims about what was tested

Keep these in the handoff:

- authored descriptions, constraints, and instructions
- observed acceptance evidence
- pinned Skillz references already present in the project
- loopback-only validation notes

## Synthetic End-to-End Example

**Synthetic example**

1. Create a `web-tool` project named `Field Notes Pack` with a clear purpose, inputs, outputs, constraints, instructions, one component, and one acceptance case.
2. Record actual evidence for the acceptance case, such as “Saved and reopened successfully.”
3. Export the project as ZIP.
4. Verify the ZIP contains `project.json`, `README.md`, `specification.md`, `evaluation.md`, `skill-references.md`, `handoff.md`, `index.html`, `style.css`, and `app.js`.
5. Open `index.html` from the ZIP on loopback and confirm add, complete, reopen, and filter behavior.
6. Send the package to a child repository reviewer with the note that it is a reviewable draft, not a publication certificate.

## Short Form

If the receiver only needs the shortest usable summary:

- `custom-gpt` exports authored instructions and starters for review.
- `agent-skill` exports a structurally valid skill draft.
- `workflow` exports a process draft plus machine-readable workflow JSON.
- `web-tool` exports a runnable local starter with record management behavior.
- All four include shared review files and must avoid secrets, private records, and publication claims.
