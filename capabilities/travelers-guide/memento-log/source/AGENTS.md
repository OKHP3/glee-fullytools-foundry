# glee-fully-gpt04e-memento-log

Canonical agent guidance for the Glee-fully Branch 04e repository.

## Project identity

- Suite: Glee-fully, Branch 04
- Repository: `https://github.com/OKHP3/glee-fully-gpt04e-memento-log`
- Project type: GPT Tool-ette scaffold and knowledge-bundle archive
- Current checkout: Git repository on `main`, tracking `origin/main`
- Related project: `https://github.com/OKHP3/glee-fully-gpt04-travelers-guide`
- Notion anchor from prior project metadata: `https://app.notion.com/p/f262f2cb317242fcace1dcab4fa80c52`

## Purpose and status

### Confirmed

This checkout contains project guidance, extracted data-ledger text files, two ZIP exports, and reusable agent-skill assets. It does not contain Memento Log application source code, a product package manifest, product tests, runtime configuration, or deployment configuration. Some reusable skills have their own scripts, manifests, and tests.

The existing project description identifies 04e as a travel souvenir and keepsake tracking assistant. That description is retained as the intended product purpose, but the repository does not yet contain an implementation that demonstrates the workflow.

The implementation status is scaffolded or dormant, not a working executable application in this checkout. Do not claim production readiness or a deployed service.

### Inferred

- Intended users are people who want to record, organize, and revisit travel souvenirs or keepsakes.
- The likely value is lightweight personal memory and collection tracking.
- The mission is to support that tracking workflow through a GPT Tool-ette.

### Unknown

- The final user interface, runtime, integrations, persistence model, and deployment target.
- The owner-approved mission, vision, roadmap, and release status.
- Whether the ZIP bundles are source-of-truth exports, historical snapshots, or temporary scaffolding.

## Repository structure

- `AGENTS.md`: canonical project and agent guidance.
- `CLAUDE.md`: short pointer to `AGENTS.md` for Claude-specific entry.
- `README.md`: product purpose, repository contents, and scaffold status.
- `knowledgebundle/ledgers/`: eight `dataLedger_*_v2.txt` files.
- `knowledgebundle/archives/glee_mementolog_knowledgebundle.zip`: eight ledger files.
- `knowledgebundle/archives/gleefully_mementolog_exportbundle_v1.0.zip`: the same eight ledger files in a different archive order and metadata set.
- `.agents/skills/`: reusable skill packages, including Notion capture, skill cataloging, and skill creation. These are agent assets, not Memento Log application code.
- `.gitattributes`: enables automatic text line-ending normalization.
- `LICENSE`: MIT license, copyright 2026 OverKill Hill P³.

There are no nested Git repositories or clearly independent application projects in this checkout.

## Data and architecture

Project ledger data is present as extracted text files and in both ZIP bundles. The ledger files define empty or near-empty sections for registry, system rules, persona, narrative, processing, and archive data. The parameters ledger contains these flags:

```text
autoload_index: false
use_symbolic_indexing: true
tone_recalibration: off
personality_coherence_enforced: true
```

The ideation ledger contains thread-seed records for multiple Glee-fully projects. It does not provide a Memento Log implementation or a validated application data flow. Treat the bundles as archives until the owner identifies a canonical editable format.

## Development and validation

No Memento Log product build, test, lint, package, or local-run command is defined. Do not invent one. Individual reusable skills may document their own validation commands.

Verified repository checks:

- Before this guidance update, `git status --short --branch` was clean on `main` and matched `origin/main`.
- `unzip -t knowledgebundle/archives/glee_mementolog_knowledgebundle.zip` passed.
- `unzip -t knowledgebundle/archives/gleefully_mementolog_exportbundle_v1.0.zip` passed.
- Each same-named ledger file has identical extracted SHA-256 content in both archives.

If executable code is added later, document its runtime, entry point, setup, test, and deployment commands here and in `README.md` after verifying them.

## Change conventions

- Keep this file factual. Label conclusions as confirmed, inferred, or unknown when evidence is limited.
- Preserve existing archive files and their versioned names unless the task explicitly concerns archive maintenance.
- Do not edit files inside a ZIP in place. If an archive must change, explain the source and regeneration process and validate the resulting archive.
- Do not treat generic files in `.agents/skills/` as product requirements. Follow their local instructions only when working on those skill packages.
- Keep application, dependency, generated-artifact, secret, and CI changes outside a context-alignment task.
- Use the repository's `main` branch as observed. No additional branch or release convention is documented.

## Brand and writing rules

- Do not use em dashes in generated content.
- Preserve standalone punchy lines. Do not consolidate them into paragraphs.
- Apply the ROY principle: understanding produced, explanation invested. Verbosity must earn its space.
- AutoCAD version is R10, locked and not negotiable.

## Risks and open questions

- The README describes the scaffold but cannot document a product setup or usage workflow that does not yet exist.
- The repository name and project description suggest a Memento Log product, but the bundled ideation content is mostly cross-project scaffolding and the registry is empty.
- The two ZIP files contain the same extracted ledger content, so their intended distinction is unclear.
- There is no evidence here for a runtime, persistence, external integration, or deployment model.

Before implementing product behavior, resolve the intended runtime and interface, canonical data model, relationship to the Travelers Guide project, archive ownership, and current product status with the owner.

## Keeping this guide current

Update `AGENTS.md` whenever the repository gains a runtime, source tree, canonical data format, test or build command, deployment target, or owner-confirmed product direction. Re-check claims against files and executable validation rather than carrying forward placeholders.

## Imported Claude Cowork project instructions
