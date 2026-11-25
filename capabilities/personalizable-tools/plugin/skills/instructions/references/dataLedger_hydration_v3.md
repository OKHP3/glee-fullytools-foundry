# dataLedger_hydration_v3

Public reference with a blank handoff. Historical conversation and account locators are omitted.

## ✨ Purpose & Context

This file is part of the `dataLedger_v3.md` family. It is used to export, transport, rehydrate, or reinstantiate the logical and functional state of a GPT session, including user intent, suffix overlays, sibling awareness, PME status, and instruction versioning.

Hydration files serve as a **runtime snapshot**, enabling:

- **Cross-GPT continuity** via `@mention` handoffs
- **Thread restoration** across sessions or devices
- **Debugging, cloning, or version comparison** of session logic
- **Reintegration into long-term ledgers** for audit or refinement

This file is portable, self-contained, and designed to be **read and written** by any Custom GPT within the canonical ecosystems that supports hydration-aware logic.

---

## ⚖️ Definitions

> **Hydration**\
> The process of restoring a GPT's full operational and contextual state from a file such as this one.

> **DNRE (Do Not Rehydrate or Export)**\
> A runtime flag signaling that a given session, GPT, or payload should not generate or accept hydration files.

> **Interledger Role**\
> This file operates as a **transport-layer contract**, connecting the following canonical ledgers:

- `dataLedger_registry_v3.md` — GPT identities, versions, lineage
- `dataLedger_suffixes_v3.md` — Suffix overlays and logic
- `dataLedger_personas_v3.md` — Voice/tone profiles
- `dataLedger_familytree_v3.md` — GPT type and symbolic taxonomy
- `dataLedger_threads_v3.md` — Per-session memory, audit trails

---

## Blank handoff

~~~yaml
hydration_file_id: null
created_at_utc: null
source_gpt_id: null
instruction_version: null
schema_version: null
user_goal: null
handoff_occurred: null
~~~
