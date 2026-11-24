# glee-fully-gpt02-treasured-finds

## Project identity and status

- Suite: Glee-fully
- Repository: https://github.com/OKHP3/glee-fully-gpt02-treasured-finds
- Branch role: Branch 02, Treasured Finds
- Project root: `/Volumes/OKH-Local/04_GitHub_Mirrors/glee-fully-gpt02-treasured-finds`
- License: MIT, as declared in `LICENSE`
- Status: Confirmed documentation-first repository with an unresolved Treasured Finds planning concept and an active Agent Skill migration/publication workbench. The original planning artifacts were placeholders and have been retired; the current skill surfaces are maintained separately below.
- Lifecycle and activity: Reboot-in-progress / planning and migration stage. The latest commit is `8665a63` (2026-08-05); recent history includes Agent Skill migration support and a 46-package local skill suite.

Mission and vision:

- Inferred mission: develop and organize personal shopping, collecting, and discovery tool concepts for the Glee-fully suite.
- Primary users and business value: not documented. The available artifacts suggest an owner or agent workflow, not a shipped end-user product.
- Vision: unknown. Do not turn the branch name or placeholder plans into a product roadmap.

## Scope and boundaries

This repository currently contains project guidance, migration prompts, reusable local Agent Skills, and a publication mirror for one promoted skill. It does not contain application source code, a service, a product package, a database, or a deployment target.

Keep work in this repository focused on:

- project context and planning documentation;
- migration prompts under `.agents/prompts/`;
- local skill sources under `.agents/skills/` when a skill-specific change is requested;
- the generated publication mirror under `skills/` when promotion work explicitly requires it.

Do not invent runtime behavior, integrations, production guarantees, or domain requirements. No ledger-based project source of truth is present in the current repository. Treat the unresolved Treasured Finds concept as planning-only until authoritative domain material is added and defined.

There is one Git repository at this root and no nested project was found.

## Repository map

- `README.md`: public orientation map for the repository and its two confirmed surfaces.
- `.agents/prompts/`: migration and project-onboarding prompts added for Agent Skill work.
- `.agents/skills/`: 46 tracked local skills, references, assets, evaluations, tests, and helper scripts.
- `.agents/skills/README.md` and `.catalog-meta.json`: generated catalog surfaces; regenerate them with the local skill cataloger rather than editing them manually.
- `skills/okhp3-skill-promotion/`: byte-for-byte publication mirror of the matching local source under `.agents/skills/`.
- `CLAUDE.md`: delegates to this file with `@AGENTS.md`.
- `LICENSE` and `.gitattributes`: repository metadata.

## Architecture snapshot

- Planning layer: the Treasured Finds concept remains unresolved; the original empty ideation, build, directive, and prompt-export checkpoints were retired after approval.
- Migration layer: `.agents/prompts/` contains reusable prompts for project onboarding and GPT-to-Agent-Skill migration.
- Guidance layer: `AGENTS.md` is canonical; `CLAUDE.md` points to it.
- Skill layer: `.agents/skills/` contains reusable local skills, references, assets, evaluations, tests, and helpers. It is supporting tooling, not application runtime.
- Publication layer: `skills/` contains the explicitly maintained publication mirror for `okhp3-skill-promotion`; it is generated output, not a second authoring surface.
- No application entry point, service boundary, data store, or deployment component is present.

## Clarity verdict

AMBIGUOUS for the Treasured Finds concept. The repository identifies the branch theme but does not state the concrete user problem, primary audience, intended workflow, or product vision. The Agent Skill migration and publication workbench purpose is confirmed by recent commits and current files. Do not resolve the Treasured Finds unknowns by inference.

## Technology and runtime

- Confirmed formats: Markdown, YAML, JSON, Python, JavaScript, and CommonJS.
- Confirmed executable material: helper scripts and tests inside the local skills and the publication mirror. They are not the runtime of a Treasured Finds product.
- No application language, framework, dependency manifest, package manager configuration, test framework, CI configuration, or deployment configuration was found.
- No local build, test, lint, or run command is currently defined.

The local skill suite includes repository organization and janitorial workflows, skill authoring and validation, GPT and conversation migration, process capture, evidence and research operations, Glee-fully overlays, and publication support. The generated catalog under `.agents/skills/README.md` is the authoritative inventory for the current 46 packages.

Read the applicable `.agents/skills/<skill>/SKILL.md` before using a local skill. Do not invoke a skill merely because it is present.

## Development and validation

Useful evidence and hygiene checks from the repository root:

```sh
git status --short --branch
git ls-files
rg --files -g '!node_modules' -g '!vendor'
git diff --check
```

Because this is a documentation-first repository, validate changes by re-reading the edited guidance or artifact, checking referenced paths, and confirming that placeholders and lifecycle claims are not presented as implemented behavior. Do not add a build command to this file until a real build system exists and the command has been verified.

## Change conventions

- Preserve existing user changes and use non-destructive Git operations.
- Keep `AGENTS.md` as the canonical agent guide. Update `CLAUDE.md` only if its pointer or Claude-specific instructions become inaccurate.
- No branch naming or release workflow is documented locally. Do not assume one when creating branches, tagging, or publishing.
- Keep generated content free of em dashes. Preserve standalone punchy lines where they are intentional. Follow the OverKill Hill P3 ROY principle: explanation should earn its space.
- If AutoCAD artifacts are ever introduced, the inherited suite rule requires AutoCAD R10. No AutoCAD artifacts are present today.
- Do not add secrets, private connector identifiers, or unnecessary machine-specific paths to tracked files.
- When adding project behavior, add the smallest supporting documentation, validation command, and status update needed to make the new behavior verifiable.

## Known gaps and risks

- The product purpose is only partially specified. The branch name and existing purpose statement support the shopping, collecting, and discovery theme, but user workflows are not defined.
- The Treasured Finds concept remains unresolved. The repository is not ready to be described as a working product.
- The original project directive named a ledger-based source of truth, but none of its named ledger files existed; that obsolete directive was removed after approval.
- The Treasured Finds product purpose remains unresolved. The current repository also has a distinct, confirmed Agent Skill migration purpose.
- Skill structural validation exists, but it does not prove task quality, runtime behavior, deployment, or canonical publication.

## Keeping this guide current

Update this file when the repository gains an executable product, a dependency or build manifest, CI, deployment, authoritative domain sources, a confirmed product mission, or a changed skill-source/mirror contract. Record only facts that can be supported by files or verified commands. Keep unknowns labeled as unknown rather than filling them with assumptions.

## Related Glee-fully repositories

- [glee-fully-gpt02a-personal-librarian](https://github.com/OKHP3/glee-fully-gpt02a-personal-librarian)
- [glee-fully-gpt02b-decor-detective](https://github.com/OKHP3/glee-fully-gpt02b-decor-detective)
- [glee-fully-gpt02c-present-hoarder](https://github.com/OKHP3/glee-fully-gpt02c-present-hoarder)
- [glee-fully-gpt02d-scentinal-journal](https://github.com/OKHP3/glee-fully-gpt02d-scentinal-journal)
- [glee-fully-gpt02e-spirited-journal](https://github.com/OKHP3/glee-fully-gpt02e-spirited-journal)
- [glee-fully-gpt02f-supply-haus](https://github.com/OKHP3/glee-fully-gpt02f-supply-haus)
- [glee-fully-gpt02g-bag-nabbit](https://github.com/OKHP3/glee-fully-gpt02g-bag-nabbit)

## Imported Claude Cowork project instructions
