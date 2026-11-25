# ChatGPT runtime tests for the Glee-fully plugins

The [subsequent workflow acceptance run](workflow-acceptance.md) covers the
completed releases of the 14 plugins identified as under construction below.
The [other 39 workflow tests](remaining-workflow-acceptance.md) complete
two-turn coverage across all 53 private plugins.

On November 24, 2026 (US Central), all **53 current private plugins** passed their final representative instruction-following and knowledge checks in signed-in ChatGPT. The test run produced 76 answered conversations. The [per-plugin results](hosted-plugin-runtime-results.json) preserve the tested versions, prompts, observed answers in summary, handoff destinations and earlier attempts.

| Final check | Result |
| --- | --- |
| Follow a product-specific instruction | 53 of 53 passed |
| Answer a question checked against a bundled text reference | 51 of 51 passed |
| Use a visual reference to produce an icon | Icon Maker passed using the verified text companion |
| Handle a plugin with no knowledge uploads | Identity Known correctly identified the absence of an attached source |
| Offer a working handoff when a final answer contained a ChatGPT plugin link | All 15 links in 12 answers matched the intended private plugins |

## What changed after testing

| Finding | Repair and observed retest |
| --- | --- |
| Healthy Bee-ing named Moody Log but linked to Calm Keep. Other hosted instructions also used retired or misassigned GPT addresses. | Replaced 150 launch-link occurrences across 35 private plugins. The second Healthy Bee-ing now opens the current Moody Log plugin, and Discovered Careers links to the current Resume Customizer. [Routing changes](hosted-plugin-routing-updates.json) |
| Some answers still offered a historical link from a knowledge file after the instructions had been updated. The toolbox also stopped at a family when asked for a specific tool. | Added explicit current-destination rules. In fresh chats the toolbox linked to Personal Librarian, Letter Composer to Career Seeker, Palatably Profiled to Flavor Meister and Decor Detective to Scentinal Journal. Giftlist Helper identified two historical names whose successors could not be verified and offered Organized Life for browsing. [Handoff rules](hosted-plugin-handoff-rules.json) |
| Icon Maker could identify a reference filename but could not read its PNG or deliver the requested icon. | Added a verified visual description and a usable SVG fallback. In a fresh chat, version 0.7.2 generated a 1254 × 1254 image. Visual inspection confirmed the multicolored butterfly overlapping the brown filing drawer, the gold keyhole plate, the three ruled marks on the protruding card, the striped background and the cream wordmark. ChatGPT attributed its rendering to the companion description. [Icon Maker repair](../capabilities/personalizable-tools/icon-maker/operational/icon-output/README.md) |

## How to interpret a pass

Each conversation started with **Try in chat** on the owner’s plugin directory page. The page supplied the release version, and the sent message linked to the selected plugin. A reviewer compared the completed response with the plugin instructions and independently inspected source material. For handoffs, the review checked the clickable destination as well as its displayed name.

For example, Dreamland Journeys matched *Foggy Cities* to Edinburgh and San Francisco in spring. Personal Librarian returned its eight-column import header. Organized Life identified both indexing defaults in its parameter ledger. These questions exercise distinct content that a generic on-topic answer would miss.

The results cover the tested scenarios. ChatGPT exposed no independent file-open trace. The knowledge checks establish answer accuracy for the sampled material. Icon Maker still requires its companion for that PNG. Fourteen plugins explicitly describe their principal workflows as under construction. Their tests checked whether they explained that limitation accurately and could still answer from the relevant guide.

The [migration package index](hosted-gpt-plugins.md) identifies the archived public editions. The test record identifies the private hosted versions exercised after repair. The owner retains the conversation receipts separately.
