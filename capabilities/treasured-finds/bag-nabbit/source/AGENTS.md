# glee-fully-gpt02g-bag-nabbit

Canonical agent guidance for the repository. `CLAUDE.md` points here.

## Project identity

- Suite: Glee-fully, Branch 02
- Project: 02g, Bag Nabbit
- Repository: `https://github.com/OKHP3/glee-fully-gpt02g-bag-nabbit`
- Type: prompt/tool-ette repository, confirmed by the current tree
- License: MIT, as declared by `LICENSE`
- Current status: placeholder and pre-audit, confirmed by the YAML metadata

## Purpose and boundaries

The declared purpose is a bag and accessories collection tracking and discovery assistant. This purpose is documented in the prior agent guide, but the current repository does not implement a tracker, discovery interface, data store, integration, or deployment.

Mission: not independently established. The available evidence supports only the narrower goal above.

Vision: unknown. Do not invent a roadmap or production role.

Until the project gains an implementation, treat the repository as a source and context record for a future prompt-based tool. Do not assume that the fields in the YAML file are an executable schema or that the declared workflow is operational.

## Repository structure

- `prompts/02g-glee–fully-bag-nabbit_prompts_v1.yaml`: the only project artifact. It is a placeholder processing draft for an extracted legacy prompt.
- `README.md`: minimal project title only.
- `AGENTS.md`: this canonical guide.
- `CLAUDE.md`: pointer to this guide.
- `.agents/skills/`: local agent skills and supporting references. These are agent metadata, not the Bag Nabbit application.
- `LICENSE`: MIT license.
- `.gitattributes`: text normalization settings.

There are no nested repositories or independent application projects in the current tree.

## Prompt metadata

The YAML record declares:

- ID: `02g Glee–fully Bag Nabbit_Prompts_v1`
- Summary: placeholder for an extracted legacy prompt awaiting audit by `TellEPrompt-Ry`
- Thread origin: `BudgetBalancer_Build_Design`
- Target phase: `Anvil`

The meanings of the auditor name, thread origin, and target phase are not defined in this repository. Preserve them as source metadata unless an owner supplies a current interpretation.

## Technology and runtime

Confirmed:

- The repository currently contains YAML and Markdown, plus local Markdown-based agent skills.
- No application language, framework, package manifest, dependency lockfile, build tool, test runner, CI workflow, container configuration, or deployment configuration is present.

Do not add runtime or deployment assumptions to this guide until the repository contains and verifies them.

## Validation

The following checks are appropriate for the current repository:

```sh
git status --short --branch
git log -8 --oneline --decorate
ruby -e 'require "yaml"; YAML.load_file(ARGV.fetch(0)); puts "valid YAML"' 'prompts/02g-glee–fully-bag-nabbit_prompts_v1.yaml'
git diff --check
```

There is currently no project-specific build, test, lint, run, or deployment command. If a future change introduces one, verify it and document it here.

## Change conventions

- Work only on the requested files and preserve unrelated user changes.
- Do not use destructive version-control commands.
- Keep the existing Unicode filename and metadata values stable unless a deliberate migration is requested.
- Do not add secrets, credentials, private Notion anchors, or machine-specific paths to committed guidance.
- Preserve the OverKill Hill P3 writing rules: no em dashes in generated content, preserve standalone punchy lines, and apply the ROY principle that explanation should earn its space.
- The prior AutoCAD R10 rule is not applicable to this repository and is intentionally not carried forward.

## Local agent skills

The repository includes these local skills under `.agents/skills/`:

- `find-skills`: discover or recommend agent skills.
- `okhp3-notion-capture-router`: route AI conversation material into Notion workflows when the required connector context is available.
- `okhp3-skill-cataloger`: catalog local agent skills when explicitly requested.
- `skill-creator`: create or improve agent skills when explicitly requested.

Use these skills only when their documented trigger conditions match the task. Do not treat them as product functionality.

## Known gaps and open questions

- The active or archived status is unresolved. The prior guide contained a placeholder rather than evidence.
- The intended user, collection data model, assistant interface, integrations, and deployment model are unknown.
- It is unknown whether the YAML should be audited, transformed into a prompt, or used as input to another repository.
- `TellEPrompt-Ry`, `BudgetBalancer_Build_Design`, and `Anvil` are source labels only; their current meanings need owner confirmation.
- There is no automated validation beyond basic repository and YAML checks.

When new evidence answers any of these questions, update this file and identify the evidence. Keep this guide factual, operational, and shorter than the analysis used to create it.

## Imported Claude Cowork project instructions
