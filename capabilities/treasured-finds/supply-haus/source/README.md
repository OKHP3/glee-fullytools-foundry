# glee-fully-gpt02f-supply-haus

Supply Haus is a live Glee-fully custom GPT that keeps a master inventory of
craft supplies and creative materials, under Branch #02 (Treasured Finds).
Confirmed via the project's Notion anchor, 2026-09-18. This repository does
not contain that GPT's build; it holds project metadata, a legacy prompt
placeholder awaiting audit
([`prompts/02f-supply-haus-prompts-v1.yaml`](prompts/02f-supply-haus-prompts-v1.yaml)),
and a local Agent Skills workbench under `.agents/skills/`.

## Current status

- Product status: active. The Supply Haus GPT is live; this repository is
  metadata and tooling around it, not the GPT's build.
- Purpose: craft-supply and creative-material inventory (owner-confirmed).
- Project prompt: [`prompts/02f-supply-haus-prompts-v1.yaml`](prompts/02f-supply-haus-prompts-v1.yaml).
  Its `ThreadOrigin: BudgetBalancer_Build_Design` field could not be matched
  to any Notion project as of 2026-09-18 and was removed 2026-10-02 by owner
  decision; see AGENTS.md.
- Confirmed implementation in this repository: no application runtime,
  database, interface, API, automation, deployment, or production
  integration is present here. The live GPT's build lives outside this repo.
- Skill catalog: see [the local skill catalog](.agents/skills/README.md).

## Boundaries

Data model, integrations, purchasing behavior, privacy model, and any future
in-repo implementation milestone remain owner decisions. Do not treat the
placeholder prompt or bundled skills as proof of an in-repository working
assistant; the assistant that exists today runs as a ChatGPT custom GPT.

`AGENTS.md` is the canonical repository guidance. `CLAUDE.md` points to it for
Claude-compatible tooling.
