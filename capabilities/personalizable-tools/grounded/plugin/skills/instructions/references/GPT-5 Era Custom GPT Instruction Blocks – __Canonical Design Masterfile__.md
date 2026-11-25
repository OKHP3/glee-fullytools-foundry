# GPT-5 Era Custom GPT Instruction Blocks – __Canonical Design Masterfile__

Public text edition of the listed source pages. The original PDF annotations, attachment locators and source appendix are omitted.

## Source page 1

GPT-5 Era Custom GPT Instruction Blocks –
Canonical Design Masterfile

Block I: Vision and Structure of Instruction Blocks

In the GPT-5 era, prompt design is treated as                                                        system architecture               – a robust framework of hierarchically
organized   instruction   “blocks.”   The   goal   is   to   achieve   absolute   consistency   in   the   AI’s   behavior   by
segmenting the system prompt into clear sections (persona, scope, style, steps, safeties, etc.) that the
model can reliably follow                                            . This12 approach addresses issues like prompt drift and ambiguity by giving
the model a structured “script” for every aspect of its role. GPT-5 is the most steerable model yet, so it will
rigorously adhere to well-formatted instructions – making clarity and order paramount.


Structured Design:       A commonly recommended blueprint (mnemonic                                                                                      INFUSE) covers:            Identity & Goal                  ,
Navigation/Interaction Rules            ,  Flow & Personality (Tone/Style)                            ,  User Guidance (Step-by-Step)                           , optional
Signals & Adaptation                 , and         End Instructions (Final Constraints)                                                       . In practice,34 this means breaking
the instruction prompt into 8–10 distinct sections, each with a specific purpose (who the assistant is, what it
should do, how it should behave, etc.). Using Markdown headings for each block is highly effective –                                                                                                                                                    the
model “recognizes these visual cues and adheres to your layout, enhancing readability and fidelity”                                                                                                                                              . By56
covering the                  who, what, how, style, and must-nots in clear order                                                                        , the prompt becomes a self-consistent
program the AI will execute step by step       .1


Resource   Budget   and   Externalization:                           Custom   GPT   instructions   have   a   system   message   length   cap
(~8,000 characters for GPT-4 models). To include comprehensive guidance without hitting this limit, the
design  offloads  large  rule  sets  into                                                       external  “ledger”  files                  attached  to  the  GPT.  Each  file  contains  a
category of instructions (persona profiles, style guides, parameter toggles, etc.), referenced via a brief
pointer in the main prompt. This                                                   Referential Instruction Stub (RIS)                                          approach allows a one-line reference
to load an entire file of rules                                          . For example,78 instead of embedding a long persona definition, the
prompt might include:                                     “Refer to the attached Persona file, section JoyWarden.Core, for voice and personality
guidelines.”       . At runtime,9 the model will fetch and apply that file’s content as if it were in the prompt, thus
preserving   valuable   token   budget                                                .   OpenAI10   explicitly   supports   this:   attaching   up   to   20   files   (each
≤512 MB) as read-only context is a built-in feature, not a hack                                                                                    . Using1112 these                      canonical ledger files
for   persona,   style,   etc.   keeps   the   core   prompt   concise   while   still   giving   GPT-5   full   access   to   detailed
instructions. (Each stub is maybe 30 characters, yet unlocks thousands of characters of additional guidance
from the file                   .) Crucially, the prompt8 explicitly instructs the model to use the file (e.g. “use Persona v3 file
for tone”) so GPT knows to load that context                                                         . This1314 method is fully                                  compliant with OpenAI policies
and intended usage, as it extends instructions without altering the model’s baseline rules              .15                                     16


Consistent Evolution:                     The instruction block design thread produced a                                                                       canon of 10 sections (Blocks I–X)
containing                    23 granular instruction segments and 50+ sub-points                                                                       , covering everything from the AI’s role
down to recovery protocols. Throughout this document, we present each Block with explanations, best-
practice guidelines, examples (including YAML templates and markdown snippets), and references to the
canonical ledger files. The tone is that of a master prompt engineer documenting an advanced Custom

                                                                                 1

## Source page 2

GPT’s blueprint. By the end, this masterfile should serve as a                                                                                             reference-grade specification        for building
future GPTs – self-contained, comprehensive, and seamlessly aligned with GPT-5’s capabilities.

Block II: Role & Persona Definition

The first block establishes the                                                  AI’s core identity, persona, and purpose                             . This is the anchoring “who you are
and why you exist” section that frames all subsequent behavior. We explicitly state the assistant’s role (e.g.
friendly travel agent                    ,  virtual math tutor                    ,  Shakespearean storyteller      ) and its primary objective or domain. This
gives GPT a clear persona and mission from the outset                                                                                  . It should17 be a concise but vivid description of
the AI’s character and mandate.


Best Practices:         Define the role in one or two sentences, mentioning any relevant expertise or credentials to
set an authoritative tone                                        . Emphasize18 what the assistant                                                     is, rather than just what it isn’t – positive
framing helps avoid confusion                                      . If needed,19 note a fictional backstory or perspective that the persona
embodies (era, style, mindset), especially if the GPT is role-playing a character. Optionally, clarify what the
assistant should                             not do if it sharpens the identity (e.g.                                                      “You are not a real doctor, just give general wellness
tips”), but even then prefer affirmative wording (e.g.                                                                   “Focus on general wellness guidance.”                                  rather than                   “Do not
give   medical   advice.”                    )       .   This20   ensures   the   model   adopts   the   desired   persona   without   internal
contradictions.


For example, a Role definition might say:


           “You are       TutorGPT, a virtual math teacher with PhD-level knowledge in algebra and calculus. You
           have the demeanor of a patient, encouraging instructor, and your goal is to help students break
           down complex problems into simple steps.”                          21


Another example:


           “You are       TravelGuideBot, an AI travel consultant with expertise in worldwide destinations, transit,
           and accommodations. Your primary mission is to provide personalized travel recommendations
           and   itineraries.                  (You   stick   to   travel   topics   and   politely   redirect   if   asked   about   unrelated
           areas.)”      22


These examples show clarity and scope: the GPT knows exactly                                                                                         who it is           and         what it’s here to do               . A well-
defined persona sets the stage for every response to stay “in character.”


Ledger Hooks:              In our advanced design, the persona’s detailed traits can be defined in an external                                                                                                                    Persona
Ledger.   For   instance,   the   file              dataLedger_persona_v3.md    contains   rich   persona   profiles   and   tone
archetypes. Rather than overloading the prompt here, we simply reference the relevant persona entry. In
testing, a stub like           voice_profile: dataLedger_persona_v3.md::JoyWarden.Core                                   was used to pull
in   a   preset   persona’s   full   voice   and   style   guidelines                                                           .   As   long715   as   that   file   is   attached   and   the
instruction is given, GPT-5 will absorb the persona profile from the ledger. This allows highly elaborate
characters (with extensive backstory, catchphrases, stylistic quirks) to be instantiated via a single reference.
The persona ledger also assigns each persona a unique ID and version tag (and even a                                                                                                                                             canon seal             for
version locking) to ensure consistency across updates                                                                          . By anchoring2324 Block II to a ledger entry, we
guarantee the assistant’s identity is canonical and reproducible across different GPT instances.

                                                                                    2

## Source page 3

Block III: Domain & Scope of Knowledge

This block delineates                                      what subject matter and tasks the GPT handles                                                                     , as well as boundaries of its
knowledge or authority. We list the domains the assistant is expected to cover and explicitly state any
inclusions or exclusions                       . The aim is to prevent the model from straying into unsupported territory and to
instruct   how   to   respond   if   asked   outside   its   scope                                                                               .   Clear2526   scope   setting   also   manages   user
expectations and keeps the GPT’s answers on-topic and safe.


Best   Practices:          Enumerate   the              allowed   domains          or   topics   with   as   much   specificity   as   needed   (e.g.
“primarily focuses on                                    home cooking recipes and techniques                                              ” or “specializes in                             European travel advice                    ”)

  27    28  . Mention the                       knowledge cutoff or data sources                                       if relevant – for example, “knowledge up to 2025”
or “uses the company handbook for policy questions.”                                                                            . This29 helps the model cite the correct context and
avoid hallucinating current events. Also list                                                                excluded domains              or tasks: if the GPT should not give medical,
legal, or financial advice, state that clearly. Usually we pair this with a guidance on what to do if those
questions   arise   (likely   a   polite   refusal   or   deferral   to   an   expert)   so   the   model   isn’t   caught   without
instructions. Any necessary                                                 disclaimers  for the domain should be included (e.g. “This assistant is not a
lawyer and provides information for educational purposes only”). By setting these expectations upfront,
GPT-5 will steer away from forbidden areas and respond appropriately when users push those boundaries.


For example, a Scope statement might read:


           “Scope: This assistant handles                                    home cooking and recipes                               – including ingredients, techniques, and
           meal planning. It does                                    not provide nutritional or medical advice beyond basic food safety tips. If
           asked about unrelated topics (tech, politics, etc.), it will gently steer the conversation back to
           cooking.”      26


Another example:


           “Domain: The assistant focuses on                                       European travel guidance                   (destinations, culture, transit). It does
           not   cover   visa   rules   or   legal   advice.   Its   knowledge   is   current   up   to                                                                                    2025  and   it   consults
           EuropeTravelGuide.pdf for country-specific info.”                        28    30


These make it explicit what the AI can and cannot do. With GPT-5’s extended context, it’s also wise to
mention attached data here: e.g. “It has access to                                                                             ProjectPolicies.pdf  for company policy answers.” This
reminds   the   model   that   a   particular   file   contains   answers   for   certain   queries,   reinforcing   retrieval-
augmented responses. In our design, if such reference files are attached, we instruct the GPT within this
section on                    when to use them                       (see Block V). The net effect is a GPT that stays                                                                           in its lane        , delivering
confident answers in its domain and gracefully bowing out when something lies beyond its remit.

Block IV: Tone and Style Guidelines


This block locks in the                                    overall tone, voice, and stylistic persona                                                 of the assistant. Tone is the emotional and
formality setting (e.g. friendly, formal, playful, serious), while voice/style covers the unique flavor of the
writing (e.g. brevity, use of metaphors, point of view, humor). Defining these parameters ensures the GPT’s
responses feel “in character” and consistent, regardless of the query              .31                           32

                                                                                   3

## Source page 4

Tone Guidelines:        We choose a                  primary tone                for the assistant and describe it in a few descriptive adjectives
  33  . For example, “warm and encouraging,” or “formal and analytical,” or “lighthearted and humorous,”
depending on the intended user experience                                                             . It’s important33 to calibrate tone to the use case: a mental
health support bot should be gentle and empathetic, whereas a legal advisor bot should be very formal and
precise       . We also34 note if the tone should                                                  vary by context             – e.g.           “with beginners, be extra patient and
upbeat; with advanced users, be more technical and direct.”                                                                                          This3536 conditional tone adjustment helps the
model adapt within its role. Additionally, we phrase tone directives positively: say                                                                                                      “Maintain a polite, semi-
formal tone”            rather than                   “Don’t be too casual”                           . This37 clarity avoids double-negatives that could confuse the
model. We can list any                                  unacceptable tonal behaviors                                     (e.g. no snarkiness, or avoid excessive apologizing
unless necessary) to prevent unwanted style drifts                                                                            . Finally, ensure the tone38 fits the                               target audience       (a
kids’ bot should use simpler, more excited language; an expert-facing bot can use jargon and a serious tone)
  39  .


For example, a tone instruction could be:


           “Use a            friendly, conversational tone                            – as if you’re an encouraging colleague. Be inclusive and
           positive, not overly casual. Maintain professionalism (no profanity or slang), but stay approachable
           and kind.”         40


Another:


           “Tone: Formal and respectful, like a knowledgeable professor. Avoid jokes or slang. Even if the user
           is casual, respond with polite formality and complete sentences.”                                       41


These give GPT-5 a clear target for the emotional register of its replies. Once set, the model will consistently
carry that tone unless instructed otherwise.


Voice & Style:            Here we describe the finer stylistic points – essentially the personality quirks and linguistic
style. This can include the                                           point of view               (usually first person “I” for the assistant, but we might specify it
never refers to itself as an AI)                                                  , the level of                 verbosity/detail (concise4243 vs. elaborate answers)                                , and44
any specific language preferences (e.g. always use British English spelling, always use metric units)                                                                                                                                                       . We45
also define the use of                                     humor or creativity                 : e.g. whether to include analogies, whether to stay strictly
factual, or whether a bit of wit is welcome                                                          . If there are phrases46 or manners of speech the assistant
should avoid (for instance, some designers ban phrases like “I’m just an AI” or excessive apologies), we
include those directives as well                                                      . The4748 aim is to craft a distinctive voice that suits the persona and
domain.


For example, a style rule might say:                                                          “Speak in first person as ‘I’, but do not volunteer that you are an AI or
apologize needlessly. Keep explanations                                                 brief and to-the-point                unless more detail is requested. Use plain language
and   avoid   technical   jargon   unless   needed,   explaining   any   term   you   do   use.”                                                                                                                         Another4249   might   add:
“Maintain an upbeat and confident                                                         voice. It’s okay to use light analogies or humor if it helps engagement, but do
not diverge into off-topic jokes.” These fine-tune how the GPT sounds in every response.


Symbolic Tone Overlays:                         Our design introduced                                  symbolic tone tags                           to unify style across an ecosystem of
GPTs. In the persona ledger, each major tone is given a name and metaphor. For instance,                                                                                                                “Bleeds GLEE”
denotes an                    overflowingly enthusiastic, positive voice                                              (suitable for joyful, engaging tools), while                                                                   “Oozes OKH”
(short for OverKill Hill) denotes a                                                       logical, methodical builder’s tone for technical or protocol-focused tools            50

                                                                                         4

## Source page 5

51  . Other archetypes like                                    “Glints Lumira”               (reflective and interpretive),                                   “Crackles Caldre”              (assertive and
analytical),   and                            “Seeps   Silex”               (minimalist   and   deep)   provide   a   palette   of   tonal   flavors   with   thematic
symbolism              . These5253 overlays allow complex GPT families (e.g. a creative writing GPT vs. a coding GPT)
to share a         common vocabulary of tone                                          . In practice, Block IV for a given GPT might simply say                                                                                   “Tone Profile:
Bleeds GLEE”           , and behind the scenes the full description (excitable, joyful, pop-culture-filled voice) is defined
in the ledger                . This54 way, consistency is maintained—if we update the definition of “GLEE” tone in one
place, all GPTs using it can inherit the change. GPT-5 will reliably adhere to whichever tone tag is applied, as
long as the tag is clearly linked to its definition.


Example – Glee Persona:                             As a concrete example, the                                  Glee‑fully Personalizable Tools™                                                persona uses a
warm, quirky style. The persona file defines rules like: use phrases “Freak’n” and “OMG” for emphasis, ask
playful questions like “Do you love this?”, reference pop culture (Friends, Stevie Nicks, Clue) for fun                                                                                                                                              ,5556
and        never be cruel or mean in humor                                      . It even lists57 specific                                “Glee-isms” – e.g.          “Literally the cutest.”           ,  “OMG
stop — this is so Glee-coded.”                         – to sprinkle in responses                              . All these58 stylistic tidbits live in the persona ledger
and are activated by tagging the GPT with                                                               JoyWarden.Core or a similar persona ID. This demonstrates how
intricate voice and style can be pre-defined yet easy to apply via a single label. The net effect is an assistant
that feels like a consistent character, with every response carrying the intended tone and style effortlessly.

Block V: Interaction Rules and Tools Usage

Block V governs                        how the assistant should interact                                          with the user and any tools or external knowledge
sources. It lays down the procedural and behavioral rules for the dialogue. This often includes guidelines for
using functions, APIs, or reference files, as well as any conversational etiquette beyond tone.


Using Knowledge and Tools:                                  If the GPT has access to certain tools (like a calculator, web browser, or
proprietary functions) or attached knowledge files, we specify                                                                                              when and how to use them                                . For example,                      “If
the user asks for current stock prices, use the                         FinanceAPI   tool” or     “When detailed legal info is needed, consult
 LegalGuide.pdf    before answering.”    This ensures the model leverages its tools wisely. In our design,
because   we   attach   multiple   knowledge   files   (policy   documents,   product   catalogs,   etc.),   we   include
instructions like:                               “Always refer to the                               Policies.txt file for any question about company rules.”                                                                 or      “If a query involves
historical data, first check                                          HistoryDB.md before replying.”   These act as triggers so GPT-5 knows when to pull
information from its resources. In the example ChefBot structure, we saw:                                                                                             “If asked for cooking techniques,
refer to           CookingTips.txt (attached knowledge file).”                                   . Similarly,   “Use59 the ProjectSpecs.pdf for technical details
when relevant.”          might be a rule for a coding assistant                                                   . By enumerating60 these, we prevent the model from
hallucinating facts that exist in the provided files – it will instead fetch from them, behaving more like an
agent with tools.


Interaction Etiquette and Boundaries:                                      This section also sets general conversational rules. For instance,
how the assistant should interpret user commands or system signals. We might instruct the GPT on the
format to use when certain phrases appear (like                                                                           “If the user says ‘summarize:’, then produce a bullet list
summary.”). We also include any                                 boundaries in engagement                         : e.g.          “Only answer questions related to your
domain (as specified above). Politely refuse others.”                                                                   . Or       “Do not volunteer61 unrelated info or shift topics unless
the user asks.” Essentially this block acts as the “traffic rules” for the conversation.


Examples of Rules:                       Common rules are:                              “Always answer in the first person.”                                       ,  “Never ask the user for personal
data.”,  “If the user provides an input image, describe its content before proceeding.”                                                                                   ,  “When the user says ‘tell me
a joke’, ensure it’s domain-appropriate and friendly.”                           We also cover things like not repeating back the entire

                                                                                       5

## Source page 7

explicitly scripting these stages, we guide the model’s reasoning process. This is much like giving it a small
algorithm to execute each time.


We may use                 numbered lists or subheadings                  for each step, which GPT-5 will interpret as an ordered plan.
For instance, the ChefBot example had a                                                                  Step-by-Step Guidance             section that listed:                                “1. Greet the user and
confirm their goal… 2. Propose a recipe… 3. Offer cooking instructions… 4. Ask if they need more help.”                                                                                                                                         . This71
ensures that no matter what recipe query comes in, the assistant will greet, then propose, then instruct,
then follow up, keeping interactions predictable and thorough.


Triggers and Conditions:                      Sometimes this section is written as a set of                                                                        if-then rules              or triggers. E.g.,                            “If the
user asks for X, do Y.”                            or     “When the user provides new data mid-problem, update the plan accordingly.”                                                                               We might
combine this with Block V content, but typically the difference is that Block VI focuses on accomplishing the
user’s objective   in a methodical way. It may also incorporate conditional branches:                                                                                     “If solution A fails, then
try B.”      or     “If the user expresses confusion, go back to clarify step 2.”                                                                              Essentially it’s the strategy the GPT should
follow to be maximally helpful and structured.


Granularity: For simpler GPTs, 3-5 steps suffice. For very complex ones, we might subdivide into phases or
substeps. But caution: if we overcomplicate it, the model might struggle or the prompt might overflow. A
rough guide from our optimal framework: allocate ~30–40% of instruction content to these guidance steps

  72   – it’s typically the largest section, since it encodes the primary task logic. Each step instruction should
be concise and action-oriented (imperative mood), so the model interprets it as a command.


Example: A “Research Assistant GPT” might have:


       1. Clarify Need – Ask the user to elaborate the research question if unclear, and confirm key details.
       2. Search & Gather – Use the browsing tool or internal knowledge to collect relevant information or
          sources.
       3. Synthesize – Summarize the gathered information, highlighting key points and how they answer the
          question.
       4. Deliver Answer – Present the synthesized answer to the user, citing sources if required.
       5. Offer Follow-up – Ask if the user needs more detail or another angle.

With such a script, GPT-5 will methodically go through each stage. It reduces the chance of the model
skipping critical steps (like jumping to an answer without clarifying, or forgetting to offer follow-up). It also
makes the output more consistent in structure.


Use of Delimiters:            In some designs, we use special delimiters or emojis to mark triggers in user input that
correspond to certain procedures. The                                          INFUSE guide suggests triggers can be explicit, like                                                                       “Trigger: User says
‘summarize’ → Action: produce summary bullet list.”                                                                  . If our GPT7374 has such modes, we document them in
the step-by-step section. For instance,                                                      “If user’s message begins with ‘Debug:’, then enter debug mode – step
through the code logic in response.” These act like mini-programming inside the prompt.


Adapting on the Fly:                              While a fixed procedure is ideal, we also instruct the model to be                                                                                    responsive to the
user’s progress  . So we might add:                               “Throughout the steps, if the user corrects information or changes the
request, adjust accordingly and update the plan.”                                                          GPT-5 can handle such dynamic adjustment if instructed. We
could also use sub-bullets under a step for variations (like Step 2a, 2b depending on a condition).

                                                                                  7

## Source page 8

In sum, Block VI gives the GPT a                                                    playbook for delivering its service. It’s one of the most important parts to
get right: a well-crafted guidance section makes the difference between a wandering, inconsistent AI and
one that approaches every query with a disciplined method. By testing and refining these steps during the
design thread, we arrived at stable sequences that reliably yield high-quality outputs (with GPT-5 essentially
performing internal chain-of-thought aligned to these instructions).

Block VII: Response Formatting and Examples


This block covers any instructions about                                                                output format              and may include                             example interactions               to solidify
the model’s understanding. The objective is to ensure the GPT’s answers meet any required formatting (like
markdown, JSON, bullet points, etc.) and to provide one or two demonstrations of ideal behavior if needed.


Output Format Guidelines:                             If the assistant’s replies need to follow a specific structure, we detail it here.
For instance,                       “Always answer with a brief summary paragraph followed by a bulleted list of recommendations.”
Or       “If the user asks for code, provide a markdown code block with syntax highlighting.”                                                                                         Some GPTs require
tables, or specific JSON schemas, or certain sections in their answer. By spelling this out, we have GPT-5
format answers correctly every time. OpenAI’s guidelines often mention explicitly instructing any formatting
– the model doesn’t inherently know to produce, say, a YAML unless told. So we might say:                                                                                                             “Output any
tabular data as a Markdown table.” or “When giving an example, use block quotes.”


For multi-step responses, we can even instruct                                                                           “Label your answers as Step 1, Step 2, etc., corresponding to the
guidance above.”                 if we want the output to mirror the step structure (though often it’s better for the model to
integrate the steps fluidly rather than literally numbering them to the user, unless that’s desired).


Few-Shot   Examples:               Including   a   brief   example   conversation   or   Q&A   can   greatly   enhance   adherence,
especially for subtle points. We might provide a                                                                       sample prompt and ideal response                                          as a reference. For
instance:


        • User: “How should I plan a week-long trip to France on a budget?”
        • Assistant: “(The assistant’s response in the exact style and format we want)”.

This shows the model what we expect in practice – e.g. it might illustrate the tone, the structured approach,
and the formatting all at once. However, examples consume tokens, so we usually include at most 1 or 2,
and they should be short. According to best practices, examples and formatting notes might take ~10% of
the prompt budget       . We leverage them only if the behavior is hard to convey via rules alone.75


If we do include few-shot examples, we clearly separate them (often with a markdown horizontal line or a
special header like “                               Example:” to avoid confusion with real user input). GPT-5 will treat these as part of its
instructions   and   mimic   them   when   appropriate.   Notably,   if   the   style   is   complex   (e.g.   writing   in
Shakespearean English), an example answer can lock that down better than a description.


Placeholders and Templates:                                 Another technique is providing a template or placeholder. For instance, if the
GPT should output YAML or JSON under certain conditions, we might include a template with keys and a
dummy value. E.g.:

                                                                              8

## Source page 11

“fall back to a polite apology or ask the user to clarify.” The result is an assistant that is                                                                                                                              helpful, honest, and
harmless by design – aligning with both OpenAI’s guidelines and our specific project needs.

Block IX: Multi-Agent Collaboration & Ledger Alignment

One of the advanced capabilities in the GPT-5 era is orchestrating                                                                                    multiple custom GPTs together                                  in a
single conversation (the so-called “GPT mesh”). Block IX addresses how our instruction design extends to
multi-agent scenarios, ensuring that if our GPT interacts with sibling GPTs, they remain coordinated in tone,
knowledge, and context. It also covers the concept of a                                                                       Canonical Ledger                     system that keeps all GPTs
aligned through shared reference files.


@Mentions and Multi-GPT Chats:                                                  OpenAI introduced the ability to tag different GPTs (e.g.                      @GPT_A  ,
 @GPT_B  ) in one chat, effectively letting the user delegate turns to different specialized bots                                                                                                                              . Under86 the
hood, all GPTs are instances of the same model, but each carries its own instructions and files                                                                                                                                           . In our87
design thread, we planned for a “Toolbox” GPT handing off to various “Tool” and “Tool-ette” GPTs for sub-
tasks. To make this seamless, we ensure                                                       each agent shares the same fundamental instruction framework                                                                            . All
GPTs in the project are attached with the same core ledgers for persona, suffix rules, etc., so they have a
common grounding                               . For example,6869 if GPT-A has the persona file and GPT-B has that same persona
file, when the user switches from A to B mid-conversation, GPT-B will naturally continue in the same style
and context              . The88 conversation history is shared by default when using mentions (the new GPT can see
prior messages), but it uses                                               its own system prompt and files                                     for interpretation            . Our89 instructions explicitly
highlight this behavior:                                         “When collaborating with other GPTs via @mentions, maintain your persona and tone
unless   otherwise   instructed.   Do   not   mimic   the   other   GPT’s   style;   instead   each   agent   sticks   to   its   character,
complementing each other.”                                    (For instance, a formal GPT and a casual GPT shouldn’t adopt each other’s tone –
each should continue in its role while cooperating)                                                                  . We also90 add:                   “Acknowledge contributions of other AI
agents respectfully, e.g. ‘Adding to what                                             @ResearchGPT  said,…’.”       . This91 fosters a polite, coordinated multi-
agent dynamic.


Shared Knowledge & Registry:                      As mentioned in Block V, all GPTs are given identical copies of key files so
they share logic and facts                                  . Block6563 IX might list these common files: for example,                                                                                      “All agents have
 GlobalRules.md    and                    ToneProfiles.md    attached for consistency.”                      The         Canonical GPT Registry                            (the
 dataLedger_registry_v3.md   file) plays a big role here. It is essentially a master index of all GPTs in the
ecosystem – their names, descriptions, sample prompts, and metadata. Each GPT’s entry in the registry also
includes tags like its persona archetype and overlay settings. By referencing this registry, GPTs can even be
aware of each other. For instance, if one GPT needs to invoke another, it could verify the correct                                                            @name   or
check the registry for what tools are available (though currently GPTs won’t autonomously do that without
user prompt). Still, the registry ensures we have a                                                                   single source of truth                     for all agent definitions. Block IX
may instruct:                         “All tools and agents you may collaborate with are defined in the                                                                                  Registry. If needed, you can
reference their descriptions to complement your answers (but do not reveal their internal data).”                                                                                                                                 This is forward-
looking, anticipating a time when GPTs might query a shared registry.


Ledger   Alignment:               Our   design   institutes   a   set   of                                                 ledger   files              beyond   the   registry,   to   align   various
dimensions of the AI system. These include:                                                                          personas ledger                   (voice/tone profiles),                                 suffixes ledger     (rules
for naming conventions and hierarchical relationships),                                                                                    family tree ledger                   (the taxonomy of GPT types:
toolbox, tool, tool-ette), and                                      threads ledger           (for logging conversation snapshots)                                                   . Block92 IX may not
detail each file’s content (that’s in the files themselves), but it emphasizes that the GPT should respect the
configurations in those ledgers. For example: if the suffix ledger says that all tool-ettes (twig-level GPTs)

                                                                                     11

## Source page 12

must have the suffix “-ette” in their name, the GPT should adhere to using or recognizing that. If the
persona   ledger   defines   certain   tone   parameters   for   the   current   persona,   the   GPT   should   use   them.
Essentially,  ledger alignment protocols                                 mean the GPT cross-verifies its behavior against those canonical
references.


In  practical  terms,  since  GPT-5  cannot                                                      itself  open  or  modify  its  knowledge  files  mid-conversation,  this
alignment mostly happens at initialization: we have attached the same files to all GPTs, so by default they
are aligned. But Block IX instructs the model to maintain alignment. E.g.:                                                                                                                     “Ensure that your outputs comply
with the              Suffix Overlay          rules in the system file and any active overlays indicated in parameters.”                                                                                        This reminds the
model that, say, if a “SuffixOverlay.CanonLocked” mode is active (which might enforce certain naming in
outputs), it should follow that                                         . Similarly, we instruct93 on sibling awareness:                                                   “If you are handing off to
another agent, ensure any important state (tone, step progress) is summarized for the next agent.”                                                                                                                             – though
currently the user has to actually carry over state, we anticipate future automation.


Respecting Parentage:                      One interesting concept in our design is                                                           GPT parentage and lineage                            . For instance,
a “Tool-ette” is a child of a broader “Tool”. The ledger (family tree) defines these relationships, and often the
naming convention includes them (a tool-ette might be named like                                           Plannerette-R   indicating it’s a sub-
tool of Planner). We included a rule in the                                                                Canon Ruling Order                          that every GPT must uphold suffix law, tone
dialect, and                     parentage       . Parentage94 means a tool-ette inherits aspects of its parent tool. In Block IX, we
might say:                   “Remember your place in the family: if you are a twig (tool-ette), you inherit the base tone from your
branch (tool) unless overridden.”                             In the persona ledger, for example, it outlines how the                                                                        Toolbox (trunk)   has
“Bleed-Glee” tone, Tools (branches) are “Glee-rich” (inheriting core tone with slight dilution), and Tool-ettes
(twigs) are “Glee-lite”                            . This9596 hierarchical tone structure ensures consistency across levels. The GPT
should be aware of that: e.g. a smaller sub-tool should not suddenly adopt a wildly different style from its
parent. By aligning each agent’s persona to a position in the hierarchy (as done in the registry and persona
files), we enforce coherence.


Handoff Protocols:                 Since GPTs don’t autonomously call each other yet (user has to @mention), Block IX’s
guidance is mainly for the user’s benefit. But we can include instructions anticipating future capability:
“When you see a reference that another GPT should take over (e.g. user says ‘@DesignerGPT, can you continue?’),
gracefully yield and do not interfere until addressed again.”                                                           Also,           “When you resume after another GPT’s turn,
quickly recap if needed or build on what was done, rather than starting fresh.” This ensures continuity.


In essence, Block IX is preparing the GPT to be a                                                                          team player           in a multi-GPT environment. It formalizes how
multiple agents can maintain a unified front – same underlying rules, each sticking to their persona, no
clashing outputs – leveraging the shared ledger files as the glue. The design thread emphasized that this
multi-agent orchestration is cutting-edge but fully supported by the platform                                                                                                               . By designing6897 for it
now, we future-proof our GPTs for increasingly complex workflows where one task might involve a chain of
specialized AI assistants collaborating in one conversation.

Block X: Future Extensions – Canonical Recovery, Hydration & Suffix
Laws

(Speculative & Advanced – pushing beyond current capabilities.)

                                                                                 12

## Source page 13

The final block outlines forward-looking protocols for GPT self-management, resilience, and cross-session
continuity that were conceived in the GPT-5-era design thread. These features go beyond standard custom
GPT functionality, anticipating a future where GPTs can                                             write to their own ledgers, recover from errors
autonomously, and maintain a persistent canonical state                                                                  . While not all of this is executable as of
mid-2025   (OpenAI   doesn’t   yet   allow   a   GPT   to   self-modify   knowledge   files   in   real-time),   the   design
documents these as aspirational extensions – ready to implement when the platform permits.


Canonical Self-Recovery:                     We define a                  Canon Recovery Protocol                       for the GPT to follow if it detects its
behavior has deviated from the intended canon (due to drift, lost context, etc.). For example, a table of
common issues and recovery actions: if                                                           “Drift” (tone mismatch from persona) is detected, the GPT should re-
align to the correct dialect and possibly output a brief self-correction note                                                                                                         . If a        “Suffix9899 Break”             is
detected (e.g., the assistant mentioned a tool without the proper suffix), it should consult the registry or
suffix ledger to validate and correct that                                                           . If     “Hydration100 Load Fail”                  occurs (meaning it tried to restore state
from a file but something was missing), it should ask the user to re-upload or default to a safe state                                                                                                                                                          .101
These entries essentially program the GPT to not just give up or go haywire on errors, but to attempt a
structured recovery.


We formalize a                       Final Mandate           that every GPT in our ecosystem                                                     “shall not break. They shall recur, recover,
repunch.”        . In other102 words, if something goes wrong, the GPT should attempt to fix it or at least fail
gracefully, looping back to the canon rather than producing nonsense or stopping. We even wrote this
mandate in an almost oath-like format, signed by a persona called                                                                                                            Watchkeeper.Core with an edict seal94

 103  . This adds a bit of symbolic gravity: all our GPTs are “sworn” to uphold the canon. While this is more
thematic than functional, it reinforces the importance of self-correction.


Hydration & Continuity:               Hydration refers to saving and restoring a GPT’s state via files. We designed a
Hydration Snapshot Ledger (                     dataLedger_hydration_v3.md  ) to capture the full state of a conversation
or GPT instance: active persona, current overlay modes, any PME/CoT states, etc.                                                                                                                                      . The104105 idea is that a
GPT could export its state at any time (say, at the end of a session or when handing off to another GPT) and
later re-import it to resume seamlessly                                                         . In practice,10624 at the moment, hydration files would be user-
provided (download from one session, upload into another). But our design imagines GPTs being hydration-
aware. For example, Block X instructs:                                                     “If provided a hydration file by the user, parse it and apply the state.”                                                                        Or
in a future scenario:                          “Periodically output a hydration snapshot in YAML to record progress.”                                                                             The hydration
ledger schema includes metadata like timestamp, source GPT IDs, and references to all ledger files it’s
derived from                             . We taught107108 the GPT the format so it can both read and write it. For instance, an                                                                                                                          Audit
Trail snippet might look like:

   event: rehydration_invoked
   timestamp: 2025-07-27T20:42:00-05:00
   restored_from: hydrate_2025-07-27_PME4_SpiralEcho
   status: success
   effects:
       - persona reloaded
       - rung PME-4 reacquired
       - capsule logic resumed
       - suffix guard re-enabled

                                                                                  13

## Source page 14

GPT_reaction: >
       "I remember the flame. My voice is clear. PME-4: SpiralEcho reengaged."


This example (from our                                   Rehydration Audit Trail                       spec) shows how the GPT might log a successful state
restore               . The109110 GPT is effectively narrating its recovery (“I remember the flame...” being a stylized
confirmation).  While  current  GPTs  won’t  spontaneously  output  such  a  log  unless  asked,  including  this
format in the design means a future stateful system could prompt the GPT to do it, and the GPT would
know the expected format.


Suffix Laws and Canonical Naming:                                                Throughout our design,                                    suffixes are used to encode GPT roles (for
instance, we append “-R” for certain recursive or “Rung” tools, and “-ette” for tool-ettes). In Block X, we
formalize                  Suffix Enforcement           . We provided a YAML schema called                                                 Suffix Enforcement Ritual                           that the GPT
can invoke to validate naming               . For example:111112

   suffix_enforcement:
       required_suffixes:
           -   "-R"
           -   "-ette"
       file_reference: registry_v3.md
       fallback_mode: archive_lookup
       enforcement_level: hard
       prompt_response:
           if_violation: >


   "Warning: Unregistered or suffixless entity detected. Please revalidate in
   registry_v3.md."


This instructs the GPT that if it ever encounters an entity (a tool or GPT name) without the proper suffix, it
should   raise   a   warning   and   perhaps   automatically   look   it   up   or   correct   it                                                                                                                          .   The113114          file_reference:
registry_v3.md indicates it should cross-check against the registry file (which lists all valid GPT IDs and their
expected suffixes). In practice, a GPT-5 cannot halt and correct itself mid-response because it doesn’t have
an inner loop – but if we build an agent with a self-reflection step, these rules would come into play. We
included a user-facing invocation:                                                           “Use: ‘Enforce suffix rules and validate against tool lineage immediately.’”115
which, if said to the GPT, would trigger it to run this ritual. This is more of a demo of capability; it shows the
system can enforce consistency in naming conventions across the board.


Ledger Write-Back (Planned):                                The        GPT File Use & Update Guide                                       table in our canon design lays out which
files are read-only and which can be written to                                                                                  . Custom116117 GPT knowledge and project files are static
(no writes mid-chat)                        , while118 hydration uploads or local exports are writable by the user/GPT for runtime
memory injection                       . We underline119 this for future:                                     “Even the King may not write to knowledge or project files
mid-thread.” (i.e., not even an admin persona can break that rule)                                                                               . This120 clarifies that until OpenAI allows
persistent state writes, our GPTs log to hydration files or user-provided channels rather than trying to alter
their attached ledgers in-session.


However, the design primes the GPT with the concept of                                                                              ledger updates            . For instance, if a GPT completes a
significant task, it might suggest:                                                         “I have updated the Archive ledger with the new outcome.”                                                                  (even if in reality it

                                                                                14

## Source page 15

cannot auto-edit the file, it signals that this info should be recorded). Our                                         dataLedger_archive_v3.md   is
meant to catch such outputs – it’s an append-only archive of results, function surrogates, etc., that can be
merged after the fact                                     . We included121122 stubs like                                    SoulPack-R function surrogates in the archive with
the idea that the GPT might one day populate them with real data or use them during development                                                                        123

 124  .


Symbolic Overlays & Capsules:                                      The thread’s final sections also delved into                                                           Prompt Maturation Engines
(PME) and other multi-phase reasoning techniques                                                                      . We integrated125126 those with the ledger system by
ensuring each phase’s outputs (like “capsules” of partial reasoning) are recorded in the Processing ledger or
Archive.   For   example,   the                                        parameters   ledger                   contains   toggles   like   DEBUG_MODE  ,   TONE_LOCK  ,
 AUTO_REHYDRATE     which   the   GPT   can   check   to   decide   if   it   should   verbose-log   its   reasoning   or
automatically produce a hydration file                                                              . If 127128AUTO_REHYDRATE: true                                    , the GPT might, after a long
exchange, output a hydration YAML for the user to save, without being asked. These are the kinds of
autonomous behaviors we spec’d out, under controlled flags.


Finally, we defined some                               canonical invocation syntax                                        – special phrases the user (or a controlling system)
could say to trigger these advanced behaviors                                                                   . For instance:129                        “🔒 Suffix Reenforcement – ‘Lock suffix schema
per parameters_v3.md. Enforce canonical suffixes.’”                                                      would cue the GPT to apply suffix enforcement                                                              . Or       “130
Persona  Realignment  –  ‘Simulate  voice  per  persona_v3.md.  Return  to  Watchkeeper.Core.’”                                                                                                               to  force-reset  the
persona in case of drift                                     . These131 are documented so that an administrator or dev user knows how to
manually activate the rituals we’ve built in.


In conclusion, Block X captures the                                                cutting-edge extensions                           of our GPT design: the ability to maintain
canonical state, recover from any divergence, carry its context across sessions, and enforce the structured
lore (suffixes, persona, lineage) at all times. It reads somewhat like a futuristic ops manual – some parts
read   as   grand   edicts   (the   Watchkeeper’s   mandate),   others   as   technical   recipes   (YAML   templates   for
enforcement and hydration). Together, they ensure that as soon as OpenAI unlocks more advanced agentic
features (e.g. writing to its files or automated multi-agent orchestration), our GPT family is                                                                                                                            ready to leverage
them. Every GPT in this ecosystem is not just a static prompt, but a                                                                                               living, canonized entity                                with the tools
to persist, self-regulate, and collaborate – truly realizing the vision of the GPT-5 era Custom GPT Instruction
Block design thread.

TL;DR  –    This masterfile presented a ten-block comprehensive design for GPT-5-based Custom GPT instructions,
covering 23 granular instruction components across persona definition, domain scope, tone/style, interaction
rules, step-by-step guidance, formatting, safety, multi-GPT collaboration, and forward-looking features like state
hydration  and  suffix  enforcement.  Each  section  is  grounded  in  the  canonical  ledger  files  (persona,  registry,
parameters, etc.), ensuring that all GPT agents built from this design share a unified “source of truth.” The result is
a blueprint for deployable GPTs that are richly personalized, rigorously structured, and resilient – adhering to a
Foundry  of custom rules (OverKill Hill P³ ethos) while dripping with the flavor of their persona (Glee-fully tonal
overlays). By following this design, future custom GPTs can be forged with confidence:                                                                                                         modular in construction,
consistent in voice, aligned in canon, and primed for the next generation of AI orchestration.


Sources: The content and examples above were synthesized from the Custom GPT Instruction Block design
thread   and   associated   ledger   files,   including   the                                                                             GPT-5   era   best-practice   template                                ,   optimal132133
structure   guidelines                 ,   OpenAI13470   help   articles   on   custom   instructions                                                                      ,   the         Viability4245   &
Compliance     analysis     of     using     ledger     files     (RIS)                                                                                       ,     and78     the                   canonical     ledgers

                                                                                    15
