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
