# Usability criteria (US) — 14 criteria

Dimension scope: clarity of actions, feedback/system status, error prevention and
recovery, recognition over recall, cognitive load, affordances, user control.
Not here: contrast/screen-reader concerns (accessibility.md), aesthetics
(visual-design.md), internal/platform consistency (consistency.md), cross-screen
navigation logic (user-flow.md).

Verdicts: pass = 1, partial = 0.5, fail = 0, N/A excluded from the denominator.
Platform-dependent thresholds resolve via `platforms.md`. "Needs" tells you what
honestly supports the check — degrade to N/A rather than guess.

---

### US-01 Self-evident purpose and actions
- **Standard:** The screen's purpose and primary actions are understandable at a glance, without deciphering names or hunting for a starting point.
- **Source:** Steve Krug, *Don't Make Me Think* (2nd ed.), 2006, Ch. 1.
- **Check:** Cold-read the screen for ~5 seconds; name (a) what it's for, (b) the most likely next action. Sweep for cute/marketing/internal names, near-duplicate links, no obvious start.
- **Pass:** both nameable instantly; nothing required guessing. **Partial:** purpose clear but one significant control needs decoding. **Fail:** purpose or primary action requires inference, or 2+ controls have obscure names.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### US-02 Clickability signifiers
- **Standard:** Every interactive element carries a visual signifier of interactivity; no static element mimics one.
- **Source:** Kate Moran, "Flat UI Elements Attract Less Attention and Cause Uncertainty", NN/g, 2015.
- **Check:** Inventory clickable/tappable elements; for each, ask what marks it interactive without hover. Count unsignified interactive elements and button-styled static ones. DOM roles resolve ambiguity.
- **Pass:** all signified, no false signifiers. **Partial:** 1–2 secondary actions rely on position alone, or one static element looks clickable. **Fail:** primary action or 3+ elements indistinguishable from static content.
- **Applies:** both · **Platforms:** all (weigh heavier on touch — no hover discovery) · **Needs:** screenshot-only (DOM/Figma preferred)

### US-03 Visible system status
- **Standard:** Current state is shown without user action: location, selections, applied filters, step, item status.
- **Source:** Nielsen heuristic #1; Aurora Harley, "Visibility of System Status", NN/g, 2018.
- **Check:** List state variables the screen implies (where am I / what's selected / what's filtered / what step); verify each has a visible indicator.
- **Pass:** every implied state shown. **Partial:** one state variable undisplayed. **Fail:** location or effect of last action absent everywhere.
- **Applies:** both (multi: post-action screens must acknowledge the action) · **Platforms:** all · **Needs:** screenshot-only

### US-04 Users' language
- **Standard:** Labels and messages use the target user's words — no unexplained acronyms, internal feature names, or developer terms; information in task order.
- **Source:** Nielsen heuristic #2; Anna Kaley, "Match Between the System and the Real World", NN/g, 2018; Krug Ch. 4.
- **Check:** Read every string as a first-time member of the stated audience; flag jargon, unexpanded acronyms, brand names as sole handles, system-ordered sequences. When the audience/locale is **inferred rather than stated** (e.g., UI-vs-content language mixing where the user's context is unknown), record the mismatch as an **advisory** conditional on the inference — not a verdict hit (critique principle: intent before evaluation).
- **Pass:** no flags. **Partial:** 1–2 flags off the primary path. **Fail:** primary action or required field labeled in terms users must look up.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### US-05 Visible exits and reversal
- **Standard:** Every modal, wizard step, or destructive-adjacent context has a clearly labeled way out; Cancel (abandon) is distinct from Close (dismiss view).
- **Source:** Nielsen heuristic #3; Maria Rosala, "User Control and Freedom", NN/g, 2020.
- **Check:** For each enclosed context, identify the exit and its label; flag unlabeled X where data loss is possible; wizards need a one-step back, not restart.
- **Pass:** labeled exits everywhere, semantics unambiguous. **Partial:** exit present but ambiguous, or back overshoots. **Fail:** a context traps the user.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### US-06 Error prevention by design
- **Standard:** Inputs constrain to valid values, set sensible defaults, and forgive format variation rather than demanding it.
- **Source:** Nielsen heuristic #5; Page Laubheimer, "Preventing User Errors: Avoiding Unconscious Slips", NN/g, 2015.
- **Check:** Per input: constraining control where standard (date picker, dependent fields)? Defaults where a common value exists? Helper text demanding rigid formats ("no dashes") = unforgiving parsing signal.
- **Pass:** constraining controls / forgiving formats throughout, defaults set. **Partial:** some free-text where constrained is standard, or one rigid-format demand. **Fail:** error-prone free entry for structured data plus strict-format instructions.
- **Applies:** both · **Platforms:** all · **Needs:** DOM/Figma preferred

### US-07 Confirmations reserved for destruction
- **Standard:** Irreversible actions get one specific confirmation with verb-labeled buttons; routine actions get none (habituation).
- **Source:** Jakob Nielsen, "Confirmation Dialogs Can Prevent User Errors — If Not Overused", NN/g, 2018.
- **Check:** If a destructive control or a confirmation dialog is visible: does the dialog name the object/consequence, use verb labels ("Delete file"/"Keep file"), and guard only consequential actions?
- **Pass:** specific, verb-labeled, destruction-only. **Partial:** generic "Are you sure?" + Yes/No. **Fail:** destruction fires unconfirmed with no undo, or confirmations blanket routine actions.
- **Applies:** both — N/A when nothing destructive is visible · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma preferred to verify the dialog exists)

### US-08 Error message quality and recovery
- **Standard:** Errors sit adjacent to their source, use redundant cues, name the exact problem without blame, propose a fix, preserve input — and lead back into the flow rather than forcing a restart.
- **Source:** Nielsen heuristic #9; Neusesser & Sunwall, "Error-Message Guidelines", NN/g, 2023; Rosala, "User Control and Freedom", NN/g, 2020 (recovery).
- **Check:** On any captured error state, score six checks: (1) adjacent to cause, (2) color + non-color cue, (3) specific problem named, (4) constructive next step, no blame-words, (5) input preserved, (6) a path back into the task (not start-over).
- **Pass:** 6/6. **Partial:** 4–5. **Fail:** ≤3, or restart forced.
- **Applies:** both — N/A when no error state captured (report suggests supplying one) · **Platforms:** all · **Needs:** screenshot-only

### US-09 Recognition over recall
- **Standard:** Everything needed for the current decision is visible; nothing must be remembered from elsewhere.
- **Source:** Nielsen heuristic #6; Raluca Budiu, "Memory Recognition and Recall in User Interfaces", NN/g, 2024.
- **Check:** Per decision point: is the reference information co-present (item beside its edit form, earlier values echoed)? Flag prompts referring to off-screen information.
- **Pass:** no off-screen memory required. **Partial:** one decision leans on short-term memory. **Fail:** core task requires recalling values the interface knew and hid.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### US-10 Icon labels
- **Standard:** Icon-only controls are limited to recognizable symbols; anything a typical user couldn't name on sight gets a permanent text label — not hover-only.
- **Source:** Aurora Harley, "Icon Usability", NN/g, 2014 (sourced universal core); tier 2 is our 2026-07 operationalization (Clemens ruling) on Jakob's-Law grounds — ecosystem-learned symbols.
- **Check:** Classify each icon control into three tiers. **Tier 1 — sourced universal** (home, magnifier/search, print): no label needed. **Tier 2 — established ecosystem conventions** (hamburger menu, kebab/meatball overflow, gear, cart, back chevron/arrow, ⊕ add, camera-in-search-field, share sheet): unlabeled is acceptable; record an **advisory** ("keep an eye on"), not a verdict hit. **Tier 3 — everything else**: needs an adjacent, always-visible label.
- **Pass:** all tier-3 icons labeled permanently (tier-2 advisories don't affect the verdict). **Partial:** 1–2 unlabeled tier-3 icons in secondary spots, or hover-only labels. **Fail:** primary nav/actions are unlabeled tier-3 icons.
- **Applies:** both · **Platforms:** all (stricter on touch) · **Needs:** screenshot-only

### US-11 Persistent field labels
- **Standard:** Every field has a label outside the field that survives entry; placeholders never carry the name or format alone.
- **Source:** Katie Sherwin, "Placeholders in Form Fields Are Harmful", NN/g, 2014/2018.
- **Check:** Per field: external label? Filled fields still identifiable? Format hints not placeholder-only?
- **Pass:** external persistent labels throughout. **Partial:** floating labels, or 1–2 placeholder-only hints. **Fail:** any placeholder-as-only-label.
- **Applies:** both · **Platforms:** all · **Needs:** DOM/Figma preferred (distinguishes placeholder from label on empty forms)

### US-12 Form economy and structure
- **Standard:** Forms ask only what's needed: single column, labels adjacent, related fields grouped, conventional order, optional marked (and few), width ≈ expected input, requirements up front, no Reset.
- **Source:** Kathryn Whitenton, "Website Forms Usability: Top 10 Recommendations", NN/g, 2016.
- **Check:** Score the 9-point checklist above against the visible form (error display is US-08's job).
- **Pass:** ≥8/9 incl. single-column and no-Reset. **Partial:** 6–7, or multi-column on an otherwise clean form. **Fail:** ≤5, a Reset button, or evidently unnecessary fields.
- **Applies:** both · **Platforms:** all (label position: above on mobile, beside acceptable on desktop) · **Needs:** screenshot-only

### US-13 Choice clarity and load
- **Standard:** Options are mutually exclusive and exhaustive for the user's case; long lists get defaults, recommendations, or steps. (No numeric option-count threshold exists in the sources; none is applied.)
- **Source:** Laws of UX, "Hick's Law" (Hick & Hyman 1952); Krug Ch. 4.
- **Check:** Per decision point: can the target user always tell which option holds their case (no "Home vs Office" overlaps)? Long lists mitigated? Labels differentiated by the distinguishing attribute?
- **Pass:** all choices non-overlapping and mitigated. **Partial:** one overlapping choice or unmitigated long list. **Fail:** a gating choice on the primary path users can't confidently make.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### US-14 Signal over noise (content and decoration)
- **Standard:** Every element carries task value: no happy-talk, no instruction blocks standing in for self-evident design, no decoration or promo competing with primary content.
- **Source:** Nielsen heuristic #8; Therese Fessenden, "Aesthetic and Minimalist Design", NN/g, 2021; Kate Moran, "The Characteristics of Minimalism in Web Design", NN/g, 2015; Krug Ch. 5.
- **Check:** Classify each element/text block signal vs noise (decoration, redundant messaging, promos, welcome copy, instruction paragraphs). Cross-check against VD-01's blur test whether any noise element wins attention. Also flag over-minimalism that removed task-critical content.
- **Pass:** ≤1 noise element, none competing with primary content. **Partial:** 2–3 noise elements, or one visibly competing. **Fail:** 4+ noise elements, a decorative/promotional element dominating, or missing task-critical content from over-removal.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

---

## Severity guidance (annotation only — never in score math)

Rate each failed/partial finding 0–4 (Nielsen 1994) by reasoning through frequency
(how many users, how often), impact (recoverable?), persistence (once or every
time). In this dimension: unsignified primary actions and trapped contexts trend
3–4; jargon off the main path and one noisy promo trend 1–2. Always word severity
as an estimate — single-evaluator ratings are unreliable by the method's own source.

---

Last reviewed: 2026-07

Sources: see `research/reference-sources.md` (kept out of the skill's load path).
