# Neighborly Bazaar by Glee-fully

Neighborly Bazaar is a documentation and configuration repository for a seller-facing Custom GPT that helps people in the United States sell legal, tangible goods locally.

It supports item identification, transparent local pricing, listing creation, marketplace selection, negotiation coaching, and scam-aware meetup guidance. The repository is not an executable marketplace application.

## Start here

- [Operating brief](specifications/05f-organized-life-neighborly-bazaar.md)
- [Pulsebook](specifications/gpt-pulsebook-v1.md)
- [Knowledge corpus](knowledge/)
- [Agent guidance](AGENTS.md)

## Repository map

- `specifications/` contains the concise behavioral brief and the detailed historical Pulsebook with its DOCX and PDF exports.
- `knowledge/` contains 15 numbered knowledge articles, each preserved as a DOCX/PDF pair.
- `.agents/` contains project-local prompts and reusable agent skills used to maintain the repository.
- `skills/` contains the project-local skill-promotion package.

## Boundaries

The assistant serves sellers only, focuses on U.S. local exchanges, and does not provide legal, tax, or financial advice. Safety guidance takes priority over persona styling. Current marketplace rules and legal thresholds require fresh verification before being presented as current advice.

## Status

The repository is documentation-first. Historical deployment metadata in the Pulsebook is not evidence that the Custom GPT is currently live or healthy.
