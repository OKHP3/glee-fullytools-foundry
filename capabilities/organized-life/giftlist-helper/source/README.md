# Glee-fully Giftlist Helper

Giftlist Helper is a cozy Glee-fully Tool-ette prompt for capturing, planning,
tracking, hiding, wrapping, giving, and remembering gifts.

## Status

The authored prompt declares `PME_READY`. This repository contains the prompt,
supporting ledger scaffolds, a brand asset, and distributable ZIP bundles. It
does not contain an application runtime, deployment configuration, database,
calendar connector, notification service, or verified GPT deployment.

## Start here

- [giftlist-helper-final.md](giftlist-helper-final.md): canonical authored prompt
- [AGENTS.md](AGENTS.md): repository guidance and validation commands
- [knowledgebundle/](knowledgebundle/): supporting ledgers, brand asset, and bundles

The copy of the prompt inside `giftlisthelper_builderbundle.zip` is intentionally
kept synchronized with the root prompt. The ZIP files are distribution artifacts,
not source trees to edit in place.

## Repository map

```text
giftlist-helper-final.md                     canonical prompt
knowledgebundle/                             product support and distribution
  dataLedger_*.txt                           ledger scaffolds and metadata
  Glee–fully Square Giftlist Helper.png      brand asset
  giftlisthelper_builderbundle.zip            prompt and brand bundle
  giftlisthelper_canonicaldataledgerbundle.zip ledger bundle
.agents/skills/                               repository-local agent tooling
skills/                                       migration support mirror
```

## Scope boundary

The prompt describes conversational behavior and lightweight CSV or Markdown
formats. Those descriptions are not evidence that persistence, reminders,
calendar export, uploads, or Present Hoarder synchronization are implemented.
