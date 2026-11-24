# Historical evaluation workspace

The Foundry's historical version 1.0.0 benchmark refers to this workspace. Its
18 grading, metrics, and response files were removed from the working tree in
commit `d6af8a4`. They remain in Git commit
`56ba92e6f9b9a571953936a40b9e5ad06611383a` at this same repository-relative
path. For example, inspect the original grading evidence with:

```text
git show 56ba92e6f9b9a571953936a40b9e5ad06611383a:.agents/skills/okhp3-skill-foundry/workspace/iteration-1/eval-1/with_skill/grading.json
```

These historical results do not validate the current Foundry version. This
pointer preserves access without restoring the temporary evaluation outputs.
