# Glee-fully Branch 04: Traveler's Guide

This repository is an early-stage planning workspace for a Glee-fully travel
tool family covering travel planning, journaling, and discovery.

## Current status

The travel project is a prompt and specification scaffold. It does not contain
a verified application, service, runtime, deployment, integration, or test
workflow. The planning documents in `docs/` contain placeholders and proposed
design language, not a completed product contract.

## Start here

- [Project instructions](docs/04-glee-fully-travelers-guide-instructions.md)
- [Ideation scaffold](docs/04-glee-fully-travelers-guide-ideation.md)
- [Build-design scaffold](docs/04-glee-fully-travelers-guide-build.md)
- [Agent guidance](AGENTS.md)

## Repository map

- `docs/`: travel-project intent, ideation, and build planning.
- `.agents/skills/`: project-local Agent Skills used for repository and
  knowledge operations. These are tooling assets, not travel-product code.
- `skills/okhp3-skill-promotion/`: the publication mirror for the local skill
  promotion package. It is intentionally kept separate from its runtime source.

## Important limits

The instructions reference `dataLedger_*v2.txt` and related lifecycle files,
but those files are not present in this checkout. Their location, authority,
format, and validation process remain unresolved. Do not treat the proposed
ledger lifecycle as an implemented system.

The five sibling Branch 04 repositories are related by naming, but their shared
interfaces and implementation relationship are not established here.

See [AGENTS.md](AGENTS.md) for evidence boundaries, validation commands, and
open questions.
