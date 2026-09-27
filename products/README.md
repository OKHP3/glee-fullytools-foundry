# Glee-fully product subtrees

This is the destination for consolidating Glee-fully's former Custom GPT child
projects under their regional Foundry. The folder is reserved now; no child
repository has been imported by this adaptation. The migration register is
[migration-map.json](migration-map.json). Its `not-inventoried` status is explicit;
an empty list is not evidence that the portfolio has no child projects.

## Layout for each product

```text
products/<capability-slug>/
  README.md                   Current purpose, aliases, ownership and status
  product.json                Sources, versions, rights and release evidence
  source/                     History-preserving subtree of the source repository
  skills/<skill-name>/         Portable core, SKILL.md and optional resources
  adapters/<host>/             Host-specific manifests and integration code
  evals/                      Fixtures and results tied to exact artifact versions
```

The folders inside a future product are a contract, not generated placeholders.
Add them when the corresponding material exists. Use a stable lowercase ASCII
capability slug without GPT numbering or provider branding. Preserve prior names,
GPT links and repository URLs as aliases. Existing Toolbox/Tool/Tool-ette/domain
relationships remain useful metadata, not a platform dependency.

`source/` holds the preserved imported tree. Evolved skill and adapter code lives
alongside it. A subtree contains tracked files and source history, not a nested
`.git` directory or a submodule pointer. Runtime builder skills in `.agents/skills/`
and existing publication mirrors in root `skills/` keep their distinct roles.

## Import procedure

1. Inventory Glee-fully child repositories and associate each with exactly one
   regional Foundry. Record canonical URL, default branch, exact source commit,
   license, visibility, new capability slug and aliases. Inspect uncommitted work,
   active branches/PRs, worktrees and any assigned Replit integration first.
2. Review both files and reachable source history for public suitability. This
   destination is public. Do not import private material, credentials or a history
   that cannot safely be made public. Record the blocker and use a separately
   reviewed sanitized snapshot if full history cannot be imported. Do not describe
   a snapshot as a history-preserving subtree.
3. Preserve source refs and a recovery bundle outside tracked product data. Start
   from a clean integration branch and verify the destination prefix is absent.
4. With Git subtree installed, use the reviewed URL and exact commit:

   ```bash
   git subtree add --prefix=products/<capability-slug>/source <source-url> <full-commit>
   ```

   This is an operator recipe with placeholders, not an executable bulk-import
   script. Omit `--squash` when retaining full history. Verify `git subtree -h`
   on the executing host before attempting import. Never substitute a moving
   branch tip for the recorded reviewed commit.
5. Compare the imported Git tree with the source commit's tree, including dotfiles,
   executable modes and links. Inspect nested automation and agent instructions as
   imported source material; they do not override root guidance. Keep the subtree
   out of the application's static and reference-serving allowlists.
6. Add `product.json`, current README and a register entry using the contract below.
   Record source tree ID, destination tree ID, import commit and verification.
   Use the [conversion workflow](../docs/application/portable-capabilities.md) to
   author skills and then adapters without editing the preserved source tree.
7. Review the import diff and release evidence through the normal PR process.
   Verify links and consumer routing before changing the source repository's role.
   Archive/delete/rename remote repositories and redirect sites only in a separately
   specified cutover. Source access remains the recovery path until then.

Once cut over, this product directory is the editing authority. Record any later
upstream import explicitly; do not permit silent two-way synchronization or two
editable copies of the portable core. Shared Skillz promotion uses its existing
governed provenance and mirror workflow.

## Migration register entry contract

Each entry in `migration-map.json` must include:

| Field | Value |
|---|---|
| `productId`, `displayName`, `aliases` | Stable capability slug, public name, previous names |
| `region` | `gleefully` |
| `destination` | `products/<productId>` |
| `sourceRepository`, `sourceCommit`, `sourceTree` | Reviewed URL and exact Git object IDs |
| `sourceLicense`, `publicHistoryReview` | Rights and evidence permitting a public import |
| `importMode` | `full-history-subtree` or `sanitized-snapshot` |
| `importCommit`, `destinationTree` | Import receipt and imported tree verification |
| `status` | `inventoried`, `blocked`, `imported`, `skill-draft`, `adapter-draft`, `validated`, `released` |
| `skills`, `adapters` | Relative package paths and pinned versions; empty until authored |
| `evidence`, `blockers` | Review/test receipts and unresolved work |

Unknowns must remain `null` or explicit blockers, never invented revisions or
inferred compatibility. `validated` requires dated evidence, not just files.
This migration register tracks source movement; it does not replace canon or
register new sealed entities.
