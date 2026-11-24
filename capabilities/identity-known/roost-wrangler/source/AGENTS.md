# glee-fully-gpt07b-roost-wrangler

## Project identity

- Suite: Glee-fully, Branch 07.
- Project label: 07b, Roost Wrangler.
- Repository: `OKHP3/glee-fully-gpt07b-roost-wrangler`.
- GitHub: <https://github.com/OKHP3/glee-fully-gpt07b-roost-wrangler>.
- Notion anchor recorded by the existing project guidance: <https://app.notion.com/p/e97fa7c1eebe4b408ec73a3e4991f763>.
- Project status: unknown. The checkout is a documentation and agent-tooling skeleton, not a working application.

## Purpose and scope

The existing project description identifies Roost Wrangler as a bird identification and backyard birding assistant. This purpose is inherited guidance, not currently demonstrated by source code, product documentation, or executable behavior in the repository.

- Confirmed scope: this Git repository and its tracked documentation and `.agents/skills` content.
- No nested Git repositories or independent application packages were found.
- No application source, data model, integrations, deployment configuration, or runtime entry point is present.
- Mission, vision, target users, supported birding workflows, and non-goals are not documented well enough to state as facts.

Do not infer product behavior or production readiness from the repository name alone.

## Repository layout

- `README.md`: evidence-based project overview, status, repository contents, development constraints, and open questions.
- `LICENSE`: MIT license, copyright 2026 OverKill Hill P³.
- `AGENTS.md`: canonical repository guidance.
- `CLAUDE.md`: short pointer to this file.
- `.agents/skills/`: seeded agent skills, references, assets, scripts, and Claude command files. This is repository metadata, not application runtime code.
- `.gitattributes`: text normalization configuration.

## Technology and commands

No language, framework, package manager, dependency manifest, build system, test runner, linter, local server, or deployment target is present. Consequently, no application run, build, test, lint, or deployment command has been verified.

The repository is a single Git repository. The checked-out `main` branch tracks `origin/main`. No branch naming or release convention is documented beyond that fact.

## Safe change guidance

- Treat this as a context and documentation skeleton until implementation evidence appears.
- Preserve existing user changes and do not use destructive version-control commands.
- Before adding product code, document the chosen runtime, entry point, development commands, validation checks, and deployment model in this file and in `README.md`.
- Keep claims labeled as confirmed, inferred, or unknown when repository evidence is incomplete.
- Do not add secrets, credentials, private personal information, or machine-specific paths.
- Do not modify `.agents/skills` content unless the task specifically concerns those skills.

## Organization and brand guidance

The following rules were retained from the existing project guidance. They are organization-level conventions and are not otherwise evidenced by repository files:

- Do not use em dashes in generated content.
- Preserve standalone punchy lines. Do not consolidate them into paragraphs.
- Follow the ROY principle: understanding produced and explanation invested. Verbosity must earn its space.
- AutoCAD version is R10, locked and not negotiable, if AutoCAD content is ever added.

## Validation for guidance changes

For changes to this file or other repository guidance:

1. Re-read every changed guidance file.
2. Confirm referenced paths exist.
3. Run `git diff --check`.
4. Run `git status --short --branch` and review the diff for unrelated changes.

There are currently no project tests or build checks to run.

## Known gaps and open questions

Urgent context gaps:

- Is the project active, in development, archived, or on hold?
- What runtime, framework, model or API dependencies, and user interface are intended?
- Who are the target users, and what bird identification or backyard birding workflows are in scope?
- What are the development, test, deployment, and release commands once implementation begins?

Optional documentation improvements:

- Add a README with the product brief, current status, setup instructions, and validation commands.
- Record the relationship to `glee-fully-gpt07-identity-known` if the repositories share code, data, or workflow contracts.

## Keeping this file current

Update this guide when source code, manifests, commands, integrations, deployment configuration, project status, or repository conventions change. Replace unknowns only when repository evidence or an explicit owner decision supports the new statement.

## Imported Claude Cowork project instructions
