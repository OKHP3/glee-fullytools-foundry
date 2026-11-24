# glee-fully-gpt01e-blinkin-tuner

## Project identity

- **Suite:** Glee-fully / Branch 01
- **Repository:** `https://github.com/OKHP3/glee-fully-gpt01e-blinkin-tuner`
- **Declared product label:** 01e, bLinkIn Tuner
- **Repository type:** Git repository containing documentation and seeded agent skills
- **Current status:** Scaffold or pre-implementation. No application runtime is present in this checkout.
- **License:** MIT, copyright OverKill Hill P³, 2026
- **Notion anchor:** `https://app.notion.com/p/f2111beaf2324e349cfed82b9862078a`

## Purpose, mission, and vision

- **Declared purpose:** The prior project guide describes this as a tool for optimizing LinkedIn profiles and content for visibility and relevance. This purpose is not implemented or explained in the current README, so treat it as product context rather than a verified runtime capability.
- **Intended users:** Unknown. The repository does not document a user persona, operating model, or supported LinkedIn workflow.
- **Mission:** Unknown. Do not infer a business mission from the repository name alone.
- **Vision:** Unknown. Do not turn the Notion link or related repository names into roadmap claims without supporting project evidence.
- **Scope boundary:** Work in this repository concerns project guidance, documentation, and the seeded agent-skill content unless the owner explicitly adds or requests an application implementation.

## Repository structure

The tracked top level is intentionally small, but the substantive content is a
seeded Agent Skills library rather than an application:

- `README.md`: Public orientation for the seeded-skill scaffold and its current limits.
- `AGENTS.md`: Canonical guidance for agents working in this repository.
- `CLAUDE.md`: Short compatibility pointer to `AGENTS.md`.
- `LICENSE`: MIT license.
- `.gitattributes`: Enables text auto-detection and LF normalization.
- `.gitignore`: Excludes generated Python bytecode and local operating-system files.
- `.agents/prompts/`: Project onboarding, context bootstrap, and GPT-to-skill migration prompts.
- `.agents/skills/`: Seeded local skills and supporting assets, references, scripts, evaluations, benchmarks, and Claude command files.
- `skills/okhp3-skill-promotion/`: A byte-for-byte publication mirror of the local `okhp3-skill-promotion` package. It is managed output, not a second authoring location.

No nested Git repositories or nested instruction files were found. No application source directory, database schema, or deployment configuration is present. The repository does contain generated catalog metadata, benchmark records, and historical evaluation workspace files within the seeded skills.

## Technology and architecture

- **Confirmed:** Git, Markdown, JSON, and Python files are present in the seeded skill materials.
- **Not confirmed:** No application language, framework, package manager, runtime, API integration, LinkedIn integration, data store, or deployment target is defined.
- **Architecture:** There is no implemented product architecture to extend. The current repository is a documentation and capability-seeding layer. Do not describe the seeded skill scripts as a product runtime or public interface.
- **Publication model:** `.agents/skills/` is the local skill source surface. The top-level `skills/` path is retained only where a package has an intentional publication mirror and must not be edited independently.
- **Entry points:** No application entry point or supported run command is documented. The scripts under `.agents/skills/` belong to their respective skills and should be used only according to those skill instructions.

## Development and validation

No build, test, lint, package-install, or deployment commands are defined by the repository. Do not invent commands or claim production readiness.

For documentation-only changes, use the following baseline checks from the repository root:

```sh
git status --short --branch
git ls-files
find . -path './.git' -prune -o -type f -print | sort
```

When implementation is added, update this file and `README.md` with verified setup, run, test, lint, build, and deployment commands. Validate commands in the actual supported environment before documenting them.

## Change conventions

- Preserve existing user changes and do not use destructive version-control commands.
- Keep `AGENTS.md` as the canonical project guide. Update `CLAUDE.md` only when its pointer or any future Claude-specific instruction needs to change.
- Keep the seeded `.agents/skills/` content within its existing scope. Read a skill's `SKILL.md` before modifying that skill or its assets.
- Use evidence from repository files and executable checks. Label conclusions as confirmed, inferred, or unknown when the distinction matters.
- Do not add secrets, credentials, private personal information, or machine-specific paths to tracked guidance.
- There is no repository-specific branch or naming policy recorded. Follow the active task workflow and document a policy here only when the owner establishes one.

## Brand and content rules

- Do not use em dashes in generated content.
- Preserve standalone punchy lines. Do not consolidate them into paragraphs.
- Follow the ROY principle: explanation should earn its space.
- AutoCAD version is R10 and is locked. No AutoCAD integration is present in this repository, so do not imply one exists.

## Related context

The prior guide names these related repositories, but their relationship is not validated by this checkout:

- `https://github.com/OKHP3/glee-fully-gpt01-discovered-careers`
- `https://github.com/OKHP3/glee-fully-gpt01f-career-seeker`

Treat these links and the Notion anchor as pointers for future owner-led discovery, not as implementation dependencies.

## Known gaps and open questions

- The README does not yet describe the repository's seeded-skill purpose, users, workflows, setup, or status.
- The relationship between the broad seeded skill library and the declared bLinkIn Tuner product label is unresolved.
- The product implementation, if it exists elsewhere, is not represented in this repository.
- The intended LinkedIn inputs, outputs, integrations, privacy model, and success measures are undocumented.
- The supported runtime, test strategy, deployment model, and ownership workflow are unknown.
- The owner should resolve these questions before implementation or external capability claims are added.

## Keeping this guide current

Update this file whenever the repository gains an application runtime, a supported command, a deployment path, a new instruction scope, or a confirmed product decision. Keep statements tied to current repository evidence and retain uncertainty labels for facts that remain unresolved.

## Imported Claude Cowork project instructions
