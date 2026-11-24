# glee-fully-gpt06c-snappy-count

## Project identity

- Suite: Glee-fully, Branch 06
- Repository: `https://github.com/OKHP3/glee-fully-gpt06c-snappy-count`
- Type: Git repository containing documentation and reusable Agent Skills
- Local root: `/Volumes/OKH-Local/04_GitHub_Mirrors/glee-fully-gpt06c-snappy-count`
- Default branch observed: `main`
- Current status: documentation and skill-seeding stage. No application implementation is present in this checkout.

## Purpose and product context

### Confirmed

- The repository is named for 06c, Snappy Count, within the Glee-fully Healthy Bee-ing branch.
- The existing project description calls Snappy Count a calorie and macro tracking assistant.
- The pulsebook identifies Snappy Count as a sibling twig for quick, photo-based nutrition awareness.
- The repository currently stores reusable agent capabilities rather than a deployed nutrition tracker.

### Inferred

- The intended user value is lightweight food and nutrition awareness with low-friction capture, likely as part of the broader wellness branch.
- The eventual product boundary may include calorie or macro estimation, but no implementation or detailed behavior is documented here.

### Unknown

- Whether the Snappy Count GPT is currently deployed, who its current users are, and what its production instruction block contains.
- The supported image, nutrition-data, persistence, privacy, health-disclaimer, and escalation workflows.
- The intended runtime, deployment surface, release process, and owner contact channel.

Do not turn the inferred or unknown items into implementation requirements without owner or source documentation.

## Mission, vision, and scope

- Confirmed parent mission: support everyday wellness with calm, clear, confidence-building guidance.
- Inferred Snappy Count mission: make nutrition awareness quick and approachable.
- Inferred vision: a focused nutrition twig that complements the other Healthy Bee-ing tools without replacing medical guidance or a full clinical nutrition system.
- Current repository scope: authoring, validating, cataloging, and maintaining Agent Skills and their supporting references.
- Out of scope until explicitly requested: building a calorie tracker, adding a web or mobile interface, connecting nutrition APIs, storing health data, or claiming medical or production readiness.

## Repository structure

- `AGENTS.md`: canonical instructions for agents working in this repository.
- `CLAUDE.md`: short compatibility pointer to `AGENTS.md`; keep it aligned if its role changes.
- `README.md`: title-only placeholder; it is not a reliable product specification.
- `docs/06-glee-fully-healthy-bee-ing_pulsebook_20250901.md`: historical parent-branch pulsebook and the main product-context source currently checked in.
- `.agents/skills/find-skills/SKILL.md`: helps discover and choose installable or local Agent Skills.
- `.agents/skills/okhp3-notion-capture-router/`: Notion knowledge-capture routing skill with references and templates.
- `.agents/skills/okhp3-skill-cataloger/`: skill inventory and catalog-generation skill, including its Python catalog script.
- `.agents/skills/skill-creator/`: skill authoring, evaluation, validation, reporting, and packaging support.
- `LICENSE`: repository license.

No nested Git repositories or independent application projects were found.

## Technology and architecture

- Confirmed formats: Markdown, YAML frontmatter, JSON, HTML, and Python scripts.
- Confirmed runtime dependency: Python 3 for the bundled scripts. The quick validator also imports `yaml`.
- There is no package manifest, build system, application entry point, test suite, CI configuration, container definition, or deployment configuration in the repository.
- The architectural unit is an Agent Skill directory. `SKILL.md` defines metadata and instructions; optional `assets/`, `references/`, `agents/`, `.claude/commands/`, and `scripts/` provide supporting material.
- Keep public skill files free of private Notion URLs, database IDs, credentials, and connector-only identifiers. The Notion capture skill explicitly requires private anchors to come from runtime or non-committed context.

## Verified commands

Run from the repository root:

```text
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --check
```

This is a read-only catalog check. It passed on 2026-07-13 and found four skills. It reported warnings that `find-skills` and `skill-creator` have no version in metadata.

Validate an individual skill with:

```text
python3 .agents/skills/skill-creator/scripts/quick_validate.py .agents/skills/<skill-name>
```

On 2026-07-13, `okhp3-notion-capture-router` and `skill-creator` passed. `find-skills` failed because its `enabled` frontmatter key is not accepted by the validator. `okhp3-skill-cataloger` failed because its description is longer than the validator's 1024-character limit. These are existing findings, not introduced by this guide update.

There is no verified application run, test, lint, build, or deployment command. Do not invent one.

## Working conventions

- Preserve user changes and use non-destructive version-control operations.
- Make the smallest change that satisfies the request. Do not edit application code, dependencies, generated artifacts, secrets, CI behavior, or unrelated files during context-maintenance work.
- Treat `AGENTS.md` as the canonical guide. Keep `CLAUDE.md` as a pointer unless Claude-specific instructions are genuinely needed.
- Preserve standalone punchy lines when editing branded content.
- Do not use em dashes in generated content.
- Apply the ROY principle: explanation should earn its space.
- Do not add private Notion anchors or personal contact details to committed public skill files.
- When changing a skill, preserve its frontmatter contract, update directly related references or tests, and run the catalog check plus the skill validator when practical.
- Do not regenerate `.agents/skills/README.md` or other catalog artifacts unless the task explicitly asks for that output. The catalog script can write files.

## Change safety

Before editing:

1. Check `git status --short --branch` and preserve existing changes.
2. Read the applicable `SKILL.md` completely before changing that skill.
3. Confirm whether a file is hand-maintained or generated.
4. Keep claims tied to repository evidence, and label inferences or unknowns.

After editing:

1. Re-read every changed guidance file.
2. Run the read-only catalog check and any relevant skill validation.
3. Review `git diff --check` and `git diff` for scope, formatting, and accidental secrets.
4. Report unresolved product or deployment questions instead of filling them with assumptions.

## Known gaps and risks

- Product identity is only partially represented: the only product-specific evidence is the existing guide and a parent-branch pulsebook.
- The pulsebook is dated 2025-08-31 and describes the parent Healthy Bee-ing branch, not a detailed Snappy Count implementation.
- `README.md` does not explain the repository or its skills.
- Skill metadata validation is inconsistent with two checked-in skills, as recorded above.
- Health-related behavior, disclaimers, data handling, and production status are not established by repository evidence.

## Related context

- Parent or sibling reference: [glee-fully-gpt06-healthy-bee-ing](https://github.com/OKHP3/glee-fully-gpt06-healthy-bee-ing)
- A private Notion anchor existed in the prior guide. Retrieve private anchors from the user's current context or approved connector context; do not commit them here or copy them into public skill content.

## Keeping this guide current

Update this file when the repository gains an application runtime, changes its skill inventory, adds verified commands, establishes deployment or data-handling behavior, or receives authoritative product documentation. Record the evidence and distinguish confirmed facts from inferences and owner questions.

---
Generated from repository inspection on 2026-07-13. The file is maintained as project guidance, not as a substitute for product requirements.

## Imported Claude Cowork project instructions
