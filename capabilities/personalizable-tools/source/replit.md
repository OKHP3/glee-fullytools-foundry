# glee-fully-gpt00-personalizable-tools

## Project Overview

Root toolbox and architecture documentation hub for the "Glee-fully" personalizable tools suite (GPT00). This is a meta-repository for managing Agent Skills — specialized instruction sets and scripts for AI agents — and providing a canonical framework for building and personalizing GPTs.

**GitHub**: https://github.com/OKHP3/glee-fully-gpt00-personalizable-tools

## Tech Stack

- **Language**: Python 3.12
- **Environment**: Nix (stable-25_05)
- **No frontend or backend web server** — this is a documentation and agent-skills toolbox

## Project Structure

- `.agents/skills/` — Agent Skills installed in this project (find-skills, okhp3-notion-capture-router, okhp3-skill-cataloger, skill-creator)
- `.local/skills/` — Replit-provided agent skills
- `.local/secondary_skills/` — Additional secondary skills
- `.local/state/` — Persistent state (SQLite DB, assets, scripts)
- `00a-*` / `00b-*` — Glee-fully tool instructions, build docs, prompts, and pulsebook

## Key Scripts

- `.agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py` — Catalogs all agent skills into a structured README

### Run the skill cataloger

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills
```

## User Preferences

- No em dashes in any generated content
- Preserve standalone punchy lines — do not consolidate into paragraphs
- ROY principle: verbosity must earn its space
