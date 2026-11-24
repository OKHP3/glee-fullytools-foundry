# Agent guidance for glee-fully-gpt07c-sight-seeker

This file is the canonical agent guide for the repository root.

## Project identity

- Suite: Glee-fully, Branch 07
- Repository: `OKHP3/glee-fully-gpt07c-sight-seeker`
- Intended name: 07c Sight Seeker
- Declared target purpose: visual scene analysis and point-of-interest identification
- Repository type confirmed by inspection: Git repository containing a flat collection of 46 Agent Skills, project onboarding prompts, and one verified publication mirror
- Current status: the checkout is a project-local Agent Skill bundle, not a visual-analysis application. It contains no visual-analysis model integration, service entry point, or deployment configuration.

The repository name suggests Sight Seeker as an intended product, but the checkout does not document that product or provide implementation evidence for it. Treat visual scene analysis and point-of-interest identification as an unconfirmed target direction until owner input or new implementation evidence confirms otherwise.

## Mission, vision, and scope

Confirmed current mission: provide reusable agent guidance for skill discovery, authoring, evaluation, migration, repository organization, evidence handling, process work, and skill promotion. The 46 checked-in skill packages under `.agents/skills/` are the current functional surface.

Inferred target mission: support a future Sight Seeker assistant that can inspect visual scenes and identify useful points of interest. This is inferred from the repository name and declared target purpose only.

Vision and production role: unknown from repository evidence.

Lifecycle and recent activity:

- Confirmed: the repository has 13 commits, with the latest on 2026-08-05. Recent history includes removal of copied skills, catalog generation, migration support, and a bulk Agent Skill bundle import.
- Inferred: the repository is a maintained project-local skill bundle and promotion workbench rather than active product implementation.
- Unknown: whether the visual Sight Seeker application is intentionally out of scope or missing from this checkout.

In scope:

- Agent Skill definitions under `.agents/skills/`.
- Markdown, YAML frontmatter, JSON assets, references, and bundled Python utilities that belong to those skills.
- Documentation needed to explain the repository and its skill workflows.

Out of scope unless the owner explicitly expands the task:

- Inventing or implementing visual-analysis behavior based only on the repository name.
- Adding model, API, Notion, or deployment credentials.
- Changing application code, dependencies, CI, generated catalogs, or unrelated repository content during context-maintenance work.

## Repository layout

```text
.
├── AGENTS.md                         # canonical agent guidance
├── CLAUDE.md                         # short pointer to AGENTS.md
├── README.md                         # repository orientation and validation
├── LICENSE
├── .agents/prompts/                  # onboarding and migration prompts
├── .agents/skills/                   # 46 project-local Agent Skill packages
└── skills/okhp3-skill-promotion/     # verified publication mirror
```

No nested Git repositories, package workspaces, or independent projects were found. `.agents/skills/` is one repository-local skill surface, not a monorepo.

Important entry points:

- Each skill starts at its own `SKILL.md`.
- The cataloger entry point is `.agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py`.
- The Foundry suite validator is `.agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs`.
- The promotion mirror checker is `skills/okhp3-skill-promotion/scripts/sync_skill_mirror.py`.
- Cataloger slash-command templates are bundled under `.agents/skills/okhp3-skill-cataloger/.claude/commands/`; they are not installed at the repository root.

## Technology and runtime

- Markdown with YAML frontmatter is the primary format.
- JSON is used for catalog metadata schemas and Notion-router trigger data.
- Python is used by the cataloger, promotion mirror, and other bundled helper scripts.
- The cataloger declares Python 3.9 or newer and standard-library-only dependencies. It was checked successfully with the local Python 3.14.5 runtime.
- No `package.json`, `pyproject.toml`, requirements file, lockfile, Makefile, container definition, or service manifest is present.
- No application runtime, web interface, visual model, external API integration, or deployment process is currently represented in the tree.

The skills are instruction packages for an agent host. Their prose may describe external connectors or tools, but those capabilities are not configured by this repository alone.

## Skill conventions

- Keep one skill per directory under `.agents/skills/<skill-name>/`.
- Put the required `SKILL.md` at the skill directory root.
- Use YAML frontmatter with at least `name` and `description`.
- Keep the frontmatter `name` aligned with the directory name.
- Use `metadata` for package information such as author, version, category, origin, and maturity when those values are known.
- Keep references, assets, scripts, and evaluator resources inside the owning skill directory.
- Do not place private Notion URLs, database identifiers, credentials, or connector-only resource IDs in public skill content. The Notion router documents a private `routing-anchors.private.md` convention for local use; do not commit that file unless the owner explicitly establishes a safe policy.
- Prefer progressive disclosure: keep core workflow guidance in `SKILL.md` and put large or variant-specific material in `references/`.

When adding or changing a skill, preserve its intended trigger conditions, output contract, safety boundaries, and license metadata. Update related references when a workflow or file path changes.

## Development and validation

Run commands from the repository root:

```bash
# Validate discovered skills without writing a catalog or metadata file
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --check

# Show the discovered skill inventory as JSON without writing files
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --json
```

The cataloger currently discovers 46 skills. The check passes against the current tree. The Foundry suite validator also validates all 46 packages, with advisory package-quality warnings only.

The normal catalog command is intentionally write-producing. It updates `.agents/skills/README.md` and `.agents/skills/.catalog-meta.json`:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills
```

Run it only when updating the generated catalog is part of the requested change. The `--full` mode is for a distribution repository with root-level skill families. This repository has no such families, so do not use full-index mode for routine project skill inventory.

No automated test suite, lint configuration, build command, CI workflow, or deployment command was found. Validation for documentation-only changes is therefore file review plus the cataloger check above when skill files are involved.

Recon snapshot: root files are `README.md`, `AGENTS.md`, `CLAUDE.md`, `LICENSE`, `.gitattributes`, and `.gitignore`; `.agents/prompts/` contains onboarding prompts, `.agents/skills/` contains 46 skill packages, and `skills/okhp3-skill-promotion/` is an exact local publication mirror. There are no nested `AGENTS.md` or `CLAUDE.md` files.

## Safe change procedure

1. Confirm the repository root with `git rev-parse --show-toplevel`.
2. Check `git status` and preserve unrelated user changes.
3. Inspect the affected skill's `SKILL.md` and directly referenced resources before editing.
4. Keep changes within the requested skill or guidance scope.
5. Run the cataloger check for skill metadata changes, and run any directly relevant helper script only when its inputs and outputs are understood.
6. Re-read every changed guidance file and inspect `git diff` before handoff.
7. Do not use destructive version-control commands.

## Existing guidance and repository conventions

- `CLAUDE.md` contains `@AGENTS.md` and is a pointer to this file. Keep it short unless Claude-specific instructions are genuinely needed.
- The repository's brand guidance requires no em dashes in generated content, preservation of standalone punchy lines, and a level of explanation justified by the value it provides.
- AutoCAD R10 is an organization-level locked rule recorded in prior guidance. No AutoCAD content exists in this repository, so it does not currently define implementation behavior here.
- The declared relationship to `glee-fully-gpt07-identity-known` has not been verified from local repository files. Do not infer shared APIs or architecture from that relationship.

## Known gaps and open questions

Urgent clarification needed before product implementation:

- Is this repository intentionally a seeded skill bundle, or is the visual Sight Seeker application missing from the checkout?
- If visual analysis is intended, what runtime, model or API provider, input and output contract, and user interface should be treated as authoritative?
- What is the intended lifecycle and deployment model? No production status can be confirmed from this repository.

Optional maintenance:

- Decide whether all 46 packages are intended to remain in this project-local bundle.
- Review advisory Foundry warnings package by package; do not treat them as release failures.
- Confirm whether the Sight Seeker product direction should remain attached to this repository.

## Keeping this guide current

Update this file when the repository gains an implementation, changes its runtime, adds validation or deployment workflows, changes skill layout, or receives owner-confirmed product direction. Label claims as confirmed, inferred, or unknown when the evidence is not direct. Do not turn a name, placeholder, or speculative plan into a current capability claim.

## Imported Claude Cowork project instructions
