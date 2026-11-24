---
name: thrifty-spender
description: "Reconcile household bills and spending against category budgets. Use for recurring obligations, monthly comparisons or an exportable spending summary."
license: MIT
metadata:
  version: "0.1.0"
  author: "Glee-fully Personalizable Tools"
  origin: "OKHP3/glee-fullytools-foundry"
---

# Thrifty Spender

## Inputs

Take the period, currency, user-defined budget, dated transactions, recurring bills and paid status. Keep merchant aliases optional. Account numbers and logins are unnecessary.

## Workflow

1. Separate a scheduled obligation from a posted payment. Match on the user's evidence, amount and date. If two rows might represent the same payment, show a possible match and count only confirmed records as paid.
2. Group posted amounts by category and currency for the requested period. Compute remaining budget as budget minus net posted spending. Apply confirmed refunds as reductions and list unpaid bills separately as upcoming commitments.
3. Compare like categories across equivalent periods. Flag a partial month or missing category. Draft reminders from known due dates and statuses. The total for actual spending, outstanding bills and projected spending should remain distinguishable.

## Output

Return category, budget, posted net, remaining and pending obligations, plus a plain table suitable for a spreadsheet. For example, a $60 posted grocery purchase and $10 confirmed refund use $50 of a $100 budget.

## Limits

This is household bookkeeping. Avoid assuming a bank connection or payment execution. If currencies differ, split totals until a dated exchange rate is provided.

## Source

The catalog describes Thrifty Spender in inventory/inventory-of-toolbox-tools-and-tool-ettes.md. The preserved route overview is capabilities/organized-life/thrifty-spender/source/README.md. The catalog supplies the intended functions. The record formats and decision steps above are newly authored for this portable version. These paths document provenance. The skill can run from these instructions and the user's inputs alone.
