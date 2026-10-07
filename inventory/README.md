# inventory/ — Complete Entity Catalog

This is a historical GPT source catalog, not current deployment proof. The September 27, 2026 direction uses these entities as conversion candidates for portable skills. Track repository consolidation separately in [the product migration register](../products/migration-map.json).

> The **authoritative human-readable catalog** of every deployed GPT in the Glee-fully
> Personalizable Tools™ ecosystem. Full entity listings for the Toolbox, all 7 Tools
> (Branches), and all 40+ Tool-ettes (Twigs) — with live ChatGPT links, descriptions,
> elevator pitches, and function listings for each.

---

## Purpose

`inventory/` is the browsable, linkable master catalog of the deployed ecosystem.
Where `canon/dataledger-registry-v3.md` is the machine-readable authority (YAML schema
blocks, clause IDs, governance tags), the inventory is its human-readable companion —
suitable for reference, onboarding, and web content generation.

It answers: *what exists in this ecosystem right now, and how do I reach it?*

---

## Files

| File | Lines | Purpose |
|------|-------|---------|
| [`inventory-of-toolbox-tools-and-tool-ettes.md`](inventory-of-toolbox-tools-and-tool-ettes.md) | ~1,272 | Complete entity catalog — Toolbox + 7 Tools + 40+ Tool-ettes with descriptions, functions, elevator pitches, and live ChatGPT links |

---

## Entity Hierarchy (The Toolbox Tree)

The ecosystem uses a living-tree metaphor. Every entity has a defined role and position:

| Tier | Symbol | Metaphor | Role |
|------|--------|----------|------|
| Toolbox | 🧰 | Trunk 🌳 | Navigation concierge — routes users to the right branch |
| Tool | 🪚 | Branch 🌵 | Domain-level category GPT — routes to Tool-ettes |
| Tool-ette | 🔩 | Twig 🌿 | Functional specialist — executes one focused task |
| Function | ⚙️ | Leaf 🍃 | Specific action within a Tool-ette (export, tag, format) |
| Function-ette | 🪛 | Falling Leaf 🍂 | Atomic sub-action (text clean, metadata stamp) |

---

## Currently Deployed Entities (Summary)

### 🧰 Toolbox — #00
**Glee-fully Personalizable Tools** (Trunk) — Central navigation GPT for the full suite
🔗 [chatgpt.com/g/g-68578aaa...](https://chatgpt.com/g/g-68578aaa54588191b70c6aa8aa9bf228-glee-fully-personalizable-tools)

| Tool # | Tool Name | Tool-ette Count |
|--------|-----------|-----------------|
| #01 | Discovered Careers | 6 (01a–01f) |
| #02 | Treasured Finds | See inventory |
| #03 | Tasty Tracker | See inventory |
| #04 | Traveler's Guide | See inventory |
| #05 | Organized Life | See inventory |
| #06 | Healthy Bee-ing | See inventory |
| #07 | Identity Known | See inventory |

For complete Tool-ette listings with individual links, see the full catalog:
→ [`inventory-of-toolbox-tools-and-tool-ettes.md`](inventory-of-toolbox-tools-and-tool-ettes.md)

---

## What Each Inventory Entry Contains

- **Full Description** — the public-facing description used in ChatGPT Builder
- **Parent link** — Toolbox (for Tools) or Tool (for Tool-ettes)
- **Primary Functions** — key leaf-level actions this entity performs
- **Tool-ette list with links** (for Tool entries)
- **Elevator Pitch** — ~200-word technical summary: architecture, routing behavior,
  integration points with sibling entities

---

## Relationship to Canon

| Inventory | `canon/dataledger-registry-v3.md` |
|-----------|-----------------------------------|
| Human-readable Markdown | YAML schema + clause IDs |
| Descriptions and elevator pitches | PME tags and compliance data |
| Live ChatGPT links | Entity IDs and lifecycle status |
| Browsable catalog | Machine-readable canonical authority |

The **registry wins on conflicts.** The inventory is kept in sync with the registry
but is subordinate to it as an authoritative source.

---

## Maintenance Rules

- Entries **added** when an entity reaches PME-ready status in the registry
- Entries **never deleted** — retired entities are marked `[RETIRED]` with links preserved
- Elevator pitches follow the ~200-word format: role, architecture, routing, integrations
- ChatGPT links are authoritative live links — verify they resolve before adding

---

## Relationship to Other Folders

```
inventory/    <-- tracks deployed entities from --> canon/dataledger-registry-v3.md
inventory/    <-- describes entities built via  --> prompts/ (PromptChain + templates)
inventory/    <-- confirmed compliant by        --> evaluation/ (PulseBook)
inventory/    <-- content source for            --> web-templates/ (public site pages)
inventory/    <-- described at ecosystem level  --> docs/ (narrative + technical overviews)
```
