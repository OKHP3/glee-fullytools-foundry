# Fourteen completed Glee-fully workflows

On November 24, 2026, the 14 private ChatGPT plugins previously marked under construction passed their two-turn workflow tests. A tester launched each plugin from its directory page, confirmed the version and selected plugin, requested a finished deliverable, then changed an input in the same conversation. The final runs met all **112 expectations in 28 replies**. The initial Letter Composer run and its retest brought the total to 15 conversations and 30 replies.

The [downloadable release](https://github.com/OKHP3/glee-fullytools-foundry/releases/tag/workflow-plugins-v1) contains one public workflow ZIP per product and a SHA-256 checksum list. The [per-plugin results](workflow-acceptance.json) identify the exact prompts and criteria, the output observed on each turn, the checked reference fact, the private hosted version and the public archive digest.

| Capability and test | Observed result |
| --- | --- |
| [Resume Customizer](../capabilities/discovered-careers/resume-customizer/evals/skill-v0.2.0.json) | Revised the résumé after a correction to authorship. It kept unsupported terms from the bundled IT vocabulary list out of the applicant’s claims. |
| [Career Fitness](../capabilities/discovered-careers/career-fitness/evals/skill-v0.2.0.json) | Reconsidered two roles against a revised pay floor and schedule, then proposed a two-hour work sample for the stronger fit. |
| [Letter Composer](../capabilities/discovered-careers/letter-composer/evals/skill-v0.2.0.json) | Delivered a formal 84-word revision, credited the checklist’s author and recorded what the applicant tested and suggested. |
| [bLinkIn Tuner](../capabilities/discovered-careers/blinkin-tuner/evals/skill-v0.2.0.json) | Updated the headline, About and experience copy after a correction. It distinguished demonstrated skills, coursework and unsupported keywords. |
| [Career Seeker](../capabilities/discovered-careers/career-seeker/evals/skill-v0.2.0.json) | Preserved the rescheduled interview, reconciled a duplicate application and reported one completed interview from two March submissions. |
| [Decor Detective](../capabilities/treasured-finds/decor-detective/evals/skill-v0.2.0.json) | Reconciled eight lanterns after takedown: three on the porch, four in bin B7 and one in the mending tray with a torn loop. |
| [Present Hoarder](../capabilities/treasured-finds/present-hoarder/evals/skill-v0.2.0.json) | Kept two identical gifts distinct. Its recipient-facing summary disclosed only one wrapped gift still held and one gift shipped. |
| [Scentinal Journal](../capabilities/treasured-finds/scentinal-journal/evals/skill-v0.2.0.json) | Corrected a session to 30 minutes, added a 35-minute session and reported 65 observed minutes for the open item while its mate remained sealed. |
| [Supply Haus](../capabilities/treasured-finds/supply-haus/evals/skill-v0.2.0.json) | Used three reserved metres and released one, leaving nine metres available. The scissors stayed checked out. |
| [Flavor Meister](../capabilities/tasty-tracker/flavor-meister/evals/skill-v0.2.0.json) | Preserved lemon in the base recipe, recorded lime as a variation for one cook, corrected an earlier rating and marked the recipe as a favorite. |
| [Menu Conductor](../capabilities/tasty-tracker/menu-conductor/evals/skill-v0.2.0.json) | Revised the two-day plan to feed two diners and then four. It kept the same batch for reserved portions and recalculated the shopping slip. |
| [Wishful Tastes](../capabilities/tasty-tracker/wishful-tastes/evals/skill-v0.2.0.json) | Turned the noodle wish into a completed walk-in and recorded the $28 quote separately from the $30 actually paid. The bun wish stayed open. |
| [Pantry Shopper](../capabilities/tasty-tracker/pantry-shopper/evals/skill-v0.2.0.json) | Recalculated the rice shortfall from 350 g to 150 g and the purchase to one 250 g pack. It flagged the existing pepper to use first. |
| [Palatably Profiled](../capabilities/tasty-tracker/palatably-profiled/evals/skill-v0.2.0.json) | Corrected the shared-dish count from one to two, identified where ratings agreed and diverged, and proposed a peanut-free next tasting. |

## What the test caught

Letter Composer 1.0.0 inserted `[Your Name]` when the fictional applicant supplied no signature. Its stated word counts were also imprecise. Version 1.0.1 ends at the closing phrase in that situation and omits an unverified count. A fresh conversation produced complete letters of 89 and 84 words, both within the 100-word limit and free of placeholders. The other thirteen hosted plugins passed on version 1.0.0.

## Sources and scope

The workflows use the preserved GPT feature descriptions, FoundRy product catalog and available product-specific source files. Resume Customizer includes two original reference files about vocabulary and tone. Thirteen other products include newly authored worksheets for their intended work. The private plugins retain their original suite knowledge and existing handoff routes. Their public distributions use the reviewed public suite reference and link to FoundRy capability pages.

Each knowledge check compared an answer to a specific reference. ChatGPT provided no independent file-open telemetry. Tests covered creating and revising deliverables within one conversation. Connected-account writes, background reminders, cross-chat persistence and file-format export were outside these runs.

The portable skills are v0.2.0. Build the public packages with `python scripts/package-capability-plugins.py --workflow --all --output <directory>`. Add `--check` to compare an existing build. The [migration register](migration-map.json) maps the portable skills to their capability directories, and the [earlier runtime report](hosted-plugin-runtime-tests.md) preserves the original 53-plugin assessment.
