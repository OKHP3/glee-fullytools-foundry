# glee-fully-gpt07e-motif-muse

Canonical agent guidance for this repository. Keep this file aligned with the
repository evidence whenever the project structure or operating model changes.

## Project identity

- Suite: Glee-fully, Branch 07
- Project label: 07e, Motif Muse
- Declared type: GPT tool-ette
- Git remote: `https://github.com/OKHP3/glee-fully-gpt07e-motif-muse.git`
- Repository root: this directory
- Current status: scaffold or early development. The exact product status is
  not established by the repository.

## Purpose, mission, and vision

**Confirmed declaration:** The original project guide describes Motif Muse as
pattern and motif identification for art, textiles, and design.

**Current evidence:** The repository contains documentation and reusable agent
skills, but no motif-identification implementation, user interface, model
integration, data set, or runtime service.

**Inferred mission:** Help a future GPT tool-ette explain and identify visual
motifs in art, textiles, and design.

**Vision:** Unknown. Do not turn the inferred mission into a roadmap or product
claim without owner input.

**Users:** Unknown. No user-facing interface or workflow is defined here.

## Scope and boundaries

- This repository is currently a Git-tracked guidance scaffold with a local
  Agent Skills library; it does not contain the Motif Muse implementation.
- The `.agents/skills/` directory is the local skill-library surface today.
- Do not invent application behavior, supported inputs, model providers,
  production guarantees, or deployment targets.
- Do not modify application code, dependencies, generated artifacts, secrets,
  CI behavior, or unrelated files when performing context maintenance.
- Preserve existing user changes and never use destructive version-control
  commands.
- There are no nested repositories or independent projects in the current
  tree.

## Repository layout

- `AGENTS.md`: canonical agent guide.
- `CLAUDE.md`: short compatibility pointer to `AGENTS.md`.
- `README.md`: project title only at present.
- `LICENSE`: repository license.
- `.gitattributes`: text normalization rules.
- `.agents/prompts/`: project bootstrap and migration prompts.
- `.agents/skills/README.md`: generated catalog of the local skill packages.
- `.agents/skills/okhp3-skill-cataloger/`: cataloger and Python generator for
  indexing skills in a repository.

Skill bundles may contain `SKILL.md`, references, assets, scripts, and Claude
command files. Treat each skill's own `SKILL.md` as the operating specification
when that skill is explicitly in scope.

## Technology and runtime

- Confirmed formats: Markdown, YAML frontmatter, JSON, HTML, and Python.
- No application language, framework, package manifest, lockfile, build system,
  test runner, deployment configuration, or runtime entry point is present.
- Some local validation and catalog scripts use Python 3. Package-specific
  validators may require additional runtime dependencies; check each package's
  own instructions before using them.
- The Notion capture skill requires a Notion connector and project-specific
  private anchors at runtime. Do not commit private anchors.

## Development and validation

There is currently no repository-wide build, test, lint, or deployment command.
For documentation or skill changes, run the checks relevant to the changed
files:

```sh
git status --short --branch
git diff --check
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py \
  --skills-dir .agents/skills --dry-run
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs \
  --skills-dir .agents/skills
```

The catalog dry run is read-only. The Foundry validator checks the local skill
packages structurally. Regenerate the catalog only when the package set changes
or the generated catalog is intentionally being refreshed.

Current package validation may report warnings without failing the structural
check. Treat warnings as review items, not as proof of runtime readiness.

## Change conventions

- Keep guidance factual and label confirmed facts, inferences, and unknowns.
- Use repository-relative paths in documentation where possible.
- Keep skill metadata valid, especially the required `name` and `description`
  frontmatter fields.
- Read a skill's full `SKILL.md` before changing that skill or its bundled
  resources.
- Keep public skill files free of private Notion URLs, database IDs,
  credentials, and connector-only identifiers.
- Preserve standalone punchy lines.
- No em dashes in generated content.
- Apply the ROY principle: understanding produced, explanation invested. Added
  verbosity should earn its space.
- AutoCAD version is R10 when AutoCAD context is actually in scope.

## Related context

The prior guide identified
`https://github.com/OKHP3/glee-fully-gpt07-identity-known` as a related
repository. The relationship and any shared contract are not documented here,
so verify them before making cross-repository changes.

## Known gaps and open questions

- Whether the Motif Muse GPT tool-ette is active, in development, archived, or
  on hold is unknown.
- The intended user workflow, input and output contract, model or API choice,
  training or reference data, and deployment surface are unknown.
- `README.md` does not yet explain the project or list the seeded skills.
- The local skill library is broad and may contain packages unrelated to Motif
  Muse; its final intended scope remains an owner decision.

Resolve these with repository evidence or owner input before documenting them
as current behavior. When the implementation gains a runtime, update this file
with verified entry points and validation commands.

## Imported Claude Cowork project instructions
