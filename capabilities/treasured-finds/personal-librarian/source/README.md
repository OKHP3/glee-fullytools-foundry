# Glee-fully 02a Personal Librarian

An early-stage content and data-fixture scaffold for a personal book-library
assistant. The repository defines reusable library import and export examples,
and local Agent Skills used to maintain the project.

## Current status

This repository does not contain an executable application, importer, exporter,
database, deployment configuration, or automated test suite. The book-library
files are working artifacts for a future runtime or tool-assisted workflow.

## Library schema

Every library fixture uses these eight columns, in this exact order:

`Title`, `Author`, `Format`, `ISBN/ASIN`, `Status`, `Rating (1-5)`, `Tags`, `Notes`

CSV files are comma-separated. Files with the `.md` extension in this
repository are tab-separated data fixtures, not ordinary Markdown documents.

## Start here

- [Project guidance](AGENTS.md) explains evidence, boundaries, and validation.
- [CSV upload template](examples/library/personal_librarian_upload_template.csv) is a header-only import template.
- [Tab-separated upload template](examples/library/personal_librarian_upload.md) is the equivalent tab-separated template.
- [CSV download example](examples/library/personal_librarian_download_example.csv) shows one exported record.
- [Tab-separated download example](examples/library/personal_librarian_download.md) shows four exported records.
- [Local skill catalog](.agents/skills/README.md) indexes the retained project skills.

## Open decisions

The intended runtime surface, owner status, allowed values, validation rules,
and any Notion or Treasured Finds integration remain to be confirmed. Do not
treat the sample records or local skills as proof that those integrations or a
deployed product exist.
