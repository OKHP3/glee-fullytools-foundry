# Portable capabilities: the Foundry's current direction

Owner decision recorded September 27, 2026. Glee-fully Foundry now prioritizes
portable Agent Skills, skill composition, and host-specific plugin or connector
adapters. Existing Custom GPTs are migration sources. A new capability can begin
directly as a skill; it does not need a GPT predecessor.

This decision applies to this repository. OverKill/OKHP3 Foundry and AskJamie
Foundry retain their own products, records and release decisions. They can reuse
this method. Shared reusable skills remain candidates for the Skillz catalog,
not three separately maintained copies of the same core.

See the [adaptation verification record](portable-capability-verification.md)
for local test evidence and what remains unimplemented.

## Product architecture

```text
Preserved GPT source and provenance
  -> capability map and explicit semantic-loss review
  -> small portable skills with references, scripts, assets and evaluations
  -> composition of versioned skills and tool contracts
  -> separate host adapters and native plugin/connector packages
  -> observed tests for each claimed host and release
```

The skill is the durable method. An adapter describes or implements how a
particular client discovers that method and supplies tools, authentication and
UI behavior. A connector supplies an integration; a plugin may bundle several
skills and integrations. These terms do not imply a universal package format.

ChatGPT/Codex, Claude, Perplexity, OpenClaw and other clients are intended
evaluation targets. No support claim follows from being named here. Record the
exact product/version, documented format, available capabilities, test date,
result and limitations for each target. Mark untested targets `not-run`, blocked
access `blocked`, and unavailable capabilities `unsupported`. The portable core
must not require an OpenAI account or an OpenAI-specific manifest.

## Workbench workflow available now

1. Choose **Agent Skill** for new work. For existing GPTs, choose **Legacy GPT
   source** and record the available specification, or import an existing Foundry
   project JSON. The importer is not a ChatGPT configuration or account exporter.
2. Under **Conversion & portability**, inventory instructions, knowledge files,
   actions, starters, examples, source revisions, rights and missing material.
   Mark each asset `available`, `partial`, `missing` or `unverified`.
   For original skills, record newly authored material as the source and explain
   any absence of inherited behavior. Saved skill portability records require
   provenance, mapping, loss review and target-host notes before review.
3. From a GPT source, select **Derive Agent Skill**. From a skill, select
   **Derive plugin blueprint** or **Derive connector blueprint**. The source
   stays intact; the derived draft records its local source ID and revision,
   copies authored content for review, and resets test evidence. This operation
   does not rewrite the instructions or fetch source assets.
4. Map each source behavior to a procedure, reference, script, output contract,
   adapter, explicit exclusion or blocker. Split a broad GPT into multiple
   focused skills where warranted. Record semantic loss, mitigation and tests.
5. Rewrite the skill instructions. Define triggers, inputs, outputs, boundaries,
   failure handling and verification. Keep host assumptions in adapter records.
6. For plugin and connector blueprints, identify the versioned skills, tool
   operations, schemas, authentication method, scope names, read/write consent,
   error behavior and recovery. Never record actual credentials.
7. Save the contract, then record observed acceptance evidence. Material changes
   to conversion or integration fields invalidate earlier passes. Newly derived
   drafts add preservation, platform-loss and boundary cases, all initially unrun.
8. Inspect and export the package. Implement native adapters against the target
   host specification, validate them, and run behavior tests before release.

The app's field checks establish that review material was recorded; they cannot
judge its truth or substitute for an independent behavioral evaluation. A plugin
or connector ZIP contains `adapter-blueprint.json` and `adapter.md`, with
`installable: false` and `compatibilityStatus: not-verified-by-foundry` even when
the working record is ready for review. It contains references to skills, not
automatically copied or installed dependencies. No native packaging or connector
execution is implemented by these blueprints.

Agent Skill ZIPs retain `SKILL.md` at the package root. Extract into the directory
named by its frontmatter; `build.md` gives that name. The discovery description is
limited to 1024 characters while the full authored description remains in the
specification. Review the description's trigger quality before release.

## Migration gates

| Gate | Required evidence |
|---|---|
| Preserve | Source repository/revision, asset inventory, license and public-data review |
| Map | Every behavior assigned a destination, accepted loss, exclusion or blocker |
| Author | Focused skill contract, resources and explicit tool requirements |
| Evaluate | Expected-use, missing-input, platform-loss and adversarial boundary evidence |
| Package | Versioned dependencies and independently validated native host adapter |
| Release | Exact artifact hashes, tested hosts, remaining limitations and release decision |

Use the repository-local conversion-plan and skill-foundry skills for detailed
authoring and evaluation. With/without-skill benchmarks, holdouts and independent
review must be labeled `not-run` until actually executed. An old GPT evaluation
does not validate a converted skill or adapter.

The repository consolidation path is [product subtrees](../../products/README.md).
Product naming describes the capability instead of the former platform. Keep
old GPT names, IDs and repository URLs as aliases and provenance. Do not rewrite
sealed canonical IDs or remove historical material to achieve rebranding.

## Source and platform boundaries

Owner direction is the basis for this product change, not a claim that Custom
GPTs have been discontinued. Local records remain private, the server stays on
loopback, and only the fixed source allowlist is readable through the app.
Subtree sources, arbitrary repository files and credentials are not served.

Technical references checked September 27, 2026:

- [Agent Skills specification](https://agentskills.io/specification): directory
  package, SKILL.md frontmatter, optional resources, naming and description rules.
- [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro):
  a protocol for connecting AI applications to external systems, distinct from
  the instructions and host packaging of a skill.

These references support the format and integration distinction. They do not
prove this repository's packages run on any particular client.
