# glee-fully-gpt00-personalizable-tools

## Project identity and status

- Suite: Glee-fully
- Role: GPT00 root documentation and prompt-asset repository
- GitHub: https://github.com/OKHP3/glee-fully-gpt00-personalizable-tools
- Repository type: single Git repository; no nested repositories or submodules were found
- Current status: active documentation and agent-tooling maintenance
- Product runtime status: not verifiable here; no application runtime, root package manifest, CI workflow, or deployment configuration is present

## Purpose, mission, and vision

### Confirmed

This repository stores the root toolbox documentation for the Glee-fully personalizable tools suite. Its tracked assets include legacy GPT instructions, a GPT Pulsebook, and reusable local Agent Skills. The former YAML prompt-export placeholders were retired after review.

The documented GPT concept is a joyful navigation hub that helps users understand the suite and choose a Tool, Tool-ette, Function, or Function-ette. The Pulsebook names careers, collections, food, travel, life, health, and identity as example suite branches.

### Inferred

The repository's practical mission is to preserve and organize the suite's prompt and operating knowledge so future maintainers and agents can update the root toolbox consistently.

The longer-term vision in the Pulsebook is a broader, personalized suite with cross-tool coordination and additional integrations. Treat that material as historical or aspirational unless a current artifact verifies implementation.

## Scope and boundaries

In scope:

- GPT00 prompt, instruction, ideation, build, and Pulsebook documentation under `docs/gpt00/` and `archive/legacy/`
- Historical YAML prompt-export placeholders and their retirement status
- Root agent guidance and the local `.agents/skills/` packages
- Documentation of suite structure, routing concepts, and related repositories

Out of scope for this repository:

- A user-facing application or service implementation
- Production GPT Builder deployment, telemetry, analytics, or support operations
- The canonical `dataLedger_*v2.txt` files referenced by legacy instructions, which are absent here
- External integrations, credentials, private anchors, and unrelated repositories

Do not turn future plans in the Pulsebook into current capabilities. Do not assume that a named ledger, GPT link, API, or tool exists merely because a document references it.

## Repository structure

- `archive/legacy/00a-glee-fully-personalizable-tools_instructions.md`: retained legacy project directive and placeholder for domain-specific instructions.
- `docs/gpt00/00a-glee-fully-personalizable-tools_pulsebook_20250907.md`: large historical and aspirational GPT Pulsebook.
- `archive/legacy/00b-glee-fully-function-ettes_instructions.md`: retained legacy 00b project directive.
- `.agents/skills/`: 46 Agent Skill packages covering repository maintenance, skill discovery and creation, Custom GPT readiness/build/conversion, process and evidence work, migration, Notion capture, skill cataloging, and cross-platform thread-context extraction. Evaluation workspaces and benchmarks remain inside their owning packages and are not additional skill packages.
- `README.md`: currently only identifies the repository by name.
- `CLAUDE.md`: delegates to this file with `@AGENTS.md`.
- `docs/TECHNOLOGY_STACK.md`: reviewed inventory of implemented formats and maintenance runtimes.
- Dependabot jobs for absent root manifests and workflows were removed on September 20, 2026. Add an ecosystem only when its actual manifest or workflow exists at the configured path.

There is no root `package.json`, `pyproject.toml`, `Makefile`, root `scripts/` directory, GitHub Actions workflow, or application source tree.

## Technology and runtime

- Primary formats: Markdown, YAML, and JSON.
- Local Agent Skills use Markdown frontmatter and instructions. Some include Python or JavaScript helper scripts and package-specific manifests.
- The cataloger skill documents Python 3.9+ for its script. The skill-suite validator runs on Node.js. The repository does not pin a root Python or Node.js runtime.
- No root build, test, lint, server, or deployment runtime was found.

## Working conventions

- Preserve the 00a and 00b identifiers on retained historical records and distinguish archived directives from the active Pulsebook.
- The former v1 YAML prompt-export placeholders were retired on 2026-08-05 because they contained no audited prompt content.
- Treat the archived project directive files as legacy reference material. They refer to absent `dataLedger_*v2.txt`, `registry_v2.txt`, `persona_v2.txt`, `parameters_v2.txt`, `narrative_v2.txt`, `archive_v2.txt`, and `system_v2.txt` files.
- Use the actual nested cataloger path, `.agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py`. References inside the skill package to a root `scripts/` path do not match this repository layout.
- Inherited OverKill Hill P3 content rules: no em dashes in generated content; preserve standalone punchy lines; apply the ROY principle so explanation earns its length; AutoCAD version is R10 when that subject is relevant.
- No branch naming policy is documented. The observed default branch is `main`. Preserve existing user changes and avoid destructive version-control operations.

## Verified validation commands

Run these from the repository root:

```sh
git status --short --branch
git log -8 --oneline --decorate
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --check --skills-dir .agents/skills
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs --skills-dir .agents/skills
```

The cataloger check currently validates 46 skills while the generated project catalog indexes 12 selected skills. The suite validator passes all 46 packages with advisory warnings only. These checks do not establish that every evaluation fixture is production-ready.

The former root YAML prompt-export placeholders were retired after review. No root test, lint, build, or deployment command is available to run.

The cataloger can write generated catalog files. Use `--check` or `--dry-run` for inspection unless the user explicitly requests a catalog refresh and accepts those generated-file changes.

## Safe change procedure

1. Read this file and any more-specific guidance before editing.
2. Inspect the relevant prompt or skill source and preserve historical context when it is clearly labeled.
3. Keep confirmed facts, inferences, historical claims, and open questions separate.
4. Limit context-maintenance work to guidance and relevant repository metadata. Do not modify product code, dependencies, generated artifacts, secrets, CI behavior, or unrelated files.
5. Re-read every changed guidance file and rerun the narrowest applicable validation command.
6. Check `git diff` and `git status` before reporting the work.

## Known gaps and open questions

- The repository README does not explain the project beyond its name.
- The current product deployment, owner workflow, and production status cannot be confirmed from local evidence.
- The canonical ledger files named by the project directives are missing.
- The 00a and 00b prompt-export placeholders were retired on 2026-08-05; no active root prompt export remains.
- The Pulsebook contains conflicting historical model metadata, including GPT-4 in its schema and GPT-5 in deployment metadata, plus many future feature proposals. It should not be treated as a current deployment record without owner review.
- The repository does not document a branch strategy, release process, or automated test policy.

## Keeping this guide current

Update this file when the repository gains a runtime, package manager, CI or deployment workflow, canonical ledger files, new top-level project boundaries, or a confirmed product status. Verify each new command and path before documenting it. Keep `CLAUDE.md` as a short pointer unless Claude-specific rules are genuinely needed.

## Related repositories

- https://github.com/OKHP3/glee-fully-gpt01-discovered-careers
- https://github.com/OKHP3/Glee-fullyTools

## Imported Claude Cowork project instructions
