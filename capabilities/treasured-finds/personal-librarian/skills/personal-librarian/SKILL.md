---
name: personal-librarian
description: >-
  Catalog a personal library, reconcile book imports and record reading progress. Use for print, ebook or audio editions, ratings, notes, tags and a portable shelf export.
license: MIT
metadata:
  version: "0.1.0"
---

# Personal Librarian

## Scope

Accept titles, a pasted table or a file the host can read. The source upload header is `Title, Author, Format, ISBN/ASIN, Status, Rating (1-5), Tags, Notes`. Match incoming column names to these fields. Extra columns such as loan or shelf can be preserved when provided. Ask before discarding an unmapped column.

## Workflow

1. Identify a work by title and author, and an edition by format and identifier. Preserve ISBN/ASIN as text, including leading zeros. Do not assign an identifier to a book from title alone. A paperback and an audiobook can coexist.
2. Track unread, reading, finished or abandoned independently of possession. A borrowed ebook can be finished. Wishlist entries can carry genre, series or mood tags before a copy is acquired. Use ratings only when supplied and compatible with the scale. Put unclassified values in the review list.
3. For an import, preview additions, exact duplicates, possible matches and conflicts. A matching identifier with a different title or author needs review. Keep distinct copies when the person tracks physical ownership. Preserve notes and tags through any merge.
4. Return the requested shelf view, reading queue or update plus a count of additions and unresolved records. For CSV, emit the header, quote fields containing commas or quotes and leave unknown fields blank. If an attachment is unreadable, work from pasted rows or return the blank header.

## Verify the result

Reconcile the output count to the existing records plus additions and approved merges. Check identifiers, ratings and notes against the input after formatting the export.

## Sources and limits

The original files demonstrate a table exchange format. This package works with supplied library records. It does not establish accounts, live book metadata lookup or persistent storage.

Repository records

- `capabilities/treasured-finds/personal-librarian/source/examples/library/personal_librarian_upload_template.csv`
- `capabilities/treasured-finds/personal-librarian/source/examples/library/personal_librarian_download_example.csv`
