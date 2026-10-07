# Portable capability adaptation verification

Date: September 27, 2026. Base: `a88e799`, with the local
`codex/portable-capability-foundry` working changes. This records local evidence,
not GitHub CI, publication, Replit synchronization or native host compatibility.

## Observed results

| Check | Result |
|---|---|
| `python3 scripts/foundry-release-check.py` | Passed: 128 tests run, 127 passed and one Windows symlink-privilege skip; Python/JS syntax, skill catalog, pilot links and whitespace passed |
| `python3 -m unittest app.tests.test_portable_capabilities -v` | Seven passed, rerun after tightening the cleared-provenance readiness check |
| `python3 -X utf8 scripts/validate-manifest.py` | Passed; UTF-8 mode avoids the Windows console encoding failure when printing the success symbol |
| `scripts/check-markdown-links.py` with all 13 changed/new guidance documents selected explicitly | 91 relative links passed |
| `node scripts/foundry-authoring-qa.mjs` with installed Playwright/Chrome and an isolated temporary data directory | Passed: existing authoring/recovery journey plus GPT-to-skill, skill-to-plugin, skill-to-connector, portability persistence, source preservation and mobile checks |
| Browser screenshot review | Conversion form readable at 390px; no document horizontal overflow; browser console clean |
| `git diff -- canon snapshots` | No changes to preserved canonical or snapshot material |
| `git subtree -h` | Full-history subtree command is available on the executing host; no import executed |

The API regression tests exercise stale revisions and malformed conversion
requests, evidence reset for every portability field, source preservation,
historical snapshot bytes, backup/restore, HTML escaping, non-installable adapter
exports, and skill frontmatter length boundaries. The browser runner uses only
synthetic records; it does not open the owner's private workspace data.

The first browser attempts exposed two runner assumptions, a mismatched save
message and a check that ran before reopening finished. Corrected the runner's
message match and waited for the loaded project kind; the complete journey then
passed. No failed run is counted as successful evidence.

## Remaining evidence boundaries

- No individual GPT has been semantically converted or behaviorally benchmarked.
- No native plugin manifest or executable connector has been implemented.
- No compatibility run on ChatGPT/Codex, Claude, Perplexity, OpenClaw or other
  agent hosts has occurred. Blueprint metadata explicitly preserves that limit.
- No child repositories have been imported, renamed, archived or removed.
- OverKill Foundry, AskJamie Foundry and Skillz were not modified.
- Source work is local; no PR, push, merge or deployment is part of this receipt.

Use [the workflow](portable-capabilities.md) and [product subtree contract](../../products/README.md)
for the next migration stage.

## Integration verification, October 6, 2026

Integrated adaptation `fc0b7a094ba0f64ef08c7c22f34d42b1d165c643` with
main `bf2b24ed20de600761d22a90fffb203e7c485fd5` in an isolated checkout.
The README retains the current cover, startup instructions and presentation,
with skills-first authoring and blueprint boundaries added. The frontend retains
the newer form-scoped field selection alongside derivation controls, preserving
the revision-recovery fix.

- Release gate passed: 133 application tests, 132 passed and one Windows
  symlink-privilege skip; syntax, generated skill catalog and pilot checks passed.
- The browser journey passed with synthetic data, including source preservation,
  all three derivation routes, persistence, export/import, backup recovery,
  keyboard access, console health and 390px mobile overflow checks. The mobile
  conversion screenshot was inspected.
- Manifest validation, the governance-field audit and all 35 manifest regression
  tests passed. The first regression run did not propagate UTF-8 to child Python
  processes; setting `PYTHONUTF8=1` corrected the environment and the rerun passed.
- All 120 relative links in the 13 changed guidance documents passed. The default
  maintained-index check also passed. Whitespace checks passed for both the index
  and working tree. Canon and snapshot files are unchanged.

These checks cover the integrated application and guidance. They do not extend
the product, native-package or host-compatibility evidence listed above. GitHub
integration and external synchronization have separate receipts; the September
27 source-only entry remains a historical record.
