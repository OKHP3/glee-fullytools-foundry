# Glee-fully GPT06D Medi Minder

Medi Minder is the planned medication-support twig of the Glee-fully Healthy
Bee-ing wellness branch. The parent pulsebook places its scope at medication,
refill, and appointment tracking.

## Current status

This repository is a documentation and agent-workbench scaffold. It does not
currently contain a Medi Minder application, GPT instruction export, runtime,
data store, integration, UI, test suite, CI workflow, or deployment
configuration.

The parent Healthy Bee-ing pulsebook records a private parent GPT, but that is
not evidence of a separate Medi Minder deployment.

## Start here

- [Agent guide](AGENTS.md): canonical repository rules, evidence, boundaries,
  and open decisions.
- [Healthy Bee-ing pulsebook](docs/healthy-bee-ing-pulsebook-2025-09-01.md):
  parent identity and sibling twig context.
- [Local skill catalog](.agents/skills/README.md): agent capabilities currently
  present in this checkout.
- [Migration prompts](.agents/prompts/): project onboarding and GPT-to-skill
  migration support.

## Boundaries

Future health-related work must define a not-medical-advice boundary, avoid
diagnosis and prescribing, protect medication data, and specify escalation for
urgent or ambiguous situations before implementation begins.

Product requirements, the user-facing instruction contract, supported
workflows, runtime, storage, integrations, validation, release process, and
deployment remain TBD.
