# Repository agent guide

## Project identity

- Repository: `OKHP3/glee-fully-gpt06b-calm-keep`
- Suite: Glee-fully Personalizable Tools, Branch 06b
- Intended concept: Calm Keep, a wellness and mental-wellness assistant focused on stress, rest, sleep, and everyday balance
- Git remote: `https://github.com/OKHP3/glee-fully-gpt06b-calm-keep.git`
- Repository type: content-first documentation repository with a checked-in Agent Skills workbench
- Current repository state: `main` tracks `origin/main`; no project-specific branch or release convention is documented.

The repository name and the existing project notes identify Calm Keep as the intended product concept. The repository does not currently contain an implementation, product prompt, deployment export, or direct Calm Keep pulsebook.

Related context is the parent wellness repository `glee-fully-gpt06-healthy-bee-ing`. Its archived pulsebook is useful lineage, but it does not establish this repository's implementation status.

## Mission and vision

The intended mission is to help a user approach stress and everyday wellness with calm, clear, supportive guidance. This is an inference from the repository identity and the parent wellness pulsebook, not a verified current product specification.

The intended vision is a focused wellness companion that helps users build steadier habits around stress, rest, sleep, and gentle movement. This remains inferred and should be confirmed before it is treated as a roadmap or product commitment.

The intended audience, ownership model, live deployment state, and production guarantees are not established by this repository. Do not describe Calm Keep as live or medically validated without new evidence.

## Scope and boundaries

- Keep Calm Keep distinct from the parent Tool #06, Healthy Bee-ing, and from sibling tools such as Care Check, Snappy Count, Medi Minder, Moody Log, and Maven Wise.
- Treat `archive/parent-context/healthy-bee-ing-pulsebook-20250901.md` as parent-level lineage and context. It is not a direct specification for this repository.
- Do not claim that the parent pulsebook's six-twig routing, sibling mentions, or Toolbox fallback are implemented here. No executable routing exists in this repository.
- Future wellness content should be supportive and non-diagnostic. It should not present itself as medical advice, diagnosis, treatment, or emergency response.
- Do not modify application code, dependencies, secrets, CI behavior, or unrelated repositories during context maintenance. Update generated catalog outputs only through the local cataloger workflow.

## Repository layout

Current tracked content is primarily a local skill workbench:

- `README.md`: public orientation, current status, boundaries, and repository map.
- `archive/parent-context/healthy-bee-ing-pulsebook-20250901.md`: historical parent Tool #06 pulsebook with Calm Keep listed as one sibling twig.
- `AGENTS.md`: canonical guidance for agents working in this repository.
- `CLAUDE.md`: short pointer to this guide for Claude-based tooling.
- `.agents/skills/`: active local skills and their supporting assets, references, fixtures, scripts, tests, and generated catalog.
- `skills/okhp3-skill-promotion/`: managed publication mirror of the local promotion package.
- `.gitignore`: excludes Python bytecode, caches, and common temporary files.
- `LICENSE`, `.gitattributes`: repository metadata.

The repository has no nested Git repository or independently identifiable application/package project. No root `package.json`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `go.mod`, Dockerfile, workflow configuration, or deployment configuration was found.

## Local skills

The checked-in `.agents/skills/` tree contains the local skill packages listed in
`.agents/skills/README.md`. The generated catalog is the inventory surface and
must be refreshed with:

```text
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --mode project
```

These are reusable agent assets, not evidence that Calm Keep itself is implemented. Change them only when the user explicitly requests skill work.

## Commands and validation

No project-specific run, build, test, lint, or deployment command is currently defined. Do not invent one. For documentation-only changes, use checks appropriate to the files changed, including:

```text
git diff --check
git status --short
git ls-files
python3 .agents/skills/okhp3-repository-organizer/scripts/inventory_repo.py --root .
python3 .agents/skills/okhp3-repl-repo-janitor/scripts/audit-repo.py --root . --base origin/main
```

When code or a build manifest is added, update this guide with commands that have been verified in the repository.

## Working conventions

- Preserve the Glee-fully voice: calm, clear, supportive, and confidence-building.
- Do not use em dashes in generated content.
- Preserve standalone punchy lines when editing project prose. Do not merge them into paragraphs without a reason.
- Apply the ROY principle: explanation and detail should earn their space.
- Keep historical material labeled as historical or parent-level context when it does not describe this repository directly.
- Prefer small, evidence-backed documentation changes. Preserve unrelated user changes.
- Never add credentials, private connector identifiers, or speculative deployment details.

## Known gaps and risks

- The archived pulsebook is for Healthy Bee-ing, not Calm Keep, and is dated 2025-08-31.
- The archived pulsebook references `dataLedger_*` files that are absent from this repository.
- The archived pulsebook references an icon file that is absent from this repository.
- Its owner contact, checksum, compliance, succession, and change-log fields contain placeholders or stubs.
- The local skill catalog is generated and must remain consistent with the actual `.agents/skills/` inventory.
- No direct evidence establishes whether Calm Keep was ever separately deployed, what its final prompt should be, or whether this repository is active, archived, or on hold.

## Open questions

- Is Calm Keep an active product concept, an archived export, or an on-hold repository?
- What is the authoritative Calm Keep prompt, deployment export, or product specification, if one exists outside this repository?
- Should the archived parent pulsebook remain as lineage, or should it eventually be removed?
- Which owner-approved safety language and escalation behavior should future wellness content follow?

## Safe change process

1. Inspect the current working tree before editing and preserve existing user changes.
2. Confirm that a proposed change belongs to this repository and to Calm Keep rather than the parent wellness tool or a sibling repository.
3. Update this guide when project structure, commands, or verified product identity changes.
4. Re-read every guidance file changed and run the applicable documentation checks.
5. Keep unresolved owner decisions in the open-questions section of the guide instead of guessing.

## Keeping this guide current

This file is the canonical repository guide. Update it when implementation files, manifests, tests, deployment configuration, or authoritative product documentation are added. Record important conclusions as confirmed, inferred, or unknown so future agents can distinguish repository evidence from suite-level intent.

## Imported Claude Cowork project instructions
