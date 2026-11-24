# glee-fully-gpt04-travelers-guide

## Scope and precedence

This is the canonical agent guide for the repository root. `CLAUDE.md` contains only `@AGENTS.md` and therefore points Claude work to this file. The files under `.agents/skills/` are task-specific skill instructions. Read the relevant `SKILL.md` before using one; those skills are tooling guidance, not the product architecture.

## Project identity

- **Suite:** Glee-fully
- **Branch:** 04, Traveler's Guide
- **Repository:** `https://github.com/OKHP3/glee-fully-gpt04-travelers-guide`
- **Notion anchor listed by the repository:** `https://app.notion.com/p/5f9f1804cff747deb24905304a9c1db4`
- **Repository type:** Git repository containing planning and prompt-design documents
- **Confirmed status:** Early-stage documentation scaffold. No application or service implementation is present in the tracked root files.
- **License:** MIT, as stated in `LICENSE`

## Purpose and intent

- **Confirmed from repository guidance:** The project is described as a Glee-fully branch for travel planning, journaling, and discovery tools.
- **Inferred:** The repository is intended to develop the prompts, specifications, and related artifacts for travel-oriented GPT tools. The concrete product boundary and primary users are not defined in the repository.
- **Vision:** Unknown. Do not invent a roadmap, production claim, or user workflow until the owner documents one.

This repository must currently be treated as a planning workspace. The existing documents contain placeholders and aspirational directives, not a verified implementation contract.

## Repository structure

- `README.md`: public orientation, current status, repository map, and open limits; it does not document an application setup because no application is present.
- `docs/04-glee-fully-travelers-guide-instructions.md`: project directive and proposed ledger-routing rules. It references `dataLedger_*v2.txt` and other `*_v2.txt` files that are not present.
- `docs/04-glee-fully-travelers-guide-ideation.md`: early ideation scaffold with placeholder prompt fragments and `!IDEA_STAGE` tags.
- `docs/04-glee-fully-travelers-guide-build.md`: build-design scaffold targeting prompts, YAML exports, Markdown, and `!PME_READY`; its canonical build prompt is still a placeholder.
- `docs/`: the intentionally small home for travel-project planning and specification documents.
- `.agents/skills/`: project-local Agent Skills for repository, knowledge, evaluation, migration, and promotion workflows. These are tooling assets, not travel product code. The generated catalog in `.agents/skills/README.md` describes the current package set.
- `skills/okhp3-skill-promotion/`: intentional publication mirror of the local promotion skill; compare it with `.agents/skills/okhp3-skill-promotion/` before changing either surface.
- `AGENTS.md`: this canonical guide.
- `CLAUDE.md`: pointer to this guide.
- `LICENSE`, `.gitattributes`: repository metadata.

No nested Git repositories or independent application packages were found.

## Technology, architecture, and operations

For the travel product, no programming language, framework, dependency manifest, executable entry point, test suite, build system, deployment configuration, external integration, database, or runtime environment is currently confirmed. There is no verified travel-product run, test, lint, build, or deploy command. The repository-local tooling skills separately contain scripts, manifests, and tests; consult the relevant skill's instructions before using them.

The instructions document proposes this lifecycle:

`ideation_v2.txt` -> `processing_v2.txt` -> `registry_v2.txt`, `persona_v2.txt`, `parameters_v2.txt` -> `narrative_v2.txt` -> `archive_v2.txt`

Those files do not exist here. Treat the lifecycle, tagging, signing, and routing rules as proposed design language until the referenced canon files are added and their format and execution process are documented.

## Development and validation

The following checks are appropriate for the current repository shape:

- `git status --short --branch` to check branch and working-tree state.
- `rg --files` to inventory tracked and working files.
- `git log --oneline --decorate -8` to review recent repository history.
- `git diff --check` to catch whitespace errors in documentation changes.

There is no verified application command yet. Do not claim that the project builds, tests, runs, deploys, or integrates with a service unless those capabilities are added and verified.

## Change conventions

- Preserve existing planning documents and their standalone punchy lines unless the owner explicitly asks for editorial restructuring.
- Keep claims tied to repository evidence. Label conclusions as confirmed, inferred, or unknown when the distinction matters.
- Do not fabricate missing ledgers, PME identifiers, schemas, commands, credentials, users, integrations, or production guarantees.
- Keep generated content free of em dashes, consistent with the suite rule recorded in the prior guide.
- Retain the suite's ROY principle: explanation should earn its space.
- The prior guide listed AutoCAD R10 as locked. No repository evidence connects that rule to this travel project, so it is not an active project convention unless the owner confirms it.
- Avoid modifying `.agents/skills/` when making ordinary project-document changes. If a task targets a skill or its generated catalog, follow that skill's own instructions and scope.
- Do not hand-edit the generated catalog section in `.agents/skills/README.md`; regenerate it with `.agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py`.
- Do not modify dependencies, generated artifacts, secrets, CI behavior, or unrelated files as part of documentation maintenance.

## Related projects

The repository lists these sibling branches:

- `glee-fully-gpt04a-journey-diary`
- `glee-fully-gpt04b-itinerary-hacker`
- `glee-fully-gpt04c-detour-discoverer`
- `glee-fully-gpt04d-dreamland-journeys`
- `glee-fully-gpt04e-memento-log`

Their implementation relationship and shared interfaces are not established here. Inspect a sibling repository directly before assuming shared code, schemas, commands, or release processes.

## Known gaps and open questions

The following remain unresolved because the repository does not contain enough evidence:

- Is this branch intended to remain a prompt/specification repository, or will it contain a runnable product?
- Who are the primary users, and what user-facing workflow is the first target?
- What is the current project status beyond the early-stage planning evidence?
- Which `dataLedger_*v2.txt` files are canonical, where do they live, and how are they validated?
- What languages, runtimes, schemas, integrations, tests, and deployment model should future implementation use?
- How should this branch coordinate with the five related repositories?
- Is the Notion anchor current and authoritative for project decisions?
- Does the suite-level AutoCAD R10 rule apply to this repository?

The absent ledger files are the most important operational risk. Until their location and authority are confirmed, agents should not treat the directive document as sufficient source-of-truth for canonical outputs.

## Keeping this guide current

Update this file when the repository gains an implementation, a canonical ledger, verified commands, a defined user workflow, or a confirmed project status. Keep `CLAUDE.md` as a short pointer unless Claude-specific instructions are genuinely needed.

---
*Updated 2026-08-05 from repository evidence and current tracked files.*

## Imported Claude Cowork project instructions
