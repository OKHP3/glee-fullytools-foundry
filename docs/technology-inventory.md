# Technology inventory and update policy

Reviewed September 18, 2026 (America/Chicago); upstream requests continued into
September 19 UTC. Question: which technologies does this solution actually use,
how do their versions compare with stable releases, and how will it stay current?

## Scope and evidence

Confirmed source baseline: `b5bfeb30f11330d564eb30477dbcb013687c8fd7`.
The Windows checkout was clean and matched freshly fetched `origin/main`.
The GitHub connector returned the same existing technology inventory.
All 771 tracked paths were inventoried, including hidden skill packages, manifests,
workflow files, source imports, CDN URLs, and optional QA scripts.

This covers the FoundRy application, repository maintenance, reusable skill tools,
and child-page source templates. It is not an operating-system SBOM or an audit of
every linked child repository. Source documents, example code, historical snapshots
and reference-only skill instructions do not establish installed dependencies.

The Replit browser shell was inspected directly. Its `main` was at `d372bec`,
one local commit beyond `b5bfeb3`. That commit changes only two agent-reference
documents. Its runtime and package versions below are directly observed; the
connector separately returned an authentication error. Nothing in Replit was
changed or synchronized during this audit.

## Application and development runtimes

Latest values are source observations, not promises of compatibility. Each source
link is maintained by the software publisher, package publisher or standards body.
“In place” distinguishes declarations from the executable selected on a host.

| Technology | In-place version and use | Latest stable verified | Update route |
|---|---|---|---|
| Python / CPython standard library | App requires **3.11+**. Existing app CI selects **3.11**. Windows default `py -3`: **3.14.0rc1**; explicit `py -3.13`: **3.13.14**. Replit: **3.11.14**. | **3.14.7**; maintained branches include **3.13.15**, **3.11.16**. [PSF downloads](https://www.python.org/downloads/) | Test floor and latest stable in CI. Upgrade each host deliberately; replace the Windows release candidate with a supported final release. |
| SQLite / SQL dialect | Python `sqlite3`; no independent DB service. Windows default Python bundles **3.49.1**; explicit 3.13 bundles **3.50.4**. Replit bundles **3.51.1**. | **3.53.4**. [SQLite release history](https://sqlite.org/changes.html) | Update the owning Python/platform distribution and verify the loaded SQLite version plus backup/restore tests. A Python version does not uniquely determine SQLite across hosts. |
| JavaScript / ECMAScript | Vanilla browser scripts in `app/static/app.js` and templates; no transpiler target. Node also executes maintenance/skill scripts. | **ECMAScript 2026, edition 17**. [Ecma ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) | Browser compatibility testing. A new language standard is not a package upgrade. |
| HTML | `app/static/index.html`, source templates and exported starters use HTML; no numbered pin. | Living Standard, continuously maintained. [WHATWG](https://html.spec.whatwg.org/) | Review features and render in supported browsers. |
| CSS | Handwritten application/template styles; no framework. | **CSS Snapshot 2026**, Group Note dated June 22, 2026. [W3C](https://www.w3.org/TR/css-2026/) | Review module support in browsers. CSS has independently evolving modules. |
| Node.js | Windows **24.11.1**; Replit **24.13.0**, module `nodejs-24`. Existing CI used runner-provided Node for syntax checking. Seven skill package manifests and standalone `.mjs`/`.cjs` tools use Node. | **26.9.0 Current**; **24.21.0 LTS**. [Node.js](https://nodejs.org/en/download) | Use moving `lts/*` with `check-latest` in CI; inspect Current separately before changing policy. No Node server or frontend build is introduced. |
| npm | Windows and Replit **11.6.2**; skill test command wrapper, not an app build requirement. | **12.0.2**. [npm package metadata](https://registry.npmjs.org/npm/latest) | Follow supported Node/npm combinations. Review major npm changes independently. |
| pip | Windows default Python **25.1.1**; explicit 3.13 **26.1.2**; Replit **25.0.1**. Installs maintenance dependencies only. | **26.2.1**. [PyPA package metadata](https://pypi.org/pypi/pip/json) | Upgrade in isolated validation environments; record the selected interpreter. |
| Playwright and playwright-core | Optional browser QA imports; no repository pin. Neither package resolves from the initial Windows repository environment. This does not exclude installations in unrelated tool environments. | Both **1.63.0**. [Playwright](https://registry.npmjs.org/playwright/latest), [playwright-core](https://registry.npmjs.org/playwright-core/latest) | Pin a tested driver and matching browser when formalizing browser CI. Optional QA remains an explicit gap, not a green check. |
| Mermaid | Exact CDN pin **12.2.0** in `web-templates/index.html`; GitHub-rendered Markdown diagrams use GitHub's separately managed renderer. | **12.2.0**. [Publisher releases](https://github.com/mermaid-js/mermaid/releases), [12.2.0 release](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.2.0) | Weekly audit and candidate updater select stable `mermaid@` publisher tags. Review release changes and render representative diagrams before propagating to consuming repositories. |

Mermaid 12 targets ES2024 and Safari 17.4+ and declares Node 22.12+ for npm
consumers. These are material compatibility changes, and the template now explicitly retains the prior Dagre layout and classic look.
A Chromium comparison rendered flowchart links and sequence diagrams successfully under both 11.17.2 and 12.0.0. Safari and Firefox were not tested.
The application itself does not import Mermaid.

## Python maintenance dependencies

Exact declarations are in `requirements.txt`; all seven resolved dependencies
and reviewed hashes are in `requirements-lock.txt`. Windows default Python and
Replit had all seven versions below installed. The initially selected Windows
3.13 environment did not have these validators installed, so validation used an
isolated environment rather than modifying a shared interpreter.

| Package | Role | Declared/locked version | Latest stable verified |
|---|---|---|---|
| PyYAML | Direct manifest YAML parser | **6.0.3** | **6.0.3** ([PyPI](https://pypi.org/pypi/PyYAML/json)) |
| jsonschema | Direct manifest schema validator | **4.26.0** | **4.26.0** ([PyPI](https://pypi.org/pypi/jsonschema/json)) |
| attrs | Validator transitive dependency | **26.1.0** | **26.1.0** ([PyPI](https://pypi.org/pypi/attrs/json)) |
| jsonschema-specifications | Validator transitive dependency | **2025.9.1** | **2025.9.1** ([PyPI](https://pypi.org/pypi/jsonschema-specifications/json)) |
| referencing | Validator transitive dependency | **0.37.0** | **0.37.0** ([PyPI](https://pypi.org/pypi/referencing/json)) |
| rpds-py | Validator transitive dependency | **2026.6.3** | **2026.6.3** ([PyPI](https://pypi.org/pypi/rpds-py/json)) |
| typing-extensions | Validator transitive dependency | **4.16.0** | **4.16.0** ([PyPI](https://pypi.org/pypi/typing-extensions/json)) |
| LibYAML | Native library included in observed PyYAML builds; Replit also declares `libyaml` | **0.2.5** on Windows and Replit | **0.2.5** ([publisher](https://pyyaml.org/wiki/LibYAML)) |

The application server's imports are Python standard library modules, including
HTTP serving, JSON, SQLite, ZIP, threading and hashing. Those modules follow the
Python distribution; they are not independent pip dependencies. The seven local
skill `package.json` files are private **0.1.0** authored packages without external
dependency fields. Their authored package versions are not Node versions.

## Automation, host tooling and services

| Technology | In-place version / scope | Latest stable or version contract | Update route |
|---|---|---|---|
| Git | Windows **2.55.0.windows.5**; Replit **2.50.1** | Git **2.55.0**; Windows **2.55.0.windows.5**. [Git](https://git-scm.com/install/), [Git for Windows](https://github.com/git-for-windows/git/releases/latest) | Host package manager; preserve work and recheck sync independently. |
| GitHub CLI | Windows **2.96.0**; used by optional repository-management skills | **2.101.0**. [GitHub CLI](https://github.com/cli/cli/releases/latest) | Host tooling update, separate from app releases. |
| Bash | Replit **5.2.37(1)-release**; post-merge hook and CI shell steps | **5.3** release line. [GNU manual](https://www.gnu.org/s/bash/manual/html_node/index.html) | Host-managed shell; keep hooks compatible and test on each host. |
| Nix / Replit environment | Replit reports **Determinate Nix 3.11.2 / Nix 2.31.1**; `.replit` selects `stable-25_05`, `python-3.11`, `nodejs-24`, `web` | Upstream Nix download lists **2.35.2**, NixOS **26.05**; stable manual still labels **2.34.9**. [Downloads](https://nixos.org/download/), [manual](https://nix.dev/manual/nix/stable/) | Replit owns available modules/channels. Its fork/channel is not interchangeable with upstream NixOS. Do not automatically rewrite ignored platform configuration. |
| actions/checkout | Mutable major tag **v7**, all existing workflows | **v7.0.1**. [GitHub release](https://github.com/actions/checkout/releases/latest) | Dependabot weekly; patches within v7 follow the maintained major tag. |
| actions/setup-python | Mutable major tag **v7**, all existing workflows | **v7.0.0**. [GitHub release](https://github.com/actions/setup-python/releases/latest) | Dependabot weekly. |
| actions/setup-node | Added by this change, **v7** | **v7.0.0**. [GitHub release](https://github.com/actions/setup-node/releases/latest) | Dependabot weekly; explicitly selects latest LTS for CI. |
| GitHub Actions runner | `ubuntu-latest`, image/revision chosen per run; not a fixed Ubuntu pin | Provider-managed. [Runner images](https://github.com/actions/runner-images) | Record actual runtime versions in every CI run; GitHub manages OS image refreshes. |
| Dependabot | Hosted service; configuration format **version: 2** | No installed semantic version. [GitHub configuration](https://docs.github.com/en/code-security/concepts/supply-chain-security/about-the-dependabot-yml-file) | Weekly pip and action PRs, grouped per ecosystem. |
| jsDelivr | Template's versioned Mermaid ES-module URL | Hosted CDN; package version is the Mermaid pin | Audit package release and test the exact asset URL when upgrading. |
| Google Fonts | Template stylesheet: Fredoka, Open Sans, Poppins, DM Sans; no numeric font pin | Service-managed URL and family/weight contract. [Google Fonts](https://developers.google.com/fonts/docs/css2) | Check appearance and font loading during template review. |
| Ko-fi widget | Template `overlay-widget.js`; no public numeric version in URL | Service-managed integration. [Ko-fi help](https://help.ko-fi.com/hc/en-us/articles/360018381678-Ko-fi-tip-widget) | Check official integration contract and render in consuming pages. |
| GitHub / Replit / ChatGPT | Development, source/rendering or export destinations; no versioned SDK imported by app | Hosted products, no application-controlled stable pin | Review provider changes; never infer deployment status from repository links. |

Replit's ignored configuration includes a static deployment stanza and port
mapping. Their presence does not prove publication or authorize changing the
owner-local application boundary. No hosted deployment is added.

## Data and document standards

| Technology | In-place use | Latest published reference checked |
|---|---|---|
| YAML | Manifests, workflow definitions and governed fenced content; no universal dialect declaration. PyYAML semantics are separate from the YAML specification. | **1.2.2**. [YAML specification](https://yaml.org/spec/1.2.2/) |
| JSON | API, skill metadata, imports and exports using language-standard parsers | **RFC 8259**. [IETF](https://www.rfc-editor.org/info/rfc8259/) |
| JSON Schema | Root manifest explicitly declares **Draft 2020-12** | **Draft 2020-12**. [JSON Schema specification](https://json-schema.org/specification) |
| Markdown | Authored documents, fenced Mermaid and tables; platform renderer not pinned | **CommonMark 0.31.2**; GitHub adds its own extensions. [CommonMark](https://spec.commonmark.org/) |
| TOML | Replit-only `.replit` configuration; no language-version declaration | **1.1.0** ([TOML specification](https://toml.io/en/)); actual supported syntax follows [Replit's parser](https://docs.replit.com/replit-app/configuration). |
| ZIP, DOCX and PDF | ZIP exports use Python's library; existing DOCX/PDF files are preserved source artifacts | Artifact formats, not independently installed app libraries; no Word/PDF SDK in runtime. |

These standards are reviewed for compatibility, not automatically rewritten every
time a new edition appears. Existing canonical material and seals are preserved.

## Explicitly absent from the implemented stack

TypeScript, Vite, Tailwind, React, Next.js and PostCSS are not installed application
dependencies. There is no root frontend manifest, frontend lockfile, TypeScript
source/configuration or Vite/Tailwind build configuration. References in skills
and planning material describe other projects or reusable guidance.

There **are** seven nested skill package manifests and the Python hash lock.
The previous inventory's blanket claim that the repository had no package
manifests or lockfile was incorrect. A browser, VS Code or an assistant being used
to edit this repository does not make its entire dependency tree part of the app.

## Implemented update mechanism

1. **Weekly release audit, Mondays 09:17 UTC and manual dispatch.**
   `scripts/audit-technology-versions.py` discovers the Mermaid pin, every entry
   in the Python lock, and action references in workflow YAML. It checks publisher
   metadata, compares complete numeric versions (patch, minor and major), excludes
   prereleases and yanked Python releases, and appends a timestamped Actions summary.
   Python, SQLite, Node LTS/Current, npm, pip and optional browser drivers are also
   reported for the executing host. Host drift is advisory by default.
2. **Dependency update PRs.** Dependabot checks pip requirements and GitHub Actions
   weekly. Its proposed edits must keep both requirement files synchronized and
   preserve approved hashes. The required manifest check now explicitly checks
   lock agreement. If Dependabot cannot produce a consistent hashed lock, the PR
   stays blocked until the lock is regenerated and reviewed on Ubuntu Python 3.11.
   No credentials or bypass of repository protection are added.
3. **Runtime compatibility follows stable releases.** Application CI runs Python
   `3.11` and `3.x` with `check-latest: true`, plus explicit Node `lts/*`.
   It runs weekly at 09:47 UTC and on relevant pull requests. Requirements changes
   trigger application checks. Keep the 3.11 support floor until a deliberate
   compatibility decision changes the manifest and documentation together.
   Hashed maintenance installation and maintenance tests run on Ubuntu Python 3.11;
   the latest-Python job exercises the dependency-free application. The existing
   hashes are not portable approvals for newer CPython or Windows wheels.
4. **Mermaid migration candidates.** The command below updates only the exact CDN
   version and preserves other bytes. It refuses major upgrades by default.
   For the current 11-to-12 upgrade, review the release notes, then opt in with
   `--allow-major` on a feature branch. The weekly audit continues to signal drift
   until a compatible version is merged.
5. **Merge and adopt.** Review release notes and the actual diff; pass the manifest
   gate, both application jobs and applicable browser QA. Merge through the normal
   PR process. Replit and developer machines then update their own runtimes and
   pull the merged source, preserve private data, and rerun checks. A merged CI
   change does not upgrade those machines automatically.
6. **Manual coverage.** Each monthly maintenance review checks Git, CLI, Bash,
   LibYAML, Replit modules, hosted integrations, standards and newly introduced
   manifests/imports against this inventory. Assign discovered updates to an owner
   and target the next maintenance window. Major migrations get their own test plan.
   These manual categories are not represented as automatically updated packages.

The automation proposes dependency updates and exercises current runtimes.
It does not automatically merge breaking releases, alter machine installations,
rewrite canon, or publish the owner-local application.

## Commands and failure handling

Run from the repository root with a supported final Python release:

```bash
python3 scripts/audit-technology-versions.py
python3 scripts/audit-technology-versions.py --include-host
python3 scripts/audit-technology-versions.py --json-output .local/technology-audit.json --markdown-output .local/technology-audit.md
python3 -m unittest discover -s scripts/tests -p 'test_technology_versions.py' -v
```

Candidate creation, only when ready to review a source change:

```bash
python3 scripts/audit-technology-versions.py --prepare-mermaid
# After reviewing the major migration:
python3 scripts/audit-technology-versions.py --prepare-mermaid --allow-major
git diff -- web-templates/index.html
```

On Windows use an explicitly selected final interpreter (for example `py -3.13`).
Existing maintenance scripts print Unicode; use `PYTHONUTF8=1` for their tests.

Exit **0** means monitored repository pins are current; **1** means an update is
available; **2** means incomplete evidence (network failure, unexpected metadata,
unsupported pin, or source older than the declared version). npm throttling and
GitHub API limits are reported as unknown. Wait for the next scheduled run or
retry once the service recovers. Never translate an incomplete check into “current.”
The workflow supplies its existing read-only GitHub token only to GitHub API URLs.

## Evidence limits and next action

| Claim | Tier | Evidence | Consequence if false / next check |
|---|---|---|---|
| Runtime stack and pins above | Confirmed | Source baseline, Windows commands, Replit shell | A hidden host dependency could be missed; repeat the host inventory when adopting an update. |
| Stable release values | Confirmed at retrieval | Publisher links in each row | Releases change; use the weekly audit. Nix manual/download discrepancy is retained explicitly. |
| Broad browser compatibility | Unknown | Optional drivers are not pinned or available from the initial checkout | Run browser QA before accepting a Mermaid major or UI/platform change. |
| New scheduled automation is active | Not established by local files | Activation requires merging these workflow/configuration changes to the default branch | Verify the first scheduled/manual run and first Dependabot PR after merge. |
| Automatic updates of every host or service | Not provided | Host installs and hosted services are separately owned | Execute the per-host adoption step; preserve local work and private databases. |

The September 20 maintenance pass adopted Mermaid 12 after the bounded browser comparison above. Host interpreter migration remains separate.
