# Glee-fully FoundRy application

This public-source, locally run workspace helps you convert GPT source material into
portable Agent Skills and design plugins and connectors with separate host adapters. Canon remains in the existing ledgers; application projects are drafts
with their own revision history. No draft is automatically registered or PME-approved.

See the [current-state assessment and maturation roadmap](current-state-and-maturation.md)
for implemented capabilities, evidence limits and the proposed next stages.

## Run

Use Python 3.11 or newer. From the repository root:

```bash
python3 -m app.server
```

Open <http://127.0.0.1:8765>. There is no install or build step and no paid model
or external service is required. To use another local port:

```bash
python3 -m app.server --port 8766
```

Stop with Ctrl+C. The application intentionally binds only to loopback. It is
not an authenticated multiuser service or a public deployment target. Do not
reverse-proxy it onto a network or serve the repository root.

## Make a useful package

1. Start with an Agent Skill, plugin blueprint or connector blueprint. Use Legacy GPT
   source to begin a conversion; workflow and web-tool drafts remain available.
2. Record the owner, version, purpose, audience, inputs, outputs, constraints and instructions.
3. Define components and their dependencies. Give each acceptance case a clear
   expected result, then record what you actually observed when testing it.
4. Attach relevant pinned Skillz references when useful. These are optional source
   links, not automatically installed or executed agents.
5. Save and review the validation report. Unrun or failed cases are not evidence
   of readiness. Material specification changes invalidate earlier test results.
6. Inspect the generated package files and manifest, then download JSON for portable
   project import, Markdown for review, or a ZIP package.

The web-tool ZIP contains a runnable record-management starter with add, complete,
reopen and filter behavior. It also contains your complete specification and
handoff material. It is a starting implementation to adapt, not an AI-generated
implementation of arbitrary requirements. Custom GPT/Skill/workflow exports are
reviewable authored packages; platform publication remains a separate action.

Import and duplicate create a new project identity, preserve the source identity
in history, and reset evaluation results to unrun. Archive hides completed or
paused drafts from active work while keeping them recoverable.

## Convert and compose

Follow [the portable capability workflow](portable-capabilities.md). **Conversion &
portability** records source inventory, capability mappings, semantic loss, target
hosts and integration requirements. Derive a skill from a legacy GPT, then derive
plugin or connector blueprints from that skill. Derivation preserves the source
and resets acceptance evidence. Plugin/connector ZIPs contain design contracts,
not installed tools or native host packages. Material portability edits reset passes.

[Product subtrees](../../products/README.md) define the child-repository consolidation
path. Imports and external repository changes are separate from application export.

## Persistence, lifecycle and backup

By default, private SQLite working data is stored in `.foundry-data/`, which is
ignored by Git. It persists across browser reloads and server restarts. Worktree
copies have independent data folders. Use **Backup workspace** to download the
projects and complete revision trails as one validated JSON snapshot. Use
**Restore workspace** only after confirming replacement; the service validates
every project and history entry before changing anything and leaves current data
unchanged when the backup is malformed. The raw SQLite folder remains a useful
private disaster-recovery copy, but it is not exposed by the application.

Delete requires explicit confirmation and removes the saved project and its
revision trail. Make a workspace backup first when deletion may need to be
reversed.

`--data-dir` accepts a private directory of your choice. Keep it out of source
control. JSON exports and workspace backups may contain your authored private
information; choose where to share them. The app makes no outbound model
requests and has no telemetry.

Revisions prevent a stale tab from silently overwriting a newer save. If a save
conflicts, preserve your unsaved text, reopen the current project and reconcile
it. Validation and exports refer to saved records.

## Reference material and boundaries

The reference shelf exposes a fixed allowlist of the portable-capability and subtree
guides, PromptChain, scaffold, current
PulseBook, vernacular and canon-overview text. It cannot browse arbitrary files.
It does not execute those prompts or modify their sources. Historical text may
retain the older cross-FoundRy model; the current universe boundary is explained
in the [research report](../research/okhp3-universe-2026-09-07/report.html).

`app/data/skills.json` lists selected public Skillz distribution contracts with
full commit revisions and source paths. Refresh it only after verifying each
new target file; do not treat catalog generation timestamps as behavioral proof.
This is a curated reference shelf, not a replacement catalog or live sync.
If a reference becomes unavailable, its existing project remains editable and
archivable. The shelf displays that ID for optional removal, and readiness names
it as unresolved. Newly attached references must exist in the current shelf.

The API contract is in [api-contract.md](api-contract.md). There are no endpoints
for executing code, fetching arbitrary URLs, changing canon, sending messages,
publishing repositories or invoking AI providers.

## Verify

```bash
python3 -m unittest discover -s app/tests -v
python3 -m py_compile app/server.py
node --check app/static/app.js
python3 scripts/verify-foundry-backup.py
python3 scripts/foundry-release-check.py
git diff --check
```

The service tests cover persistence, validation, request boundaries, lifecycle
recovery and exported packages. The dated [verification record](verification.md)
distinguishes these checks from browser behavior and external-service evidence.
The browser journey is `scripts/foundry-authoring-qa.mjs`; if its driver or
browser is unavailable it reports **NOT RUN** rather than claiming browser proof.
Historical maintenance audits have documented baseline mismatches and do not
establish application health.

The release gate is a local check only. It does not publish the app, create a
deployment, upload project data, or authorize publication of a generated
capability. Any hosted builder or public Pages release requires a separate,
owner-approved task and architecture decision.
