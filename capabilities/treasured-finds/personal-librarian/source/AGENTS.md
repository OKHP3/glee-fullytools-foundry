# glee-fully-gpt02a-personal-librarian

Canonical agent guidance for this repository. `CLAUDE.md` points here, so
update this file when the repository changes.

## Project identity

- Suite: Glee-fully, Branch 02
- Project: 02a Personal Librarian
- Repository: `https://github.com/OKHP3/glee-fully-gpt02a-personal-librarian`
- License: MIT
- Current status: early-stage content and data-fixture scaffold. No executable
  application is present in the repository.

## Understanding

### Confirmed

- The repository stores book-library import/export examples, templates, and
  reusable Agent Skills.
- The library schema has eight columns: `Title`, `Author`, `Format`,
  `ISBN/ASIN`, `Status`, `Rating (1-5)`, `Tags`, and `Notes`.
- CSV files use comma-separated values. The `.md` library files are tab-separated
  values despite their Markdown extension.
- `.agents/skills/` contains the retained project-local Agent Skills. The
  generated catalog in `.agents/skills/README.md` is the authoritative list.
- `skills/okhp3-skill-promotion/` is a verified publication mirror of the
  matching `.agents/skills/okhp3-skill-promotion/` package.

### Inferred

- The intended user value is helping a person maintain a personal book library,
  reading statuses, ratings, tags, notes, and related discovery workflows.
- The likely data flow is manual or tool-assisted exchange through the provided
  upload and download templates. No importer, exporter, database, or service
  implementation has been found.

### Unknown

- The intended runtime surface, deployment model, GPT configuration, and owner
  status are not documented in the repository.
- The allowed values and validation rules for `Format`, `Status`, `Rating (1-5)`,
  identifiers, tags, and notes are not formally specified.
- The relationship to the Notion anchor and the related Treasured Finds
  repository is not implemented or documented here beyond the project links.

## Repository map

- `examples/library/personal_librarian_upload_template.csv`: header-only CSV upload template.
- `examples/library/personal_librarian_upload.md`: header-only tab-separated upload template.
- `examples/library/personal_librarian_download_example.csv`: one-row CSV export example.
- `examples/library/personal_librarian_download.md`: four-row tab-separated export example.
- `.agents/skills/`: retained local Agent Skills and their bundled resources.
- `skills/okhp3-skill-promotion/`: verified publication mirror.
- `README.md`: public project orientation.
- `CLAUDE.md`: pointer to this file.
- `LICENSE`, `.gitattributes`, `.gitignore`: repository metadata and local cache
  protections.

There are no nested repositories, package manifests, source modules, test
suites, build configuration, CI workflows, or deployment configuration in the
tracked repository at present.

## Working conventions

- Preserve the eight-column library header exactly across all import/export
  artifacts unless a schema change is intentional and documented.
- Keep CSV quoting correct when fields contain commas, especially `Tags` and
  `Notes`.
- Treat the `.md` tab-separated files as data fixtures, not ordinary Markdown.
- Keep sample data fictional or already public. Do not commit private library
  records, credentials, connector identifiers, or other secrets.
- Keep generated Python caches and bytecode untracked through `.gitignore`.
- Preserve standalone punchy lines in generated content. Follow the ROY
  principle: explanation should earn its space.
- Do not use em dashes in generated content.
- Preserve the current branch and existing user changes. Do not force-push,
  rebase shared history, or use destructive version-control commands.

## Validation

No build, test, lint, or run command is defined. For changes to the current
artifacts, use the checks that match the files changed:

```sh
git status --short --branch
git diff --check
```

For schema-sensitive changes, verify that every CSV or tab-separated fixture
has the exact eight-column header and that every data row has eight fields.
Python's standard-library `csv` module is sufficient for this check. Re-read
the changed files after editing.

For catalog changes, use the retained cataloger in check mode first, then
regenerate the marked catalog only after reviewing the discovered skill set.

## Safe change procedure

1. Read this guide and inspect the relevant fixture or skill package before
   changing it.
2. Make the smallest change that serves the requested behavior. Do not invent
   runtime behavior from filenames or placeholder metadata.
3. Preserve existing user data and formatting conventions.
4. Run the applicable schema, catalog, and whitespace checks.
5. Update this guide when purpose, schema, runtime, validation, or repository
   structure changes.

## Risks and follow-ups

- The README and fixtures do not establish a runtime or deployment contract.
- The data schema has examples but no formal contract or automated validator.
- The root fixture filenames use underscores and the `.md` data files have a
  misleading extension. They remain unchanged until any external link or
  workflow dependency is confirmed.
- Owner input is needed to confirm the target runtime, intended GPT behavior,
  allowed field values, and whether the Notion or Treasured Finds links should
  become active integrations.

Generated from repository evidence on 2026-08-05. Refresh this file when those
facts change.

## Imported Claude Cowork project instructions
