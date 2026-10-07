# Current state and maturation roadmap

## September 27, 2026 direction update

The [portable capability workflow](portable-capabilities.md) supersedes the earlier GPT-first product focus. The app adds derivation and plugin/connector blueprints. The dated assessments below remain historical; they do not establish current host compatibility or subtree-import completion.


## September 8 closeout update

The assessment and staged roadmap below preserve the original baseline and
proposals. The application and all 26 coop-pertition deliverables are now merged.
The current service suite passes 72 tests; backup-test connection cleanup,
TRACE/CONNECT JSON errors and browser-QA unavailable-prerequisite exit statuses
were corrected. See the [closeout audit](../delegation/2026-09-07-coop-pertition/cleanup-2026-09-08.md#follow-up-closeout-verification)
for source revisions, validation, delivered proposals and the unresolved worker-file
preservation incident. Replit parity and later maturation stages remain unverified.


Current visibility update, September 7, 2026: the owner confirms all three
FoundRy repositories are intentionally public, corroborated by GitHub API
metadata. This application remains locally run; public source availability does
not create a hosted service or publish its ignored SQLite working records.


Assessment date: September 7, 2026. Application baseline: `a2eebe88eb46de0537a3fc225041433a9ef54c08`.
This assessment separates implemented behavior, recorded verification and proposed work.
It is not a formal maturity certification or a commitment to a delivery date.

## September 8, 2026 closeout update

The assessment and staged roadmap below preserve the original baseline and
proposals. The application and all 26 coop-pertition deliverables are now merged.
The current service suite passes 72 tests; backup-test connection cleanup,
TRACE/CONNECT JSON errors and browser-QA unavailable-prerequisite exit statuses
were corrected. See the [closeout audit](../delegation/2026-09-07-coop-pertition/cleanup-2026-09-08.md#follow-up-closeout-verification)
for source revisions, validation, delivered proposals and the unresolved worker-file
preservation incident. Replit parity and later maturation stages remain unverified.


Current visibility update, September 7, 2026: the owner confirms all three
FoundRy repositories are intentionally public, corroborated by GitHub API
metadata. This application remains locally run; public source availability does
not create a hosted service or publish its ignored SQLite working records.


Assessment date: September 7, 2026. Application baseline: `a2eebe88eb46de0537a3fc225041433a9ef54c08`.
This assessment separates implemented behavior, recorded verification and proposed work.
It is not a formal maturity certification or a commitment to a delivery date.

## Assessment

Glee-fully FoundRy is a functional first release for an owner working locally:
design a tool, record its requirements and acceptance evidence, and export an
inspectable package. It is ready for a bounded owner pilot. Wider release readiness
has not been established. The largest remaining gap against the broader
systems-building ambition is the transition from an authored specification to a
domain-specific implementation and independently observed evaluation.

The application and mentoring clarification are committed on
`codex/foundry-application-2026-09-07` in [PR #5](https://github.com/OKHP3/Glee-fullyTools-FoundRy/pull/5).
At this assessment, the PR is open and ready for review, not merged into main.
The [application CI run](https://github.com/OKHP3/Glee-fullyTools-FoundRy/actions/runs/34139527218)
passed on the baseline above. Application CI success does not establish that
every independent review has finished.

## Place in the universe

OverKill Hill is the centroid and common baseline for the distinct regional sites.
Its intentionally public Found-Ry provides the mentor pattern for AskJamie and
Glee-fully FoundRys. Mentoring is reciprocal: a useful pattern may originate in
any of the three and flow to either sibling. Shared principles can be reconciled
at OverKill Hill, and reusable Agent Skills distributed through Skillz.

This application's identity, projects and private records belong to Glee-fully.
Mentoring is currently represented in guidance, metadata and the universe view;
there is no implemented cross-FoundRy synchronization protocol or shared database.
The [research report](../research/okhp3-universe-2026-09-07/report-source.md) and
[claim ledger](../research/okhp3-universe-2026-09-07/claim-ledger.md) preserve source
evidence, owner clarification and access limits.

## What works now

| Area | Implemented behavior | Practical boundary |
|---|---|---|
| Project authoring | Four templates: Custom GPT, Agent Skill, workflow and web tool; editable brief, audience, inputs, outputs, constraints, instructions, components and acceptance cases | Template content requires the builder's domain knowledge |
| Durable working records | SQLite persistence, revision conflict detection, searchable library, archive/restore, immutable revision snapshots and activity history | Pre-feature databases expose only a current-state baseline; workspace backup still restores current state plus metadata rather than historical snapshot bodies |
| Evaluation | Expected and actual results with not-run/pass/fail status; missing information and evidence block review readiness | Results are entered by the user; the app does not execute the tests or verify that the described observation happened |
| Stale evidence | Material specification, attached-skill or acceptance-contract changes reset earlier test evidence | This protects the working record, not the quality of the test design |
| References | Five allowlisted local reference documents and seven public Skillz references pinned to a full revision | Prompts and skills are neither installed nor executed; this is a curated shelf, not the full live catalog |
| Portability | JSON import/export, Markdown and ZIP; imports receive a fresh identity and reset evidence | Project JSON does not include the full database or activity history |
| Interface | Glee-fully styling, explicit errors, unsaved-change handling, responsive layout and the seven-element universe view | Accessibility and browser coverage remain bounded by the verification record |

A Custom GPT package supplies authored instructions and starter material for review
and platform setup. An Agent Skill package supplies a structurally valid
`SKILL.md`; usefulness and behavioral quality still need evaluation. A workflow
package describes the process in Markdown and JSON; it is not a workflow execution
engine. A web-tool package includes a functioning record-management starter with
add, complete, reopen, filtering and browser persistence, together with the
project specification. The starter must be adapted to meet domain-specific
requirements.

## Architecture and operation

The browser interface is static HTML, CSS and JavaScript. A Python 3.11+ standard
library service handles the JSON API, validation, SQLite and package generation.
No package installation, frontend build, AI-provider credential or paid model call
is required. Start with `python3 -m app.server` from this branch's repository root.

The service binds to loopback. Host/origin checks, bounded request bodies, a
content security policy and fixed source/static allowlists constrain its exposure.
These are implemented controls, not a completed security certification. Public or
multiuser hosting needs its own architecture, authentication and operations work.

Working data lives in ignored `.foundry-data/`; each checkout/worktree has its own
default data directory. A full backup requires stopping the service and copying
that directory. Importing a project JSON makes a new draft and resets evidence,
so it is a portability operation rather than an exact full-state restore.

Existing canon, governance, snapshots and seals remain unchanged from the
integration baseline. Application drafts do not register clauses, alter canon,
execute PromptChain stages or confer PME approval. The reference shelf makes
selected source material readable; it does not automate the entire historical
FoundRy methodology. See the [operating guide](README.md) and
[API contract](api-contract.md).

## Evidence and remaining uncertainty

Fifteen automated service tests passed locally and in GitHub Actions. They cover
persistence, optimistic revisions, validation, imports, archive preservation,
request/source boundaries, evidence invalidation and the four export kinds.
JavaScript syntax and whitespace checks passed.

Recorded browser checks exercised creation, editing, saving, evidence/readiness,
JSON download/import, archive/restore, Skillz attachment, source reading, reload
persistence, invalid-input recovery and narrow layout. The exported web starter
was separately executed and its record lifecycle observed. These were session
checks; no committed automated browser regression suite exists yet.

The [verification record](verification.md) states the exact scope. Full
assistive-technology testing, cross-browser coverage, concurrency/stress testing,
automated backup recovery, production hosting and external GPT/skill behavior
remain unverified. Replit workspace visibility was observed through a parallel
authenticated coordinator; exact commit parity and application deployment there
were not established.

## Subsequent review follow-up

The committed assessment was followed by corrections to readiness messages,
browser ID fallback, inline-HTML escaping across Markdown exports, retained
unavailable Skillz references and CI coverage of the reference shelf. The local
suite now has 17 passing tests, including all-kind Markdown export checks and
retired-reference edit/archive/restore behavior. See the PR for the latest commit
and CI result; the baseline CI link above remains historical evidence.

## Recommended order of maturation

The following stages are proposals. Advance on evidence of useful outcomes, not
feature count. No external migration, deployment or paid integration is authorized
by this roadmap itself.

| Stage | Work | Evidence needed to advance |
|---|---|---|
| 1. Establish the release baseline | Finish PR review, address concrete findings, merge through the normal repository process and identify a tested release commit; record how to launch and recover data | Reviewed main commit with green application checks; successful clean-start and full backup/restore exercise |
| 2. Run an owner pilot | Build one real Glee-fully deliverable of each supported kind; start with the kind most likely to be reused; record missing inputs, confusing steps and manual rework | Four reviewed packages; the intended output of each tested in its actual target environment, with observed results and a prioritized defect list |
| 3. Strengthen reliability and evidence | Automate the highest-value browser journeys; extend snapshot recovery through backup rehearsal; define broader database schema migrations; preserve richer evaluation provenance | Regression checks detect broken save/import/export/restore flows; a prior version and an older data fixture restore without loss; every evaluation identifies the tested revision and environment |
| 4. Make mentoring operational | Define a small versioned pattern contract with source revision, regional overrides, compatibility notes and feedback route; compare practices across the three FoundRys; publish reusable approved skills through Skillz | One useful pattern adopted across two FoundRys with explicit differences, then improved through feedback without copying private projects |
| 5. Deepen each builder | Add kind-specific guidance, domain templates, real target-environment evaluation and a reviewable export-to-child-repository path; map selected PromptChain/PulseBook requirements into explicit checks | A real project progresses from brief through implementation and target evaluation to a reviewable child-repository PR; incomplete work remains visibly incomplete |
| 6. Add bounded assistance where justified | If pilot evidence supports it, add an optional provider adapter, explicit run scope, budget limits, provenance and isolated execution; retain manual/offline authoring | Each run records input/output, model, actual cost when available and checks; cancellation/failure preserves work; measured reduction in rework justifies the expense |
| 7. Choose a hosting model if needed | Compare continued local operation with a private hosted service; design identity, authorization, secrets, data isolation, backups, observability and release/rollback before deployment | Verified access and restore tests, documented operations, and an owner-approved deployment route with confirmed source parity |

The immediate recommendation is stages 1 and 2. Actual owner projects will reveal
whether the next investment should be stronger GPT guidance, richer skills,
workflow execution or broader application generation. Introducing a large agent
or hosting stack before that evidence would add operational work without proving
the most valuable building workflow.

## Cost-aware delivery practice

Keep work in small, reviewable changes with explicit acceptance criteria and
disjoint branch/worktree ownership. Use lower-cost models for bounded research,
documentation and straightforward implementation; use stronger reasoning for
architecture, ambiguous validation or integration defects when needed. Escalate
on a concrete failure or unresolved decision rather than repeatedly retrying an
undersized model. Reuse source captures and test evidence when the underlying
revision has not changed.

Track completed useful artifacts, owner rework, cost per accepted artifact when
available, defects found after export and recovery success. These are proposed
pilot measures, not measurements already collected. Exact token spend for the
initial delegated build was unavailable, so no savings percentage is claimed.
