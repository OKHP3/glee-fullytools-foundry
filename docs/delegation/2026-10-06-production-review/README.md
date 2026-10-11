# Portable-foundation review and next-series work

Owner local date: October 6, 2026. Reviewed foundation:
`de092dbc4b70ebad7caad799a44ad785c7133252`, tree
`84c6436442e09257c0e90236691cb87d1627508f`.

The portable-capability authoring foundation is released through
[PR #25](https://github.com/OKHP3/glee-fullytools-foundry/pull/25).
It supports skill-first drafts, preserved legacy sources, derivation, provenance,
semantic-loss records and plugin/connector blueprints. The
[integration verification](../../application/portable-capability-verification.md)
records the local application, manifest, links and synthetic browser checks;
[both main Python jobs](https://github.com/OKHP3/glee-fullytools-foundry/actions/runs/37551170505)
passed at the reviewed foundation. Seven portable regressions passed again during
this review. Canon and snapshots are preserved.

The prior October 5 coordinator handoff is retained privately with SHA-256
`0bdafc7e372cb03661fecda8e540d5c0e34a1229f5126063b5b61658bca4a150`.
It described then-unresolved scope, access and publication. The owner's replacement
root guide and the [current workflow](../../application/portable-capabilities.md)
and [product contract](../../../products/README.md) govern this later review.
No separate named PRD was supplied. Comparison against that unavailable document
remains unperformed; P01 resolves the requirement artifact for the next series.
Historical GPT-only and other-product requirements do not override current owner
direction.

## Review and remaining product gaps

The [machine-readable review](equilibrium-review.json) records the five role
passes and their evidence limits. Independent prompts used separate contexts
with the same model and frozen source set. Their judgments are analytical;
agreement does not establish migrated-product quality or host compatibility.
No protected representative-user/native-host holdout ran.

| Pass | Finding and disposition |
| --- | --- |
| Evidence | Exact source and current requirement basis supported. Foundation approved with limits; final archive needs fresh receiving-surface evidence. |
| Outcome | Authoring and derivation foundation supported. Actual portfolio migration, native compatibility and unavailable-PRD conformance remain unperformed. |
| Safety and portability | Loopback, serving, canon and private-source boundaries retained. Preserve other assignments and separately authorize any new permissions. |
| Disruptor | No material source-level counterexample survived. A synthetic formatter test exposed arbitrary gate strings as non-authoritative; the P15 request condition and independent receipt checks were corrected. |
| Negotiator | Bounded foundation approved with limits. The strongest surviving objection is final publication/readback freshness. Archive deferred at review time until the coordinator supplies those exact receipts. |

The evidence-role deferral and the other foundation approvals address different
scopes. The decision follows exact source evidence and the explicit limits,
not a vote. The final closeout receipt can clear the archive conditions after
publication without changing unperformed product claims into successes.

The migration register remains `not-inventoried`. No child source has been
imported, no individual GPT has been behaviorally converted, and no native adapter
or executable connector has been released. Plugin/connector exports remain
non-installable blueprints. The 15 tasks below are proposals with prerequisite
gates, not dispatched implementation or evidence of completion.

Current source parity, app-connector authentication and Git-provider
authentication are separate claims. The direct Replit observation matched the
foundation SHA on HEAD, main and origin/main; an unrelated active branch retained
its modified validation test. Both Replit app connections require reauthentication.
No added OAuth permissions were granted. The
[handoff](session-handoff.md) defines final publication/readback gates and keeps
other assignments intact. Source publication does not authorize hosted workbench
operation, private-history disclosure or retirement of child repositories.

## Separately owned operational follow-ups

The receiving workspace has its own active queue. At the latest inspection,
PRs #26 through #29 remained open for presentation, export regressions and
manifest-workflow validation changes. Their writers retain ownership; this
review does not declare them merged or close their assignments. A later merge
requires their exact head, checks, review and receiving-host reconciliation.

Replit app-connector reauthentication and the separate GitHub provider reconnect
remain access follow-ups. The visible provider request adds project-read and
workflow-write permissions, which were not approved by this review. Git source
receipt verification does not resolve those authentication or permission states.

The presentation owner's latest receipt reports the repository Social preview
setting still awaiting upload of the published artwork. README/application
artwork is already source-published; configuring the GitHub setting remains
that assignment's separate UI step. The current Replit task is also checking
protection-alert access and delivery; its stated access limitation does not
establish missing branch protection or successful owner notification. These
follow-ups are not additional launched workers or hidden acceptance successes.

## Executable delegation

[next-series.json](next-series.json) is the task source. From this directory:

```text
python3 prepare-task.py validate
python3 prepare-task.py list
```

Prepare one task only after its coordinator has inspected the prerequisite
evidence and selected the source revision, product/host and isolated writer.
The following is a parameter template: replace the private paths and full SHA.

```text
python3 prepare-task.py prepare P01 --state PRIVATE-RECEIPTS.json --source-ref FULL-COMMIT-SHA --output-root PRIVATE-RESULTS
```

Private receipt structure:

```json
{"completed": {}, "gates": {"inventory_scope_selected": "Owner decision and inspected source evidence"}}
```

Later product/adapter tasks require the matching lowercase slug arguments shown
by `python3 prepare-task.py --help`. A fresh full commit is mandatory; a branch
name is insufficient. The output report directory must be outside the source
checkout. The helper prints structured agent arguments, launches nothing and
writes no state. Receipt strings require coordinator inspection; the script
checks mechanics rather than evidence truth or authority. Generated prompts
include the supplied receipt references and require independent inspection.
P15 requires a specific owner request for that separate audit repair; a
coordinator selection alone is insufficient.

Default recommendation is `gpt-6-luna` with low reasoning and a goal ceiling of
2,000,000 tokens per duty, three concurrent workers, no recursive spawning.
Expected task effort in the JSON excludes instruction/context overhead.
Verify the host goal counter, preserve its existing allocation, reserve closure
capacity, and escalate only on an observed acceptance failure. The coordinator
retains the actual dispatch/usage ledger privately and checks the series-wide
30-worker ceiling before any new worker. Preparing packets does not enforce
provider billing or purchase credits. No implementation task below was launched
by this review.

The helper passed valid-packet checks and eleven negative cases: duplicate IDs,
unknown dependencies, cycles, unsafe paths, excessive/zero resource bounds,
missing prerequisites, an in-repository private output path and a moving source
ref, plus an obsolete P15 selection without an explicit-request receipt.
The synthetic test launched no agent or external action. Receipt presence still
does not prove its truth.

## Detailed unfinished tasks

### P01: Confirm requirements and inventory migration sources

Identify a current owner-approved portable-capability PRD, or draft one from the current root/workflow/product contracts for review. Replace not-inventoried with an evidence-backed register. Identify the selected regional child sources, exact commits and trees, aliases, asset availability, licenses, visibility, active work and destination slugs. An empty register is not evidence of an empty portfolio.

- Prerequisites: none; selected-evidence gates: inventory_scope_selected.
- Owned source paths: `docs/application/portable-capability-prd.md`, `products/migration-map.json`.
- Closure evidence: Requirements have a recorded owner decision, intended users/outcomes, measurable acceptance and release boundaries. Every selected source has verified identity/revision/rights fields or explicit nulls and blockers; each belongs to Glee-fully; active assignments and recovery needs are recorded privately. No source import or public private-repository crosswalk.
- Deliverable: Sanitized register candidate and private inventory evidence.

### P02: Review rights and complete source history

Review the selected source's tracked assets and complete reachable history for rights, secrets, personal/client material, unsafe automation and missing source assets. Choose full-history subtree, separately reviewed sanitized snapshot, or blocked intake.

- Prerequisites: P01; selected-evidence gates: pilot_product_selected.
- Owned source paths: `products/<capability>/product.json`.
- Closure evidence: Exact commit/tree and rights decision cited; recovery refs/bundle verified outside public data; public-history suitability is explicit. A sanitized snapshot is never described as history-preserving. Do not publish private identifiers or source material merely to fill a field.
- Deliverable: Public-safe intake decision and private evidence.

### P03: Import one reviewed pilot source

Import only the selected, reviewed exact source revision into an absent product source prefix using its approved mode. Preserve history where authorized and compare source and destination trees, dotfiles, modes and links.

- Prerequisites: P02; selected-evidence gates: public_import_authorized, isolated_writer_owned.
- Owned source paths: `products/<capability>/source`, `products/<capability>/product.json`, `products/<capability>/README.md`, `products/migration-map.json`.
- Closure evidence: Source/destination tree comparison and import commit recorded; no nested Git repository; imported automation is inert source; no application serving allowlist changes; recovery verified and normal PR checks passed.
- Deliverable: Reviewable single-product import PR.

### P04: Map behavior and semantic loss

Map every selected source behavior, instruction, action, knowledge asset and example to a portable procedure, reference, script, adapter, explicit exclusion or blocker. Define focused capability boundaries and review losses with the owner.

- Prerequisites: P03; selected-evidence gates: isolated_writer_owned.
- Owned source paths: `products/<capability>/README.md`, `products/<capability>/product.json`.
- Closure evidence: No source behavior disappears silently; accepted losses, mitigations and decisive tests are explicit; legacy identities remain aliases; sealed canon and preserved source bytes remain unchanged.
- Deliverable: Behavior/loss map and authoring contract.

### P05: Author the first portable skill core

Author focused skill instructions and real resources from the accepted map. Define discovery triggers, inputs/outputs, tool needs, boundaries, failure recovery and verification without requiring an OpenAI account or provider manifest.

- Prerequisites: P04; selected-evidence gates: loss_map_accepted, isolated_writer_owned.
- Owned source paths: `products/<capability>/skills/<skill-name>`.
- Closure evidence: SKILL.md frontmatter and discovery description validate; references exist; examples use synthetic data; executable resources are reviewed; no implicit account connection, publication, tool execution or canonical registration.
- Deliverable: Versioned portable skill draft.

### P06: Build development evaluation fixtures

Specify expected-use, missing-input, ambiguous-trigger, platform-loss, permission-denial and adversarial-input cases for the pilot. Define baseline behavior and measurable acceptance without writing the unseen holdout for the optimizer.

- Prerequisites: P04; selected-evidence gates: isolated_writer_owned.
- Owned source paths: `products/<capability>/evals/development`.
- Closure evidence: Cases tie to source behaviors and failure boundaries; expected outputs are independently checkable; fixtures are synthetic; local/static checks are distinguished from behavior and host evidence.
- Deliverable: Development cases and evaluation protocol.

### P07: Run independent benchmark and unseen holdout

Freeze the skill hash, run representative with/without-skill comparisons, and independently supply protected or external holdout cases. Record failures, denominators, model/host versions, costs when exposed and shared-source limitations.

- Prerequisites: P05, P06; selected-evidence gates: independent_evaluator_owned, evaluation_environment_available.
- Owned source paths: `products/<capability>/evals/results`.
- Closure evidence: Observed results tied to exact artifact; optimizer has not seen protected cases; no uplift/compatibility claim from agreement alone; unsuccessful or unavailable runs remain failed, blocked or not-run. A changed skill hash expires affected evidence.
- Deliverable: Independent evaluation and release limits.

### P08: Define versioned skill composition

Declare which versioned skills are composed, their operation/input/output contracts, prerequisites, provenance, consent and recovery. Keep core methods separate from host packaging and tool providers.

- Prerequisites: P05; selected-evidence gates: composition_scope_selected, isolated_writer_owned.
- Owned source paths: `products/<capability>/product.json`, `products/<capability>/adapters/composition`.
- Closure evidence: Dependencies are pinned and resolvable; missing/unsupported tools produce bounded failures; no credentials or automatically installed dependencies; ownership prevents duplicate mutable cores across FoundRys or Skillz.
- Deliverable: Composition contract.

### P09: Implement one native host adapter

Read the selected host's current official format and implement its native discovery/packaging adapter. The current workbench ZIP is a design blueprint, not the native package.

- Prerequisites: P07, P08; selected-evidence gates: first_host_selected, existing_permissions_sufficient, isolated_writer_owned.
- Owned source paths: `products/<capability>/adapters/<first-host>`.
- Closure evidence: Native format validates on a named version; installation/discovery and expected-use/error behavior observed; exact package hash and permission scope recorded; unsupported capabilities stay explicit; new access requires its applicable approval.
- Deliverable: Tested first-host adapter candidate.

### P10: Evaluate portability on a second host

Implement/evaluate a separately declared adapter on another available host, including a non-OpenAI environment when making an account-independence claim. Reuse the exact portable core and document semantic loss.

- Prerequisites: P07, P08; selected-evidence gates: second_host_selected, existing_permissions_sufficient, isolated_writer_owned.
- Owned source paths: `products/<capability>/adapters/<second-host>`.
- Closure evidence: Named host/version, operations and failures observed on exact core/package hashes; no generic multi-host support claim; unavailable execution remains blocked or not-run rather than inferred from syntax.
- Deliverable: Second-host evidence matrix.

### P11: Implement a selected connector safely

Implement a selected connector from its blueprint with explicit operations, schemas, least-privilege consent, credential handling, denial, retry limits and recovery. Start with synthetic or test data where possible.

- Prerequisites: P08; selected-evidence gates: connector_scope_selected, approved_permissions_recorded, isolated_writer_owned.
- Owned source paths: `products/<capability>/adapters/<connector-host>`.
- Closure evidence: Allowed and denied operations, authentication expiry, malformed input and bounded retry tested; no real credentials in source/export/fixtures; external writes individually authorized; app/source/provider authentication states are separate.
- Deliverable: Connector implementation and boundary evidence.

### P12: Package and release an evaluated capability

Package pinned core/dependencies and separately validated native adapters. Record rights, hashes, tested hosts, known limitations, installation instructions and rollback/recovery. Include connector evidence only when P11 is selected and complete.

- Prerequisites: P07, P09, P10; selected-evidence gates: capability_release_authorized, isolated_writer_owned.
- Owned source paths: `products/<capability>/product.json`, `products/<capability>/README.md`, `products/<capability>/evals/release`, `products/migration-map.json`.
- Closure evidence: Fresh installation/upgrade/recovery succeeds on claimed hosts; exact release artifacts match tested hashes; normal PR/CI and owner release criteria satisfied; blueprint readiness is never presented as native compatibility or PME approval.
- Deliverable: Evidence-backed release candidate.

### P13: Validate the real authoring and migration journey

Observe a representative owner/builder complete intake, loss review, derivation, evidence recording and export. Extend keyboard/screen-reader/responsive testing where existing synthetic checks do not establish accessibility or usability.

- Prerequisites: P05, P06; selected-evidence gates: representative_user_test_selected, isolated_writer_owned.
- Owned source paths: `products/<capability>/evals/usability`.
- Closure evidence: Task success/failure, accessibility findings and evidence-reset behavior recorded on exact versions; no broad accessibility certification from viewport/overflow tests; implementation fixes receive separately owned paths and regression criteria.
- Deliverable: Observed journey findings and bounded repair packets.

### P14: Prepare consumer cutover and surface receipts

Identify consumer links, public wording, editorial records and receiving workspaces that need the selected released capability. Plan one editing authority and verify each adopted surface separately without automatically renaming, deleting or archiving child repositories.

- Prerequisites: P12; selected-evidence gates: consumer_cutover_selected.
- Owned source paths: `products/<capability>/README.md`, `products/<capability>/product.json`.
- Closure evidence: Exact GitHub source/artifact refs, receiving-host parity and editorial readbacks recorded; historical links/aliases remain recoverable; external destination writes and repository cutover have their own explicit authorization; no public workbench hosting added.
- Deliverable: Reviewed cutover packet and surface evidence.

### P15: Resolve the scoped protection-audit identity defect

Reproduce the canonical lowercase repository slug versus mixed-case constant/fixture mismatch diagnosed by T24. Repair identity handling without weakening branch protections, and retain meaningful wrong-repository/default-branch negatives.

- Prerequisites: none; selected-evidence gates: explicit_owner_audit_repair_requested, isolated_writer_owned.
- Owned source paths: `scripts/check-main-protection.py`, `scripts/tests/test_main_protection.py`.
- Closure evidence: Before editing, verify the explicit owner request for this separate audit repair; a coordinator selection string is insufficient. Canonical identity accepted; unrelated repository/default-branch still rejected; 403 or unavailable administration evidence remains incomplete rather than falsely absent protection. No GitHub settings mutation. Technology pin candidates and inherited-layout audits remain separate proposals requiring fresh scope and sources.
- Deliverable: Narrow audit-repair PR or no-change diagnosis.

## Learning and expiry

[The retry lessons](lessons.md) preserve the reasons for earlier failures and
the verified corrections. The [session handoff](session-handoff.md) records
source/host boundaries and the next action. Reopen affected conclusions when
the core changes, a selected requirement changes, a host claim is added or a new
defect appears. Refresh version candidates against official publishers when
their own upgrade scope is selected. Historical drift reports are not current
release recommendations.
