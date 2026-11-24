# Glee-fully 04c: Detour Discoverer

Detour Discoverer is a pre-implementation Glee-fully concept intended to help
travelers find off-the-beaten-path attractions and hidden gems.

## Current status

This repository is a concept and agent-workspace scaffold. It does not yet
contain a verified product interface, runtime, data source, integration,
automated test suite, deployment, or production implementation.

The product form and end-user workflow remain TBD. The concept may eventually
become a GPT configuration, service, web application, or another tool, but the
repository does not establish that decision.

## Repository map

- `AGENTS.md`: canonical project guidance, evidence boundaries, and open questions.
- `.agents/skills/`: repository-local Agent Skills and their supporting assets,
  evaluations, references, and scripts. The current catalog is generated in
  `.agents/skills/README.md`.
- `skills/`: a publication-mirror surface currently containing the
  `okhp3-skill-promotion` package. Its source relationship is documented by
  that package and is intentionally preserved.
- `CLAUDE.md`: compatibility pointer to `AGENTS.md`.
- `LICENSE`: MIT license.

The Agent Skills corpus supports repository and knowledge operations. It is
not evidence that the Detour Discoverer product itself is implemented.

## Open decisions

- What is the actual end-user workflow and interface?
- Which attraction, map, travel, or other data sources are allowed and required?
- What runtime, dependencies, integrations, deployment environment, and
  security requirements should be used?
- What is the owner-approved lifecycle, roadmap, and release convention?
