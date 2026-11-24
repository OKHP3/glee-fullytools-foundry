# glee-fully-gpt07a-critter-spotter

Canonical agent guidance for this repository. 'CLAUDE.md' points here.

## Project identity

- Suite: Glee-fully, Branch 07
- Intended product label: 07a, Critter Spotter
- Repository: https://github.com/OKHP3/glee-fully-gpt07a-critter-spotter
- License: MIT, Copyright 2026 OverKill Hill P3
- Related repository: https://github.com/OKHP3/glee-fully-gpt07-identity-known
- Notion anchor: owner-provided and private; do not store the URL in this
  repository. Use runtime context or an untracked local anchor file when
  needed.

## Current understanding

### Confirmed

The repository is a Git repository whose tracked implementation is a seeded
Agent Skills collection under '.agents/skills/'. It currently contains four
skills:

- 'find-skills': discover and recommend installable skills.
- 'okhp3-notion-capture-router': route AI conversation material into Notion
  and reconcile reusable extracts with GitHub repositories.
- 'okhp3-skill-cataloger': scan skills and generate a project catalog.
- 'skill-creator': create, evaluate, and improve Agent Skills.

The root also contains a minimal 'README.md', this guide, the 'CLAUDE.md'
pointer, '.gitattributes', and 'LICENSE'.

There is no application runtime, wildlife-identification implementation,
package manifest, dependency lockfile, test suite, CI configuration, or
deployment configuration in the repository at this time.

### Inferred

The repository appears to be an early or dormant skill-seeding scaffold for a
future wildlife and animal identification assistant. The current contents
support agent workflow and knowledge-capture infrastructure, but do not yet
implement the Critter Spotter product itself.

### Unknown

The intended user experience, product mission, vision, data sources, model or
vision provider, runtime, deployment target, ownership, and implementation
status beyond this scaffold are not established by repository evidence.
Do not invent these details in code or documentation.

## Scope and boundaries

Treat '.agents/skills/' as the current product surface. Preserve each skill's
frontmatter, trigger description, privacy rules, and referenced resources
when editing it.

Do not describe the repository as a working animal-identification product
until an implementation, entry point, and validation path are added. If a
future change introduces application code, document its runtime, entry point,
dependencies, tests, and deployment model here at the same time.

The Notion capture skill must not contain real private Notion URLs, database
IDs, collection IDs, or connector-only resource IDs. Use runtime context or a
local untracked 'routing-anchors.private.md' file when private anchors are
needed. Never commit secrets or private source material.

## Repository structure

~~~text
.
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── LICENSE
├── .gitattributes
└── .agents/skills/
    ├── find-skills/
    ├── okhp3-notion-capture-router/
    ├── okhp3-skill-cataloger/
    └── skill-creator/
~~~

Each skill is a directory with a 'SKILL.md' file. Supporting references,
assets, scripts, and Claude command files are local to the skill that uses
them. There are no nested Git repositories in the current tree.

## Runtime and validation

The repository is primarily Markdown and Agent Skills metadata. Python 3 is
used by the cataloger and by helper scripts bundled with 'skill-creator'.
There is no pinned Python version or dependency environment.

The cataloger supports these verified read-only checks:

~~~bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check --json
~~~

The normal catalog refresh is:

~~~bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills
~~~

The refresh writes '.agents/skills/README.md' and
'.agents/skills/.catalog-meta.json'. Run it only when intentionally updating
generated catalog artifacts. Use '--dry-run' to preview changes.

There are currently no repository-wide build, test, lint, or deployment
commands. At minimum, after guidance or skill edits:

~~~bash
git diff --check
git status --short --branch
~~~

Also verify that every skill directory name matches its 'SKILL.md' 'name'
field and that referenced local files exist.

## Change conventions

- Keep guidance factual. Label confirmed facts, inferences, and unknowns.
- Use relative repository paths in instructions. Avoid machine-specific paths.
- Keep one canonical source of agent guidance. Keep 'CLAUDE.md' as a short
  pointer unless Claude-specific behavior is later required.
- Use the existing Agent Skills frontmatter format and match 'name' to the
  containing directory.
- Update generated catalogs through the cataloger script rather than by hand.
- Keep public skill content free of private Notion anchors and credentials.
- Follow the OverKill Hill P3 brand rules: no em dashes in generated content;
  preserve standalone punchy lines; apply the ROY principle so verbosity earns
  its space; AutoCAD version is R10 when that unrelated rule is applicable.

Before changing a skill, read its complete 'SKILL.md' and only the directly
relevant references or scripts. Preserve existing user changes and do not use
destructive version-control commands.

## Known gaps and maintenance

- 'README.md' documents the current scaffold and four-skill surface; expand it
  when an owner-confirmed product mission or implementation exists.
- Repository status is not declared in project metadata. Until owner input
  exists, describe it as scaffolded or dormant rather than active or
  production-ready.
- No product implementation or wildlife-domain evidence is present.
- '.gitignore' protects the suggested private routing-anchor filename and Python
  working artifacts. Keep any private anchor untracked.

Update this guide when the repository gains an application runtime, new skill
families, validated commands, deployment behavior, or an owner-confirmed
mission and status. Re-check the tree and recent history before replacing an
inference with a confirmed fact.

Maintained 2026-07-13 from local repository evidence.

## Imported Claude Cowork project instructions
