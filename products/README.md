# Glee-fully capability migration

The [capability directory](../capabilities/README.md) organizes the former GPTs
by toolbox, Tool family and Tool-ette. The [migration register](migration-map.json)
records each public destination and its source status. An inventoried route
identifies where a project belongs. The source-consolidation batch uses
`sanitized-snapshot` imports from pinned `main` revisions. Only files reviewed
for public use belong under `source/`. Private records, secrets and the
original Git histories stay in their source repositories. See each register
entry for its review evidence, import status and any outstanding work.

## November 2026 import

Each of the 50 capability pages links to its reviewed source files, import
receipt and original revision. Each `product.json` lists the public files,
their Git blob IDs, modes and SHA-256 hashes. An excerpt or redaction also
records the original blob ID and describes the change. The original MIT
license is included in each `source/` directory.

The [shared tooling index](shared-tooling.json) points to byte-identical
public copies of tools bundled in the former repositories. Use the GPT code
in the migration register to find its entries. Historical links in the source
documents may point to private files or to this shared tooling. To follow a
historical link in its original context, open the capability's pinned
**Original revision** with an account that has access.

Private operational records, files with private attachment references and
contact-bearing career examples stay upstream. [Resume Builder](../capabilities/discovered-careers/resume-builder/)
includes five blank public templates derived from the original examples.

## Layout for each product

```text
capabilities/<family>/               Toolbox or Tool family
capabilities/<family>/<tool-ette>/    Tool-ette within that family
  README.md                         Public navigation and source status
```

A capability with reviewed source or newly authored packages can also contain
the following files and directories at either level.

```text
  product.json                Sources, versions, rights and release evidence
  source/                     Files approved for publication, retaining their paths
  skills/<skill-name>/         Portable core, SKILL.md and optional resources
  adapters/<host>/             Host-specific manifests and integration code
  evals/                      Fixtures and results tied to exact artifact versions
```

Add each file or directory when the corresponding material exists. Use the
names in the capability directory, including the owner-selected
`identity-known/gpt07g-self-fixer` route. Preserve public names, GPT links
and repository URLs as aliases. Keep private source material in its existing
access-controlled location until reviewed and authorized for publication.

`source/` contains ordinary tracked files. A sanitized snapshot keeps the
approved files at their source paths while the original history stays upstream.
A separately reviewed full-history subtree also preserves commit ancestry.
New skills, adapters and evaluations belong alongside `source/`. Runtime builder
skills in `.agents/skills/` and publication mirrors in root `skills/` keep their
distinct roles.

## Import procedure

1. Inventory Glee-fully child repositories and associate each with exactly one
   regional Foundry. Record the canonical URL, default branch, exact source commit,
   license, visibility, capability destination and aliases in the appropriate
   public or access-controlled record. Inspect uncommitted work,
   active branches/PRs, worktrees and any assigned Replit integration first.
2. For a sanitized snapshot, review the files at the selected revision, including
   document contents and metadata. Select the files authorized for public use.
   Document what was included and any exclusions using public-safe descriptions.
   A full-history subtree additionally requires review and authorization for all
   reachable history.
3. Preserve source refs. If recovery requires a bundle, keep it outside tracked
   product data. Start from a clean integration branch and verify that the
   proposed `source/` directory is available.
4. For a snapshot, add the selected files at their source-relative paths under
   `source/` and keep upstream commits out of the FoundRy ancestry. For an
   authorized full-history subtree, use the reviewed URL and exact commit.

   ```bash
   git subtree add --prefix=<capability-directory>/source <source-url> <full-commit>
   ```

   This is an operator recipe with placeholders, not an executable bulk-import
   script. Substitute the exact repository-relative folder from the register,
   for example `capabilities/discovered-careers/resume-builder`.
   Omit `--squash` when retaining full history. Verify `git subtree -h`
   on the executing host before attempting import. Never substitute a moving
   branch tip for the recorded reviewed commit.
5. For a snapshot, compare the destination paths, blob IDs and modes with the
   approved selection. Record the resulting destination tree ID. Any redactions
   require their own review and evidence. For a full-tree import, verify that
   the entire destination tree equals the pinned source tree, including dotfiles,
   executable modes and links. Treat nested automation and agent instructions
   as source material. Keep these files outside the application's serving allowlists.
6. Update the capability README and its register entry using the contract below.
   Record the source tree ID where publicly shareable, the destination tree ID,
   the import commit and verification evidence. Use `product.json` when a
   capability adds version, package or release details.
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

Each entry in `migration-map.json` identifies a destination. Fill in the
source and import fields as evidence becomes available for public use.

| Field | Value |
|---|---|
| `productId`, `displayName`, `aliases` | Stable capability slug, public name, previous names |
| `region` | `gleefully` |
| `destination` | Full path under `capabilities/`, including the parent family for a Tool-ette |
| `sourceRepository`, `sourceCommit`, `sourceTree` | Publicly shareable source URL and exact Git object IDs, or `null` where unavailable for publication |
| `sourceLicense`, `publicHistoryReview` | Source rights and public-history review evidence, or `null` pending review |
| `importMode` | `full-history-subtree` or `sanitized-snapshot` for an import, otherwise `null` |
| `importCommit`, `destinationTree` | Commit introducing the source and verified destination tree ID, both `null` until import |
| `status` | `inventoried`, `blocked`, `imported`, `skill-draft`, `adapter-draft`, `validated`, `released` |
| `skills`, `adapters` | Relative package paths and pinned versions; empty until authored |
| `evidence`, `blockers` | Review/test receipts and unresolved work |

Unknowns must remain `null` or explicit blockers, never invented revisions or
inferred compatibility. `validated` requires dated evidence, not just files.
This migration register tracks source movement; it does not replace canon or
register new sealed entities.
