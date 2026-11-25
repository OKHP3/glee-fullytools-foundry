# Workflow acceptance for the remaining 39 Glee-fully plugins

All **39 private ChatGPT plugins passed their two-turn workflow tests**. The final conversations met **286 of 286 expectations**. Each test asked for a usable result, then changed a fact, constraint or destination in the same conversation. Four plugins needed a repair and a fresh test, bringing the total to **43 conversations and 86 replies**. Together with the [earlier 14 workflow tests](workflow-acceptance.md), these runs cover all 53 migrated plugins.

The tests ran on November 24, 2026 (US Central). All 43 conversations were reopened and both replies were checked against the original prompts. The tables show what changed between turns and which reference fact the reply demonstrated. The [machine-readable results](remaining-workflow-acceptance.json) give the prompts, criteria, observed outcomes and versions for individual products.

## Personalizable Tools and Discovered Careers

| Product | What the plugin produced and revised | Knowledge check |
| --- | --- | --- |
| [Personalizable Tools](../capabilities/personalizable-tools/) | Routed an 18-paperback collection and its loans to Personal Librarian. When the task changed to tracking applications, it supplied the Career Seeker handoff. | Identified the toolbox Pulsebook’s visit-aware conversation flow. |
| [Grounded](../capabilities/personalizable-tools/grounded/) | Drafted instructions for a fictional paper-craft concierge. The revision kept two desks active, redirected requests away from a closed desk and distinguished first visits from return visits. | Located the As-Deployed Star and Protoform instruction sections in Pulsebook v1.7. |
| [Icon Maker](../capabilities/personalizable-tools/icon-maker/) | Generated a square card-file icon with a butterfly, keyhole and three ruled lines. The edited image replaced those lines with one five-point star. | The accessible visual description supplied the original design details. Both generated images were inspected. |
| [Discovered Careers](../capabilities/discovered-careers/) | Routed résumé tailoring and application tracking separately. It kept the same job ad when the user replaced tracking with a cover-letter request. | Returned the exact branch pulse identifier and named its Pulsebook. |
| [Resume Builder](../capabilities/discovered-careers/resume-builder/) | Built a first résumé from volunteer notes. The revision credited the applicant for proofreading four signs a teammate created and greeting visitors at two events. | Located Responsibilities and Accomplishments, in order, in the résumé schema. |

## Treasured Finds and Tasty Tracker

| Product | What the plugin produced and revised | Knowledge check |
| --- | --- | --- |
| [Treasured Finds](../capabilities/treasured-finds/) | Kept six paperbacks with Personal Librarian and replaced the candle handoff with Spirited Journal for four unopened bottles of wine. | Named burn time and scent throw for candles. |
| [Personal Librarian](../capabilities/treasured-finds/personal-librarian/) | Exported two books as CSV, then added an unread paperback edition. The four-star rating stayed with the audiobook. The result had two titles and three format records. | Used the eight upload-template columns in order. |
| [Spirited Journal](../capabilities/treasured-finds/spirited-journal/) | Moved a gifted bottle from unopened to opened, added the picnic tasting and retained the other bottle’s rating. The unopened view became empty. | Applied nose, palate, finish and occasion, leaving unsupplied impressions open. |
| [Bag Nabbit](../capabilities/treasured-finds/bag-nabbit/) | Logged a tote in rotation and a satchel on the wish list. After the tote was lent out, its earlier use remained in the history and neither bag was available. | Identified the four tracking states, including a loan to a friend. |
| [Tasty Tracker](../capabilities/tasty-tracker/) | Routed a favorite soup through recipe filing and Friday meal planning. After supper was canceled, it replaced the meal planner with a pantry comparison. | Identified Flavor Meister as Menu Conductor’s source for favorite or highly rated meals. |

## Traveler’s Guide

| Product | What the plugin produced and revised | Knowledge check |
| --- | --- | --- |
| [Traveler’s Guide](../capabilities/travelers-guide/) | Handed a future weekend to Itinerary Hacker and a ferry ticket to Memento Log. After the trip, Journey Diary replaced the planner and the ticket retained its own handoff. | Identified scrapbook and logbook as collection formats. |
| [Journey Diary](../capabilities/travelers-guide/journey-diary/) | Revised a solo trip entry and its structured record to include the traveler’s sister and the correct meal. The paper ticket remained a physical keepsake. | Applied emotion, location and type to the ticket while leaving emotion unspecified. |
| [Itinerary Hacker](../capabilities/travelers-guide/itinerary-hacker/) | Moved a break to fit an earlier departure, preserving both transfers, the fixed tour and lunch. The revised return buffer was 30 minutes. | Identified hours, fees, travel time and detour distance. |
| [Detour Discoverer](../capabilities/travelers-guide/detour-discoverer/) | Selected the 60-minute gallery visit in a 100-minute window. When only 55 minutes remained, it marked both off-site stops skipped. | Identified solo, family and romantic as example trip types. |
| [Dreamland Journeys](../capabilities/travelers-guide/dreamland-journeys/) | Kept Edinburgh on a wishboard and replaced San Francisco with Tokyo. The total USD 900 ceiling stayed unallocated. | Matched the CSV’s Foggy Cities and Neon Nights rows, including Tokyo’s season value of `All`. |
| [Memento Log](../capabilities/travelers-guide/memento-log/) | Left the reflection empty on a ferry-ticket card, then corrected the ticket color and inserted the supplied reflection verbatim. | Identified what the archive ledger holds and how it preserves entries as read-only historical snapshots. |

## Organized Life

| Product | What the plugin produced and revised | Knowledge check |
| --- | --- | --- |
| [Organized Life](../capabilities/organized-life/) | Prepared separate bill and chore handoffs. When asked for a single view of the bill and a habit, it redirected both to Lifestyle Wallboard. | Correctly read the two parameter-ledger settings for automatic and symbolic indexing. |
| [Task Maestro](../capabilities/organized-life/task-maestro/) | Scheduled a short task ahead of a report. It marked the short task complete once and split the revised 12-minute report into ten minutes now and two pending. | Identified project, mood and required effort as task dimensions. |
| [Thrifty Spender](../capabilities/organized-life/thrifty-spender/) | Reconciled a corrected price and another purchase to $43 spent and $47 left. The separately paid utility bill stayed outside groceries. | Identified alerts before the due date, on the day and when overdue. |
| [Giftlist Helper](../capabilities/organized-life/giftlist-helper/) | Updated a scarf to bought and wrapped and an atlas to bought and unwrapped. The revised list showed $26 spent, $14 remaining and one gift to wrap. | Identified intent, source and category as optional Idea Catcher tags. |
| [Scheduling Wizard](../capabilities/organized-life/scheduling-wizard/) | Drafted four Friday appointments and moved only the second one an hour later, preserving the other three times and durations. | Named Sunrise Sprints, Midday Sparkles and Twilight Anchors. |
| [Lifestyle Wallboard](../capabilities/organized-life/lifestyle-wallboard/) | Updated a weekly dashboard after a parcel errand and overdue fee were resolved. Stretching remained completed on two of four days. | Identified printable and digital status reports. |
| [Neighborly Bazaar](../capabilities/organized-life/neighborly-bazaar/) | Revised a fictional dryer listing to $240 and kept its model, width, repair, cosmetic flaw and pickup terms together. | Distinguished the worked dishwasher example and its illustrative $275 price from the user’s dryer. |

## Healthy Bee-ing

| Product | What the plugin produced and revised | Knowledge check |
| --- | --- | --- |
| [Healthy Bee-ing](../capabilities/healthy-bee-ing/) | Corrected a Monday sleep entry, retained Tuesday’s observation and left Wednesday’s energy unknown. | Identified the three subjects in Maven Wise’s graphing entry. |
| [Healthy Bee-ing hosted variant](../capabilities/healthy-bee-ing/hosted-variant/) | Kept Moody Log for hydration and mood, then replaced the desk-reset handoff with Medi Minder when the request changed. | Located Caregiver Mode and kept reminder sharing inactive. |
| [Care Check](../capabilities/healthy-bee-ing/care-check/) | Revised the start and duration of a fictional episode in a clinician-facing note. The unmeasured temperature remained unknown. | Identified Medi Minder’s visual prescription-refill countdown. |
| [Calm Keep](../capabilities/healthy-bee-ing/calm-keep/) | Corrected one stress-rating change and logged a separate walk with unchanged ratings, preserving unknown rest data. | Identified stress, rest and movement as inputs without inferring a cause. |
| [Snappy Count](../capabilities/healthy-bee-ing/snappy-count/) | Changed one lunch drink to tea and logged an evening apple separately. Portions and images remained unspecified. | Identified the weekly plate collage. |
| [Medi Minder](../capabilities/healthy-bee-ing/medi-minder/) | Moved only a pharmacy call, preserved another check and marked a separate appointment canceled. No reminders or sharing were activated. | Identified Caregiver Mode for trusted reminder sharing. |
| [Moody Log](../capabilities/healthy-bee-ing/moody-log/) | Corrected an afternoon mood and drink amount. Known intake totaled 500 mL, with the evening amount still unknown. | Identified the hydration and mood overlay. |
| [Maven Wise](../capabilities/healthy-bee-ing/maven-wise/) | Revised a morning-to-evening rating difference from three points to two while preserving an unknown context in a later entry. | Identified medications and appointments as links for side-effect logs. |

## Identity Known

| Product | What the plugin produced and revised | Knowledge check |
| --- | --- | --- |
| [Identity Known](../capabilities/identity-known/) | Routed a possible chair to Roost Wrangler, then redirected the same object to Maker Matcher when the description revealed a ceramic brooch. | Correctly reported zero uploaded knowledge files and attributed the routing to the branch instructions. |
| [Critter Spotter](../capabilities/identity-known/critter-spotter/) | Kept two candidates open on a first description, then revised the field journal to probable chipmunk after the user added stripe details. | Identified the image-and-identification export pair. |
| [Roost Wrangler](../capabilities/identity-known/roost-wrangler/) | Revised a chair card to record manufacture in 2021, retaining modernist styling as a possible influence and leaving the maker unknown. | Identified room, vibe and period influence as furniture tags. |
| [Sight Seeker](../capabilities/identity-known/sight-seeker/) | Compared two bridge candidates from a scene description and changed its leading identification after the user supplied a Lisbon caption. | Identified overlaid labels for annotated images. |
| [Snap Decoder](../capabilities/identity-known/snap-decoder/) | Preserved verbatim text and kept possible causes separate. A wider-crop description updated the same entry and retained the reported paused state. | Identified theme, urgency and sentiment as organizing fields. |
| [Motif Muse](../capabilities/identity-known/motif-muse/) | Revised a swatch from navy and cream to navy and oatmeal, identifying herringbone after a description of the staggered pattern. | Identified style cards and color swatches as reusable exports. |
| [Maker Matcher](../capabilities/identity-known/maker-matcher/) | Updated a provisional macramé profile to paper basket weaving, keeping square knots as a feature of the suspension ties. | Identified the hobby profile card and discovered-interest tags. |
| [Self Fixer](../capabilities/identity-known/gpt07g-self-fixer/) | Turned an estimated shelf-peg description into a revised parts-counter request using the supplied caliper measurements. Compatibility remained unverified. | Identified a diagnostic snapshot and tool crib log as outputs. |

## Download the tested versions

Download the [39 verified public workflow packages](https://github.com/OKHP3/glee-fullytools-foundry/releases/tag/workflow-plugins-v2). The [package register](remaining-workflow-packages.json) lists each ZIP’s tested version, SHA-256 checksum and knowledge files. The public editions use FoundRy capability links and reviewed reference material. Self Fixer uses the public ideation ledger in place of the correspondence held in the private release.

## Repairs and retests

Journey Diary, Itinerary Hacker and Detour Discoverer gave correct travel answers but attached links to retired GPTs. The updated releases use the [travel specialist directory](../capabilities/travelers-guide/operational/specialist-handoffs.json) for handoffs and cite a reference directly when a user asks a factual question. Fresh conversations passed on Journey Diary 0.4.2, Itinerary Hacker 0.6.2 and Detour Discoverer 0.6.2.

Identity Known 0.10.2 correctly reported that it had no knowledge uploads. It omitted both requested specialist handoffs. Version 0.10.3 added its [seven-specialist directory](../capabilities/identity-known/operational/specialist-handoffs.json). The retest routed the chair to Roost Wrangler and the ceramic brooch shaped like a chair to Maker Matcher.

Icon Maker 0.7.3 [indexed its two visual reference companions](../capabilities/personalizable-tools/icon-maker/operational/icon-output/knowledge-index-additions.json) before its conversation test. The plugin reported it could not open the original PNG directly and used its verified text companion to reconstruct the design. A reviewer inspected both generated images.

## What the evidence covers

The archive audit compared all **214 original knowledge-file occurrences** with their SHA-256 digests and verified **two additional Icon Maker companion files**, an SVG and an accessible visual description. All 216 files had index entries. No original was missing or changed, no index target was missing and no duplicate index rows were found. A shared file counts once for each plugin that includes it. Identity Known intentionally has zero uploads.

The conversation tests checked specific reference facts and how each product revised a deliverable. The private transcripts, launch destinations and account details are outside this public report. ChatGPT did not expose independent per-answer file-open telemetry. Text-only identification cases establish reasoning from the supplied description. Live bookings, purchases, calendar writes, sharing and cross-chat persistence require separate tests.
