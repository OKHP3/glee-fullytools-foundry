# glee-fully-gpt01e-blinkin-tuner

Documentation and seeded Agent Skills scaffold for Glee-fully / Branch 01.

## Current status

This checkout is a scaffold or pre-implementation repository. It does not
contain an application runtime, supported build command, LinkedIn integration,
database, deployment configuration, or verified bLinkIn Tuner implementation.

The declared product context is a possible LinkedIn profile and content
optimization tool, but the intended users, workflow, inputs, outputs, privacy
model, and success measures remain unresolved.

## Repository map

- `.agents/prompts/` contains onboarding and migration prompts.
- `.agents/skills/` contains the local seeded Agent Skills and their supporting
  references, scripts, fixtures, evaluations, and benchmarks.
- `skills/okhp3-skill-promotion/` is an intentional publication mirror of its
  local source package. It is managed output, not an independent authoring
  surface.
- `AGENTS.md` is the canonical repository guidance.
- `CLAUDE.md` is a compatibility pointer to `AGENTS.md`.

## Boundaries

Do not treat the seeded skills as product runtime or deployment evidence. Do
not infer product decisions from the repository name, related repository links,
or the Notion anchor. Resolve those decisions before implementation or external
capability claims are added.
