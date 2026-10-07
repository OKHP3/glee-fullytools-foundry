# governance/ — Directives, Rules, and Cathedral Architecture

The September 27, 2026 owner direction supersedes GPT-only production scope. See [the current product workflow](../docs/application/portable-capabilities.md). Existing directives and sealed ledgers retain their content and lineage; conversion drafts do not imply canon registration.

> The **law layer** of the Glee-fully ecosystem. This folder contains the authoritative
> governance directives that all GPTs, builders, and agents must follow, plus the
> master architectural blueprint (the Operator's Cathedral Layout) that defines how
> every component of the system fits together.

---

## Purpose

`governance/` is the enforcement layer that sits above every other folder in this repo.
While `canon/` stores the data, `governance/` defines the rules for how that data is
created, maintained, and enforced. These directives override GPT-local logic, legacy
schema, and any ad-hoc decisions made during a build session.

This folder answers the question: *what are the inviolable rules of this ecosystem?*

---

## Files

| File | Purpose | Scope |
|------|---------|-------|
| [`glee-fully-project-governance-v3-0-1.md`](glee-fully-project-governance-v3-0-1.md) | Primary governance directive — ledger routing, suffix law, clause lifecycle, overlay enforcement, output signature requirements | All Projects within the Glee-fully ecosystem |
| [`glee-fully-project-instructions.md`](glee-fully-project-instructions.md) | Project-level operating instructions — how to run a Glee-fully project session | Operators and AI agents |
| [`00-glee-fully-strategy-center-instructions.md`](00-glee-fully-strategy-center-instructions.md) | Strategy Center GPT instructions — the meta-governance entity that coordinates ecosystem-level decision making | Strategy Center GPT |
| [`operators-cathedral-layout.md`](operators-cathedral-layout.md) | Master architectural reference (~20,000 lines) — the complete structural blueprint of every section, block, tone layer, and governance rule across the entire ecosystem | All builders and entities |

---

## Document Summaries

### Governance Directive v3.0.1 (`glee-fully-project-governance-v3-0-1.md`)

The constitutional document of the Glee-fully ecosystem. Canonically sealed
(`::CanonSeal[GleeCoreDirective.v3.0.1.locked]::`). Contains:

**Ledger Routing Rules** — which types of content go to which of the 9 dataLedger files.
Every clause, entity, drift event, and parameter must route to its correct ledger.

**Suffix Compliance Law** — only Tools, Tool-ettes, Functions, and Function-ettes may
use the `-R` suffix. Glee-fully branded GPTs are exempt from `-R` and `-Ry` usage (those
are reserved for OverKill Hill P³ and The GPT Found-Ry). Violators are retired to archive.

**Clause Lifecycle Flow** — the canonical path from `ideation_v3.md` → registry/persona/
parameters → `narrative_v3.md` → `archive_v3.md`. Rehydration via `hydration_v3.md` is
the only permitted re-entry point.

**Output Signature Requirement** — all canonical outputs must carry a `!CLAUSE` ID
declared in `registry_v3.md`. No anonymous or unregistered output is canon-valid.

**Overlay and Persona Enforcement** — untagged threads default to `GleeTone.A1`
(uplifting, whimsical, clear, articulate). Drift events are logged via `!DRIFT_EVENT`.

**Runtime Preservation** — no GPT may simulate memory. All continuity must flow through
`dataledger-hydration-v3.md`. Prompt-embedded toggles are prohibited.

**Project Initialization Protocol** — new Projects must declare a PhaseScope, register
all logic in the registry, declare overlays, and use hydration for continuity.

### Operator's Cathedral Layout (`operators-cathedral-layout.md`)

At ~20,000 lines, this is the master blueprint of the entire ecosystem. It is the
single most comprehensive reference in the repository, covering every structural
component, design decision, and architectural rule. It functions as:

- A **structural map** of every GPT role (Toolbox, Tools, Tool-ettes, Functions, Function-ettes)
- A **builder's codex** — how to construct each type of entity from first principles
- A **tone taxonomy** — all overlay types, their rules, and their application contexts
- A **metadata schema reference** — all YAML blocks, tags, and clause formats
- A **design philosophy document** — why the cathedral metaphor governs all decisions
- A **canonical reference** for the PromptChain and PulseBook systems

This document is intentionally comprehensive and is designed to be referenced section
by section, not read end-to-end. Use keyword search to navigate it.

---

## Key Governance Principles

| Principle | Rule |
|-----------|------|
| **Expansion-Only Discipline** | Never remove or simplify content. Only elaborate, deepen, and layer. |
| **Ledger Authority** | The 9 `dataledger_*_v3.md` files in `canon/` override all other sources |
| **CanonSeal Inviolability** | `::CanonSeal[...]::` tags must never be altered or removed |
| **No Prompt-Local Memory** | Runtime state is never stored in prompts — hydration only |
| **Tone Enforcement** | All GPTs must declare an overlay; untagged output defaults to GleeTone.A1 |
| **Registration Requirement** | Every entity must be declared in `dataledger-registry-v3.md` before deployment |
| **Forward-Only Lifecycle** | Clauses move ideation → registry → narrative → archive; never backwards except via hydration |

---

## Canonical Personas Defined Here

| Persona | ID | Role |
|---------|-----|------|
| **GleeTone.A1** | Default overlay | Uplifting, whimsical, clear, articulate — fallback for all untagged threads |
| **JoyWarden.Core** | Tone enforcer | Warm but strict — applies to all untagged or drifted clauses |

---

## Authority Chain

```
OKHP3/OverKill-Hill-FoundRy   (parent governance — root authority)
        |
        v
governance/  (THIS FOLDER — Glee-fully ecosystem authority)
        |
        v
canon/dataledger_*_v3.md      (data layer — governed by these directives)
        |
        v
All 40+ Glee-fully GPTs       (entities — governed by canon)
```

---

## Who Uses This Folder

| Actor | How They Use It |
|-------|----------------|
| **Operators / Builders** | Reference governance directive before starting any build session |
| **AI agents** | Read `glee-fully-project-governance-v3-0-1.md` to understand current rules before taking action |
| **Strategy Center GPT** | Executes using `00-glee-fully-strategy-center-instructions.md` as system instructions |
| **PromptChain** | PROMPT00 (Ignition Ritual) invokes governance clauses at chain initialization |
| **Cathedral Layout** | Referenced throughout the PromptChain and evaluation process |

---

## Relationship to Other Folders

```
governance/    <-- enforces rules on  --> canon/ (data must comply with directives)
governance/    <-- defines rules for  --> prompts/ (PromptChain must apply governance clauses)
governance/    <-- informs            --> evaluation/ (PulseBook checks compliance with these rules)
governance/    <-- described in       --> docs/ (technical overview explains the governance system)
governance/    <-- captured in        --> snapshots/ (cathedral layout is snapshotted over time)
```
