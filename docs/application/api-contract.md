# FoundRy application contract v1

The owner-authorized application lives under `app/`. Python 3.11+ standard library, SQLite durable working records, vanilla JS/CSS frontend. Start from root with `python3 -m app.server`; default bind 127.0.0.1:8765, `--port` supports another local port, `--data-dir` supports a test/private data directory. No runtime package installation required. Draft projects do not write canon. All existing canon and seals are preserved unchanged. The service exposes only its static frontend and explicitly allowlisted research/resources, never the repository root.

## JSON project schema

```
{id: UUID, schemaVersion: 1, revision: integer, name: string,
 kind: "custom-gpt"|"agent-skill"|"plugin"|"connector"|"workflow"|"web-tool",
 owner: string, version: string, purpose: string, description: string,
 audience: string, inputs: string, outputs: string,
 constraints: string, instructions: string,
 sourceProvenance?: string, capabilityMap?: string, semanticLoss?: string,
 targetHosts?: string, integrationContract?: string,
 components: [{id: string, name: string, purpose: string, dependsOn: [component id]}],
 tests: [{id: string, name: string, expected: string, actual: string,
          status: "not-run"|"pass"|"fail"}],
 skillIds: [string], status: "draft"|"archived",
 createdAt: ISO timestamp, updatedAt: ISO timestamp}
```

Server assigns IDs, revisions and timestamps. PUT requires current `revision`, returns 409 on conflict. Imports and duplicates get a fresh ID and reset evaluation evidence to not-run, keeping source identity in history. Unknown keys, malformed nested objects, oversized text, invalid enum values and missing references are rejected. `name` and `kind` required to create; other fields can be empty while drafting. All user text is untrusted and rendered as text. Component IDs unique, dependencies must exist, and cycles are flagged by validation. A pass without actual evidence is never a pass. Material specification, attached-skill or acceptance-contract changes reset evidence; save the specification before recording a new test run. No claim of automatic behavioral validation. Updates may retain unavailable skill IDs already stored on that project, so a shelf change cannot block editing, archive or restore. The UI shows those IDs for optional removal; readiness still fails until references are resolved. Creation, import and newly attached IDs require current registered references.

Optional portability strings are bounded by the existing 100,000-character text
limit. Missing extensions stay absent in old records and immutable snapshots,
preserving v1 backup bytes and digests. New fields require this version of the
app; older servers do not accept them. Skill records carrying the portability
extension (including derived records) require provenance,
capability mapping, loss review and target-host notes before review; plugin and
connector records additionally require an integration contract. Checks measure
presence, not semantic truth. All five fields participate in evidence invalidation.
Omitted optional fields on PUT retain their saved values; send an empty string to clear.

## Endpoints

All JSON errors: `{error: string}` with correct 4xx/5xx, including unsupported TRACE and CONNECT requests. JSON body <= 1 MB. Mutations require `Content-Type: application/json`, header `X-Foundry-Request: 1`, validated Host and same Origin if present. Bind only loopback. No CORS. Foreign hosts/origins rejected. HTML CSP restricts all requests/assets to self and outbound links use safe HTTPS URLs.

- GET `/api/bootstrap`: `{templates: [{id, name, description, project: partialProject}], skills: [{id,name,description,url,sourcePath,revision}], sources: [{id,title,path,url,description}], universe: [{id,name,region,role,url,shared: boolean}]}`. Templates expose six kinds, with Agent Skill first and legacy GPT source retained for migration. Coordinator supplies optional `app/data/skills.json`; engine handles its absence as an empty list during development. Sources allowlist includes the portable-capability and subtree guides, PromptChain, GPT scaffold, PulseBook current, brand vernacular and canon overview. These are local read-only reference text, no automatic execution/adoption.
- GET `/api/projects`: `{projects: [project]}` includes archives.
- POST `/api/projects`: partial project, returns complete project, 201.
- GET `/api/projects/{id}`: complete project.
- PUT `/api/projects/{id}`: editable project plus revision, returns complete updated project.
- POST `/api/projects/{id}/duplicate`: `{revision: integer}` creates a fresh draft identity with reset evidence.
- POST `/api/projects/{id}/derive`: `{revision: positive integer, targetKind: string}` returns a new draft, 201. Routes: `custom-gpt -> agent-skill`, `agent-skill -> plugin|connector`. Preserves source and lineage, resets passes, and adds three migration cases. Unsupported routes return 400; stale revision returns 409 without writes. Authored instructions are copied for review, not automatically rewritten. Existing unavailable skill references are retained and block readiness until resolved.
- DELETE `/api/projects/{id}`: `{confirm: true, revision: integer}` permanently removes the project and its revision trail. The confirmation is required.
- GET `/api/projects/{id}/validation`: `{readyForReview: boolean, checks: [{id,label,status: "pass"|"fail"|"warning",detail}], summary: string}`. Check purpose, audience, interface, constraints, instructions, components/dependencies, acceptance evidence, and attached skill provenance. Review-ready does not imply PME or publication-ready.
- GET `/api/projects/{id}/history`: `{history:[{revision,at,action,summary,restorable,baseline}]}`. `restorable` is true only for a present, digest-valid, schema-valid snapshot. `baseline` identifies a migration snapshot for the current state of a pre-feature database; earlier metadata remains non-restorable.
- POST `/api/projects/{id}/restore`: `{sourceRevision: integer, currentRevision: integer}` creates a new revision from a verified immutable snapshot, preserves project identity and original creation time, sets status to `draft`, and resets all evaluation evidence. A stale current revision returns 409; an absent or invalid source is rejected without changing the project.
- GET `/api/projects/{id}/package`: inspectable `{manifest, files}` response for the exact generated text members.
- GET `/api/projects/{id}/export?format=json|markdown|zip`: attachment. JSON is complete project. ZIP contains `manifest.json`, project.json, README.md, specification.md, evaluation.md, skill-references.md, build.md, handoff.md and type-specific files. Custom GPT: instructions.md/starters.md; agent skill: SKILL.md with a safe name and bounded description plus extraction guidance; plugin/connector: adapter-blueprint.json and adapter.md, explicitly non-installable with unverified compatibility; workflow: workflow.md and workflow.json; web tool: runnable HTML/CSS/JS starter with persisted record entry, completion and filtering. User fields must be safely encoded and cannot inject executable HTML/JS. Packages contain draft status and observed validation results, never fabricated certification, secrets, copied canon or claims of deployment. ZIP exports are checked as round-trip package contracts, including deterministic shared-file content and target-specific members for legacy export kinds, with additional conversion and adapter contract tests.
- POST `/api/import`: `{project: object}` returns new project, 201. Invalid version rejects without changing existing projects.
- GET `/api/workspace/backup`: downloads a complete `glee-fully-foundry-workspace` JSON snapshot containing projects, all revision history, and a `snapshots` map. Each snapshot record contains `revision`, `capturedAt`, `action`, `schemaVersion`, the exact canonical project JSON `data` string, and its `sha256` digest.
- POST `/api/workspace/restore`: `{backup, confirm: true, mode: "replace"}` validates every project, history entry, and supplied immutable snapshot before atomically replacing the local workspace. Snapshot identity, schema, canonical bytes, and digest must match. A malformed backup leaves current data unchanged. Backups from before snapshot export may omit `snapshots`; those retain the legacy current-state migration-baseline behavior and do not invent historical content.
- GET `/api/sources/{id}`: `{id,title,content,path,url}` from fixed allowlist; no arbitrary path or network fetching.
- GET `/api/health`: `{status:"ok"}`.

## Frontend ownership and behavior

Frontend task owns only `app/static/index.html`, `app/static/app.js`, `app/static/styles.css` and optional frontend-only local assets. Engine owns Python and tests. Coordinator owns `app/data/skills.json`, documentation and repository metadata. Project navigation must warn before discarding unsaved edits, preserve text on errors, and display conflict errors explicitly. Save before validation/export if edited, or clearly explain that actions use the saved revision. Empty states provide useful next actions; seed examples only on explicit user action. JSON import is visible, archives recoverable, external skill links optional. UI must support editing components and acceptance evidence without raw JSON editing. A three-overlapping-ring universe view positions AskJamie left, OverKill center, Glee-fully right; Skillz shared and OverKill Found-Ry exclusively central. Optional skills do not block readiness. Seven element details remain accessible on narrow screens and without diagram interpretation.
