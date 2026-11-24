# glee-fully-gpt01a-resume-builder

## Project identity

- **Suite:** Glee-fully / Branch 01
- **Repository:** `https://github.com/OKHP3/glee-fully-gpt01a-resume-builder`
- **Project type:** Content-only GPT resume-builder prototype and sample library. This is confirmed by the repository contents.
- **Current status:** Incomplete or experimental. The repository has no application source, package manifest, test configuration, or deployment configuration. The legacy prompt placeholder was removed during the 2026-08 cleanup because it contained no runnable or substantive prompt content.
- **Repository scope:** One Git repository at the project root. No nested repositories were found.

## Purpose and scope

### Confirmed purpose

The repository collects reusable inputs and examples for a GPT-assisted resume workflow. Its artifacts cover:

- Structured career-data templates and checkpoint formats.
- Resume-writing tone examples and anonymized samples.
- A small industry-to-keyword reference table.
- Three resume presentation styles in Markdown and DOCX examples.
- A placeholder location for an extracted legacy builder prompt.

### Context and lifecycle

This repository is a content and prompt-design branch within the Glee-fully suite. It appears to be a paused or reboot-in-progress prototype rather than an active application: the latest commits update repository guidance and seeded skills, while no executable resume-builder implementation is present. The next meaningful step is TBD and requires owner direction or an audited replacement for the placeholder legacy prompt.

### Inference and unknowns

- **Primary user, inferred:** A job seeker or an agent operator supplying career history and requesting a polished resume.
- **Mission, inferred:** Help turn raw career information into clear, targeted resume content and presentation options.
- **Vision, unknown:** The repository does not state a longer-term product vision.
- **Not demonstrated:** Automated data ingestion, prompt execution, DOCX generation, ATS scoring, web or API delivery, persistence, or production guarantees.

Do not describe this repository as a working service until executable implementation and validation are added.

## Architecture snapshot

- **Inputs:** `inputs/resume-schema-template.md` and the separate `inputs/resume-checkpoint-schema.md` capture candidate career information.
- **Reference layer:** `references/resume-keywords-by-industry.csv` and `references/resume-tone-examples.md` provide editorial guidance and keyword references.
- **Sample library:** `examples/resume-sample-library.md` contains an anonymized sample-library outline.
- **Presentation examples:** `examples/resumes/` contains creative, modern, and traditional resume formats, including the separate checkpoint-family DOCX examples.
- **Execution boundary:** No code, dependency manifest, test harness, deployment target, or generator connects these artifacts.

## Repository map

- `inputs/resume-schema-template.md`: Main career-data and resume-progress template, with fields for experience, education, skills, certifications, languages, extras, and gaps.
- `inputs/resume-checkpoint-schema.md`: Alternate checkpoint example. It uses a different sample person and schema wording; do not assume it is interchangeable with the main template.
- `references/resume-keywords-by-industry.csv`: Small reference map for IT, marketing, healthcare, retail, and construction keywords.
- `references/resume-tone-examples.md`: Summary-section tone examples.
- `examples/resume-sample-library.md`: Anonymized sample-library outline; several entries are still abbreviated.
- `examples/resumes/creative.md`, `examples/resumes/modern.md`, `examples/resumes/traditional.md`: Sample resume outputs in Markdown.
- `examples/resumes/creative.docx`, `examples/resumes/modern.docx`, `examples/resumes/traditional.docx`: DOCX sample outputs corresponding to the primary presentation styles.
- `examples/resumes/checkpoint/jane-smith-creative.docx`, `jane-smith-modern.docx`, `jane-smith-traditional.docx`: Separate checkpoint-family DOCX examples.
- `.agents/skills/`: Seeded local agent skills for skill discovery, Notion capture routing, skill cataloging, and skill creation. These are repository support assets, not the resume-builder runtime.
- `README.md`: Public orientation, status, workflow, content map, and non-goals.
- `CLAUDE.md`: Pointer to this file, `AGENTS.md`.
- `LICENSE`: MIT license for the repository.

## Working model

The intended content workflow is:

1. Gather career information using `inputs/resume-schema-template.md` or an explicitly chosen checkpoint format.
2. Resolve missing, conflicting, or sensitive information before drafting.
3. Use the industry keyword table, tone examples, and sample library as references, not as facts about the candidate.
4. Produce and review resume content in Markdown or an equivalent DOCX presentation.
5. Check that claims, dates, metrics, names, and contact details came from the supplied career data.

There is no verified command that runs this workflow. Treat the DOCX files as checked-in examples, not as outputs generated by a repository script.

## Technology and validation

- **Tracked formats:** Markdown, YAML, CSV, DOCX/OOXML, and plain text.
- **Runtime and dependencies:** None identified. There is no package manager manifest or executable entry point.
- **Build, test, lint, and deploy commands:** None are defined in the repository.
- **Useful checks for documentation-only changes:**
  - `git diff --check`
  - `for f in examples/resumes/*.docx examples/resumes/checkpoint/*.docx; do unzip -t "$f" >/dev/null || exit 1; done` when DOCX package integrity needs checking.

Do not add a claimed command to this file unless it exists in the repository and has been verified.

## Safe change conventions

- Preserve existing user changes and inspect `git status` before editing.
- Keep the root `AGENTS.md` as the canonical project guide. `CLAUDE.md` should remain a short pointer unless Claude-specific instructions are genuinely needed.
- Keep candidate facts separate from editorial guidance. Do not turn sample resume claims into real user data.
- Treat `inputs/resume-schema-template.md` and `inputs/resume-checkpoint-schema.md` as separate formats until their relationship is intentionally reconciled.
- Preserve standalone punchy lines when editing generated resume content.
- Do not add secrets, credentials, private personal information, or unverified production claims.
- Use the repository's existing branch and review process. No project-specific branch naming convention is documented.

## Brand constraints retained from the prior guide

For generated content, the existing project guidance states:

- Do not use em dashes.
- Preserve standalone punchy lines rather than consolidating them into paragraphs.
- Apply the ROY principle: explanation should earn its space.
- AutoCAD version is R10 and is locked when AutoCAD appears in the relevant material.

The current repository does not demonstrate an AutoCAD workflow, so do not introduce AutoCAD content merely because this rule exists.

## Known gaps and risks

- `README.md` does not explain the workflow, inputs, outputs, or validation.
- The sample library is incomplete, and the templates contain fictional sample data.
- The two schema/checkpoint documents contain different examples and field conventions, and remain intentionally separate.
- There is no automated test or generation path, so consistency between Markdown and DOCX examples is manual.
- The prior guide listed related repositories, but their contents were not available locally for this audit: `glee-fully-gpt01-discovered-careers` and `glee-fully-gpt01b-resume-customizer`.

## Keeping this guide current

Update this file when the repository gains executable code, a supported runtime, a generation or validation command, a deployment path, a new input/output contract, or a confirmed change in project status. Record uncertain claims as inferred or unknown until repository evidence or owner direction resolves them.

## Imported Claude Cowork project instructions
