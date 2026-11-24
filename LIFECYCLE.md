# LIFECYCLE.md — Glee-fullyTools-FoundRy

**Status:** Active  
**Last reviewed:** 2026-08-06
**Reviewed by:** OverKill Hill P³

---

## Current state

| Field | Value |
|---|---|
| Lifecycle status | **Active** |
| Visibility | Private workbench |
| Primary use | GPT specification authoring, governance, prompt engineering |
| Deployment | None — content-first repository, not a deployed service |

---

## State definitions

| State | Meaning |
|---|---|
| `Active` | Ongoing work; canonical source for Glee-fully tooling artifacts |
| `Draft` | Pre-structure; content exists but governance not yet established |
| `Archival` | Read-only; content preserved but no new work expected |
| `Migrated` | Content moved to successor repository; this repo retained as reference |
| `Deprecated` | Superseded; links point elsewhere; no updates |

---

## Transition rules

- **Active → Archival:** All 50 GPTs reach v1.0 AND Phase 5 Agent Skills are operational. Decision requires explicit owner authorization.
- **Active → Migrated:** Content consolidated into a successor mono-repo. Requires approved migration plan in `MIGRATION.md`.
- **Never auto-transition:** No automated process may change lifecycle status. Owner decision only.

---

## Historical phase plan

| Phase | Description | Status |
|---|---|---|
| Phase 1–4 | All 50 GPTs to v1.0 via child repos | In progress |
| Phase 5 | 7–10 domain Agent Skills (consolidation) | Planned; 52 local skill packages currently provide the broader project-local skill library |
| Phase 6 | Optional Vite/TypeScript SPA over Agent Skills | Deferred decision |

See `docs/agent-skill-conversion-strategy.md` for full phase rationale.

---

## Current source ownership

Glee-fully capability work now belongs in the [FoundRy capability directory](capabilities/README.md).
The [migration register](products/migration-map.json) records the imported
source trees. Source transfer and retirement of a GitHub repository are
separate from authoring, evaluating and releasing a portable skill.
The public storefront maintains its own catalog and launch destinations.

## Historical lifecycle dependencies

- Child repositories (`glee-fully-gpt00-*` through `glee-fully-gpt07-*`) depend on canonical material produced here.
- `OKHP3/OverKill-Hill-FoundRy` is the parent governance layer.
- Public storefront (`glee-fully.tools`) consumes published material from child repos, not directly from this workbench.

---

*Expansion-Only. New state definitions and transition rules are added; existing accepted rules are not removed.*
