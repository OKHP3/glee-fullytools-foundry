# Technology Stack and Version Review

Reviewed: 2026-07-20

## Scope

This repository is a documentation and Agent Skill repository. It does not contain a web application, package manifest, build system, deployment configuration, or runtime service. References to TypeScript, JavaScript, Vite, Tailwind, React, Java, and similar technologies were not found as implemented technologies in the repository.

The Pulsebook contains historical GPT metadata and future integration ideas. Those references are recorded below only as documentation context, not as installed dependencies.

## Implemented technologies

| Technology | Evidence in this repository | Version in use | Latest stable checked 2026-07-20 | Status and update path |
| --- | --- | --- | --- | --- |
| Markdown | `.md` documentation, Agent Skill instructions, and embedded code samples | Not pinned. The repository uses ordinary Markdown with GitHub-style conventions | CommonMark 0.31.2 | Documentation format. Review manually when the renderer or Markdown standard changes |
| YAML | Agent Skill frontmatter and retained historical references to prompt exports | Not pinned. No active root prompt-export file or YAML library is packaged here | YAML 1.2, specification revision 1.2.2 | Data format. Review manually when the parser or schema changes |
| JSON | Agent Skill assets, including evaluation queries and catalog metadata schemas | Not pinned. No JSON runtime dependency is packaged here | RFC 8259 / ECMA-404 alignment | Data format. Review manually when a consuming tool changes its JSON contract |
| Python | Helper scripts under `.agents/skills/` | Python 3.9+ is documented as the minimum. No interpreter version is pinned | Python 3.14.6 | Runtime for maintenance tooling. Pin a supported Python version in CI when a workflow is added |
| Git | Repository version control | Not pinned by the repository. Local environment: Git 2.55.0.windows.2 | Git 2.55.0 | Developer tool. Keep local installations current; no repository dependency lock is available |
| Ruby YAML parser | Mentioned by the repository validation guidance as a way to parse the prompt YAML files | Not part of the repository runtime and not installed in the current environment | Ruby latest stable not tracked because Ruby is not a repository dependency | Validation-only reference. Replace with a pinned CI parser if YAML validation becomes automated |
| GitHub | Remote hosting and expected future automation platform | No Actions workflow exists today | Dependabot supports current GitHub Actions version updates | No root update job is configured while its required input is absent. Add scoped maintenance when a real manifest or workflow is introduced. |

## Explicitly not implemented

The repository contains no evidence of the following technologies being used by the current solution:

- TypeScript
- JavaScript as an application/runtime language
- Node.js or npm
- Vite
- Tailwind CSS
- React
- Java
- Docker
- Terraform
- A Python package dependency or lock file

The word “JavaScript” appears only in external standards context when discussing JSON, not as source code in this repository.

## Historical or aspirational platform references

The Pulsebook includes GPT-4 in one metadata section and GPT-5 in another. It also describes OpenAI GPTs, APIs, and future integrations. These are product documentation references, not locally installed versions. They should not be used as the current runtime inventory without owner confirmation.

## Sources for latest stable versions

- Python 3.14.6: https://www.python.org/downloads/release/python-3146/
- Git 2.55.0: https://git-scm.com/install/
- CommonMark 0.31.2: https://spec.commonmark.org/
- YAML 1.2.2 specification revision: https://yaml.org/spec/1.2.2/
- JSON RFC 8259: https://www.rfc-editor.org/rfc/rfc8259
- Dependabot version updates for GitHub Actions: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions

## Maintenance policy

1. Keep this file as the human-readable inventory and record the review date whenever the repository gains a runtime or package manager.
2. Add a real manifest and lock file before treating a new runtime dependency as implemented. Examples are `package.json` plus a lock file for Node.js, or `requirements.txt`/`pyproject.toml` plus a lock strategy for Python.
3. Dependabot monitoring is inactive because no root workflow or dependency manifest exists. When one is introduced, add a matching, scoped update job and validate that it finds its inputs. Any resulting pull request still requires review and validation.
4. For standards such as Markdown, YAML, and JSON, record the specification or renderer version used by CI once one is selected. Standards are not package dependencies and cannot be safely auto-updated by Dependabot alone.
5. Do not convert historical GPT model labels or future integrations into runtime dependencies without a confirmed implementation and owner decision.

## September 20, 2026 maintenance correction

All four root Dependabot jobs failed with `dependency_file_not_found`: npm
run 34931898998, pip 34931898826, Docker 34931898858, and Actions 34931898812.
The configured root contains no package.json, Python dependency manifest,
Dockerfile, action.yml, or workflow. Removed those invalid jobs. This does not
change repository security settings or disable an existing application update
path. Add a narrowly scoped update entry alongside the actual manifest when
one is introduced; bundled Agent Skill examples are separate support assets.
