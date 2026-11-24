# glee-fully-gpt05-organized-life

## Scope and precedence

This file is the canonical agent guide for this repository. `CLAUDE.md` points
here, so changes to shared repository guidance belong in this file. Follow any
higher-level instructions supplied by the runtime or repository owner.

The historical project directive is archived under `archive/`. It is not
evidence of an implemented application or runtime.

## Project identity

- **Suite:** Glee-fully
- **Branch:** #05, Organized Life
- **Type:** Documentation and Agent Skill workbench for a productivity and
  life organization branch
- **Repository:** https://github.com/OKHP3/glee-fully-gpt05-organized-life
- **Notion anchor:** https://app.notion.com/p/677f3e4feec74c4abf29479659f34ca0
- **Current status, confirmed:** Early-stage documentation and Agent Skill
  workbench. It contains Markdown project material, orchestration prompts, and
  46 embedded Agent Skills, but no application source, root package manifest,
  executable product, or deployment configuration.

The Notion link and related-repository list are owner-provided metadata. They
were not verified through a live external service during this maintenance pass.

## Purpose, users, and boundaries

**Confirmed purpose:** The repository is for personal productivity, scheduling,
budgeting, and broader life organization work within the Glee-fully suite.

**Inferred product direction:** It is an umbrella or branch context for child
tools covering tasks, spending, gifts, scheduling, lifestyle visibility, and
neighborly exchange. The child repository names support this inference, but no
working integrations or shared runtime are present here.

**Likely users, inferred:** People seeking help organizing personal tasks,
money, time, and household or community life.

**Current non-goals:** Do not assume that this repository provides a user
interface, data store, scheduling integration, financial advice, production
guarantees, or a supported deployment target. Do not invent a mission,
roadmap, command set, or product status beyond the evidence in the repository.

## Repository structure

- `README.md` provides the public repository orientation.
- `archive/05-glee-fully-organized-life_instructions.md` is a historical
  directive scaffold. It references `dataLedger_*v2.txt` and related files
  that are not present here. Treat it as archival design material, not current
  runtime policy.
- `.agents/prompts/` contains project onboarding, migration, and context
  bootstrap prompts.
- `.agents/skills/` contains 46 embedded Agent Skill directories. The generated
  catalog in `.agents/skills/README.md` and metadata file are cataloger-owned.
- `skills/okhp3-skill-promotion/` is a promotion-source package whose contents
  are mirrored under `.agents/skills/okhp3-skill-promotion/`.
- `LICENSE` is the MIT license. `.gitattributes` enables text normalization.

This is a single Git repository. No nested repository or independent
application project was found under the project root.

## Technology and architecture

The confirmed technology surface is Markdown plus the Python and JavaScript
tooling bundled in the embedded skills. There is no root `package.json`,
`pyproject.toml`,
`Cargo.toml`, Makefile, Docker configuration, frontend configuration, or
application source directory.

The current architecture is therefore documentation plus agent-skill
resources. There is no confirmed application data flow, service boundary,
storage model, external integration, or deployment model.

The skill cataloger can scan the local skill directory and supports validation
without writing files:

```text
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --check
```

Use the skill's own `SKILL.md` before invoking it for a catalog or index change.
The cataloger script's help output is available with `--help`. The catalog is
generated from the 46 direct child skill packages under `.agents/skills/`.

## Validation and development commands

No application build, test, lint, or deployment command is currently defined.
For repository maintenance, use ordinary read-only checks such as:

```text
git status --short --branch
git log -8 --oneline --decorate
```

When changing embedded skills, run the cataloger's `--check` mode and inspect
the resulting diff. Do not run write modes unless the task explicitly requires
refreshing the generated skill catalog.

## Change conventions

- Keep this guide factual and label conclusions as confirmed, inferred, or
  unknown when the distinction matters.
- Preserve existing user changes and do not use destructive version-control
  commands.
- Keep context maintenance limited to guidance, project documentation, and
  relevant repository metadata. Do not modify application code, dependencies,
  generated artifacts, secrets, CI behavior, or unrelated files as part of
  context alignment.
- Preserve the OverKill Hill P3 conventions supplied for this project: no em
  dashes in generated content, preserve standalone punchy lines, and keep
  verbosity proportional to the understanding produced.
- Keep AutoCAD at version R10 when AutoCAD guidance is ever added. This is
  locked and not negotiable.
- Do not add private credentials or unverified private data. Treat Notion and
  related-repository links as metadata unless they are verified in context.
- Update this file when the repository gains a real implementation, runtime,
  test suite, deployment path, or materially different scope.

## Related repositories

- [glee-fully-gpt05a-task-maestro](https://github.com/OKHP3/glee-fully-gpt05a-task-maestro)
- [glee-fully-gpt05b-thrifty-spender](https://github.com/OKHP3/glee-fully-gpt05b-thrifty-spender)
- [glee-fully-gpt05c-giftlist-helper](https://github.com/OKHP3/glee-fully-gpt05c-giftlist-helper)
- [glee-fully-gpt05d-scheduling-wizard](https://github.com/OKHP3/glee-fully-gpt05d-scheduling-wizard)
- [glee-fully-gpt05e-lifestyle-wallboard](https://github.com/OKHP3/glee-fully-gpt05e-lifestyle-wallboard)
- [glee-fully-gpt05f-neighborly-bazaar](https://github.com/OKHP3/glee-fully-gpt05f-neighborly-bazaar)

The existence and relationship of these repositories is recorded in the
existing project metadata. Their implementation status is unknown from this
repository alone.

## Open questions and risks

- The owner has not recorded whether this branch is active, in development,
  archived, or on hold.
- The intended final product format, platform, runtime, and integration model
  are not documented.
- The ledger, routing, persona, and PME concepts in the historical directive
  have no corresponding source files or application runtime in this repository.
- The child repositories may contain the actual implementations, but their
  contracts and current status are not defined here.
- The long-term boundary between this Organized Life branch and the embedded
  Agent Skill workbench remains an owner decision.

Resolve these questions from owner or product evidence before turning the
scaffold into implementation guidance.

## Imported Claude Cowork project instructions
