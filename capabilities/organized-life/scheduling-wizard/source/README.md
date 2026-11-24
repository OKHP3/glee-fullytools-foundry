# Glee-fully Scheduling Wizard

Scheduling Wizard is a prompt-driven GPT Tool-ette in the Glee-fully Organized
Life Tool, Branch 05. Its purpose is to turn tasks, rituals, bills, focus
blocks, and Joy Anchors into structured, vibe-aware time plans.

## Start here

- [System prompt source](prompts/scheduling_wizard_gpt_system_instructions.md)
- [Knowledge bundle contents](knowledgebundle/)
- [Agent guidance](AGENTS.md)
- [Local Agent Skills catalog](.agents/skills/README.md)

## Repository map

- `prompts/scheduling_wizard_gpt_system_instructions.md` is the readable prompt source.
- `knowledgebundle/` contains the packaged ZIP snapshot, its prompt copy, and
  the narrative, parameter, processing, archive, persona, registry, system,
  and ideation ledgers.
- `.agents/skills/` contains repository-local Agent Skills and their supporting
  resources. They are maintenance tooling, not Scheduling Wizard runtime code.
- `skills/` contains an intentional publication mirror for skills selected for
  distribution. The current mirror is `okhp3-skill-promotion`.

## Status and boundaries

This repository is maintained as a prompt and knowledge asset. It does not
contain an application runtime, calendar connector, voice interface, image
parser, file-processing pipeline, export service, or deployment configuration.
The capabilities described in the prompt are intended behavior unless
executable evidence is added.

The knowledge bundle includes historical metadata and ledger material. Those
records preserve provenance and must not be treated as current runtime
configuration.

## Validation

There is no application build or test command at present. Useful integrity
checks are documented in `AGENTS.md`, including archive validation, prompt-copy
comparison, generated skill-catalog checks, and whitespace review.
