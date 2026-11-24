# glee-fully-gpt02e-spirited-journal

## Project identity

- Suite: Glee-fully, Branch 02
- Repository: `https://github.com/OKHP3/glee-fully-gpt02e-spirited-journal`
- Type: GPT tool-ette or prompt-focused project, based on the repository name and the bundled prompt record
- Root: `/Volumes/OKH-Local/04_GitHub_Mirrors/glee-fully-gpt02e-spirited-journal`
- License: MIT, Copyright 2026 OverKill Hill P3
- Current status: Scaffold or pre-development. No working product application, product runtime, product test suite, deployment configuration, or active product implementation is present in the repository.

## Purpose and boundaries

The declared project purpose is 02e Spirited Journal: discovery of spirits such as whiskey and wine, tasting notes, and collection tracking. The repository does not yet contain an implementation of those workflows, so treat this as a declared direction rather than a confirmed product capability.

Mission, vision, target users, business value, data model, integrations, and deployment model are not established by repository evidence.

Do not infer an application stack or build commands from the project name. Do not add application code, dependencies, services, secrets, CI behavior, or generated artifacts as part of documentation maintenance. If implementation work is requested, first establish the intended runtime and product scope with the owner.

## Repository layout

- `README.md`: repository orientation and current status.
- `prompts/drafts/02e-glee-fully-spirited-journal_prompts_v1.yaml`: a five-field placeholder record. It identifies the prompt set as version 1, marks it as a processing draft, and says it awaits audit. It is not an application configuration or executable workflow.
- `prompts/`: product prompt material, currently containing only the draft record under `prompts/drafts/`.
- `.agents/prompts/`: project onboarding, context, and migration prompts.
- `.agents/skills/`: bundled agent guidance and utilities, separate from product functionality.
  - `okhp3-notion-capture-router`: routes AI conversation material into Notion when the required connector and private anchors are available.
  - `okhp3-skill-cataloger`: catalogs skills in a project or skills distribution repository.
- `skills/okhp3-skill-promotion/`: publication mirror of the corresponding bundled skill, including its own tests.
- `docs/handoffs/`: task-specific audit and continuation records, when present.
- `CLAUDE.md`: points to this file with `@AGENTS.md`.
- `.gitattributes`: enables automatic text detection and LF normalization.
- `LICENSE`: MIT license.

There are no Git submodules. No product package manifest, application entry point, product test configuration, deployment files, or repository-level CI workflows are currently present. Bundled skills have their own manifests, scripts, and tests.

## Technology and commands

Repository content includes Markdown, YAML, JSON, and bundled Python and JavaScript utilities. No product runtime or dependency manager is configured.

Useful verified checks from the repository root:

```text
git status --short --branch
git rev-parse --show-toplevel
git log -8 --oneline --decorate
git submodule status
ruby -e 'require "yaml"; YAML.load_file("prompts/drafts/02e-glee-fully-spirited-journal_prompts_v1.yaml")'
```

The YAML parse check succeeds. The Git checks confirm that the root is the repository listed above, the current branch is `main` tracking `origin/main`, and no submodules are configured.

The cataloger utility can be used when the explicit task is to catalog bundled skills:

```text
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills
```

That command updates generated catalog output and should not be run for ordinary project-context maintenance.

There is no verified application run, test, lint, build, or deployment command yet.

## Working conventions

- Keep this file as the canonical repository guidance. `CLAUDE.md` should remain a short pointer unless Claude-specific instructions are genuinely needed.
- Preserve standalone punchy lines in project content. Do not consolidate them into paragraphs merely for stylistic uniformity.
- Do not use em dashes in generated content.
- Apply the ROY principle: explanation should earn its space and improve understanding.
- If AutoCAD material is ever added, use R10 as the locked version specified by the project guidance.
- No repository-specific branch naming or commit convention has been documented. Preserve the existing branch strategy and inspect current history before introducing one.
- Treat the YAML prompt record as draft material. Do not promote its placeholder text into product requirements without an audit.
- Keep private Notion anchors and connector-only identifiers out of committed public skill content. Use local or connector-provided context when a Notion workflow requires them.

## Safe change procedure

1. Read this file and any more specific guidance in the target path before editing.
2. Check `git status --short` and preserve unrelated user changes.
3. Confirm whether a requested change concerns repository guidance, bundled skills, prompt metadata, or future application code. Keep those scopes separate.
4. Prefer small, reviewable edits. Do not rewrite prompt records or bundled skill resources without a task that specifically calls for it.
5. Re-read changed guidance and run the narrowest relevant validation check.
6. Update this file when confirmed project structure, commands, status, or conventions change.

## Known gaps and open questions

The following require owner input or future repository work:

- Whether the intended deliverable is a prompt library, an agent skill, a web application, or another GPT tool-ette.
- The intended runtime, framework, dependency manager, local development workflow, and deployment target.
- The target users and the authoritative requirements for discovery, tasting notes, and collection tracking.
- Whether the project is active, on hold, archived, or still in planning. The repository currently supports only the scaffold or pre-development assessment.
- The role of the related `glee-fully-gpt02-treasured-finds` repository and the intended boundary between the two projects.
- Whether the placeholder prompt record should be audited, replaced, or retained as historical draft material.

## Imported Claude Cowork project instructions
