# Glee-fully GPT02b Decor Detective

Early scaffold for a planned Glee-fully GPT Tool-ette that would help users
identify home decor and find sourcing leads.

## Current status

This repository does not contain a product runtime, image-recognition system,
retailer or catalog integration, automated test suite, or deployment setup.
The Decor Detective product remains an early, unimplemented concept.

The repository also contains a local Agent Skills distribution and migration
workbench under `.agents/skills/`, plus a promotion mirror under `skills/`.
Those skills support repository and agent workflows. They are not evidence that
Decor Detective itself is implemented.

## Start here

- [AGENTS.md](AGENTS.md): repository scope, operating rules, and validation
- [.agents/skills/README.md](.agents/skills/README.md): current local skill catalog
- `.agents/skills/`: repository-local Agent Skills and their resources
- `skills/okhp3-skill-promotion/`: benchmarked promotion mirror

## Validation

The available checks are structural and skill-specific:

```text
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check
git diff --check
```

There is no verified command to run a Decor Detective product because no
product runtime exists yet.

## Open decisions

The future host, canonical product prompt, image and sourcing integrations,
release model, and evaluation criteria remain to be defined.
