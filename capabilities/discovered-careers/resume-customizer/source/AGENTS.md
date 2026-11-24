# glee-fully-gpt01b-resume-customizer

## Project identity

- Suite: Glee-fully, Branch 01
- Type: GPT Tool-ette with documentation and reference data
- Repository: https://github.com/OKHP3/glee-fully-gpt01b-resume-customizer
- Notion anchor: https://app.notion.com/p/37ee9421e9dc429c8358b10f30e1e265
- Current status: Documentation-only prototype, based on the tracked files and the absence of an application manifest, runtime entry point, or test configuration.

Related repositories:

- https://github.com/OKHP3/glee-fully-gpt01-discovered-careers
- https://github.com/OKHP3/glee-fully-gpt01a-resume-builder
- https://github.com/OKHP3/glee-fully-gpt01c-career-fitness

## Mission and users

- Repository-evidenced purpose, inferred: support tailoring an existing resume to a specific job description and ATS requirements through reference material.
- Primary users, inferred: job seekers preparing targeted applications.
- Longer-term vision, inferred: provide a repeatable resume-tailoring workflow that combines job-specific keywords, credible experience, and an appropriate professional tone.

The repository does not yet implement that workflow. It currently supplies reference material that could support it.

## Scope and boundaries

In scope:

- Anonymized resume examples
- Professional-summary tone examples
- Industry keyword reference data
- Agent guidance and bundled reusable skills under `.agents/skills/`

Not currently evidenced in this repository:

- A user interface, API, chatbot configuration, or executable tailoring engine
- Resume or job-description parsing
- ATS scoring or validation
- Resume document generation or export
- External integrations, deployment configuration, or production guarantees

Do not infer these capabilities from the project name. If implementation is added, update this file with the actual entry points and validation commands.

## Repository structure

- `README.md`: repository orientation and start-here map.
- `references/resume-sample-library.md`: anonymized sample resume content.
- `references/resume-tone-examples.md`: summary-section tone examples.
- `references/resume-keywords-by-industry.csv`: industry-to-keyword reference data with columns `Industry` and `Keywords`.
- `.agents/skills/`: bundled agent skills, including discovery, Notion capture, skill cataloging, and skill creation assets. Read the relevant skill's `SKILL.md` before using or changing it.
- `skills/`: publication mirrors for selected local skills, when present.
- `.gitattributes` and `.gitignore`: repository-level Git and generated-file handling.
- `CLAUDE.md`: short pointer to this file for Claude-compatible agents.
- `LICENSE`: repository license.

No nested Git repositories or independent application projects were found in the project tree. The `.agents/skills/` content is repository tooling, not a separate product.

## Technology and runtime

The project content is Markdown, CSV, and plain-text guidance. There is no package manifest, dependency lockfile, build configuration, test configuration, deployment configuration, or application source directory. Some bundled skill utilities are Python scripts, but no Python runtime is required by the resume reference content itself.

The intended data flow is only an inference from the project purpose: existing resume plus target job description, followed by keyword-aware and tone-aware tailoring. No executable pipeline currently exists.

## Working conventions

- Work from the repository root and preserve unrelated user changes.
- Make guidance and reference-data edits focused and reviewable.
- Keep anonymized examples free of secrets and unnecessary personal information.
- Preserve valid CSV structure. Keep comma-containing keyword lists quoted.
- Preserve standalone punchy lines when editing prose. Do not consolidate them into paragraphs.
- Apply the OverKill Hill P3 ROY principle: explanation should earn its space.
- Do not use em dashes in generated content.
- AutoCAD version is R10 when that inherited brand constraint is relevant.
- Ordinary reference-data filenames use lowercase kebab-case. No formal branch or commit convention is documented. The observed branch is `main`, tracking `origin/main`.

## Validation

Verified repository checks:

```text
git status --short --branch
git ls-files
git log --oneline --decorate -12
git diff --check
```

The repository has no project-specific build, test, lint, or development-server command. For changes under `.agents/skills/`, follow the validation instructions in that skill's `SKILL.md`.

## Known gaps and open questions

- The product implementation status beyond this reference repository is unknown.
- The intended GPT configuration, input and output contract, ATS methodology, and deployment surface are not represented in the tracked files.
- Ownership, release process, branch policy, and contribution workflow are not documented here.

## Keeping this guide current

Update this file when the repository gains or removes runtime code, dependencies, interfaces, integrations, tests, deployment paths, or formal contribution conventions. Label conclusions as confirmed or inferred when repository evidence is incomplete. Keep `CLAUDE.md` as a short pointer unless Claude-specific instructions are genuinely needed.

---

Last reviewed: 2026-08-06
Evidence reviewed: tracked files, repository metadata, recent Git history, and bundled skill guidance.

## Imported Claude Cowork project instructions
