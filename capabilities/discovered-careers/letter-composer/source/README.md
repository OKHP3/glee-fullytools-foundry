# glee-fully-gpt01d-letter-composer

## Status

This repository is a Glee-fully Branch 01d scaffolding and Agent Skills workspace. It does not currently contain a letter-composer implementation, prompt, application runtime, deployment configuration, or end-user workflow.

## Intended direction

The repository name suggests a future GPT or Agent Skill for drafting tailored cover letters and professional correspondence. That purpose remains inferred because no letter-composer-specific source material is present.

## Contents

- `AGENTS.md` - canonical repository guidance and current-state boundaries.
- `.agents/prompts/` - project onboarding and GPT-to-Agent-Skill migration bootstrap prompts.
- `.agents/skills/` - repository-local Agent Skill packages and their evaluation or support resources.
- `skills/` - the publication mirror for `okhp3-skill-promotion`.
- `LICENSE` - MIT license.

The local skill set currently includes general OKHP3, Glee-fully, repository-maintenance, authoring, migration, evaluation, and promotion packages. Their retention and canonical ownership are still under review; this repository should not be treated as the central Skillz distribution repository.

## Non-goals

Do not claim that letter generation, correspondence generation, deployment, integrations, or a production runtime are implemented here. Do not add credentials, private Notion anchors, personal information, or machine-specific paths.

## Validation

From the repository root:

```text
python3 .agents/skills/okhp3-skill-cataloger/scripts/gen-skills-readme.py --skills-dir .agents/skills --check
node .agents/skills/okhp3-skill-foundry/scripts/validate-skill-suite.cjs --skills-dir .agents/skills
git diff --check
```

These checks validate repository structure and package integrity. They do not prove that a letter-composer workflow or runtime exists.
