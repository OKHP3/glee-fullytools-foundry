# Glee-fully capability migration

The [capability directory](../capabilities/README.md) organizes the former GPTs
by toolbox, Tool family and Tool-ette. The [migration register](migration-map.json)
records each FoundRy destination and its source status. The owner selected
the complete tracked `main` tree of each of the 50 former repositories for
publication under its capability's `source/` directory. The register calls
this mode `exact-tree-snapshot`. Private recovery bundles preserve Git history.

## November 2026 import

Each capability page links to its source and its `product.json` receipt.
Compare the receipt's pinned source tree with the FoundRy `source/` tree.
Matching Git tree IDs verify every tracked path, file mode and blob, including
dotfiles, original licenses and bundled tools. For a legacy repository link,
find its former name in the register and open the same path under the mapped
`source/` directory. Links into other services retain their original access rules.

The first import copied a selection of public files, prepared excerpts and
recorded matching shared tools. Its evidence remains available through
`initialImport` and the historical [shared tooling index](shared-tooling.json).
The five blank [Resume Builder templates](../capabilities/discovered-careers/resume-builder/templates/)
are derived material alongside its source.

## Retirement of the 50 GitHub repositories

On November 24, 2026, the owner moved all 50 legacy repositories into this
FoundRy. At the [cutover revision](https://github.com/OKHP3/glee-fullytools-foundry/commit/64cf0c63c5d2eec64726dcabcff6efbabe17897c),
each of the 50 public `source/` trees had the same Git tree ID as its live
upstream `main`. Together they contained 17,825 tracked paths. The original
Git histories were restored and checked privately before deletion.

GitHub confirmed all 50 deletions. The owner repository inventory and an
authenticated lookup of every former repository verified their removal. Use
the destination in the [register](migration-map.json) for ongoing work.
The former repository URLs identify the sources for historical lookup.

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
  source/                     Pinned source tree, with original paths and modes
  skills/<skill-name>/         Portable core, SKILL.md and optional resources
  adapters/<host>/             Host-specific manifests and integration code
  evals/                      Fixtures and results tied to exact artifact versions
```

Add each file or directory when the corresponding material exists. Use the
names in the capability directory, including the owner-selected
`identity-known/gpt07g-self-fixer` route. Preserve public names, GPT links
and repository URLs as aliases. Keep private source material in its existing
access-controlled location until reviewed and authorized for publication.

`source/` contains ordinary tracked files. An exact snapshot preserves the
entire source tree. A sanitized snapshot preserves only approved files or
excerpts. A separately reviewed full-history subtree also preserves commit ancestry.
New skills, adapters and evaluations belong alongside `source/`. Runtime builder
skills in `.agents/skills/` and publication mirrors in root `skills/` keep their
distinct roles.

## Import procedure

1. Inventory Glee-fully child repositories and associate each with exactly one
   regional Foundry. Record the canonical URL, default branch, exact source commit,
   license, visibility, capability destination and aliases in the appropriate
   public or access-controlled record. Inspect uncommitted work,
   active branches/PRs, worktrees and any assigned Replit integration first.
2. For an exact snapshot, confirm publication authority for the complete tree
   at the selected revision. For a sanitized snapshot, review document contents
   and metadata and select the files authorized for public use.
   Document what was included and any exclusions using public-safe descriptions.
   A full-history subtree additionally requires review and authorization for all
   reachable history.
3. Preserve source refs and verify the recovery bundle before retiring the
   original repository. Keep that bundle in private storage outside tracked
   product data. Start from a clean integration branch and check the destination.
4. For an exact snapshot, import the pinned Git tree at `source/`. For a
   sanitized snapshot, add the selected files at their source-relative paths.
   Keep source commits out of the FoundRy ancestry for either snapshot. For an
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
5. For a sanitized snapshot, compare the destination paths, blob IDs and modes with the
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
7. Verify the source tree IDs on FoundRy `main`, check consumer links and
   verify private recovery before the authorized retirement of each original
   repository. Record the remote retirement separately after confirming it
   on GitHub. Import status describes the files available here.

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
| `sourceRepository`, `sourceCommit`, `sourceTree` | Former repository identity and pinned Git object IDs, or `null` where unavailable for publication |
| `sourceLicense`, `publicHistoryReview` | Source rights and public-history review evidence, or `null` pending review |
| `importMode` | `exact-tree-snapshot`, `full-history-subtree` or `sanitized-snapshot` for an import, otherwise `null` |
| `initialImport` | Reference to earlier selective-import evidence where a capability has a prior import |
| `importCommit`, `destinationTree` | Commit introducing the source and verified destination tree ID, both `null` until import |
| `status` | `inventoried`, `blocked`, `imported`, `skill-draft`, `adapter-draft`, `validated`, `released` |
| `skills`, `adapters` | Relative package paths and pinned versions; empty until authored |
| `evidence`, `blockers` | Review/test receipts and unresolved work |

Unknowns must remain `null` or explicit blockers, never invented revisions or
inferred compatibility. `validated` requires dated evidence, not just files.
This migration register tracks source movement; it does not replace canon or
register new sealed entities.
