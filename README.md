# Glee-fullyTools-FoundRy

**A publicly visible, proprietary, locally run workbench for portable Agent Skills, plugins and connectors.**

The September 27, 2026 owner direction makes skills the primary product and existing
Custom GPTs conversion sources. Preserve the capability, then adapt its packaging
to each agent host. The application keeps durable drafts alongside the preserved
canon, prompts, templates and evaluation material.

```bash
python3 -m app.server
```

Open `http://127.0.0.1:8765`. Python 3.11 or newer is required; no package
installation or build step is needed. See the [application guide](docs/application/README.md)
for setup, persistence, backups, validation and limitations.

Start an Agent Skill, plugin blueprint, connector blueprint, legacy GPT source,
workflow or web-tool project; record its owner,
version and contract; define components and acceptance cases; attach pinned Skillz
references; save evaluation evidence; inspect the generated manifest and files;
and export Markdown, JSON or a ZIP package. The workbench also supports duplicate,
archive/restore, confirmed delete, and validated whole-workspace backup/restore.
Web-tool packages include a runnable record-management starter and the authored
specification. Review-ready is a working-record check, not PME certification or
permission to publish.

Source visibility does not grant unrestricted reuse. The proprietary terms in
[LICENSE.md](LICENSE.md) govern use; its historical private-repository label does not describe current GitHub visibility. Private workbench records remain local.

## Current product workflow

**Legacy GPT source -> portable skills -> skill composition -> tested host adapters.**

The app can derive a skill draft from a GPT, then plugin or connector blueprints
from a skill. Each derivation preserves its source and resets evaluation evidence.
Use the **Conversion & portability** workspace to map source behavior, semantic
loss, target hosts, tools and permissions. Native adapters still require
implementation and host-specific tests; the blueprints are not installable packages.

Read the [portable capability workflow](docs/application/portable-capabilities.md)
and [product subtree migration contract](products/README.md). Former child projects
will consolidate under `products/<capability-slug>/`, with preserved source history,
portable skills and separate host adapters. No child import or remote cutover has
been performed by this initial adaptation. OverKill and AskJamie retain separate
regional ownership; this change adapts Glee-fully's workbench only.

## Working across agent hosts

Use the [collaboration protocol](docs/agent-collaboration.md) to coordinate
ChatGPT/Codex, Replit, Claude and GitHub Copilot with clear task ownership,
compact handoffs and validation evidence. Cost efficiency takes priority over
speed. `AGENTS.md` remains the canonical repository guide.

## Universe and ownership

AskJamie sits to the left, Glee-fully to the right, and OverKill at the connective
center. **Skillz is shared by all three. Each region has its own FoundRy.**
OverKill Hill provides the common baseline. OverKill Found-Ry belongs to OverKill
and provides a mentoring pattern; each sibling FoundRy can contribute improvements
to it or to another sibling. All three FoundRy repositories are intentionally public, as confirmed by the owner
on September 7, 2026 and verified against GitHub metadata. Mentoring does
not imply a shared runtime, database or permission to share private records.
Historical parent references remain lineage evidence.

| Element | Role |
|---|---|
| [OverKill Hill](https://overkillhill.com/) | Universe context, methodology and public research |
| [Skillz](https://okhp3.github.io/skillz/) | Shared portable Agent Skill catalog |
| [OverKill Found-Ry](https://okhp3.github.io/OverKill-Hill-FoundRy/) | OverKill's own builder |
| [AskJamie](https://askjamie.bot/) and [AskJamie FoundRy](https://github.com/OKHP3/AskJamie-FoundRy) | Interpretive experiences and their regional workbench |
| [Glee-fully Tools](https://glee-fully.tools/) | Public catalog and routing hub |
| **Glee-fullyTools-FoundRy** | Glee-fully's application and canonical fabrication workspace |

Read the [seven-element research report](docs/research/okhp3-universe-2026-09-07/report.html)
and [implementation plan](docs/application/implementation-plan.md) for evidence,
contradictions and verification boundaries.

## Canonical workbench reference

The following describes the preserved GPT-focused source workflow. It is historical
and canonical working material, not a claim that the application automatically
executes every ritual or that all external GPTs are deployed. Application drafts
are separate from canon; promotion remains an explicit governed activity.

## Preserved GPT-era product model

Glee-fully Personalizable Tools™ is a governed network of specialized GPTs organized
as a **living tree** — the Toolbox routes users to Tools (branches), which hold
Tool-ettes (twigs), supported by Functions (leaves) and Function-ettes (falling leaves).

**The seven Tool branches:**

| Branch | Domain |
|--------|--------|
| 🪚 Discovered Careers | Resume, job search, professional development |
| 🪚 Treasured Finds | Collections — books, wine, vintage, media |
| 🪚 Tasty Tracker | Meal planning, recipes, grocery lists |
| 🪚 Traveler's Guide | Trip planning, wish-boarding, itineraries |
| 🪚 Organized Life | Personal dashboards, scheduling, productivity |
| 🪚 Healthy Bee-ing | Wellness habits and lifestyle balance |
| 🪚 Identity Known | Journaling, reflection, self-discovery |

Each Tool-ette is forged through the **Builder-Ready PromptChain** (PROMPT00–PROMPT05)
and governed by the **Canon System** — ensuring tone consistency, role discipline,
and lineage preservation across 40+ GPTs.

---

## Core Governance Principles

| Principle | Rule |
|-----------|------|
| **Expansion-Only Discipline** | Never simplify or remove — only elaborate and expand |
| **Canon Authority** | `canon/` files override GPT-local logic and legacy schema |
| **Hydration-First Runtime** | All continuity flows through `dataledger-hydration-v3.md` |
| **CanonSeal Integrity** | `::CanonSeal[...]::` tags must not be removed or altered |
| **Suffix Law** | `-R` / `-Rᵧ` suffixes are exclusive to OverKill Hill P³ and Found-Rᵧ |
| **Tone Default** | Untagged threads default to `GleeTone.A1` (uplifting, whimsical, clear) |
| **Registration Requirement** | Every entity must be declared in the registry before deployment |

---

## Historical PromptChain Lifecycle

Every new GPT is forged through this sequence:

```
PROMPT00 — Ignition Ritual         (governance, payload type, expansion discipline)
PROMPT01 — Payload Ingestion       (draft ingestion, schema binding)
PROMPT02 — Icon Forge & Canon Gate (visual identity, icon lock)
PROMPT03 — Registry Upload         (entity validation, conflict scan)
PROMPT04 — Team Role Enforcement   (role assignment: Coach/QB/Specialist/etc.)
PROMPT05 — Fusion Checkpoint       (tone calibration, PME-ready status)
```

After PROMPT05 the entity is **PME-ready** and eligible for deployment in ChatGPT Builder.

---

## Folder Catalog

This workbench contains distinct artifact layers in the GPT fabrication pipeline,
alongside a repository-local Agent Skills catalog. The content folders each have a
README describing their purpose, contents, governance rules, and relationships to
other folders. The local skills are indexed separately in
`.agents/skills/README.md`.

---

### 🔴 [`canon/`](canon/README.md) — Canonical Data Ledger System

**The single source of truth for the entire ecosystem.**

Nine `dataledger_*_v3.md` files that collectively define all GPT governance, identity,
tone, runtime behavior, entity registration, and lifecycle rules. Every GPT in the
ecosystem is validated against and routes output through these files. Canon overrides
all other sources. Files are sealed with `::CanonSeal[...]::` tags and grow only forward.

| Ledger | Purpose |
|--------|---------|
| `dataledger-registry-v3.md` | All registered Tools, Tool-ettes, Functions — with IDs, links, and lifecycle tags |
| `dataledger-persona-v3.md` | Tone overlay definitions and drift event logs |
| `dataledger-parameters-v3.md` | Runtime flags, execution toggles, suffix law rules |
| `dataledger-system-v3.md` | PME/CME engine schemas and lifecycle control |
| `dataledger-hydration-v3.md` | Runtime snapshots and cross-GPT session handoff |
| `dataledger-narrative-v3.md` | Finalized brand essays and canonical copy |
| `dataledger-ideation-v3.md` | Raw idea seeds and candidate entity stubs |
| `dataledger-archive-v3.md` | Retired logic — preserved, never deleted |
| `dataledger-processing-v3.md` | Legacy scaffolds — deprioritized as of v3.0.1 |

→ **[Full canon/ README](canon/README.md)**

---

### 🟠 [`governance/`](governance/README.md) — Directives, Rules, and Cathedral Architecture

**The law layer. All other content is subject to these directives.**

Four files establish and enforce the rules that govern every GPT, builder session, and
AI agent action in this ecosystem. The Governance Directive v3.0.1 (canonically sealed)
defines ledger routing, suffix law, clause lifecycle, overlay enforcement, and output
signature requirements. The Operator's Cathedral Layout (~20,000 lines) is the master
architectural blueprint — the definitive reference for every structural component,
tone rule, and governance protocol across the entire system.

| File | Purpose |
|------|---------|
| `glee-fully-project-governance-v3-0-1.md` | Primary governance directive — CanonSealed |
| `glee-fully-project-instructions.md` | Operating instructions for project sessions |
| `00-glee-fully-strategy-center-instructions.md` | Strategy Center GPT system instructions |
| `operators-cathedral-layout.md` | Master 20K-line architectural blueprint |

→ **[Full governance/ README](governance/README.md)**

---

### 🟡 [`prompts/`](prompts/README.md) — GPT Forge Engine

**Where GPTs are born. The primary fabrication tool.**

The Builder-Ready PromptChain v2.0 (~5,077 lines) is a forward-only, governance-locked
sequence of six prompt stages (PROMPT00–PROMPT05) that transforms a raw idea or payload
into a fully-compliant, canon-sealed, PME-ready GPT. Also contains two structural
scaffold templates and a content synthesis megaprompt for website generation.

| File | Purpose |
|------|---------|
| `glee-fully-builder-ready-promptchain-v2-0.md` | The primary creation engine — PROMPT00–PROMPT05+ |
| `custom-gpt-scaffold.md` | Single-GPT canonical field template |
| `custom-gpt-hybrid-scaffold.md` | Dual-tone / multi-role hybrid scaffold |
| `glee-fully-tools-megaprompt.md` | Multi-pass website content synthesis prompt |

→ **[Full prompts/ README](prompts/README.md)**

---

### 🟢 [`templates/`](templates/README.md) — FrankenTemplate GPT Instruction Variants

**The scaffold material supply room — 22+ iterative instruction templates.**

The FrankenTemplate series represents the evolving canonical standard for GPT instruction
block structure. Each lettered variant (`_a` through `_ae`) adds or refines sections
compared to its predecessor. The most complete variant (`_ae`) defines the full
three-tier scaffold: Toolbox (trunk), Tool (branch), and Tool-ette (twig) — each with
tone blocks, visit-aware dialog, routing logic, and canonical compliance sections.
Feed into the PromptChain at PROMPT01 as the build payload.

→ **[Full templates/ README](templates/README.md)**

---

### 🔵 [`evaluation/`](evaluation/README.md) — GPT PulseBook Evaluation Framework

**Quality assurance and compliance verification for all deployed GPTs.**

Three versions (v1.4 → v1.6 → v1.7) of the GPT PulseBook Evaluation — a structured
prompt that activates a Cleanroom-mode review session generating a comprehensive
compliance document (a "Pulsebook") for any GPT. Covers identity, tone, function
coverage, instruction quality, canon compliance, and PME readiness. Run at the end of
PROMPT05 before marking any entity PME-ready, and again any time an existing GPT
shows signs of drift.

| File | Status |
|------|--------|
| `gpt-pulsebook-evaluation-v1-7.md` | **Current — use this** |
| `gpt-pulsebook-evaluation-v1-6.md` | Superseded |
| `gpt-pulsebook-evaluation-v1-4.md` | Legacy |

→ **[Full evaluation/ README](evaluation/README.md)**

---

### 🟣 [`vernacular/`](vernacular/README.md) — Voice, Tone, and Vernacular Reference

**The voice bible. Defines how Glee-fully sounds.**

Two files (complete and lite) defining the tonal character, conversational personality,
and Glee-ism vocabulary for every entity in the ecosystem. Built around the governing
muse "Glee" — a Pacific Northwest, chai-loving, color-coding, pop-culture-fluent
original. Defines the three primary tone modes (BLEED-GLEE, GLEE-RICH, GLEE-LITE),
all tone modifiers (Calm, Whisper, Nostalgic, Sass), canonical phrase vocabulary,
and the pop-culture reference library (*Schitt's Creek*, *Friends*, *Practical Magic*,
*Stevie Nicks*). Referenced during PROMPT05 tone calibration and PulseBook audits.

→ **[Full vernacular/ README](vernacular/README.md)**

---

### 🟤 [`inventory/`](inventory/README.md) — Complete Entity Catalog

**The human-readable master catalog of every deployed GPT.**

A single ~1,272-line markdown file listing all 40+ deployed entities: the Toolbox,
all 7 Tools, and every Tool-ette — with live ChatGPT links, full descriptions, primary
function listings, and ~200-word elevator pitches for each. The human-readable companion
to `canon/dataledger-registry-v3.md` (which is the machine-readable authority). Used
for reference, onboarding, and as a content source for web page generation.

→ **[Full inventory/ README](inventory/README.md)**

---

### ⚫ [`docs/`](docs/README.md) — Ecosystem Documentation

**Plain-language explanations of the system for humans and AI agents.**

Narrative and technical overviews of the entire ecosystem — the "why" (brand philosophy,
emotional design rationale, tree metaphor) and the "how" (architecture, PromptChain
lifecycle, tone overlays, role discipline). Also includes source-format documents
(Word, PDF) and a reference for canonical GPT instruction block ordering. The first
stop for anyone needing orientation before working in this repo.

| File | Purpose |
|------|---------|
| `gleefully-technical-overview.md` | Architecture, PromptChain, canon system |
| `gleefully-narrative-overview.md` | Brand philosophy, emotional design, ecosystem story |
| `structure-and-ordering-for-custom-gpt-instruction-blocks.md` | Canonical instruction block ordering |

→ **[Full docs/ README](docs/README.md)**

---

### 🔘 [`scripts/`](scripts/README.md) — Governance Utility Scripts

**Automated tooling for repo hygiene and compliance verification.**

Nine Python 3 utility scripts (no third-party dependencies) for maintaining the health
and compliance of this repository: filename normalization to lowercase-kebab-case ASCII,
manifest validation, registry integrity checks, and foundry sync posture auditing.
Run `normalize_filenames.py` after adding any files. Run the audit suite periodically
and before governance syncs.

| Script | Purpose |
|--------|---------|
| `normalize_filenames.py` | Rename files to canonical ASCII convention |
| `manifest-audit.py` | Validate `manifest.yaml` governance fields |
| `registry-audit.py` | Check registry structural integrity |
| `foundry-sync.py` | Audit repo against OKHP3 governance baseline |
| `sync-report.py` | Generate foundry relay sync posture report |

→ **[Full scripts/ README](scripts/README.md)**

---

### 🗂️ [`snapshots/`](snapshots/README.md) — Historical State Captures

**Read-only point-in-time captures of canonical files.**

Dated subfolder captures of the complete ecosystem state at significant milestones.
Two snapshots currently exist: `2025-09-08/` (ledger baseline + vernacular + cathedral
layout) and `2025-09-14/` (same + supertemplate v1.0, v1.2, v1.5). Used for version
comparison, rollback reference, and audit trail evidence. Never edit files inside a
snapshot folder.

→ **[Full snapshots/ README](snapshots/README.md)**

---

### 🌐 [`web-templates/`](web-templates/README.md) — Public Webpage Template Assets

**HTML/CSS/JS templates for Tool-ette landing pages on glee-fully.tools.**

> ⚠️ These templates are consumed by child repos — this workbench does not serve them.

The Glee-fully brand system (Fredoka/Poppins typography, rust-orange and paper palette,
retro rainbow hero stripe) packaged as a fillable HTML template for Tool-ette public
landing pages. Includes `index.html` (the page template with placeholders), `theme.css`
(the complete brand CSS system), `app.js` (scroll-reveal, mobile nav, Ko-fi widget),
and `tool-and-tool-ette-page-updates.md` (~4,861 lines of web-ready content for all
Tools and Tool-ettes).

→ **[Full web-templates/ README](web-templates/README.md)**

---

## Repository Structure

```
Glee-fullyTools-FoundRy/
│
├── README.md              ← This file — repo overview and folder catalog
├── AGENTS.md              ← AI agent navigation guide
├── CHANGELOG.md           ← Version history
├── LICENSE.md             ← Proprietary license
├── manifest.yaml          ← Repo metadata (schema, lifecycle, visibility)
├── replit.md              ← Replit project context
├── .gitignore
│
├── canon/                 ← 🔴 THE 9 CANONICAL DATALEDGER FILES (authoritative)
│   ├── README.md
│   ├── dataledger-registry-v3.md      ← All registered GPT entities
│   ├── dataledger-persona-v3.md       ← Tone overlays and persona schema
│   ├── dataledger-parameters-v3.md    ← Runtime flags and toggles
│   ├── dataledger-system-v3.md        ← PME/CME engine schemas
│   ├── dataledger-hydration-v3.md     ← Runtime snapshots and handoff
│   ├── dataledger-narrative-v3.md     ← Finalized narrative clauses
│   ├── dataledger-ideation-v3.md      ← Idea seeds and stubs
│   ├── dataledger-archive-v3.md       ← Retired / deprecated logic
│   └── dataledger-processing-v3.md    ← Legacy only (deprioritized)
│
├── governance/            ← 🟠 Project directives and cathedral blueprint
│   ├── README.md
│   ├── glee-fully-project-governance-v3-0-1.md  ← Primary directive (CanonSealed)
│   ├── glee-fully-project-instructions.md
│   ├── 00-glee-fully-strategy-center-instructions.md
│   └── operators-cathedral-layout.md             ← Master 20K-line blueprint
│
├── prompts/               ← 🟡 GPT forge engine — PromptChain and scaffolds
│   ├── README.md
│   ├── glee-fully-builder-ready-promptchain-v2-0.md  ← Primary build engine
│   ├── custom-gpt-scaffold.md
│   ├── custom-gpt-hybrid-scaffold.md
│   └── glee-fully-tools-megaprompt.md
│
├── templates/             ← 🟢 FrankenTemplate instruction variants (a–ae)
│   ├── README.md
│   └── [22 iteration files — see README for index]
│
├── evaluation/            ← 🔵 GPT PulseBook quality evaluation rubrics
│   ├── README.md
│   ├── gpt-pulsebook-evaluation-v1-7.md  ← Current
│   ├── gpt-pulsebook-evaluation-v1-6.md
│   └── gpt-pulsebook-evaluation-v1-4.md
│
├── vernacular/            ← 🟣 Voice and tone reference library
│   ├── README.md
│   ├── glee-fully-vernacular-complete.md
│   └── glee-fully-vernacular-lite.md
│
├── inventory/             ← 🟤 Full entity catalog — all Tools and Tool-ettes
│   ├── README.md
│   └── inventory-of-toolbox-tools-and-tool-ettes.md
│
├── docs/                  ← ⚫ Human-readable ecosystem documentation
│   ├── README.md
│   ├── source-material/   ← Imported research, drafts, and non-canonical references
│   ├── gleefully-narrative-overview.md
│   ├── gleefully-technical-overview.md
│   ├── structure-and-ordering-for-custom-gpt-instruction-blocks.md
│   └── [source .docx and .pdf files]
│
├── scripts/               ← 🔘 Governance utility scripts (Python 3)
│   ├── README.md
│   ├── normalize_filenames.py
│   ├── manifest-audit.py
│   ├── registry-audit.py
│   ├── foundry-sync.py
│   ├── check-registry.py
│   ├── sync-report.py
│   └── validate-manifest.py
│
├── snapshots/             ← 🗂️ Read-only historical state captures
│   ├── README.md
│   ├── 2025-09-08/        ← Ledger snapshot: Sep 8, 2025
│   └── 2025-09-14/        ← Ledger snapshot: Sep 14, 2025 (most recent)
│
└── web-templates/         ← 🌐 Webpage templates for child repo sites (NOT served here)
    ├── README.md
    ├── index.html
    ├── theme.css
    ├── tool-and-tool-ette-page-updates.md
    └── assets/  (css/, js/, img/)
```

---

## Required Files (All Repos in This Ecosystem)

Every repository governed by this FoundRy must include:

- `AGENTS.md` — AI agent navigation guide
- `README.md` — Project overview
- `CHANGELOG.md` — Version history
- `LICENSE.md` — License declaration
- `manifest.yaml` — Repo metadata

---

## Quick Reference — Where Does X Live?

| I need to… | Go to |
|------------|-------|
| Find a deployed GPT's ChatGPT link | `inventory/` or `canon/dataledger-registry-v3.md` |
| Check what tone rules apply to a Tool-ette | `vernacular/` |
| Build a new Tool-ette from scratch | `prompts/glee-fully-builder-ready-promptchain-v2-0.md` |
| Get a scaffold to fill in | `templates/glee-fully_frankentemplate_ae.md` |
| Evaluate a GPT before deployment | `evaluation/gpt-pulsebook-evaluation-v1-7.md` |
| Check what canonical rules apply | `governance/glee-fully-project-governance-v3-0-1.md` |
| Understand the full architecture | `governance/operators-cathedral-layout.md` |
| Read a plain-language explainer | `docs/gleefully-technical-overview.md` |
| Find a past version of a ledger file | `snapshots/2025-09-14/` |
| Generate website content | `prompts/glee-fully-tools-megaprompt.md` |
| Fix or check filenames | `python3 scripts/normalize_filenames.py .` |
| Understand who built what & when | `CHANGELOG.md` + `manifest.yaml` |

---

> *The capability is durable. The platform wrapper is temporary.*
