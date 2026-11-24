# glee-fully-gpt01f-career-seeker

## Project identity

- Suite: Glee-fully, Branch 01
- Repository: `https://github.com/OKHP3/glee-fully-gpt01f-career-seeker`
- Declared purpose: 01f Career Seeker, a job-search strategy and opportunity-discovery assistant.
- Current implementation status: early scaffold and Agent Skills workbench. The repository contains reusable Agent Skills and supporting documentation, not a runnable career-search application.
- License: MIT, as declared in `LICENSE`.

## Mission and scope

The declared mission is to support career seekers with job-search strategy and opportunity discovery.

The current repository scope is broader than a career-search runtime and is confirmed by its contents:

- Store reusable Agent Skills for future career-seeker and surrounding OKHP3 workflows.
- Provide skill-specific references, assets, scripts, evaluation cases, and project prompts.
- Support Agent Skill discovery, authoring, evaluation, promotion, cataloging, Notion capture, and repository operations.

No implemented search provider, ranking model, user interface, data store, external API integration, or production deployment is present in this repository.

Longer-term product vision is not documented here and should not be inferred from the repository name alone.

## Repository structure

- `AGENTS.md`: canonical guidance for repository agents.
- `CLAUDE.md`: short pointer to this file for Claude-specific workflows.
- `.agents/prompts/`: project onboarding, context bootstrap, and GPT-to-skill migration prompts.
- `.agents/skills/`: 46 local runtime skill packages, each self-contained with its own instructions and supporting resources.
- `.agents/skills/README.md`: generated catalog of the local skill packages.
- `skills/`: publication mirrors only for packages that have an explicit promotion workflow. It is not a second authoring surface.
- `LICENSE`: MIT license.
- `README.md`: public orientation for the current Agent Skills workbench and its career-seeker association.

Each skill directory is self-contained. Read its `SKILL.md` before changing that skill, and load its referenced assets or reference files only when the task requires them.

## Technology and entry points

Confirmed technology is Markdown-based Agent Skills with supporting JSON, YAML, HTML, JavaScript, and Python files. The cataloger explicitly requires Python 3.9 or newer and standard-library dependencies only.

The verified catalog validation command is:

```bash
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check
```

Foundry structural validation is available at `.agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs`. The publication mirror checker is available at `skills/okhp3-skill-promotion/scripts/sync_skill_mirror.py`.

There is no verified application start command, build command, unified test suite, lint configuration, CI workflow, or deployment command. Do not invent one.

## Working conventions

- Treat `AGENTS.md` as the canonical project guide. Keep `CLAUDE.md` as a short pointer unless genuinely Claude-specific instructions are needed.
- Make the smallest scoped change. Preserve existing user edits and do not use destructive version-control commands.
- Do not modify application code, dependencies, generated artifacts, secrets, CI behavior, or unrelated files when maintaining project context.
- For skill changes, preserve YAML frontmatter, keep `name` aligned with the skill directory, and update directly related references or assets when required.
- Use the bundled cataloger script rather than manually rebuilding a skills index.
- Treat `.agents/skills/` as the runtime source surface. Treat any matching path under `skills/` as a managed publication mirror and compare it before changing either surface.
- Do not commit private Notion anchors, database IDs, credentials, or connector-only resource IDs. The Notion capture skill defines a private-anchor workflow for those values.
- Use standalone punchy lines where they carry emphasis. Keep explanations proportional to their value.
- Do not use em dashes in generated content.

## Validation and change safety

Before changing a skill or its guidance:

1. Check `git status` and preserve unrelated work.
2. Read the applicable `SKILL.md` and any directly referenced instructions.
3. Run the cataloger check above when the skill inventory or frontmatter may be affected.
4. Re-read every changed guidance file and verify referenced paths.

For documentation-only changes, validate links and commands that can be checked locally. Since no application runtime or unified automated test suite exists, report that limitation instead of implying broader validation.

The repository currently exposes only the `main` branch locally and tracks `origin/main`. No branching or commit-message convention is documented by repository evidence.

## Related context

- Related repository: `https://github.com/OKHP3/glee-fully-gpt01-discovered-careers`
- Related repository: `https://github.com/OKHP3/glee-fully-gpt01e-blinkin-tuner`
- A Notion project anchor is referenced by historical guidance, but private Notion links must not be copied into new committed content.

## Known gaps and open questions

- The actual career-seeker product behavior, users, interfaces, integrations, and data model are not documented in the repository.
- The project status beyond early scaffold is not formally recorded by the owner.
- The repository contains 46 local packages, while package maturity, intended retention, and career-seeker relevance vary.
- The Foundry workspace and historical benchmark records are retained evidence, not current performance proof.
- Whether all imported general-purpose skills should remain in this career-seeker-associated repository is an owner decision.

## Keeping this guide current

Update this file when the repository gains a runtime, application entry point, test or CI workflow, deployment target, new scope boundary, or a materially different purpose. Base updates on checked-in files or executable checks, and label unresolved owner decisions as open questions rather than filling them with assumptions.

## Imported Claude Cowork project instructions
