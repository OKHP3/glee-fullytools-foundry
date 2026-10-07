# Glee-fullyTools-FoundRy — Replit Project

Current direction, September 27, 2026: build portable skills and compose host-specific plugins/connectors; preserve GPTs as migration sources. Read [the conversion workflow](docs/application/portable-capabilities.md) and [product subtree contract](products/README.md). Native adapter implementation, child imports and host synchronization require their own evidence.

## Purpose

This repository now contains an owner-local Glee-fully builder application under
`app/` alongside its preserved canonical workbench. Start locally with
`python3 -m app.server`. The service intentionally binds to loopback only.

Private Replit runtime, branch and deployment state could not be verified during
the September 7, 2026 research. Do not infer GitHub/Replit parity from this file.
A hosted preview or deployment requires authentication and an explicit hosting
boundary before adapting the loopback service. The GitHub source repository is intentionally public. Serve only the application allowlist; keep the repository root and local working data outside that boundary.

## Shared agent work

### GitHub synchronization

GitHub `origin/main` is the shared baseline. Keep Replit and desktop `main`
checkouts clean and update each separately after a pull request merges.
New work belongs on a feature branch, created from an up-to-date `main`:

```bash
git status --short --branch
git fetch origin
git pull --ff-only origin main
git switch -c codex/<task-name>
```

Run those update commands only from a clean `main`. Replace `<task-name>` with
the actual task name. Commit reviewed files on the feature branch, push it and
open a pull request. Complete review fixes and required checks before the
owner-authorized squash merge. A pushed feature branch is not yet integrated.
Direct pushes with new commits to protected `main` are rejected by design;
repeating `git pull && git push` cannot resolve review conversations or merge a PR.

After a squash merge, preserve the feature tip, switch to a clean `main` and
fast-forward from `origin/main`. If local `main` already contains unsquashed
commits, preserve its tip and reconcile it with the squash result before pruning.
Never force-push, discard authored files or disable branch protection to sync.
Verify a clean status, identical `HEAD` and `origin/main`, and ahead/behind `0/0`
on both hosts. Replit Git may need a refresh after Shell operations.

Read `AGENTS.md` and [the collaboration protocol](docs/agent-collaboration.md).
Finish the current Git synchronization directive before accepting overlapping
work. Report the fetched SHA, local-only work, branch and validation to the
coordinator. Receive code through a reviewed branch/PR or an attributable owner
handoff; do not assume another host shares this checkout or chat context.

Use this Repl for its environment-specific execution. Route substantial research
and implementation to the assigned ChatGPT/Codex worker when that saves the
owner's limited Replit allocation. Claude and Copilot can contribute focused
reviews or bounded tasks. Do not change paid settings or launch duplicate jobs.

## Authority Chain

```
OKHP3/OverKill-Hill
  → Glee-fullyTools-FoundRy  (this repo)
    → Glee-fully child repositories (glee-fully-gpt00-* through glee-fully-gpt07-*)
```

## Ecosystem Map

| Layer | Repo / Site | Role |
|-------|-------------|------|
| Shared skills | OKHP3/skillz | Portable skills for all three regions |
| Historical parent | OKHP3/OverKill-Hill-FoundRy | Lineage only; OverKill-specific builder |
| This Workbench | OKHP3/Glee-fullyTools-FoundRy | Glee-fully fabrication line |
| Public Storefront | github.com/OKHP3/Glee-fullyTools → glee-fully.tools | Consumer-facing site and catalog |
| Universe | overkillhill.com/universe | OKHP3 universe overview |

## Key Folders

| Folder | Contents |
|--------|----------|
| `app/` | Owner-local workspace, working records, validation and export |
| `canon/` | The 9 canonical dataLedger files — authoritative source of truth |
| `governance/` | Project governance directives, instructions, Cathedral Layout |
| `docs/` | Narrative and technical overviews, synthesis documents |
| `prompts/` | Builder PromptChain, GPT scaffolds, megaprompts |
| `vernacular/` | Voice and tone reference (complete and lite) |
| `templates/` | FrankenTemplate GPT instruction scaffold variants |
| `evaluation/` | GPT PulseBook evaluation rubrics |
| `inventory/` | Full catalog of Toolbox Tools and Tool-ettes |
| `snapshots/` | Point-in-time ledger and template snapshots (dated) |
| `web-templates/` | Webpage template assets (for child repo sites — NOT deployed here) |
| `.agents/skills/` | Repository-local Agent Skills, references, tests, and evaluation evidence |
| `skills/` | Explicit publication mirror for the promotion package maintained here |

## User Preferences

- Owner-local `app/` runtime is authorized; no hosted deployment is configured
- Do not serve webpage-build or web-templates as a live site from this project
- Follow Expansion-Only Discipline: never remove existing content, only elaborate
- All canon changes must flow through the dataLedger schema in `canon/`
- Maintain CanonSeal integrity on all locked ledger files
