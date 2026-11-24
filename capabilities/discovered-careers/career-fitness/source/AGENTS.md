# glee-fully-gpt01c-career-fitness

## Project identity

- Suite: Glee-fully, Branch 01
- Project label: 01c Career Fitness
- Repository: `OKHP3/glee-fully-gpt01c-career-fitness`
- License: MIT
- Repository type: single-root Git repository containing documentation and agent-skill assets
- Current status: Career Fitness scaffold plus a migrated Agent Skill library. No Career Fitness application implementation, product runtime, or deployment configuration is present.
- External project anchor: [Notion project page](https://app.notion.com/p/4779215a0ee34a9d8b2579456a86f194)

## Purpose and scope

The existing project description states that 01c Career Fitness should evaluate job-candidate fit and gaps against target roles. That is the intended purpose, not a currently implemented capability.

Confirmed current scope:

- Repository guidance in `AGENTS.md` and the short `CLAUDE.md` pointer.
- `README.md`, `.gitignore`, MIT `LICENSE`, and `.gitattributes`.
- Migration prompts under `.agents/prompts/`.
- 46 reusable Agent Skill packages under `.agents/skills/`, with a generated catalog.
- A publication mirror for `okhp3-skill-promotion` under `skills/`.

The repository currently does not define a career-fitness algorithm, input or output contract, role data model, user interface, API, external integration, or deployment target. Do not claim that any of those exist until repository evidence is added.

Mission, longer-term vision, primary users, and non-goals are not established by the repository. Treat candidates, recruiters, coaches, or other audiences as possible users only after the owner documents that choice.

## Repository structure

```text
AGENTS.md                         Canonical agent guidance
CLAUDE.md                         Short pointer to AGENTS.md
README.md                         Repository orientation and validation notes
.gitignore                        Generated-artifact ignore rules
LICENSE                           MIT license
.gitattributes                    Text normalization rules
.agents/prompts/                  Project bootstrap and migration prompts
.agents/skills/                   46 packaged Agent Skills and catalog
skills/                           Publication mirror(s)
```

The directories beneath `.agents/skills/` are skill packages, not separate
application services or nested Git repositories. The generated inventory in
`.agents/skills/README.md` is the package list and should be refreshed with the
cataloger when packages are added or removed. The packages include repository
organization, migration, evaluation, authoring, process, brand, and
knowledge-operation skills.

These skills are repository assets. They do not implement the Career Fitness product described above.

## Technology and commands

Confirmed technology:

- Markdown documentation and YAML-like skill front matter.
- Git repository metadata.
- Python, JavaScript, and Node.js scripts bundled inside the skill packages,
  including `.agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py`
  and `.agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs`.

No Career Fitness runtime, application entry point, CI workflow, or deployment
model was found. Some skill packages contain their own deterministic scripts
and tests, but those do not constitute a Career Fitness application test suite
or runtime.

Useful repository checks:

```sh
git status --short
git diff --check
git ls-files
```

When changing the skill cataloger or the package inventory, consult its
`SKILL.md` and use the documented script options. Do not hand-edit generated
catalog sections or metadata.

## Working conventions

- `AGENTS.md` is the canonical project guide. Keep `CLAUDE.md` as a short pointer unless Claude-specific instructions are later required.
- Preserve standalone punchy lines in generated content. Do not consolidate them into paragraphs.
- Follow the ROY principle: explanation should earn its space.
- Do not use em dashes in generated content.
- AutoCAD version is R10, locked and not negotiable, as an inherited OverKill Hill P3 rule. Do not broaden this rule into a product requirement without repository evidence.
- Keep changes focused on the requested scope. Preserve existing user changes and do not use destructive version-control commands.
- Do not add secrets, credentials, private personal information, or machine-specific paths to tracked guidance.
- Treat links to related repositories as context only. Inspect those repositories separately when a task depends on them.

## Safe change procedure

1. Read this file and `CLAUDE.md` before changing repository guidance.
2. Inspect the current tree and worktree status. Preserve unrelated edits.
3. Before introducing implementation, document the intended interface, runtime, data handling, and validation approach from owner-provided requirements or repository evidence.
4. Keep agent-skill changes inside the relevant `.agents/skills/<skill-name>/` package and follow that package's instructions.
5. Re-read every changed guidance file and run `git diff --check` before handoff.

## Known gaps and open questions

The following cannot be resolved from the current repository:

- Whether the intended deliverable is a GPT configuration, prompt pack, agent skill, API application, or another tool format.
- Required inputs, outputs, scoring or gap-analysis method, target-role sources, and acceptance criteria.
- Intended users, integrations, privacy requirements, hosting, and release process.
- Whether this checkout should remain the Career Fitness project or become a
  dedicated Agent Skill migration/distribution workspace.
- Which of the migrated skill packages, prompts, benchmarks, and publication
  mirror are intentionally owned by this repository.

Until those questions are answered, treat this project as an early scaffold and avoid inventing product behavior or operational guarantees.

## Keeping this guide current

Update this file when the repository gains an implementation, manifest, test or validation command, deployment configuration, new top-level boundary, or a confirmed product decision. Record confirmed facts separately from inferences and unknowns. Keep `CLAUDE.md` aligned with this file.

Related repositories:

- [glee-fully-gpt01-discovered-careers](https://github.com/OKHP3/glee-fully-gpt01-discovered-careers)
- [glee-fully-gpt01b-resume-customizer](https://github.com/OKHP3/glee-fully-gpt01b-resume-customizer)

Last reviewed: 2026-08-05

## Imported Claude Cowork project instructions
