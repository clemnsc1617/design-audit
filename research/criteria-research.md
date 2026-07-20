# Criteria research digest — M2a

Status: **draft for Clemens's review** (M2a gate). Nothing here enters `references/`
until he cuts/keeps criteria and approves. Weighting research is separate
(`research/weighting-memo.md`).

## How this was produced

Seven parallel research passes (2026-07-18), one per dimension plus platforms and
critique practice. Method rules applied to every pass:

- Every criterion's standard/threshold was verified against a **primary source the
  researcher actually fetched** (W3C normative spec + Understanding pages, Apple HIG
  via rendered browser or Apple's JSON endpoints, Material 3 via rendered browser,
  NN/g articles, Butterick/Bringhurst typography pages, Krug full text). Anything
  that couldn't be verified is marked **UNVERIFIED** in place rather than guessed.
- Where a Partial/Fail band edge is our operationalization (not a sourced number),
  the provenance note says so.
- Each pass ends with "Sources fetched" and "Rejected/uncertain" so the review can
  see what was considered and dropped, not just what survived.

## Inventory

| Section | Prefix | Draft criteria | Notes |
|---|---|---|---|
| Usability | US | 15 | Nielsen heuristics, Krug (full text), Laws of UX, NN/g |
| Visual design | VD | 13 | Gestalt (NN/g), NN/g hierarchy/grids, Butterick, Bringhurst |
| Accessibility | AC | 14 | WCAG 2.2 AA, with 3-way assessability classification |
| Consistency | CO | 12 | NN/g #4, Jakob's Law, HIG, Material 3 tokens |
| User flow | UF | 12 | Split single/multi; + 5 flow-evaluation frameworks |
| Platforms | — | threshold table + classification signals + divergence brief |
| Critique practice | — | 10 wording principles + finding template (not scored criteria) |

66 draft criteria total — deliberately over target (~58) so the M2a review cuts
rather than stretches.

## Overlap rulings — decided by Clemens, 2026-07-19 (binding for M2b)

1. **Target size:** CUT US-15's numeric check. AC-07 owns the measurement (WCAG 24px
   floor + platform 44pt/48dp flags from the platforms table); placement/adjacency
   note folds into AC-07's check.
2. **Signal-to-noise:** MERGE US-14 + VD-12 into one usability criterion covering
   content relevance and visual noise.
3. **Icon labels:** US-10 keeps the label check; VD-13 narrows to image
   informativeness + rendering quality.
4. **Cross-screen consistency:** KEEP both layers (AC-12/13 = WCAG floor,
   CO-02/03 = craft bar) with cross-references so one flaw isn't double-penalized.
5. **AC-06 text spacing:** KEEP, reframed as a measured spacing assessment
   (values measurable from a single screen, exact with DOM/Figma) plus
   breakage-risk flags — verdict language anchored to SC 1.4.12's values but not
   claiming full conformance (the SC's own test requires applying user overrides).
   **AC-09 focus visible:** KEEP as conditional (like AC-11): scoreable only when a
   captured screen/recording shows a focused state; otherwise N/A "needs keyboard
   test" + CSS risk flags.
6. **Error trio:** UF-04's recovery-path check folds into US-08; AC-11 stays
   (text-not-color is a distinct normative requirement). All share one N/A trigger
   (no error state captured).
7. **VD/CO borders (spacing, type, alignment):** KEEP all six; CO-06/CO-07 are
   auto-N/A without DOM/Figma data (no measured values → no token-discipline score).
8. **Rare conditionals (US-07, UF-05, UF-06):** KEEP; N/A costs nothing in the math.

Net effect: 66 → 63 criteria entering M2b (US-15 cut; US-14+VD-12 merged; UF-04
folded into US-08).

## Original overlap notes (superseded by the rulings above)

1. **Target size:** US-15 (NN/g 1cm physical) vs AC-07 (WCAG 2.5.8 24px) vs the
   platforms table (HIG 44pt / M3 48dp). Proposal: keep AC-07 as the scored WCAG
   criterion; US-15 narrows to *placement/spacing/relative prominence*; numeric
   thresholds live only in the platforms table.
2. **Signal-to-noise:** US-14 (content relevance) vs VD-12 (visual noise). Same
   heuristic #8 root. Proposal: keep both but with the stated boundary, or merge.
3. **Icon labels:** US-10 vs the icon-label half of VD-13. Proposal: US-10 keeps
   labels; VD-13 narrows to imagery informativeness + rendering quality.
4. **Consistent navigation/identification:** AC-12/AC-13 (WCAG 3.2.3/3.2.4,
   normative floor, multi-screen) vs CO-02/CO-03 (stricter craft bar). Proposal:
   keep both layers — WCAG scored under accessibility, craft under consistency —
   with explicit cross-references.
5. **Spacing/alignment:** VD-06/VD-07 (within-screen grid & rhythm) vs CO-07/CO-09
   (scale/token adherence, collection uniformity). Boundary stated in each block.
6. **Type discipline:** VD-02 (per-screen emphasis economy) vs CO-06 (scale/token
   binding). Boundary stated in each block.
7. **Error messages:** US-08 (message quality) vs UF-04 (recovery path) vs AC-11
   (WCAG text requirement). Three genuinely different lenses; all conditional on an
   error state being captured. Proposal: keep all three, share one N/A trigger.

---
# Dimension: Usability (US) — agent output, pending Clemens review

### US-01 Self-evident purpose and actions
- **Standard:** Each screen's purpose and its primary actions are understandable at a glance, without the viewer having to reason about what things are, what they're called, or where to start.
- **Source:** Steve Krug, "Don't Make Me Think, 2nd ed.", 2006 (New Riders), Ch. 1 — fetched copy at http://enlillebid.dk/mmd/wp-content/uploads/2012/03/Dont_Make_Me_Think.pdf
- **Check:** Auditor does a cold read of the screenshot: within ~5 seconds, name (a) what the screen is for and (b) the single most likely next action. Then sweep for Krug's "question mark" triggers: cute/marketing/company-internal names for sections or actions, near-duplicate links whose difference is unclear, no obvious starting point.
- **Pass:** Purpose and primary action are both immediately nameable; no element required guessing at its meaning. / **Partial:** Purpose is clear but at least one significant control needs a "little thought" (self-explanatory, not self-evident) — e.g., a cleverly named section a first-time user must decode. / **Fail:** Auditor cannot state the screen's purpose or primary action without inference, or two-plus controls have obscure/ambiguous names.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Ch. 1 of the fetched PDF states the first law verbatim ("Don't make me think!"), defines self-evident vs self-explanatory, and lists the name-related culprits ("cute or clever names, marketing-induced names, company-specific names, unfamiliar technical names"). High confidence — read directly from book text.

### US-02 Clickability signifiers on interactive elements
- **Standard:** Every interactive element carries at least one visual signifier of interactivity (button styling/border/shadow, link treatment, or unmistakable actionable placement + wording); no static element mimics those signifiers.
- **Source:** Kate Moran / NN/g, "Flat UI Elements Attract Less Attention and Cause Uncertainty" (flat-design article), 2015, https://www.nngroup.com/articles/flat-design/
- **Check:** Inventory all elements a user would need to click/tap. For each, ask: absent hover (impossible in a screenshot), what marks it as interactive? Count interactive elements with zero signifiers, and decorative elements styled like buttons/links. DOM data (role, `<a>`/`<button>`, cursor styles) resolves ambiguous cases.
- **Pass:** All interactive elements carry at least one clear signifier; no false signifiers on static content. / **Partial:** 1–2 secondary actions rely purely on position/convention with no visual cue, or one static element looks clickable. / **Fail:** Primary action or 3+ elements are visually indistinguishable from static text/graphics.
- **Applies:** both
- **Platforms:** all (weight higher on touch platforms, where hover discovery is impossible — noted in the NN/g article)
- **Needs:** screenshot-only (DOM/Figma preferred for resolving what is actually interactive)
- **Provenance note:** The fetched article names "the lack of signifiers on clickable elements" among flat design's biggest usability issues and recommends retaining traditional cues or subtle depth ("Flat 2.0"). High confidence. Cross-anchored by Krug Ch. 1 (fetched PDF): users should never spend "a millisecond of thought" on whether things are clickable.

### US-03 Current system status is visible
- **Standard:** The interface shows its current state without user action: active nav item, selected options, applied filters, step-in-progress, item/stock status, and results-of-last-action indicators are all explicit.
- **Source:** Aurora Harley / NN/g, "Visibility of System Status (Usability Heuristic #1)", 2018, https://www.nngroup.com/articles/visibility-system-status/ (heuristic text verified at Jakob Nielsen / NN/g, "10 Usability Heuristics for User Interface Design", 1994/2024, https://www.nngroup.com/articles/ten-usability-heuristics/)
- **Check:** List the state variables implied by the screen (where am I, what's selected, what's filtered, what step, what's loading/empty and why). For each, verify a visible indicator exists (highlighted nav, checkmarks, progress step markers, count badges, status text on unavailable items).
- **Pass:** Every implied state variable has an explicit visible indicator. / **Partial:** One state variable is undisplayed (e.g., filters applied but not summarized) while location/selection are shown. / **Fail:** User's location in the product, or the effect of their last choice, is not represented anywhere on screen.
- **Applies:** both (in multi-screen flows, additionally check that post-action screens acknowledge the action)
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Heuristic wording ("keep users informed about what is going on, through appropriate feedback") verified on the fetched heuristics page; the Harley article supplies the concrete static examples (selection checkmarks, stock/status notices). Time-based feedback (spinners within x ms) is NOT scoreable statically and is excluded. High confidence.

### US-04 Users' language, not system jargon
- **Standard:** All labels, headings, and messages use words familiar to the target user; no internal product names, unexplained acronyms, or technical terms where a plain word exists, and information appears in an order matching user expectations.
- **Source:** Anna Kaley / NN/g, "Match Between the System and the Real World (Usability Heuristic #2)", 2018, https://www.nngroup.com/articles/match-system-real-world/
- **Check:** Read every visible string as a first-time member of the stated audience. Flag: acronyms/initialisms not expanded, internal feature brand names used as the only handle for a function (Krug's "NAV for Windows" problem), developer-facing terms (e.g., "invalid input", entity names), and sequences presented in system order rather than task order.
- **Pass:** No flagged strings. / **Partial:** 1–2 flagged strings, none on the primary task path. / **Fail:** The primary action or a required field is labeled in terms the target user would need to look up.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched article gives the principle sentence, the jargon example (Abacus legal software) and the natural-order example (Global Entry). Krug Ch. 4 (fetched PDF, Symantec "NAV" example) independently verifies the internal-name failure mode. High confidence.

### US-05 Visible exits and reversal
- **Standard:** Any modal, multi-step process, or destructive-adjacent context offers a clearly labeled way out — back, cancel, close, or undo — reachable without completing the task.
- **Source:** Maria Rosala / NN/g, "User Control and Freedom (Usability Heuristic #3)", 2020, https://www.nngroup.com/articles/user-control-and-freedom/
- **Check:** For each overlay/dialog/wizard step/editor visible: identify the exit control and its label. Verify Cancel (abandon task) is distinct from Close (leave view) where both concepts exist; flag bare unlabeled X icons in ambiguous mobile contexts; in wizards, verify a back affordance to the previous step (not restart).
- **Pass:** Every enclosed context has a labeled, visible exit; cancel/close semantics unambiguous. / **Partial:** Exit exists but is ambiguous (unlabeled X where data loss is possible) or back returns further than one step. / **Fail:** A modal/step traps the user — no visible exit short of completing or abandoning via browser chrome.
- **Applies:** both (multi-screen flows additionally check step-back behavior)
- **Platforms:** all; mobile: NN/g specifically warns against ambiguous unlabeled X icons
- **Needs:** screenshot-only
- **Provenance note:** Fetched article enumerates exactly these four mechanisms (back, cancel, close, undo), the cancel-vs-close distinction, and the one-step-back rule. High confidence.

### US-06 Error prevention: constraints, defaults, forgiving input
- **Standard:** Inputs are designed so slips can't happen: impossible values are unselectable, sensible defaults are pre-set, suggestions/autocomplete assist entry, and formats are forgiving rather than strict.
- **Source:** Page Laubheimer / NN/g, "Preventing User Errors: Avoiding Unconscious Slips", 2015, https://www.nngroup.com/articles/slips/ (heuristic #5 text verified at the ten-heuristics page above)
- **Check:** For each input on screen: does the control type constrain to valid values (date picker vs free text; dependent fields like return-after-departure)? Are defaults present where a common value exists? Does visible helper text demand a rigid format (e.g., "no dashes") — a signal of unforgiving parsing? DOM/Figma reveals input types and validation attributes a screenshot can't.
- **Pass:** All inputs use constraining controls or forgiving formats; common-value defaults set. / **Partial:** Mixed — some free-text fields where constrained controls are standard, or one rigid-format demand. / **Fail:** Error-prone free entry for structured data (dates, phone) plus visible strict-format instructions shifting error-avoidance onto the user.
- **Applies:** both
- **Platforms:** all
- **Needs:** DOM/Figma preferred
- **Provenance note:** All four strategies (constraints, suggestions, good defaults, forgiving formatting) with their examples (flight dates, Uber phone formatting) appear in the fetched article. High confidence for strategies; no numeric thresholds exist in the source.

### US-07 Confirmation reserved for — and specific about — destructive actions
- **Standard:** Irreversible/destructive actions get one specific confirmation stating what will happen, with action-labeled buttons (not Yes/No); routine actions get none (overuse breeds click-through habituation).
- **Source:** Jakob Nielsen / NN/g, "Confirmation Dialogs Can Prevent User Errors — If Not Overused", 2018, https://www.nngroup.com/articles/confirmation-dialog/
- **Check:** If a destructive control (delete, discard, cancel subscription) is visible: is a confirmation step evident or implied by the design (DOM/Figma flows show it)? If a confirmation dialog is the screen under audit: verify it names the specific object/consequence and uses verb-labeled buttons ("Delete file" / "Keep file"), and that it is not confirming a trivial action.
- **Pass:** Destructive actions confirmed once with specific wording and verb-labeled buttons; no confirmations on routine actions. / **Partial:** Confirmation present but generic ("Are you sure?" + Yes/No). / **Fail:** Destructive action fires with no confirmation and no undo, or confirmations blanket routine actions.
- **Applies:** both (single-screen scoreable only when a destructive control or dialog is visible; otherwise N/A)
- **Platforms:** all
- **Needs:** screenshot-only for dialog quality; DOM/Figma preferred to verify the confirmation exists
- **Provenance note:** Fetched article verified: reserve for consequential/non-undoable operations, restate the request, action-specific button labels, habituation warning, undo as backup. High confidence.

### US-08 Error message quality
- **Standard:** Error messages sit adjacent to their source, are visually prominent with redundant cues, state the exact problem in plain non-blaming language, and offer a concrete fix while preserving the user's input.
- **Source:** Tim Neusesser & Evan Sunwall / NN/g, "Error-Message Guidelines", 2023, https://www.nngroup.com/articles/error-message-guidelines/ (heuristic #9 text verified at the ten-heuristics page)
- **Check:** On any screen showing an error state, score the message against five checks: (1) placed next to the offending field/element, (2) high-contrast styling plus a non-color cue (icon/text), (3) names the specific problem — not "an error occurred", (4) proposes an action, no blame-words like "invalid"/"illegal", (5) erroneous input still visible, not cleared.
- **Pass:** 5/5 checks. / **Partial:** 3–4 checks (typically specific but poorly placed, or well-placed but no remedy). / **Fail:** ≤2 checks — generic, blaming, orphaned from its source, or input destroyed.
- **Applies:** both (N/A when no error state is shown; auditor should request an error-state screen)
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** All five checks map one-to-one to the fetched article's visibility/communication/efficiency guidelines (proximity, redundant cues, specificity, constructive tone, input preservation). High confidence.

### US-09 Recognition over recall
- **Standard:** Everything the user needs for the current decision is visible on screen; the interface never requires remembering values, options, or commands from elsewhere.
- **Source:** Raluca Budiu / NN/g, "Memory Recognition and Recall in User Interfaces", 2024, https://www.nngroup.com/articles/recognition-and-recall/ (heuristic #6 text verified at the ten-heuristics page)
- **Check:** Identify each decision point on the screen. For each, is the needed reference information co-present (e.g., the item being edited shown beside the form; comparison data on the comparison screen; previously entered values echoed where reconfirmation is asked)? Flag command-style interactions with no visible menu of options, and any prompt referring to information shown only on a prior screen.
- **Pass:** No decision requires off-screen memory; pickable options are visible or one tap away with visible history/suggestions. / **Partial:** One decision leans on short-term memory (e.g., "re-enter the code shown earlier" without redisplay). / **Fail:** Core task requires recalling identifiers, syntax, or values the interface knew and hid.
- **Applies:** both (this is the single-screen memory criterion; cross-screen navigation memory belongs to user-flow)
- **Platforms:** all
- **Needs:** screenshot-only (multi-screen input strengthens the check)
- **Provenance note:** Fetched article verified the definitions, the more-cues mechanism, and recommendations (visible functions, history, labeled icons, contextual tips). High confidence.

### US-10 Icons carry always-visible text labels
- **Standard:** Icon-only controls are limited to the handful of near-universal symbols (home, search magnifier, print); all other icons have a text label visible at all times, not on hover.
- **Source:** Aurora Harley / NN/g, "Icon Usability", 2014, https://www.nngroup.com/articles/icon-usability/
- **Check:** Inventory every icon control. Classify each as universal (home/search/print per the source) or non-universal. For non-universal icons, verify an adjacent permanent text label — tooltips and hover reveals don't count (fail on touch, add interaction cost).
- **Pass:** All non-universal icons labeled; labels permanent. / **Partial:** 1–2 unlabeled non-universal icons in secondary positions, or labels only on hover. / **Fail:** Primary navigation or primary actions are unlabeled non-universal icons.
- **Applies:** both
- **Platforms:** all; stricter on touch (hover labels are unavailable, per the source)
- **Needs:** screenshot-only
- **Provenance note:** Fetched article verified: labels "visible at all times, without any interaction", the short universal-icon list, and the hover/touch problem. High confidence. Also reinforced by the recognition article (US-09 source), which repeats the labeled-icons recommendation.

### US-11 Persistent field labels — placeholders are not labels
- **Standard:** Every form field has a label placed outside the field that remains visible after entry; placeholder text is not the sole carrier of the field's name or format rules.
- **Source:** Katie Sherwin / NN/g, "Placeholders in Form Fields Are Harmful", 2014 (updated 2018), https://www.nngroup.com/articles/form-design-placeholders/
- **Check:** For each field: (1) label outside the field boundary, (2) filled-state check — if any field on the screenshot is filled, is its meaning still identifiable? (3) format instructions not placed only inside the field. Figma/DOM lets you distinguish placeholder attributes from real labels when the screenshot shows empty fields.
- **Pass:** All fields have external persistent labels; placeholders, if any, carry only redundant hints. / **Partial:** Floating labels, or 1–2 fields with placeholder-only hints for format. / **Fail:** Any field where the placeholder is the only label, or instructions vanish on focus/entry.
- **Applies:** both
- **Platforms:** all
- **Needs:** DOM/Figma preferred
- **Provenance note:** Fetched article verified the seven problems (memory strain, no verification pre-submit, mistaken-for-prefilled, etc.) and the explicit recommendation of clear visible labels outside empty fields. High confidence. Contrast-related placeholder harms are ceded to the accessibility dimension.

### US-12 Form economy and structure
- **Standard:** Forms ask only for needed data, run in a single column with labels adjacent to their fields, group related fields, order fields conventionally, mark the optional/required distinction, size fields to expected input, state format requirements up front, and omit Reset/Clear buttons.
- **Source:** Kathryn Whitenton / NN/g, "Website Forms Usability: Top 10 Recommendations", 2016, https://www.nngroup.com/articles/web-form-design/
- **Check:** Score the visible form against a checklist drawn from the source: single column; label above (mobile) or beside (desktop) each field; related fields visually sectioned; conventional field order; optional fields explicitly marked (and few — the source caps at one or two); field width ≈ expected input length; visible format guidance for constrained inputs; no Reset/Clear button; no fields with no plausible necessity for the stated task.
- **Pass:** ≥8 of 9 checks, including single-column and no-reset. / **Partial:** 6–7 checks, or multi-column layout on an otherwise clean form. / **Fail:** ≤5 checks, or presence of a Reset button, or evidently unnecessary fields dominating the form.
- **Applies:** both
- **Platforms:** all; label position differs by platform (above on mobile, beside acceptable on desktop) per the source
- **Needs:** screenshot-only
- **Provenance note:** All nine checks come from the fetched top-10 list (the tenth, error display, is scored under US-08). The "one or two optional fields max" figure is in the fetched summary. High confidence. Field-necessity judgment is auditor inference guided by the source's minimize-fields rule.

### US-13 Choice clarity and load
- **Standard:** Each choice presented is mindless — options are mutually exclusive, exhaustive for the user's situation, and few enough (or well-defaulted/recommended enough) that decision time stays low.
- **Source:** Laws of UX (Jon Yablonski), "Hick's Law", https://lawsofux.com/hicks-law/ (citing Hick & Hyman, 1952); Steve Krug, "Don't Make Me Think, 2nd ed.", 2006, Ch. 4 (fetched PDF above)
- **Check:** For each decision point (menu, plan picker, category split, segmented control): (1) can a target user always tell which option contains their case — no Krug "Home vs Office" overlaps or gaps? (2) When options are numerous, is a recommended/default option highlighted or the task split into steps? (3) Are option labels differentiated by their distinguishing attribute, not marketing names?
- **Pass:** Every visible choice has non-overlapping, plainly labeled options; long lists mitigated by defaults/recommendation/steps. / **Partial:** One choice with overlapping categories or an unmitigated long undifferentiated list. / **Fail:** A gating choice on the primary path where a typical user cannot confidently pick (ambiguous categories or jargon-differentiated options).
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Hick's Law definition and takeaways verified on the fetched lawsofux page, which cites Hick & Hyman 1952; the page offers no numeric choice-count threshold — any such number would be UNVERIFIED, so none is used. Krug's mutually-exclusive-choice failure examples (Home vs Office, Stamped vs Metered) read directly from Ch. 4 of the fetched PDF. High confidence.

### US-14 Content economy (signal over noise)
- **Standard:** The screen contains no content that is irrelevant or rarely needed — no happy-talk intros, no instruction blocks substituting for self-explanatory design — so relevant information keeps its relative visibility.
- **Source:** Therese Fessenden / NN/g, "Aesthetic and Minimalist Design (Usability Heuristic #8)", 2021, https://www.nngroup.com/articles/aesthetic-minimalist-design/; Steve Krug, "Don't Make Me Think, 2nd ed.", 2006, Ch. 5 (fetched PDF above)
- **Check:** Classify each text block and element as signal (needed for the current task) or noise. Specifically hunt Krug's two named offenders: promotional "welcome/blah" copy that conveys no task information, and instruction paragraphs that exist because the UI isn't self-explanatory. Estimate whether prose could lose half its words without losing meaning (Krug's stated realistic target).
- **Pass:** All visible content is task-relevant; instructions, where present, are minimal. / **Partial:** One noise block (welcome copy, redundant explainer) not obscuring the task. / **Fail:** Instructional or promotional filler competes with or precedes the primary content/action, or a full paragraph of instructions gates a simple interaction.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Heuristic #8 wording verified on both fetched NN/g pages; "Communicate; don't decorate" and the signal/noise frame are in the Fessenden article. Happy-talk and instructions-must-die passages, and the remove-half-the-words target, read directly from Krug Ch. 5. High confidence. Pure aesthetics of the visual style are ceded to the visual-design dimension; this criterion judges content relevance only. NOTE (assembler): overlaps VD-12 — de-dup at review (US-14 = content relevance; VD-12 = visual noise).

### US-15 Target size, spacing, and placement
- **Standard:** Touch targets render at ≥1cm × 1cm (0.4in) physically, with clear space from neighboring targets; frequent/primary targets are large and positioned for easy acquisition rather than small and remote.
- **Source:** Aurora Harley / NN/g, "Touch Targets on Touchscreens", 2019, https://www.nngroup.com/articles/touch-target-size/ (basis: Parhi, Karlson & Bederson, 2006); Laws of UX (Jon Yablonski), "Fitts's Law", https://lawsofux.com/fittss-law/ (citing Fitts, 1954)
- **Check:** Using known device/frame dimensions (Figma frame size or DOM viewport → physical px conversion), measure the smallest interactive targets and the gaps between adjacent ones. Compare against 1cm × 1cm on touch. On any platform, flag primary actions that are markedly smaller than secondary ones or crowded against destructive neighbors (delete beside save).
- **Pass:** All touch targets ≥1cm square with visible separation; primary actions among the largest/best-placed targets. / **Partial:** 1–2 secondary targets under threshold, or adequate sizes but destructive and constructive actions adjacent with no gap. / **Fail:** Primary or destructive-adjacent targets under threshold, or dense clusters of undersized targets on the task path.
- **Applies:** both
- **Platforms:** touch platforms (mobile/tablet): 1cm threshold applies; desktop pointer: no verified numeric threshold — score only relative size/spacing/placement (numeric desktop threshold: UNVERIFIED)
- **Needs:** DOM/Figma preferred (physical-size math needs real dimensions; screenshot-only permits only relative judgments)
- **Provenance note:** The 1cm × 1cm figure and its Parhi et al. 2006 basis verified on the fetched NN/g article; the fetched lawsofux Fitts page supplies the size/distance/spacing principle and the Fitts 1954 citation but explicitly no numbers. NOTE (assembler): overlaps AC-07 (WCAG 2.5.8) and the platforms threshold table — de-dup at weighting time.

## Sources fetched
- https://www.nngroup.com/articles/ten-usability-heuristics/ — canonical text of all 10 heuristics (Nielsen 1994, updated 2024); anchor for US-03/04/05/06/08/09/14.
- https://www.nngroup.com/articles/visibility-system-status/ — Harley 2018; static status indicators examples for US-03.
- https://www.nngroup.com/articles/recognition-and-recall/ — Budiu 2024; definitions and UI recommendations for US-09.
- https://www.nngroup.com/articles/error-message-guidelines/ — Neusesser & Sunwall 2023; the five-point checklist in US-08.
- https://www.nngroup.com/articles/user-control-and-freedom/ — Rosala 2020; back/cancel/close/undo mechanisms for US-05.
- https://www.nngroup.com/articles/slips/ — Laubheimer 2015; four slip-prevention strategies for US-06.
- https://www.nngroup.com/articles/icon-usability/ — Harley 2014; always-visible labels + universal-icon list for US-10.
- https://www.nngroup.com/articles/form-design-placeholders/ — Sherwin 2014/2018; placeholder harms + external-label recommendation for US-11.
- https://lawsofux.com/fittss-law/ — definition, takeaways, Fitts 1954 citation; confirmed NO numeric threshold on the page (US-15).
- https://lawsofux.com/hicks-law/ — definition, takeaways, Hick & Hyman 1952 citation; confirmed NO numeric choice-count threshold (US-13).
- https://lawsofux.com/millers-law/ — Miller 1956 citation and the explicit warning against using 7 as a design limit (drove a rejection).
- https://www.nngroup.com/articles/aesthetic-minimalist-design/ — Fessenden 2021; signal/noise framing for US-14.
- https://sensible.com/dont-make-me-think/ — edition metadata only (3rd ed. 2014); no principle text, so not used as the criterion source.
- https://www.nngroup.com/articles/flat-design/ — Moran 2015; clickability-signifier findings for US-02.
- https://www.nngroup.com/articles/match-system-real-world/ — Kaley 2018; jargon/conventions/order for US-04.
- https://www.nngroup.com/articles/web-form-design/ — Whitenton 2016; the 10 form recommendations behind US-12.
- https://www.nngroup.com/articles/confirmation-dialog/ — Nielsen 2018; destructive-only + specific-wording + habituation for US-07.
- https://www.nngroup.com/articles/help-and-documentation/ — Kendrick 2020; proactive/reactive help taxonomy (used only for a rejection rationale).
- https://www.nngroup.com/articles/touch-target-size/ — Harley 2019; the 1cm × 1cm threshold and Parhi et al. 2006 basis.
- http://enlillebid.dk/mmd/wp-content/uploads/2012/03/Dont_Make_Me_Think.pdf — full text of Krug 2nd ed. (2006); Ch. 1 (first law, self-evident/self-explanatory, clickability), Ch. 4 (mindless choices, Symantec/Home-vs-Office examples), Ch. 5 (omit needless words, happy talk, instructions) read directly.

## Rejected/uncertain
- **Miller's Law item-count limit** — the fetched lawsofux page itself warns against using 7±2 to justify design limits; chunking partially covered by US-12 and visual-design grouping. Dropped.
- **Doherty Threshold (400ms) / response-time feedback timing** — inherently dynamic; not observable statically. Dropped.
- **Jakob's Law** — external-convention conformity belongs to the consistency dimension per scope guard. Dropped.
- **Flexibility and efficiency of use (heuristic #7)** — shortcuts/accelerators mostly invisible in static captures; scoring their absence would be unfair. Dropped.
- **Help and documentation (heuristic #10)** — not reliably judgeable from a static screen without penalizing good minimal designs. Dropped; instructions-bloat policed by US-14.
- **Krug's trunk test / navigation orientation across pages** — verified but evaluates multi-screen navigation logic → user-flow dimension. Flagged for user-flow.
- **"3-click rule"** — Krug Ch. 4 explicitly argues click-count rules are the wrong metric vs click difficulty; rejected, superseded by US-13.
- **Numeric choice-count threshold for Hick's Law** — no such number in any fetched primary source; UNVERIFIED, so US-13 has none.
- **Desktop pointer target-size threshold** — no verified number in fetched sources (1cm figure is touch-specific); scoped out of US-15's numeric check.
- **Placeholder contrast / screen-reader harms** — verified in Sherwin article but ceded to accessibility dimension.
# Dimension: Visual design (VD) — agent output, pending Clemens review

### VD-01 Visual hierarchy and scan order
- **Standard:** The screen has a deliberate visual hierarchy: the most important element attracts the eye first, and emphasis (via scale, value/contrast, spacing, placement) descends in order of intended importance.
- **Source:** Kelley Gordon / Nielsen Norman Group, "Visual Hierarchy in UX: Definition", 2021, https://www.nngroup.com/articles/visual-hierarchy-ux-definition/
- **Check:** Apply the squint/blur test: blur the screenshot (or squint) and record the 2–3 elements that still dominate. Compare against the screen's evident purpose (primary message or primary action). Then, unblurred, trace the order in which the eye lands on elements and note whether it matches importance.
- **Pass:** Blurred view surfaces exactly the elements that matter most for the screen's purpose; a clear 1st–2nd–3rd emphasis order exists. / **Partial:** A hierarchy exists but a secondary or decorative element competes with or slightly outweighs the primary one, or the top two levels are indistinguishable. / **Fail:** Blurred view is near-uniform (no focal point) or the dominant element is irrelevant to the screen's purpose (e.g., a promo outweighs the primary action).
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Definition ("eye is guided... in the order of intended importance") and the squint test both appear in the fetched article, as do the contributing attributes (scale, value/saturation contrast, grouping, whitespace). High confidence.

### VD-02 Emphasis economy
- **Standard:** Emphasis is rationed: no more than about 3 distinct size levels, no more than about 3 contrast/emphasis treatments, and a restrained palette on the order of 2 primary plus 2 secondary colors.
- **Source:** Kelley Gordon / Nielsen Norman Group, "5 Principles of Visual Design in UX", 2020, https://www.nngroup.com/articles/principles-visual-design/ (supported by Gordon, "Visual Hierarchy in UX: Definition", 2021, https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)
- **Check:** Count distinct text/component size steps visible on the screen (headline, body, caption, etc.). Count distinct strong-emphasis treatments (bold, accent color, badge, oversized). Count hue families used for UI (excluding photography).
- **Pass:** ≤3 size levels, ≤3 emphasis treatments, palette reads as ~2 primary + ~2 secondary hues; emphasis is scarce enough that emphasized items stand out. / **Partial:** 4–5 size levels or 4–5 emphasis treatments, or one extra unmotivated accent hue; hierarchy still mostly legible. / **Fail:** >5 size levels, emphasis applied so widely that nothing stands out, or an uncontrolled palette (many unrelated accent hues).
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only (DOM/Figma preferred for exact size-step counting)
- **Provenance note:** "No more than 3 different sizes" appears under Scale in the 5 Principles article; "2 primary and 2 secondary colors" and "no more than 3 contrast variations" appear in the Visual Hierarchy article. These are NN/g rules of thumb, not empirical thresholds; verification of the numbers is high, their status as heuristics should be kept in the rubric.

### VD-03 Proximity grouping
- **Standard:** Space encodes relatedness: gaps within a functional group are visibly smaller than gaps between groups, so related items (e.g., a label and its field) read as units without relying on boxes.
- **Source:** Aurora Harley / Nielsen Norman Group, "Proximity Principle in Visual Design", 2020, https://www.nngroup.com/articles/gestalt-proximity/
- **Check:** Sample 3–5 label/control, heading/content, or icon/text pairs. For each, compare the gap to its partner vs. the gap to the nearest unrelated element (measure in px if DOM/Figma available; otherwise judge visually). Also check that no action button sits buried inside a cluster of unrelated controls, and that long forms/lists are chunked into sections rather than one undifferentiated run.
- **Pass:** Every sampled pair is closer to its partner than to any unrelated neighbor; groups are chunked (e.g., a long form broken into sections). / **Partial:** One ambiguous pairing (a label equidistant between two fields, or a heading floating between sections), rest correct. / **Fail:** Two or more false groupings, uniform spacing everywhere (no group structure), or a control placed nearer to an unrelated group than to its own.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only (DOM/Figma preferred for measuring gaps)
- **Provenance note:** The fetched article states items close together are perceived as one group, that whitespace should unite related and separate unrelated elements, that form fields chunked into sections feel less daunting, and warns against burying actions among unrelated controls. High confidence; the "within-gap < between-gap" comparison is our operationalization of its label/field spacing guidance.

### VD-04 Similarity coding
- **Standard:** Elements that share function share visual traits (color, shape, size, font treatment), and elements with different functions look different — in particular, the interactive/link color is reserved for interactive elements and the primary CTA is styled distinctly from secondary actions.
- **Source:** Aurora Harley / Nielsen Norman Group, "Similarity Principle in Visual Design", 2020, https://www.nngroup.com/articles/gestalt-similarity/
- **Check:** Inventory same-function element families visible on screen (nav links, cards, buttons, tags). Verify members of each family share styling. Then check for false similarity: non-interactive text in the link/accent color, ads or promos styled like content, or secondary buttons styled identically to the primary CTA.
- **Pass:** Same-function families are visually uniform; accent/link styling appears only on interactive elements; primary vs. secondary actions are distinguishable at a glance. / **Partial:** One false-similarity instance (e.g., a decorative heading in link color) or one family member that drifts in style. / **Fail:** Multiple false similarities, primary and secondary actions indistinguishable, or unrelated element types styled as a matching set.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** The fetched article names color, shape, size (plus font treatment/orientation) as similarity traits, recommends reserving link colors for clickable items and distinct colors for primary CTAs, and warns that same-styling of unlike content misleads. High confidence. Cross-screen uniformity of these styles belongs to the CONSISTENCY dimension; this criterion judges within-screen coding only.

### VD-05 Container restraint (common region)
- **Standard:** Borders and background containers are used where whitespace alone cannot communicate grouping, each container encloses genuinely related items, and containers are not stacked or nested to the point of clutter.
- **Source:** Aurora Harley / Nielsen Norman Group, "The Principle of Common Region: Containers Create Groupings", 2020, https://www.nngroup.com/articles/common-region/
- **Check:** Count bordered/filled containers on the screen. For each, confirm its contents belong together and that the container does real grouping work whitespace could not. Look for redundant nesting (box in a box with one child), and for full-width colored bands near the fold that could read as the end of the page ("false floor").
- **Pass:** Every container groups related content, no redundant nesting, chrome (nav/header/footer) distinguished from content, no false floor above the fold. / **Partial:** One redundant or unmotivated container, or heavy banding that fragments the page but grouping remains legible. / **Fail:** Boxes around nearly everything (grouping meaning lost), a container mixing unrelated content, or a full-width band that visually terminates the page above real content.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** The fetched article covers containers via border or background, the whitespace-first / use-sparingly advice, the clutter warning about too many borders and colored boxes, chrome-vs-content separation, and the false-floor scroll caution. High confidence.

### VD-06 Grid and alignment
- **Standard:** Content sits on a consistent column grid (a 12-column grid is the desktop norm, fewer columns at smaller sizes), block edges align to shared keylines, and content occupies columns rather than gutters.
- **Source:** Kelley Gordon / Nielsen Norman Group, "Using Grids in Interface Designs", 2022, https://www.nngroup.com/articles/using-grids-in-interface-designs/
- **Check:** Overlay vertical guides at the major left edges of content blocks (trivial in Figma/DOM; visual ruler on a screenshot otherwise). Count distinct left-edge x-positions in the main content area and flag stragglers that align to nothing. Confirm outer margins are consistent and no element sits in a gutter/margin zone.
- **Pass:** Content edges resolve to a small set of shared keylines consistent with a column grid; margins even; no stragglers. / **Partial:** 1–2 elements off-grid by a small amount, or one section using its own alignment logic while the rest is coherent. / **Fail:** Three or more unexplained alignment positions, ragged left edges across sections, or content bleeding into margins/gutters.
- **Applies:** both
- **Platforms:** all; the 12-column norm is stated for desktop/laptop widths, with column count decreasing on smaller devices (per the same source)
- **Needs:** screenshot-only (DOM/Figma preferred for pixel-exact edge verification)
- **Provenance note:** The fetched article defines grids as columns/gutters/margins, recommends a 12-column grid for desktop with fewer columns on smaller devices, says to place content in columns and never gutters, and ties grids to well-aligned, scannable interfaces. High confidence.

### VD-07 Spacing rhythm and whitespace
- **Standard:** Spacing follows a consistent rhythm (an 8-pixel base grid is the cited convention), with adequate micro whitespace (between lines, paragraphs, and neighboring elements) and macro whitespace (around major layout blocks) so no region reads as crowded.
- **Source:** Kelley Gordon / Nielsen Norman Group, "Using Grids in Interface Designs", 2022, https://www.nngroup.com/articles/using-grids-in-interface-designs/ (8px system); Mads Soegaard / Interaction Design Foundation, "The Power of White Space in Design", 2015 (upd. 2020), https://ixdf.org/literature/article/the-power-of-white-space (micro/macro distinction)
- **Check:** Sample 6–10 gaps (element padding, gaps between siblings, section margins). With DOM/Figma, test whether values fall on a small consistent scale (e.g., multiples of 8, with 4 for fine steps); from a screenshot, judge whether equivalent relationships get equal spacing. Separately scan for crowding: text touching container edges, tap/click targets abutting, or dense clusters with no macro whitespace around them.
- **Pass:** Sampled gaps fall on one consistent scale (or visually uniform per relationship type); every dense region has breathing room; nothing touches container edges. / **Partial:** Mostly rhythmic with 1–2 arbitrary gaps, or one locally crowded region on an otherwise breathing layout. / **Fail:** Gap values effectively random (equivalent relationships spaced differently), or widespread crowding with text/controls pressed against edges and each other.
- **Applies:** both
- **Platforms:** all
- **Needs:** DOM/Figma preferred (exact gap values); screenshot-only workable for crowding judgment
- **Provenance note:** The 8-pixel grid recommendation appears in the fetched NN/g grids article ("Consider an 8-pixel grid system for easier scaling"); the micro vs. macro whitespace taxonomy appears in the fetched IxDF article, which cites no quantified study — treat the comprehension benefit as qualitative. The finer 4px sub-step is UNVERIFIED against a fetched primary source. Whether spacing values reuse the same design tokens across screens belongs to CONSISTENCY; this criterion judges geometric rhythm and crowding on the screen at hand.

### VD-08 Body text line length
- **Standard:** Body-text measure is 45–90 characters per line (Butterick), with 45–75 satisfactory and ~66 ideal per Bringhurst; multi-column text runs best at 40–50 characters.
- **Source:** Matthew Butterick, "Butterick's Practical Typography — Line length", ongoing web edition, https://practicaltypography.com/line-length.html; Richard Rutter (citing Robert Bringhurst), "The Elements of Typographic Style Applied to the Web, §2.1.2 Choose a comfortable measure", 2005, http://webtypography.net/2.1.2
- **Check:** Locate the widest body-text paragraph. Count characters (including spaces) across 2–3 full lines and average them. Butterick's shortcut: roughly two to three alphabets should fit per line. Apply the 40–50 band to columns in multi-column text layouts.
- **Pass:** Average 45–90 characters per line (40–50 for multi-column text). / **Partial:** Modestly outside the band — roughly 35–45 or 90–105 characters. / **Fail:** Lines under ~35 characters (choppy) or over ~105 characters (eye-return strain) in primary body text.
- **Applies:** both
- **Platforms:** all; on narrow mobile viewports short measures are structurally expected, so score only paragraphs where the design controls the measure
- **Needs:** screenshot-only
- **Provenance note:** "45–90 characters or 2–3 alphabets" verified on the fetched Butterick page; "45 to 75... satisfactory", 66-character ideal, and 40–50 for multiple columns verified on the fetched Rutter page quoting Bringhurst. The Partial/Fail band edges (35/105) are our operationalization, not sourced numbers.

### VD-09 Line spacing (leading)
- **Standard:** Body-text line spacing is 120–145% of the type size (unitless line-height 1.2–1.45).
- **Source:** Matthew Butterick, "Butterick's Practical Typography — Line spacing", ongoing web edition, https://practicaltypography.com/line-spacing.html
- **Check:** With DOM/Figma, read line-height ÷ font-size for the main body style. From a screenshot, measure baseline-to-baseline distance and divide by the apparent point size (cap-height method) for a paragraph of 3+ lines.
- **Pass:** Body ratio in 1.2–1.45. / **Partial:** Ratio 1.0–1.2 (tight but readable) or 1.45–1.7 (loose but coherent). / **Fail:** Ratio below 1.0 (ascenders/descenders colliding) or ≥ ~1.8 (lines read as separate items) on body text.
- **Applies:** both
- **Platforms:** all
- **Needs:** DOM/Figma preferred; screenshot-only possible with careful measurement
- **Provenance note:** "120–145% of the point size" verified on the fetched page, including the note that the right value varies by font within that band. Partial/Fail edges outside the band are our operationalization. Butterick's page addresses body text; heading leading norms were not verified — UNVERIFIED, do not score headings against this band.

### VD-10 Body type size
- **Standard:** Web/desktop body text is set at 15–25 pixels (a comfort norm for screen reading distance, distinct from accessibility minimums).
- **Source:** Matthew Butterick, "Butterick's Practical Typography — Point size", ongoing web edition, https://practicaltypography.com/point-size.html
- **Check:** Read the computed font-size of the primary body style from DOM/Figma; from a screenshot, estimate from cap height only if the device pixel ratio / rendering scale is known.
- **Pass:** Body text 15–25 px. / **Partial:** 13–15 px or 25–30 px. / **Fail:** Body text under ~13 px or over ~30 px used for running text.
- **Applies:** both
- **Platforms:** web/desktop verified at 15–25 px. Mobile-native (iOS/Android) body-size norms: platform values live in the platforms threshold table (HIG 17pt default / Material 16sp Body Large) — apply those, not the 15–25px band, to native mobile.
- **Needs:** DOM/Figma preferred (screenshot-only estimation requires known scale factor)
- **Provenance note:** "The optimal size is 15–25 pixels" for the web verified on the fetched page (print: 10–12 pt). Partial/Fail edges are our operationalization. Scope guard: legal/accessibility text-size minimums stay in the ACCESSIBILITY dimension; this criterion scores reading comfort.

### VD-11 Typeface restraint
- **Standard:** The interface uses one or two typeface families; per Butterick, "Most documents can tolerate a second font. Few can tolerate a third." — and each family holds a consistent role.
- **Source:** Matthew Butterick, "Butterick's Practical Typography — Mixing fonts", ongoing web edition, https://practicaltypography.com/mixing-fonts.html
- **Check:** Count distinct typeface families visible (exclude logos, third-party embeds, and icon fonts). Verify each family maps to a stable role (e.g., display vs. body vs. mono) and that no single paragraph mixes families.
- **Pass:** 1–2 families with consistent roles. / **Partial:** 3 families, each with a clear distinct role. / **Fail:** 4+ families, or 3 without role separation, or families mixed within one paragraph/element.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only (DOM/Figma preferred to confirm families vs. weights)
- **Provenance note:** The tolerance ladder (second font fine, third rare, four+ almost never) and the one-font-per-paragraph / consistent-role guidance verified on the fetched page. High confidence.

### VD-12 Visual clutter and signal-to-noise
- **Standard:** Every visible element carries informational or task value; irrelevant, rarely needed, or purely decorative elements are minimized — the heuristic in short: "communicate; don't decorate" (Fessenden, NN/g).
- **Source:** Therese Fessenden / Nielsen Norman Group, "Aesthetic and Minimalist Design (Usability Heuristic #8)", 2021, https://www.nngroup.com/articles/aesthetic-minimalist-design/ (supported by Kate Moran / NN/g, "The Characteristics of Minimalism in Web Design", 2015, https://www.nngroup.com/articles/characteristics-minimalism/)
- **Check:** Inventory the screen's elements and classify each as signal (supports a user task: labels, content, actions, wayfinding) or noise (decoration, redundant messaging, competing promos/badges, jargon without payoff). Count noise elements and note whether any noise element competes with the primary content (cross-check with the VD-01 blur test).
- **Pass:** No more than 1 noise element, and none competes with primary content for attention. / **Partial:** 2–3 noise elements, or one that visibly competes with primary content. / **Fail:** Noise pervades (4+ elements) or a decorative/promotional element dominates the screen's hierarchy. Also fail if "decluttering" has gone so far that content needed for the core task is missing (over-minimalism, per Moran).
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** The irrelevant-information wording, signal/noise framing, and "communicate; don't decorate" all verified on the fetched Fessenden article; the over-removal warning and the 87%-of-112-minimalist-sites element-restriction finding verified on the fetched Moran article. Numeric noise-count bands are our operationalization. NOTE (assembler): overlaps US-14 — de-dup at review (US-14 = content relevance; VD-12 = visual noise).

### VD-13 Imagery and icon clarity
- **Standard:** Images carry task-relevant information rather than generic decoration (users scrutinize informative and authentic images and ignore stock filler), and icons are either universally recognized (home, search, print) or paired with always-visible text labels.
- **Source:** Jakob Nielsen / Nielsen Norman Group, "Photos as Web Content", 2010, https://www.nngroup.com/articles/photos-as-web-content/; Aurora Harley / Nielsen Norman Group, "Icon Usability", 2014, https://www.nngroup.com/articles/icon-usability/
- **Check:** Classify each image: informative (product detail, real people, data) vs. decorative/stock filler. Check rendering quality (no visible upscaling, stretching, or pixelation). Then inventory icons: for each, is it one of the few near-universal symbols, and if not, does a visible (not hover-only) label accompany it?
- **Pass:** All prominent images informative and cleanly rendered; every non-universal icon has a visible label. / **Partial:** One large decorative/stock image or one unlabeled ambiguous icon; everything else clear. / **Fail:** Multiple stock/filler images occupying prime space, visibly degraded imagery, or several unlabeled non-universal icons carrying core functions.
- **Applies:** both
- **Platforms:** all; note (per the icon article) icons carry relatively more salience on mobile than desktop
- **Needs:** screenshot-only
- **Provenance note:** The ignore-decorative/scrutinize-informative eyetracking findings and stock-photo blindness verified on the fetched Nielsen article; the short list of universal icons, the visible-label requirement (hover fails on touch), and mobile/desktop salience difference verified on the fetched Harley article. NOTE (assembler): icon-label check overlaps US-10 — de-dup at review. Icon style uniformity belongs to CONSISTENCY.

## Sources fetched
- https://www.nngroup.com/articles/gestalt-proximity/ — proximity principle (VD-03)
- https://www.nngroup.com/articles/gestalt-similarity/ — similarity traits, link-color reservation, CTA differentiation (VD-04)
- https://www.nngroup.com/articles/common-region/ — containers, whitespace-first, false-floor warnings (VD-05)
- https://www.nngroup.com/articles/principle-closure/ — closure principle, ~40% cut-off guidance for carousels (moved to Rejected/uncertain)
- https://www.nngroup.com/articles/principles-visual-design/ — scale (≤3 sizes), hierarchy, balance, contrast (VD-02)
- https://www.nngroup.com/articles/visual-hierarchy-ux-definition/ — hierarchy definition, squint test, 2+2 colors, ≤3 contrast variations (VD-01, VD-02)
- https://www.nngroup.com/articles/using-grids-in-interface-designs/ — 12-column desktop norm, 8-pixel grid, content-in-columns (VD-06, VD-07)
- https://www.nngroup.com/articles/aesthetic-minimalist-design/ — heuristic #8, signal-to-noise (VD-12)
- https://www.nngroup.com/articles/characteristics-minimalism/ — 112-site sample, over-removal warnings (VD-12 support)
- https://www.nngroup.com/articles/photos-as-web-content/ — informative vs. decorative/stock images (VD-13)
- https://www.nngroup.com/articles/icon-usability/ — universal icons, visible-label requirement (VD-13)
- https://www.nngroup.com/videos/figure-ground-gestalt/ — figure/ground definition only (see Rejected/uncertain)
- https://practicaltypography.com/line-length.html — 45–90 characters / 2–3 alphabets (VD-08)
- https://practicaltypography.com/line-spacing.html — 120–145% of point size (VD-09)
- https://practicaltypography.com/point-size.html — web body 15–25 px (VD-10)
- https://practicaltypography.com/mixing-fonts.html — font tolerance ladder (VD-11)
- http://webtypography.net/2.1.2 — Bringhurst via Rutter: 45–75 satisfactory, 66 ideal, 40–50 multi-column (VD-08)
- https://ixdf.org/literature/article/the-power-of-white-space — micro vs. macro whitespace taxonomy (VD-07)

## Rejected/uncertain
- **Figure-ground layering** — NN/g has only a video; landing page verified only the definition; technique guidance (shadows, scrims, blur, elevation) UNVERIFIED. Folded into VD-01's blur test; revisit in M2b if a citable primary article is found.
- **Closure / cut-off content cues** — Fully verified source (Kendrick, "Principle of Closure in Visual Design", NN/g 2021, ~40%-visible guidance for cut-off carousel items), but the operational check tests scroll/swipe affordance → USABILITY. Recommend handing this verified source to usability rather than duplicating.
- **Spacing-scale numeric threshold from a design system** — Material/Carbon spacing pages not fetchable this session; 8px rhythm rests solely on the NN/g grids article; 4px sub-step UNVERIFIED. (Assembler note: the consistency agent later fetched M3's 8dp spacing scale via rendered browser — see CO-07.)
- **NN/g "Line Length Readability" article** — 404; its 50–75 CPL figure not used.
- **Balance (symmetrical/asymmetrical/radial)** — verified in 5 Principles but no judgeable anchor distinct from VD-01; dropped.
- **Baseline grid / vertical rhythm** — no primary source fetched ties a testable rule to UI screenshots; dropped.
- **Mobile-native body-size minimums** — HIG typography pages not fetchable by this agent; resolved by the platforms agent (rendered-browser fetch) — see platforms threshold table.
# Dimension: Accessibility (AC) — agent output, pending Clemens review

### AC-01 Text contrast minimum (WCAG SC 1.4.3, Level AA)
- **Standard:** Text and images of text have a contrast ratio of at least 4.5:1, or at least 3:1 for large-scale text (at least 18pt, or 14pt bold — approx. 24px / 18.66px at 1pt = 1.333px).
- **Source:** W3C, "WCAG 2.2" (Recommendation 2023, updated 12 Dec 2024), https://www.w3.org/TR/WCAG22/ + Understanding SC 1.4.3 (updated 1 Jun 2026), https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- **Check:** Sample foreground/background color pairs for body text, secondary text, button labels, links, and placeholder text; compute ratio as (L1 + 0.05) / (L2 + 0.05) using relative luminance; do not round up (4.499:1 fails 4.5:1). For text over images/gradients, sample the worst-case (lowest-contrast) region behind the text. Estimate large-text status from rendered size; confirm pt size from DOM/Figma when available.
- **Pass:** all sampled text pairs meet their threshold. **Partial:** only secondary/decorative-adjacent text (e.g., placeholder, captions) fails, or failures within 0.3 of threshold where anti-aliasing makes sampling uncertain. **Fail:** body text, labels, or primary actions below threshold.
- **Applies:** both
- **Platforms:** all (thresholds identical across web/iOS/Android)
- **Needs:** screenshot-only (DOM/Figma preferred for exact hex values and font sizes)
- **Assessability:** screenshot
- **Provenance note:** Ratios and large-text exception appear in the normative SC 1.4.3 text; the "large scale" definition (18pt / 14pt bold, CJK equivalents) and the no-rounding rule are in the WCAG glossary and Understanding page. Exceptions: inactive components, pure decoration, logotypes, incidental text in photos.

### AC-02 Non-text contrast (WCAG SC 1.4.11, Level AA)
- **Standard:** UI components (the visual information required to identify controls and their states) and meaning-bearing parts of graphical objects have at least a 3:1 contrast ratio against adjacent colors.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 1.4.11 (updated 15 Jun 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- **Check:** Sample control boundaries/fills against their background for inputs, checkboxes, radio buttons, toggles, and icon-only buttons; sample state indicators (selected tab underline, toggle-on fill); sample chart lines/segments and informational icons against adjacent colors. Boundaries are only required to contrast when no other visual cue identifies the control.
- **Pass:** all identification-critical component visuals and informational graphics meet 3:1. **Partial:** isolated failures on non-primary controls, or components identifiable by another passing cue. **Fail:** primary controls or key graphics indistinguishable at 3:1 (e.g., light-gray input borders on white with no other cue).
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Assessability:** screenshot
- **Provenance note:** The 3:1 value is normative in SC 1.4.11 for "User Interface Components" and "Graphical Objects." Understanding page scopes it to parts "required for understanding"; inactive components, user-agent-default styling, and essential graphics (logos, photos, heat maps) are exempt.

### AC-03 Use of color as sole signal (WCAG SC 1.4.1, Level A)
- **Standard:** Color is never the only visual means of conveying information, indicating an action, prompting a response, or distinguishing an element.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 1.4.1 (updated 16 Sep 2025), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- **Check:** Inspect for color-only patterns: in-text links distinguished only by hue (no underline/weight — the associated technique expects 3:1 against surrounding text plus a hover cue if color alone is used); required/error fields marked only by red; charts whose series are separable only by a color legend; status dots without text/shape. Simulate a grayscale pass mentally or programmatically.
- **Pass:** every color-coded signal has a redundant cue (text, underline, icon, pattern, position). **Partial:** redundant cues present for most signals; isolated color-only instances in secondary content. **Fail:** any primary signal (links, errors, required fields, chart series) is color-only.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Assessability:** screenshot
- **Provenance note:** Normative wording in SC 1.4.1; the three canonical failures (color-only links, color-only required/error fields, color-only info in images) and the 3:1-plus-hover-cue link technique are on the Understanding page.

### AC-04 Text alternatives for non-text content (WCAG SC 1.1.1, Level A)
- **Standard:** All non-text content has a text alternative serving an equivalent purpose (controls need a name describing purpose; decoration must be ignorable by assistive technology).
- **Source:** W3C, "WCAG 2.2" + Understanding SC 1.1.1 (updated 12 Jun 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- **Check:** With DOM: enumerate `img`, SVG, canvas, icon fonts, and CSS background images carrying meaning; verify each has non-empty, purpose-equivalent alt/aria-label, and decorative images have empty alt or are hidden from the accessibility tree. With Figma: check layer alt-text/annotation properties. Judge equivalence in context, not mere presence.
- **Pass:** all meaningful non-text content has equivalent alternatives; decoration is marked decorative. **Partial:** alternatives exist but some are generic ("image", filename) or decoration is not suppressed. **Fail:** meaningful images/icon-only controls lack alternatives.
- **Applies:** both
- **Platforms:** all (web: alt/ARIA; iOS: accessibilityLabel; Android: contentDescription)
- **Needs:** DOM/Figma required
- **Assessability:** DOM/Figma
- **Provenance note:** Normative SC 1.1.1 with exceptions for controls/input, time-based media, tests, sensory, CAPTCHA, decoration. Understanding page's test rules are markup-inspection-based (alt attributes, ARIA names) — a screenshot cannot reveal whether alternatives exist, only whether images look meaningful. WAI Easy Checks confirms judging appropriateness requires seeing image and markup together.

### AC-05 Programmatic structure and relationships (WCAG SC 1.3.1, Level A)
- **Standard:** Information, structure, and relationships conveyed through presentation are programmatically determinable or available in text.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 1.3.1 (updated 9 Mar 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html
- **Check:** With DOM: verify visually apparent headings use h1–h6 (in a sensible hierarchy), form labels are programmatically associated (label/for, aria-labelledby), lists use ul/ol/dl, data tables use th with scope/headers. Cross-reference against the screenshot: anything that *looks* like a heading/label/list must be marked up as one. With Figma: check semantic annotations if present, otherwise flag.
- **Pass:** visual structure and programmatic structure match. **Partial:** structure mostly present with gaps (e.g., one unassociated label, skipped heading level). **Fail:** styled-text-only headings, unassociated labels, layout tables for data.
- **Applies:** both
- **Platforms:** all
- **Needs:** DOM/Figma required
- **Assessability:** DOM/Figma
- **Provenance note:** Normative SC 1.3.1; Understanding page states testing combines markup inspection with AT validation "rather than relying solely on visual inspection." The screenshot supplies the visual half of the comparison, but the criterion itself is about the code.

### AC-06 Text spacing resilience (WCAG SC 1.4.12, Level AA)
- **Standard:** No loss of content or functionality when users set line height to at least 1.5x font size, paragraph spacing to at least 2x, letter spacing to at least 0.12x, and word spacing to at least 0.16x.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 1.4.12 (updated 1 Oct 2025), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
- **Check:** Full test requires applying all four overrides live and checking for clipping/overlap — not possible on a static artifact. Static-risk flag only: from DOM/Figma, note fixed-height text containers, overflow:hidden on text blocks, and buttons/badges with no vertical slack; report as risk, not score.
- **Pass:** n/a statically. **Partial:** n/a. **Fail:** n/a — mark N/A ("needs manual test") with any static risk flags listed.
- **Applies:** both
- **Platforms:** web primarily (user style overrides); native apps via dynamic type analog — note as web-centric
- **Needs:** DOM/Figma preferred (for risk flags only)
- **Assessability:** interaction-required
- **Provenance note:** All four multipliers are normative in SC 1.4.12. Understanding page defines the test as "setting all of the following and by changing no other style property" and observing breakage — inherently a dynamic test; content is not required to ship with these values.

### AC-07 Target size minimum (WCAG SC 2.5.8, Level AA)
- **Standard:** Pointer targets are at least 24 by 24 CSS pixels, except when an undersized target's centered 24px-diameter circle intersects no other target or undersized-target circle (Spacing), an equivalent conforming control exists on the same page (Equivalent), the target is inline in text (Inline), sized by the user agent (User agent control), or the presentation is essential/legally required (Essential).
- **Source:** W3C, "WCAG 2.2" + Understanding SC 2.5.8 (updated 11 May 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- **Check:** Establish the CSS-pixel scale (from DOM viewport width or Figma frame size; estimate from known UI elements if screenshot-only and state the assumption). Measure bounding boxes of icon buttons, close buttons, checkboxes, pagination, list-row actions. For undersized targets, apply the 24px-circle spacing test to neighbors before failing.
- **Pass:** all targets ≥24x24 CSS px or covered by an exception. **Partial:** a few undersized targets that nearly satisfy spacing, or scale uncertainty prevents a confident fail. **Fail:** clearly undersized, tightly packed targets (e.g., 16px icons in a dense toolbar).
- **Applies:** both
- **Platforms:** all; note stricter platform conventions exist (iOS HIG 44pt, Material 48dp) but the WCAG AA floor is 24 CSS px
- **Needs:** screenshot-only (DOM/Figma preferred to resolve CSS-pixel scale exactly)
- **Assessability:** screenshot
- **Provenance note:** The 24 CSS px value and all five exceptions are normative in SC 2.5.8; the circle-intersection measurement for the Spacing exception is spelled out in the SC text and illustrated on the Understanding page.

### AC-08 Descriptive headings and labels (WCAG SC 2.4.6, Level AA)
- **Standard:** Headings and labels, where present, describe the topic or purpose of the content or control they head/label.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 2.4.6 (updated 9 Mar 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html
- **Check:** Read every visible heading and field/button label against the content it governs: is the section's topic inferable from its heading alone; do labels disambiguate similar fields; are labels specific rather than generic ("Submit" vs "Place order" where ambiguity matters)?
- **Pass:** all visible headings/labels accurately describe topic or purpose. **Partial:** mostly descriptive with isolated vague ones. **Fail:** misleading or generic headings/labels that leave purpose unclear.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Assessability:** screenshot
- **Provenance note:** Normative SC 2.4.6 is one sentence; Understanding page explicitly notes it does not require headings/labels to exist (3.3.2 covers label presence) and that correct markup is 1.3.1's job — so descriptiveness of *visible* text is legitimately judgeable from a screenshot.

### AC-09 Focus visible (WCAG SC 2.4.7, Level AA)
- **Standard:** Any keyboard-operable interface has a mode of operation in which the keyboard focus indicator is visible.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 2.4.7 (updated 17 Sep 2025), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html
- **Check:** Full test requires tabbing through the interface (test rule: "Element in sequential focus order has visible focus"). Static best-effort: if DOM/CSS available, flag `outline: none`/`outline: 0` without replacement `:focus`/`:focus-visible` styles as a strong risk signal; if a screenshot happens to capture a focused control, check the indicator exists (its contrast belongs to 1.4.11).
- **Pass:** n/a statically. **Partial:** n/a. **Fail:** n/a — mark N/A ("needs keyboard test"), plus any CSS risk flags.
- **Applies:** both
- **Platforms:** web and desktop primarily; touch-only mobile flows still need it for external keyboards — note per-platform
- **Needs:** DOM/Figma preferred (for CSS risk flags only)
- **Assessability:** interaction-required
- **Provenance note:** SC 2.4.7 requires only that an indicator be visible in some mode; the Understanding page confirms it "does not specify what that form is" (size/contrast live in 1.4.11 and AAA 2.4.13). WAI Easy Checks classifies this as an active Tab-key check.

### AC-10 Labels or instructions for input (WCAG SC 3.3.2, Level A)
- **Standard:** Labels or instructions are provided whenever content requires user input, including identification of required fields and expected data formats when non-customary.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 3.3.2 (updated 9 Mar 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html
- **Check:** For every visible input: is there a persistent visible label (placeholder-only labeling fails once the field is filled, since the label must be "presented to all users"); are required fields marked; are unusual formats (dates, phone) given format hints? Flag placeholder-as-label patterns explicitly.
- **Pass:** every input has a persistent visible label; required/format cues present where needed. **Partial:** labels present but some rely on placeholders or omit format hints. **Fail:** unlabeled inputs or placeholder-only forms.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only (DOM confirms whether an off-screen label exists, but a *visible* label is the point here)
- **Assessability:** screenshot
- **Provenance note:** Normative SC 3.3.2; Understanding page distinguishes "label" (perceivable by all users) from programmatic "name" and notes passing 4.1.2 does not imply passing 3.3.2 — which is exactly why this is screenshot-assessable.

### AC-11 Error identification in text (WCAG SC 3.3.1, Level A)
- **Standard:** When an input error is automatically detected, the erroneous item is identified and the error is described to the user in text (color/style may supplement but never replace text).
- **Source:** W3C, "WCAG 2.2" + Understanding SC 3.3.1 (updated 12 Jun 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html
- **Check:** Conditional: only scoreable when the captured screen shows an error state. Then verify each errored field is identified (which field) and described (what is wrong) in visible text, not just a red border or icon. If no error state is captured, mark N/A ("needs manual test — submit invalid input").
- **Pass:** captured error states name the field and describe the error in text. **Partial:** text present but vague ("invalid input") or not tied to a specific field. **Fail:** error indicated by color/icon only.
- **Applies:** both (multi-screen flows that include an error screen are ideal)
- **Platforms:** all
- **Needs:** screenshot-only
- **Assessability:** screenshot (conditional — only when an error state is captured; otherwise interaction-required)
- **Provenance note:** Normative SC 3.3.1; Understanding page states errors must "also be identified using text" and that the criterion targets automatically detected errors — the detection behavior is dynamic, but the *presentation* of a captured error state is statically checkable.

### AC-12 Consistent navigation (WCAG SC 3.2.3, Level AA)
- **Standard:** Navigational mechanisms repeated across a set of screens occur in the same relative order each time (insertions/removals allowed if original items keep relative order).
- **Source:** W3C, "WCAG 2.2" + Understanding SC 3.2.3 (updated 28 Jun 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation.html
- **Check:** Across the provided screens, diff repeated nav structures (top nav, sidebar, tab bar, footer): same items in the same relative order? Expanding menus adding a level of detail is permitted.
- **Pass:** repeated nav keeps relative order everywhere. **Partial:** order preserved but placement/grouping shifts inconsistently. **Fail:** reordered nav items between screens.
- **Applies:** multi (single-screen audits: mark N/A — the SC applies only to sets of pages)
- **Platforms:** all
- **Needs:** screenshot-only
- **Assessability:** screenshot
- **Provenance note:** Normative SC 3.2.3 scopes to "multiple web pages within a set of web pages"; Understanding page confirms single pages are out of scope and that insertions between items are permitted.

### AC-13 Consistent identification (WCAG SC 3.2.4, Level AA)
- **Standard:** Components with the same functionality across a set of screens are identified consistently — same labels, and consistent text alternatives for icons with the same function.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 3.2.4 (updated 9 Mar 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html
- **Check:** Across screens, match functionally identical controls (search, save, delete, back) and compare their visible labels and icons; consistent patterns like "Go to page 4"/"Go to page 5" pass. With DOM/Figma, also compare text alternatives of same-function icons.
- **Pass:** same function, same identification throughout. **Partial:** minor wording drift ("Save" vs "Save changes") without functional ambiguity. **Fail:** same function labeled or iconed differently in ways that suggest different functions.
- **Applies:** multi (single-screen: N/A per SC scope; within-page consistency is best practice, not this SC)
- **Platforms:** all
- **Needs:** screenshot-only (DOM/Figma preferred for the icon text-alternative half)
- **Assessability:** screenshot
- **Provenance note:** Normative SC 3.2.4; Understanding page explicitly limits scope to sets of pages and extends consistency to icon text alternatives.

### AC-14 Name, role, value for custom controls (WCAG SC 4.1.2, Level A)
- **Standard:** For all UI components, name and role are programmatically determinable; user-settable states, properties, and values are programmatically settable; and change notifications reach assistive technologies.
- **Source:** W3C, "WCAG 2.2" + Understanding SC 4.1.2 (updated 9 Mar 2026), https://www.w3.org/TR/WCAG22/, https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html
- **Check:** With DOM: for each interactive element, verify a native semantic element is used per spec, or ARIA supplies role, accessible name, and state (aria-expanded, aria-checked, etc.); flag div/span click targets without role/name. With Figma: not determinable — mark N/A with note.
- **Pass:** all controls expose name, role, and current state. **Partial:** names/roles present but some states missing (e.g., toggle without aria-pressed). **Fail:** unnamed or role-less custom controls.
- **Applies:** both
- **Platforms:** web (ARIA/HTML); native platforms via their accessibility APIs — DOM equivalent rarely available, note per-platform
- **Needs:** DOM/Figma required (DOM specifically; Figma is insufficient)
- **Assessability:** DOM/Figma
- **Provenance note:** Normative SC 4.1.2; Understanding page's 16 test rules are all markup/accessibility-tree inspections, and using standard HTML controls per spec satisfies it automatically. Included so the Robust principle is represented; entirely invisible in a screenshot.

## Assessability summary
- **Screenshot-assessable:** SC 1.4.3 (AC-01), 1.4.11 (AC-02), 1.4.1 (AC-03), 2.5.8 (AC-07, scale must be established), 2.4.6 (AC-08), 3.3.2 (AC-10), 3.3.1 (AC-11, only when an error state is captured), 3.2.3 (AC-12, multi-screen only), 3.2.4 (AC-13, multi-screen only). Supported by WAI Easy Checks, which treats contrast, visible labels, and heading appearance as look-at-the-page checks, and by WCAG-EM's acknowledgment that criteria with no relevant content in scope can be reported "not present."
- **DOM/Figma-only:** SC 1.1.1 (AC-04), 1.3.1 (AC-05), 4.1.2 (AC-14, DOM specifically). These concern programmatic equivalents invisible in pixels; Understanding pages define their tests as markup/accessibility-tree inspection.
- **Interaction-required (audit marks N/A with explicit "needs manual test" note; static risk flags allowed):** SC 1.4.12 (AC-06, apply spacing overrides), 2.4.7 (AC-09, Tab-key traversal), plus conditional fallback for 3.3.1 when no error state is captured. Easy Checks classifies focus and zoom checks as active-interaction tests; WCAG-EM notes most checks are not fully automatable and require the full page/process in a working state.

## Sources fetched
- https://www.w3.org/TR/WCAG22/ — normative spec; verified exact SC wording, levels, 4.5:1 / 3:1 ratios, 24 CSS px, spacing multipliers; page dated 12 Dec 2024.
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html — large-text definition, 1pt=1.333px, luminance formula, no-rounding rule, exceptions (upd. 1 Jun 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html — what parts of components/graphics need 3:1; boundary and exemption rules (upd. 15 Jun 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html — all five 2.5.8 exceptions verbatim; circle-spacing measurement (upd. 11 May 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html — canonical color-only failures; 3:1-plus-hover link technique (upd. 16 Sep 2025).
- https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html — four override values; test = apply overrides, observe clipping; script exceptions (upd. 1 Oct 2025).
- https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html — 200% requirement; testing demands interactive resizing; grounds rejection of 1.4.4 (upd. 18 May 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html — indicator form unspecified; contrast lives in 1.4.11/2.4.13; keyboard test rule (upd. 17 Sep 2025).
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html — exceptions list; markup-inspection test rules (upd. 12 Jun 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html — heading/label/table/list markup requirements; code-level testing (upd. 9 Mar 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html — does not require headings to exist; markup deferred to 1.3.1 (upd. 9 Mar 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation.html — multi-page scope; relative-order allowance (upd. 28 Jun 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html — multi-page scope; icon text-alternative consistency (upd. 9 Mar 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html — text description mandatory; color/style supplementary only (upd. 12 Jun 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html — label vs name distinction; required-field and format coverage (upd. 9 Mar 2026).
- https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html — accessibility-tree testing; native-HTML-per-spec passes (upd. 9 Mar 2026).
- https://www.w3.org/WAI/test-evaluate/preliminary/ — Easy Checks; classifies which checks are visual vs tool-based vs interactive; supports assessability split.
- https://www.w3.org/TR/WCAG-EM/ — evaluation methodology (2014); full pages/processes, human judgment needed, "not present" reporting convention.

## Rejected/uncertain
- **SC 1.4.4 Resize Text (AA) — rejected.** Understanding page is explicit that testing requires demonstrating actual resize behavior at up to 200% via a scaling mechanism; a static artifact carries zero signal (unlike 2.4.7, where DOM/CSS at least yields outline-suppression risk flags). Marking it permanently N/A adds no scoring value; the report can list it once in a global "not statically assessable" note instead.
- **SC 1.4.10 Reflow (AA) — rejected.** Same class as 1.4.4: requires rendering at 320 CSS px width; a single-viewport screenshot cannot demonstrate or refute it.
- **SC 2.1.1 Keyboard (A) — rejected.** Purely behavioral; no static risk signal reliable enough to flag, per Easy Checks' keyboard section.
- **SC 4.1.1 Parsing — rejected.** Obsolete in WCAG 2.2 (removed from the recommendation); citing it would be an error.
- **SC 2.4.13 Focus Appearance, 1.4.6 Contrast (Enhanced), 2.5.5 Target Size (Enhanced) — rejected.** Level AAA; out of the stated AA scope, though 2.4.13's indicator-size guidance could inform an advisory note under AC-09.
- **SC 3.2.1 On Focus / 3.2.2 On Input (A) — rejected.** Context-change-on-interaction behaviors; undetectable statically.
- **Uncertain: AC-11 (3.3.1) conditionality.** The Understanding page cautions that screenshots cannot demonstrate the automatic-detection behavior; I scoped the criterion to presentation of captured error states only. If Clemens prefers stricter honesty, it can move wholesale to interaction-required.
- **Uncertain: AC-07 (2.5.8) scale dependence.** The 24px value is in CSS pixels; screenshot-only audits must estimate device-pixel ratio (e.g., from status bar height or known component sizes) and should surface that assumption in the report.
# Dimension: Consistency (CO) — agent output, pending Clemens review

### CO-01 Uniform styling of repeated UI elements
- **Standard:** An element that plays the same role (primary button, link, card, field) looks and behaves identically everywhere it appears in the product.
- **Source:** Nielsen Norman Group, "Consistency and Standards (Usability Heuristic #4)", accessed 2026-07, https://www.nngroup.com/articles/consistency-and-standards/
- **Check:** Inventory every instance of each recurring element class visible in the input (buttons by role, links, form fields, cards, tags). Compare fill/border color, corner radius, typography, and internal padding across instances of the same class.
- **Pass:** Every instance of a given element class shares one visual treatment (state variants excepted). / **Partial:** One element class has a stray variant with no evident semantic reason. / **Fail:** Two or more classes have unexplained variants, or the same class has 3+ distinct treatments.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only (DOM/Figma preferred — component/instance data reveals detached or overridden instances directly)
- **Provenance note:** Fetched the NN/g heuristic #4 article; it explicitly lists visual styling and button/form placement among the things that must stay internally consistent, and warns users "should not have to wonder whether different words, situations, or actions mean the same thing".

### CO-02 Cross-screen structural stability
- **Standard:** Persistent chrome — header, navigation, logo position, page-title placement, recurring action locations — stays in the same place with the same contents on every screen of a flow.
- **Source:** Nielsen Norman Group, "Consistency and Standards (Usability Heuristic #4)", accessed 2026-07, https://www.nngroup.com/articles/consistency-and-standards/ (supporting: Material Design 3, "Grids & spacing", https://m3.material.io/foundations/layout/grids-spacing/spacing)
- **Check:** Multi-screen inputs only: overlay/compare screens; verify nav placement and item order, logo position, header height, and location of recurring key actions are identical screen-to-screen.
- **Pass:** All persistent regions identical in position and ordering across screens. / **Partial:** One region shifts position or reorders items between screens without a mode change justifying it. / **Fail:** Navigation or primary-action placement moves between screens, or persistent items appear/disappear arbitrarily.
- **Applies:** multi
- **Platforms:** all
- **Needs:** screenshot-only (DOM/Figma preferred for pixel-exact position diffing)
- **Provenance note:** NN/g article (fetched) names layout/button placement consistency across pages; M3 spacing page (fetched via rendered browser) states key actions and titles "should appear in a consistent location across pages". NOTE (assembler): overlaps AC-12 (WCAG 3.2.3 consistent navigation) — AC-12 is the normative floor (relative order), CO-02 the stricter craft bar (position identity); de-dup at review.

### CO-03 Terminology consistency
- **Standard:** The same word names the same object or action everywhere; the product never alternates between synonyms (e.g., "Delete" vs "Remove" vs "Trash") for one concept.
- **Source:** Nielsen Norman Group, "Consistency and Standards (Usability Heuristic #4)", accessed 2026-07, https://www.nngroup.com/articles/consistency-and-standards/ (supporting: Apple, "Writing", Human Interface Guidelines, accessed 2026-07, https://developer.apple.com/design/human-interface-guidelines/writing)
- **Check:** Extract all visible labels, headings, buttons, and empty/error text. Build a concept-to-term table; flag any concept referred to by more than one term, and any term used for more than one concept.
- **Pass:** One term per concept throughout. / **Partial:** One synonym pair for a peripheral concept. / **Fail:** Core objects or actions carry multiple names, or one word means different things in different places.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only (DOM preferred — accessible names and hidden labels widen the term inventory)
- **Provenance note:** Verified against both fetched sources; Apple's Writing page advises keeping a common-terms list because "Consistent language … helps everything feel more cohesive". Voice/tone consistency folded in here rather than a separate criterion (see Rejected). NOTE (assembler): overlaps AC-13 (WCAG 3.2.4 consistent identification) — de-dup at review.

### CO-04 Capitalization and label-style consistency
- **Standard:** Each UI element type uses one capitalization style (title case or sentence case) and one punctuation/label pattern consistently across the interface.
- **Source:** Apple, "Writing", Human Interface Guidelines, accessed 2026-07, https://developer.apple.com/design/human-interface-guidelines/writing
- **Check:** Group visible text by element type (buttons, menu items, headings, field labels, tabs). Within each group, classify each string as title case, sentence case, all caps, or mixed; also check terminal punctuation and label suffix patterns (e.g., colons) for uniformity.
- **Pass:** Every element type is internally uniform in case and punctuation. / **Partial:** One element type mixes styles in 1–2 instances. / **Fail:** Multiple element types mix styles, or sibling elements on one screen (e.g., two dialog buttons) differ in case.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched via Apple's HIG JSON endpoint; the page states directly: "Choose a style for each UI element type and use it consistently". The pass/fail granularity is our operationalization, not Apple's.

### CO-05 Color token discipline
- **Standard:** Every color in the UI resolves to a defined palette role or design token; no ad-hoc, near-duplicate color values.
- **Source:** Material Design 3, "Design tokens", accessed 2026-07, https://m3.material.io/foundations/design-tokens/overview (supporting: NN/g, "Design Systems 101", https://www.nngroup.com/articles/design-systems-101/)
- **Check:** Screenshot: sample fills, text colors, borders, and surfaces; cluster values and flag near-duplicates (e.g., multiple grays or brand-blues within a small perceptual distance serving the same role). Figma: pull variables/styles via token data and count colors used that are not bound to any variable/style, plus distinct raw values per role.
- **Pass:** All sampled colors map onto a small, role-based palette; with Figma data, no unbound hard-coded fills on repeated elements. / **Partial:** 1–2 near-duplicate values or a handful of unbound fills. / **Fail:** Same-role elements use visibly different values, or token data shows widespread hard-coded colors bypassing defined variables.
- **Applies:** both
- **Platforms:** all
- **Needs:** DOM/Figma preferred (measured check: count of distinct color values vs bound variables via Figma variable data; screenshot-only degrades to perceptual clustering)
- **Provenance note:** M3 tokens page (fetched via rendered browser) states "Use design tokens instead of hardcoded values" and that tokens exist so "style updates propagate consistently." UNVERIFIED: any specific numeric color budget — no fetched primary source gives one, so the check uses role-mapping and duplication rather than a hard count.

### CO-06 Type scale discipline
- **Standard:** All text maps to a small, deliberate set of type styles drawn from a defined scale, rather than one-off size/weight combinations.
- **Source:** Material Design 3, "Typography — type scale & tokens", accessed 2026-07, https://m3.material.io/styles/typography/type-scale-tokens
- **Check:** Screenshot: inventory distinct (size, weight, family) combinations and check that same-role text (body, captions, section headings) uses the same combination everywhere. Figma: count distinct text styles in use, and text nodes not bound to any text style.
- **Pass:** Distinct styles form a clear scale, same role → same style, and (with Figma data) essentially all text is style-bound. / **Partial:** 1–2 orphan combinations off the scale, or minor unbound text. / **Fail:** Same-role text varies in size/weight across screens, or the count of distinct ad-hoc combinations rivals or exceeds the defined styles.
- **Applies:** both
- **Platforms:** all
- **Needs:** DOM/Figma preferred (measured check: distinct text-style count and unbound-text count from Figma; DOM computed styles equivalently)
- **Provenance note:** Fetched page defines a type scale as "a selection of type styles used across a product to ensure consistency", specifies 15 baseline styles, and notes no single product will use all of them (its reduced-set example uses 5) — so "more distinct ad-hoc styles than a full M3 scale" is a defensible ceiling; any tighter numeric budget is UNVERIFIED. NOTE (assembler): adjacent to VD-02 (emphasis economy) — VD-02 judges per-screen hierarchy legibility, CO-06 judges scale discipline/token binding; keep the boundary explicit at review.

### CO-07 Spacing scale adherence
- **Standard:** Padding, gaps, and margins come from a consistent spacing scale (e.g., multiples of a base unit) applied the same way to equivalent element pairs.
- **Source:** Material Design 3, "Spacing", accessed 2026-07, https://m3.material.io/m3/pages/spacing/overview
- **Check:** Measure gaps between repeated sibling elements (list rows, cards, form fields) and padding inside repeated containers. Verify equivalent pairs share equal values and that values cluster on a scale (M3's system: multiples of 8dp, space100 = 8dp). Figma: check spacing values in auto-layout properties against defined spacing tokens/variables.
- **Pass:** Equivalent gaps are equal and values sit on a recognizable scale. / **Partial:** Isolated off-scale values or one unequal sibling gap. / **Fail:** Repeated structures use visibly unequal spacing with no scale evident.
- **Applies:** both
- **Platforms:** all
- **Needs:** DOM/Figma preferred (exact values from auto-layout/computed style; screenshot-only allows pixel measurement at known scale factor)
- **Provenance note:** M3 spacing page (fetched via rendered browser) states "The spacing system is measured on an 8dp scale" with space100 = 8dp. The criterion requires *a* consistent scale, not specifically 8dp, since other platforms don't mandate it. NOTE (assembler): adjacent to VD-07 (spacing rhythm) — VD-07 judges within-screen rhythm/crowding, CO-07 judges scale/token adherence across equivalents; de-dup at review.

### CO-08 Icon family and weight consistency
- **Standard:** All icons come from one visual family and share stroke weight, fill style, corner style, and optical size, matched to adjacent text.
- **Source:** Material Design 3, "Icons — applying icons", accessed 2026-07, https://m3.material.io/styles/icons/applying-icons (supporting: Apple, "SF Symbols", HIG, https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
- **Check:** Collect all visible icons; compare stroke weight, filled-vs-outlined treatment (excluding deliberate selected-state fills), corner style (rounded vs sharp), and rendered size relative to paired text.
- **Pass:** Single family, uniform weight and style, sizes consistent with text pairing. / **Partial:** One icon deviates in weight or style. / **Fail:** Mixed families or mixed filled/outlined styles without state semantics, or icon sizes vary arbitrarily in one context (e.g., a nav bar).
- **Applies:** both
- **Platforms:** all; on iOS/macOS additionally check custom icons match SF Symbols' weight/detail level; on Android check against one Material Symbols style (outlined/rounded/sharp)
- **Needs:** screenshot-only (Figma preferred — component sources reveal mixed icon libraries directly)
- **Provenance note:** M3 icons page (fetched via rendered browser) has explicit do/don't pairs: "Apply weights consistently" / "Don't mix different weights", and match icon optical weight/size to text. Apple's SF Symbols page (fetched via HIG JSON) requires custom symbols "consistent with the ones the system provides" in detail and optical weight.

### CO-09 Repeated-element uniformity and alignment
- **Standard:** Elements of the same kind in a collection (thumbnails, avatars, cards, leading icons) share identical size and alignment, producing an even visual rhythm.
- **Source:** Material Design 3, "Grids & spacing", accessed 2026-07, https://m3.material.io/foundations/layout/grids-spacing/spacing
- **Check:** For each visible collection (lists, grids, toolbars), verify item dimensions match, leading elements sit on a common alignment line, and inter-item spacing is constant along each axis.
- **Pass:** All collections uniform in size, alignment, and rhythm. / **Partial:** One collection with a single misaligned or missized item. / **Fail:** Collections with visibly mixed item sizes or broken alignment lines on multiple screens/regions.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only (DOM/Figma preferred for exact coordinates)
- **Provenance note:** Fetched M3 page states similar elements "should have the same spacing and sizing" and leading elements like thumbnails and avatars "should always be aligned". Distinct from CO-07: this is about the elements themselves, not the scale of the gaps. NOTE (assembler): adjacent to VD-06 (grid/alignment) — VD-06 judges the page grid, CO-09 judges collection-item uniformity; de-dup at review.

### CO-10 External convention adherence (Jakob's Law)
- **Standard:** Widely standardized patterns — logo top-left linking home, search affordance, cart top-right, magnifying-glass = search, link affordances — work the way the rest of the web/app ecosystem has taught users.
- **Source:** Laws of UX (Jon Yablonski), "Jakob's Law", accessed 2026-07, https://lawsofux.com/jakobs-law/ ; Jakob Nielsen / NN/g, "The Need for Web Design Standards", accessed 2026-07, https://www.nngroup.com/articles/the-need-for-web-design-standards/
- **Check:** Identify every standardized pattern the screen participates in (navigation placement, search, cart, common icon meanings, form conventions). For each, judge whether the design matches the dominant convention; flag reinvented versions of solved patterns.
- **Pass:** All standard patterns follow convention. / **Partial:** One convention bent in a discoverable way. / **Fail:** A standard element is repurposed or relocated so its learned meaning breaks (e.g., non-search magnifying glass, cart bottom-left, logo not linking as expected).
- **Applies:** both
- **Platforms:** all; the concrete convention set differs — web conventions (logo top-left, cart top-right) for web, ecosystem-app conventions for mobile
- **Needs:** screenshot-only
- **Provenance note:** Both pages fetched. Law verbatim from lawsofux.com: "Users spend most of their time on other sites." Nielsen's fetched article grades 80%+ adoption as a "standard" and 50–79% as a "convention", and gives the logo/search/cart placement examples used above; specific adoption percentages date from 2004 and current rates are UNVERIFIED, but the placements remain dominant practice. Whether a convention is itself usable is out of scope (usability dimension).

### CO-11 Platform-native pattern adherence
- **Standard:** The interface uses its platform's native components, navigation structures, and system typography/iconography — or custom equivalents that respect the platform's documented patterns.
- **Source:** Apple, "Designing for iOS", Human Interface Guidelines, accessed 2026-07, https://developer.apple.com/design/human-interface-guidelines/designing-for-ios ; Material Design 3, accessed 2026-07, https://m3.material.io (design tokens & components guidance)
- **Check:** Classify the platform from the input (status bar, chrome, component shapes; or supplied metadata). Compare visible controls against the platform's standard set: iOS — tab bars, navigation bars, SF-style symbols, system-font-like text, standard sheet/alert anatomy; Android — Material components (FAB, top app bar, navigation bar), Material Symbols; web/desktop — its own norms per CO-10.
- **Pass:** Standard controls used (or customs that keep platform anatomy and placement). / **Partial:** Isolated foreign-platform component (e.g., one Material FAB in an otherwise iOS UI). / **Fail:** Wholesale foreign or invented chrome — e.g., Android-style navigation on iOS, or standard controls redrawn so they no longer read as themselves.
- **Applies:** both
- **Platforms:** iOS/iPadOS/macOS → HIG; Android → Material; web → CO-10 conventions govern; cross-platform frameworks judged against the host platform being shown
- **Needs:** screenshot-only
- **Provenance note:** Apple's page (fetched via HIG JSON) says iOS features let people interact "in familiar, consistent ways" and frames platform integration as what makes an app feel at home on iOS. Judging the aesthetics of native components stays with visual design; this criterion only scores conformance. Depends on the Step 1 platform classification (references/platforms.md).

### CO-12 Data and format consistency
- **Standard:** Dates, times, numbers, currency, phone numbers, and units are formatted one way throughout the interface, using locale-standard formats.
- **Source:** Nielsen Norman Group, "Consistency and Standards (Usability Heuristic #4)", accessed 2026-07, https://www.nngroup.com/articles/consistency-and-standards/
- **Check:** Extract every visible formatted value; group by data type; verify one format per type (e.g., not "Jan 5, 2026" in one card and "05/01/26" in another; consistent decimal places and currency symbol placement; consistent relative-vs-absolute time usage per context).
- **Pass:** One format per data type across the input. / **Partial:** One data type shows two formats in clearly different contexts without a stated pattern. / **Fail:** The same data type is formatted differently within one screen or arbitrarily across screens.
- **Applies:** both
- **Platforms:** all (expected locale format varies by target locale, not platform)
- **Needs:** screenshot-only (DOM preferred for machine-readable datetime attributes)
- **Provenance note:** The fetched NN/g heuristic #4 article explicitly lists standard formats for dates, phone numbers, and locations among the things consistency covers. The one-screen-vs-cross-screen severity split is our operationalization.

## Sources fetched
- https://www.nngroup.com/articles/consistency-and-standards/ — NN/g heuristic #4; internal vs external consistency, elements that must stay consistent.
- https://lawsofux.com/jakobs-law/ — verbatim law statement, attribution, takeaways.
- https://www.nngroup.com/videos/jakobs-law-internet-ux/ — NN/g origin page (2017), statement confirmed at source.
- https://www.nngroup.com/articles/the-need-for-web-design-standards/ — standard/convention/confusion adoption thresholds; placement conventions.
- https://www.nngroup.com/articles/design-systems-101/ — design-system definition; fragmentation risk.
- https://www.nngroup.com/articles/design-system-maturity/ — unintended variations as adoption failure; design-code parity.
- https://developer.apple.com/tutorials/data/design/human-interface-guidelines/designing-for-ios.json — JSON backing the HIG page (HTML is JS-rendered/empty to fetchers); platform familiarity guidance.
- https://developer.apple.com/tutorials/data/design/human-interface-guidelines/sf-symbols.json — SF Symbols weights/scales, custom-symbol consistency requirement.
- https://developer.apple.com/tutorials/data/design/human-interface-guidelines/writing.json — terminology lists, voice/tone, case per element type.
- https://m3.material.io/foundations/design-tokens/overview — rendered browser; token definition, "use tokens instead of hardcoded values".
- https://m3.material.io/styles/typography/type-scale-tokens — rendered browser; type scale definition, 15 baseline styles, subset guidance.
- https://m3.material.io/foundations/layout/grids-spacing/spacing — rendered browser; rhythm, similarity, consistent cross-page placement.
- https://m3.material.io/m3/pages/spacing/overview — rendered browser; 8dp spacing scale (space100 = 8dp).
- https://m3.material.io/styles/icons/applying-icons — rendered browser; three Material Symbols styles, weight-consistency do/don't.

## Rejected/uncertain
- **Numeric color budget** — no fetched primary source states a number; CO-05 checks role-mapping/token-binding instead.
- **4dp/8dp "grid" phrasing from Material 2** — current M3 documents an 8dp *spacing scale*; older M2 page not fetched, so CO-07 cites only the verified 8dp scale.
- **Direct WebFetch of developer.apple.com/design and m3.material.io HTML** — both return title-only bodies (JS-rendered); replaced with Apple's JSON data endpoint and rendered-browser fetches — noted so the build step doesn't treat the HTML URLs as fetch-verified.
- **Nathan Curtis / EightShapes token-naming article** — useful but secondary; dropped to keep sources to platform owners and NN/g.
- **Separate voice/tone criterion** — rarely judgeable from a static screenshot; folded into CO-03.
- **Interaction-behavior consistency** — real part of heuristic #4 but unobservable statically; observable slice covered by CO-01/CO-11.
- **Publication years for NN/g articles** — fetches did not surface original publication dates; citations use "accessed 2026-07" rather than guessed years.
- **Touch-target and contrast consistency** — excluded; owned by accessibility per scope guard.
# Dimension: User flow (UF) — agent output, pending Clemens review

### UF-01 Next-step obviousness
- **Standard:** From any screen, a first-time user can identify the single action that advances them toward the screen's implied goal without guesswork.
- **Source:** Kathryn Whitenton / Nielsen Norman Group, "The Two UX Gulfs: Evaluation and Execution", 2018, https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/
- **Check:** Identify the screen's implied user goal. Locate the control(s) that advance it. Ask the cognitive-walkthrough-style question: would a user who correctly understands the current state know what to do next? Note competing calls to action, buried primary actions, or controls whose outcome is ambiguous.
- **Pass:** One clear forward path; the advancing control is prominent and its outcome predictable. / **Partial:** Forward path exists but competes with 2+ equally weighted actions, or its outcome is ambiguous. / **Fail:** No discernible way to advance, or the apparent primary action leads away from the implied goal.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched the NN/g article; it defines the gulf of execution ("taking action to accomplish a specific goal") and prescribes bridging it with familiar cues and effective mental models. Terms coined 1986 by Hutchins, Hollan, Norman per the article.

### UF-02 Orientation and progress indication
- **Standard:** In any multi-step process, the screen shows where the user is, what steps exist, and which step is current.
- **Source:** Raluca Budiu / Nielsen Norman Group, "Wizards: Definition and Design Recommendations", 2017, https://www.nngroup.com/articles/wizards/ (supporting: Aurora Harley / NN/g, "Visibility of System Status", 2018, https://www.nngroup.com/articles/visibility-system-status/)
- **Check:** If the screen belongs to a multi-step process (wizard, checkout, onboarding), look for a step list/diagram with the current step highlighted, or an equivalent position cue (e.g., "Step 2 of 4", labeled page title). For multi-screen sets, verify the indicator advances correctly between screens.
- **Pass:** Steps enumerated and current step highlighted (or the process is genuinely single-step). / **Partial:** Some position cue (title, count) but no view of remaining steps, or indicator present on some screens only. / **Fail:** Multi-step process with no position or progress cue at all.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Budiu article (fetched) recommends "displaying a list or a diagram of the steps involved" with the current step highlighted. Harley article (fetched) grounds the general current-location/status principle.

### UF-03 Exit and cancel paths
- **Standard:** Every screen in a flow offers a clearly marked way to abandon or step out of the current process without hidden penalties.
- **Source:** Maria Rosala / Nielsen Norman Group, "User Control and Freedom (Usability Heuristic #3)", 2020, https://www.nngroup.com/articles/user-control-and-freedom/
- **Check:** Look for Back/Cancel/Close controls in expected positions (X top-right of overlays, Cancel near primary action, visible back affordance). For modals/wizards, confirm an exit exists on every step. For destructive exits mid-task, look for a confirmation guarding data loss. Flag flows that appear to disable or fight back navigation.
- **Pass:** Marked exit on every screen/step, positioned conventionally; data-loss exits are guarded. / **Partial:** Exit exists but is obscure, mislabeled (Close vs Cancel ambiguity), or missing on some steps. / **Fail:** No way out of a modal/step, or the design traps the user in the process.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched the NN/g heuristic page; it requires a clearly marked "emergency exit", cancel available at any point in multi-step processes, and warns against trapping users or breaking Back.

### UF-04 Error-state recovery path
- **Standard:** When an error is shown, it appears adjacent to its cause, states the problem constructively, and lets the user correct rather than restart.
- **Source:** Tim Neusesser & Evan Sunwall / Nielsen Norman Group, "Error-Message Guidelines", 2023, https://www.nngroup.com/articles/error-message-guidelines/
- **Check:** On any screen showing an error state: verify placement next to the offending field/element, redundant visual cues (color + icon/text), human-readable wording that proposes a fix, and evidence the user's prior input is preserved (fields still populated). In multi-screen sets, check the error screen leads back into the flow, not to a restart.
- **Pass:** Adjacent, constructive, recovery-oriented error that preserves input. / **Partial:** Error is visible and readable but generic, misplaced, or appears to discard input. / **Fail:** Error is a dead-end message (jargon, no next step) or forces starting over.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched article; guidelines include displaying errors adjacent to the problem, offering constructive solutions, and letting users edit "instead of starting over" with input preserved. Only auditable when an error state is among the captured screens; otherwise score N/A, not Fail.

### UF-05 Empty-state guidance
- **Standard:** An empty container tells the user the system is working, why it is empty, and what to do next.
- **Source:** Kate Kaplan / Nielsen Norman Group, "Designing Empty States in Complex Applications: 3 Guidelines", 2021, https://www.nngroup.com/articles/empty-state-interface-design/
- **Check:** For any contentless container/panel/screen: confirm (1) a status message distinguishing "no data" from loading/error, (2) a cue explaining what would populate the space, (3) a direct action (button/link) to start populating it. A blank region with none of the three is the failure signature.
- **Pass:** All three present: status, cause, actionable next step. / **Partial:** Status text only ("no results") with no learning cue or pathway. / **Fail:** Totally blank container indistinguishable from a loading failure.
- **Applies:** single
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched article; its three guidelines are communicate system status, provide learning cues, and create direct pathways for key tasks, with DataDog/Power BI/Loggly examples. Judged per screen whenever an empty container is visible.

### UF-06 Wait-state feedback
- **Standard:** Any visible wait state uses a feedback mechanism matched to its likely duration, with an explanation of what is happening.
- **Source:** Katie Sherwin / Nielsen Norman Group, "Progress Indicators Make a Slow System Less Insufferable", 2014, https://www.nngroup.com/articles/progress-indicators/
- **Check:** If a loading/processing state is captured: verify an animated indicator is present, accompanied by text naming the operation (e.g., "Loading comments…"). Judge fit: spinner-style is appropriate for short waits (~2–10s class operations); long operations (bulk upload, export, report generation) should show percent-done or step progress, not a bare spinner. Flag static, unexplained indicators.
- **Pass:** Indicator type plausibly matches the operation class and is labeled. / **Partial:** Indicator present but unlabeled, or a bare spinner on an obviously long operation. / **Fail:** No feedback for a visible wait state, or a static indicator that could mask a hang.
- **Applies:** single
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched article: looped animations for 2–10s, percent-done for 10s+, feedback for anything over ~1 second; cites the Nebraska-Lincoln finding that progress bars made users willing to wait about 3x longer. Score N/A when no wait state is captured.

### UF-07 In-form flow sequencing
- **Standard:** Form steps present fields in a logical single-column order with requirements disclosed up front, so users move forward instead of looping back to fix surprises.
- **Source:** Kathryn Whitenton / Nielsen Norman Group, "Website Forms Usability: Top 10 Recommendations", 2016, https://www.nngroup.com/articles/web-form-design/
- **Check:** On form screens: fields in one column (short related fields excepted), sequence follows convention (e.g., name before address), formatting/input requirements stated at the field rather than deferred to error messages, optional fields marked, no Reset/Clear hazard next to Submit.
- **Pass:** Single-column, conventional order, requirements visible before submission. / **Partial:** Order is logical but requirements are hidden until errors, or layout breaks vertical momentum in places. / **Fail:** Scrambled field order, undisclosed format rules, or a Clear/Reset button positioned to destroy progress.
- **Applies:** single
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched article; recommendations 3, 4, 8, 9, 10 map directly (single column because "multiple columns interrupt the vertical momentum", logical sequencing, upfront requirements, no Reset, visible specific errors). Scoped here to progression mechanics; field-label clarity itself belongs to the usability dimension.

### UF-08 Dead-end avoidance
- **Standard:** No screen leaves the user with zero productive options — every state offers a forward action, a way back, or both.
- **Source:** Maria Rosala / Nielsen Norman Group, "User Control and Freedom (Usability Heuristic #3)", 2020, https://www.nngroup.com/articles/user-control-and-freedom/
- **Check:** Single screen: verify at least one enabled action exists (terminal confirmations count if they link onward, e.g., "Continue shopping"). Multi-screen: trace the sequence for states reachable but not leavable — final screens with no navigation, error/empty screens with no exit, overlays with no close.
- **Pass:** Every captured state has an onward or backward path. / **Partial:** A state relies on browser/OS chrome (system back) as its only escape. / **Fail:** Any captured state with no visible way forward or back.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Anchored to the fetched heuristic's emergency-exit requirement and its warning against trapping users; the dead-end framing is my synthesis of that page's Back/Cancel/Close guidance applied to whole screens — flagged as derived, not quoted doctrine.

### UF-09 Action-result continuity
- **Standard:** Each screen in the sequence visibly confirms that the previous action succeeded and moved the user closer to the goal.
- **Source:** Kim Flaherty / Nielsen Norman Group, "Evaluate Interface Learnability with Cognitive Walkthroughs", 2022, https://www.nngroup.com/articles/cognitive-walkthroughs/
- **Check:** For each consecutive screen pair, apply cognitive-walkthrough question 4: "will users see that progress is made toward the goal?" Look for carried-over context (the item just added appears in the cart, the chosen plan is echoed on the payment screen), advanced progress indicators, and headers that acknowledge the prior step. Flag screens that could equally follow success or failure of the previous action.
- **Pass:** Every transition shows unambiguous evidence the prior action took effect. / **Partial:** Most transitions confirm progress but at least one is ambiguous. / **Fail:** One or more transitions give no evidence the previous action worked.
- **Applies:** multi
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Fetched the NN/g article; it quotes the four walkthrough questions and attributes the method to Lewis, Polson, Wharton, Rieman (CHI 1990; Wharton et al. 1994 in Usability Inspection Methods). The original 1994 chapter PDF could not be parsed, so the questions are verified via this NN/g page.

### UF-10 State persistence across steps
- **Standard:** Information the user has already provided persists across the flow — later steps reflect earlier choices, and moving back does not destroy work.
- **Source:** Raluca Budiu / Nielsen Norman Group, "Wizards: Definition and Design Recommendations", 2017, https://www.nngroup.com/articles/wizards/ (supporting: Rosala, "User Control and Freedom", 2020, https://www.nngroup.com/articles/user-control-and-freedom/)
- **Check:** Across the screen set: earlier selections are echoed where relevant (summaries, "editing plan: Pro" headers); if a back-navigation screen is captured, previously entered values are still populated; look for save-and-resume affordances ("Save draft", "Finish later") in long flows. From static screens, absence of any echo of prior input is the detectable failure signal.
- **Pass:** Prior inputs visibly persist and long flows offer save/resume. / **Partial:** Some carried state but a review/summary step is missing where entries span many screens, or no save-and-resume in a long flow. / **Fail:** A later screen contradicts or ignores earlier input, or a revisited step is shown empty.
- **Applies:** multi
- **Platforms:** all
- **Needs:** DOM/Figma preferred
- **Provenance note:** Budiu article (fetched) says to let users "exit the wizard midway and save state" and resume later, and to make steps self-sufficient without re-entering data; Rosala article (fetched) requires forms that survive Back without losing work. Static screenshots only show echoes of state, so prototype/DOM access materially improves this check.

### UF-11 Step-order logic
- **Standard:** The sequence of screens follows a logic the user would predict — each step needs only information already available, and dependent steps come after their prerequisites.
- **Source:** Raluca Budiu / Nielsen Norman Group, "Wizards: Definition and Design Recommendations", 2017, https://www.nngroup.com/articles/wizards/ (supporting: Rosala, "Task Analysis", 2020, https://www.nngroup.com/articles/task-analysis/)
- **Check:** Reconstruct the implied goal and decompose it into subtasks (informal hierarchical task analysis). Compare against the captured order: does any screen demand data the user could not yet have (e.g., shipping method before address)? Are navigation labels descriptive of what comes next rather than generic Next/Previous? Is the enforced order justified by dependencies rather than arbitrary?
- **Pass:** Order matches the task decomposition; no step depends on later information; forward labels describe the next step. / **Partial:** Order is workable but one step is misplaced or labels are generic. / **Fail:** A step requires unavailable information or the sequence forces obvious backtracking.
- **Applies:** multi
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Budiu article (fetched) covers enforced sequential ordering, self-sufficient steps, and descriptive forward/back labels; Rosala's task-analysis article (fetched) supplies the goal-to-subtask decomposition used as the comparison baseline.

### UF-12 Completion feedback
- **Standard:** The flow ends with an explicit, plain-language confirmation of the outcome plus a sensible next step.
- **Source:** Aurora Harley / Nielsen Norman Group, "Visibility of System Status (Usability Heuristic #1)", 2018, https://www.nngroup.com/articles/visibility-system-status/ (supporting: Rosala, "Status Trackers and Progress Updates: 16 Design Guidelines", 2019, https://www.nngroup.com/articles/status-tracker-progress-update/)
- **Check:** On the final screen (or a standalone confirmation screen): verify a success statement in user language (not jargon like "fulfilled"), a summary of what was accomplished (order number, saved item), what happens next (email, shipping, review timeline), and an onward action. Flag flows whose last captured screen is the action button with no confirmation state.
- **Pass:** Clear success message, outcome summary, and onward path. / **Partial:** Success stated but with jargon, no summary, or no next step. / **Fail:** No completion state — the user cannot tell whether the task succeeded.
- **Applies:** both
- **Platforms:** all
- **Needs:** screenshot-only
- **Provenance note:** Harley article (fetched) requires feedback for every interaction and transparency about backstage events (e.g., shipping progress); Rosala's status-tracker article (fetched) supplies the plain-language and latest-update-first guidance. Single-screen applicable only when the screen under audit is itself a confirmation state; otherwise multi.

## Flow-evaluation frameworks

1. **Cognitive Walkthrough** — Lewis, Polson, Wharton, Rieman (CHI 1990; Wharton et al. 1994), verified via Flaherty / NN/g, "Evaluate Interface Learnability with Cognitive Walkthroughs", 2022, https://www.nngroup.com/articles/cognitive-walkthroughs/. Inputs: a persona, a concrete task, and its action sequence; at each step the evaluator asks four questions (right goal? action noticeable? action associated with result? progress visible afterward?). Contribution to our audit: this is the natural engine for the multi-screen mode — the skill should ask the four questions at every screen transition, which directly powers UF-01, UF-09, and UF-12 and gives per-step failure locations for the annotated report.

2. **Seven stages of action / the two gulfs** — Norman (with Hutchins & Hollan, 1986; elaborated in The Design of Everyday Things), verified via Whitenton / NN/g, "The Two UX Gulfs", 2018, https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/. Every interaction must bridge a gulf of execution (can I figure out what to do?) and a gulf of evaluation (can I tell what happened?). Contribution: the pairing gives the single-screen inference rule — even one screenshot can be scored on both gulfs: execution-side (UF-01, UF-03, UF-08) and evaluation-side (UF-02, UF-06, UF-12). I did not find a fetchable primary page listing Norman's seven per-stage questions verbatim; the seven-question checklist itself is UNVERIFIED beyond the gulf structure this article confirms.

3. **Task analysis / hierarchical task analysis** — Rosala / NN/g, "Task Analysis", 2020, https://www.nngroup.com/articles/task-analysis/. Decomposes a goal into operations and subtasks, capturing step order and conditional paths. Contribution: gives the audit its expected sequence — before walking the screens, the skill should reconstruct the implied task hierarchy from the screen set, then diff the actual screen order against it (this is the procedure behind UF-11) and count steps as an efficiency signal.

4. **Journey mapping** — Gibbons / NN/g, "Journey Mapping 101", 2018, https://www.nngroup.com/articles/journey-mapping-101/. Five components: actor, scenario+expectations, phases, actions/mindsets/emotions, opportunities. Contribution: mostly above our altitude (multi-channel, emotional, longitudinal), but two pieces transfer — phase labeling (the report should name which journey phase each screen serves, exposing missing phases like "seek support") and the opportunities lane as the template for how flow findings are reported.

5. **User flows / wireflows** — Kaplan / NN/g, "User Journeys vs. User Flows", 2023, https://www.nngroup.com/articles/user-journeys-vs-user-flows/. Defines a user flow as the typical/ideal interaction steps for one task in one product, documented as wireflows pairing screens with system responses. Contribution: defines the scope boundary for the skill's flow step — a multi-screen input is treated as a candidate wireflow (minutes-scale, single product, no emotion tracking), which cleanly excludes journey-level concerns from scoring and tells the auditor what an ordered screenshot set is supposed to represent.

## Sources fetched

- https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/ — Whitenton 2018; gulf definitions, 1986 coinage, bridging guidance. Anchor for UF-01, framework 2.
- https://www.nngroup.com/articles/wizards/ — Budiu 2017; step display, enforced order, save-state, descriptive labels. Anchor for UF-02, UF-10, UF-11.
- https://www.nngroup.com/articles/progress-indicators/ — Sherwin 2014; duration thresholds for spinner vs percent-done, 3x-wait finding. Anchor for UF-06.
- https://www.nngroup.com/articles/user-journeys-vs-user-flows/ — Kaplan 2023; flow vs journey definitions, wireflows. Framework 5.
- https://www.nngroup.com/articles/error-message-guidelines/ — Neusesser & Sunwall 2023; adjacency, constructive fixes, input preservation. Anchor for UF-04.
- https://www.nngroup.com/articles/visibility-system-status/ — Harley 2018; heuristic #1, location and feedback examples. Anchor for UF-12, support for UF-02.
- https://www.nngroup.com/articles/user-control-and-freedom/ — Rosala 2020; emergency exits, cancel anywhere, back without data loss, no trapping. Anchor for UF-03, UF-08, support UF-10.
- https://www.nngroup.com/articles/empty-state-interface-design/ — Kaplan 2021; three empty-state guidelines. Anchor for UF-05.
- https://www.nngroup.com/articles/web-form-design/ — Whitenton 2016; top-10 form recommendations. Anchor for UF-07.
- https://www.nngroup.com/articles/journey-mapping-101/ — Gibbons 2018 (updated 2026); five components. Framework 4.
- https://www.nngroup.com/articles/task-analysis/ — Rosala 2020; HTA decomposition. Framework 3, support UF-11.
- https://www.nngroup.com/articles/cognitive-walkthroughs/ — Flaherty 2022; four walkthrough questions, attribution to Lewis/Polson/Wharton/Rieman. Anchor for UF-09, framework 1.
- https://www.nngroup.com/articles/status-tracker-progress-update/ — Rosala 2019; plain-language status, latest-update-first. Support for UF-12.
- https://ics.uci.edu/~dfredmil/ics104-WQ06/Chapter_4/CognitiveWalkthroughRev2006.pdf — fetched but returned unparseable scanned-PDF binary; could not be used for citation.
- https://www.usabilitybok.org/cognitive-walkthrough/ — HTTP 403; not usable.

## Rejected/uncertain

- **Wharton, Rieman, Lewis & Polson 1994 chapter as direct citation** — the UCI-hosted PDF fetched but was image-encoded and unreadable, and Usability BoK returned 403. The four questions are therefore cited via the fetched NN/g page, which itself attributes them to the 1994 chapter. A saved PDF exists in the session tool-results dir and could be OCR'd in a later milestone if direct citation is wanted.
- **Norman's seven per-stage design questions (verbatim checklist)** — no fetchable primary located; only secondary blogs surfaced. The two-gulf structure is verified via NN/g; the seven-question list itself is marked UNVERIFIED and was not used as a criterion source.
- **Streamlined Cognitive Walkthrough (Spencer 2000)** — known variant reducing the questions to two for engineering teams, but no primary source fetched, so excluded rather than cited from memory. UNVERIFIED.
- **Breadcrumb/back-button criterion (separate)** — dropped; orientation is covered by UF-02 and escape by UF-03, and breadcrumb styling/navigation-chrome consistency belongs to the consistency dimension per the scope guard.
- **Skeleton screens as a distinct criterion** — NN/g has a dedicated article, but it would fragment wait-state scoring; folded conceptually into UF-06 without citing the unfetched skeleton-screens page.
- **Single-screen "action clarity" (label comprehension, affordance strength)** — excluded per the scope guard: belongs to the usability dimension. UF-01 is deliberately restricted to which action advances the flow, not whether individual controls are well-designed.
- **Journey-map emotional lanes** — not auditable from screenshots; retained only as reporting inspiration in framework 4, not as a criterion.
# Platforms: classification signals + threshold divergence — agent output, pending Clemens review

Units note: 1 pt (iOS) ≈ 1 dp (Android) ≈ 1 CSS px (web) at 1x density; WCAG states 1pt = 1.333px (WCAG, Understanding SC 1.4.3).

## Threshold table

| Property | iOS (HIG) | Android (Material 3) | Web (WCAG + convention) |
|---|---|---|---|
| Touch target minimum | 44×44 pt hit region — "As a general rule, a button needs a hit region of at least 44x44 pt" (HIG, Buttons); visionOS 60×60 pt | 48×48 dp (~9mm physical) — "consider making touch targets at least 48 x 48dp" (M3, Foundations > Designing > Structure "Target sizes") | 24×24 CSS px, Level AA — WCAG 2.2 SC 2.5.8 Target Size (Minimum); 44×44 CSS px only at Level AAA — SC 2.5.5 Target Size (Enhanced) |
| Absolute minimum control size (visual) | iOS/iPadOS 28×28 pt (default 44×44 pt); macOS min 20×20 pt (default 28×28 pt); watchOS 44/28; tvOS 66/56; visionOS 60/28 — control-size table (HIG, Accessibility "Mobility") | No separate visual minimum; icon may be 24dp within 48dp target — "an icon may appear to be 24 x 24dp, but the padding surrounding it comprises the full 48 x 48dp touch target" (M3, Designing > Structure) | No normative visual minimum; SC 2.5.8 exceptions: spacing, equivalent, inline, user-agent, essential (W3C, Understanding 2.5.8) |
| Mouse/pointer target | macOS default 28×28 pt, min 20×20 pt (HIG, Accessibility control-size table) | 44×44 dp — "Consider making pointer targets minimums 44 x 44dp" (M3, Designing > Structure) | Same 24px AA floor; SC 2.5.8 applies to all pointer inputs (W3C, Understanding 2.5.8) |
| Spacing between targets | ~12 pt padding around bezeled elements, ~24 pt around non-bezeled visible edges (HIG, Accessibility "Mobility"); visionOS button centers ≥60 pt apart (HIG, Buttons > visionOS) | ≥8 dp between targets — "targets separated by 8dp of space or more" (M3, Designing > Structure "Target spacing") | No standalone spacing SC; spacing exception = non-intersecting 24px-diameter circles centered on each undersized target (WCAG 2.2 SC 2.5.8) |
| Body text default | 17 pt iOS/iPadOS; 13 pt macOS; 16 pt watchOS; 29 pt tvOS; 17 pt visionOS (HIG, Typography "Ensuring legibility" table; same table on HIG Accessibility) | Body Large 16 (sp on Android); Body Medium 14 — scale base is 14: "Major Second type scale with 14 as its key base size" (M3, Type scale & tokens) | 16 px browser default ("browser's font-size... default value of 16px" — MDN font-size; "The default for modern web browsers is 16px" — M3 type-scale page). Convention, not a WCAG requirement |
| Minimum text size | 11 pt iOS/iPadOS; 10 pt macOS; 12 pt watchOS/visionOS; 23 pt tvOS (HIG, Typography legibility table) | Smallest scale token: Label Small 11 / Body Small 12 (M3, baseline type-scale tokens) | None normative in WCAG. Text must resize to 200% (SC 1.4.4 — UNVERIFIED this session, cited from memory) |
| Body text contrast | 4.5:1 up to 17 pt; 3:1 at 18 pt+; 3:1 for any bold text (HIG, Accessibility contrast table) | Follows WCAG; active/inactive nav icons ≥3:1 vs container (M3, Navigation bar guidelines) | 4.5:1 normal, 3:1 large text = ≥18 pt (~24px) or ≥14 pt bold (~18.5px); no rounding — 4.499:1 fails (WCAG 2.2 SC 1.4.3, Understanding) |
| Primary nav location | iPhone: tab bar floats above content at bottom; iPadOS: tab bar near top, convertible to sidebar (HIG, Tab bars) | Navigation bar at bottom, full window width, mobile/tablet only; nav rail on leading edge for medium+ windows (M3, Navigation bar / Navigation rail guidelines) | Header/banner landmark containing navigation landmark (ARIA landmark roles, quoted on M3 structure page). Top-header convention itself: UNVERIFIED against a single canonical source |
| Nav item count | No hard number in current HIG; "use the appropriate number of tabs," avoid overflow More tab; customizable iPad tab bars: "aim for a default list of five or fewer" (HIG, Tab bars) | Nav bar: 3–5 destinations ("Navigation bars provide access to three to five destinations"); collapsed rail: 3–7; 5+ or 2+ hierarchy levels → drawer/expanded rail (M3, nav-bar / nav-rail / nav-drawer guidelines) | No standard. UNVERIFIED |
| Back navigation | App-provided Back button in top toolbar + edge-swipe shortcut: "people expect to find a Back button in a top toolbar... many apps also offer a shortcut gesture — such as swiping from the side" (HIG, Gestures) | System-level back with predictive preview (Android Developers, Predictive back design). Which edges (both L/R): UNVERIFIED on fetched page | Browser back button/gesture is user-agent-provided; no in-page back required. UNVERIFIED as a formal source |
| Desktop layout nav | macOS: sidebar/toolbar conventions (HIG Tab bars: "No additional considerations for macOS") | Explicit: "Don't use navigation bars for desktop layouts. Instead, use a navigation rail or tabs" (M3, Navigation bar > Adaptive design) | Header nav / sidebar; landmark roles as above |

## Classification signals

Buckets: mobile app (iOS) / mobile app (Android) / mobile web / desktop web / desktop app / responsive pair.

- **Aspect ratio (W/H):** 0.42–0.52 portrait → phone-class (modern iPhones 393/852≈0.46, 402/874≈0.46, 440/956≈0.46; older 375/667≈0.56 — extend to 0.56 for legacy). 0.70–0.80 → tablet portrait (834/1194≈0.70, 768/1024=0.75, 1024/1366≈0.75). ≥1.3 landscape → desktop-class (16:10 = 1.6, 16:9 ≈ 1.78) or tablet landscape.
- **Exact logical dimensions** (verified against HIG Layout device table): 393×852 (iPhone 16/15/14 Pro), 402×874 (iPhone 17/17 Pro/16 Pro), 440×956 (17/16 Pro Max), 420×912 (iPhone Air), 430×932 (16 Plus/15 Pro Max), 390×844 (16e/14/13), 375×812 (X/XS/11 Pro), 360×780 (12/13 mini), 375×667 (SE 4.7"), 320×568 (SE 4"); iPads: 1024×1366, 1032×1376, 834×1194/1210, 820×1180, 810×1080, 768×1024, 744×1133. A screenshot at exactly 2x/3x these px values (e.g. 1179×2556) is a device screenshot; at 1x it's likely a Figma frame.
- **Figma frame presets** (UNVERIFIED — Figma does not publish dimensions in help docs; iPhone values corroborated by Apple's device table): iPhone presets track device pt sizes; Android Compact 412×917, Android Medium 700×840, legacy Android 360×800; Desktop 1440×1024, MacBook Air 1280×832, MacBook Pro 14" 1512×982, generic 1440×900/1280×800. Treat non-device round sizes (1440×1024) as "desktop web design frame."
- **Status bar:** iOS — time top-left, cellular/Wi-Fi/battery top-right, Dynamic Island/notch centered, home-indicator bar at bottom. Android — time top-left, icons top-right, punch-hole cutout, gesture pill or 3-button nav at bottom. Presence of either → native mobile or mobile web (not desktop).
- **Browser chrome:** iOS Safari — rounded URL pill at bottom (default) or top; Android Chrome — omnibox at top. Any URL bar + status bar → mobile web. Desktop: tab strip + URL bar + window controls (traffic lights top-left / Windows controls top-right) → desktop web. Window chrome without URL bar → desktop app.
- **Nav-pattern cues:** floating/translucent bottom tab bar with SF-Symbols-style icons, grouped inset lists, back chevron top-leading, large title → iOS app. Bottom nav bar with pill-shaped active indicator, filled-vs-outlined icon swap, FAB above the bar, ripple states, Roboto/Google Sans → Material/Android. Left rail with vertical icon+label stack → Material medium+ window. Header logo + horizontal links + footer, cookie banner, underlined links → web.
- **Widget cues:** iOS switches/segmented controls/action sheets vs Material FAB/snackbar/exposed dropdowns vs browser-styled selects/checkboxes.
- **Responsive pair rule:** two screenshots showing the same content/brand/URL where one width ≥1024 (logical) and the other ≤480, with reflowed (not merely scaled) layout → classify as "responsive pair"; audit each against its own column (desktop web + mobile web) plus consistency between them.
- **Ambiguity meriting the one clarifying question:** phone-sized screenshot with no status bar and no browser chrome (cropped or Figma frame) — cannot distinguish native app vs mobile web. Ask: "Will this ship as a native app (iOS/Android) or as a mobile website/PWA?" Secondary ambiguity: iOS-style UI at Android dimensions (or vice versa) — ask which platform ships first. Default if unanswered: audit against WCAG 2.2 AA (24px floor) but flag anything under 44/48 as platform risk.

## Divergence brief

- Target minimums genuinely disagree: 44×44 pt (HIG) vs 48×48 dp (M3 — which itself notes "iOS recommends 44 x 44dp") vs 24×24 CSS px at WCAG AA (44px is AAA-only). A 32px button passes a web AA audit but fails both native conventions — verdict must be platform-conditional.
- HIG's 2025 accessibility table reframes 44 pt as the *default* control size with a 28×28 pt *minimum*, and macOS defaults to 28×28/min 20×20 — desktop-app audits should not import the 44pt rule; M3's mouse equivalent is 44 dp pointer targets. Same control, three different pass thresholds by input modality.
- Spacing rules differ in kind: M3 gives a flat ≥8 dp between targets; HIG gives asymmetric padding guidance (~12 pt bezeled, ~24 pt non-bezeled); WCAG has no spacing SC — spacing only functions as an escape hatch for undersized targets (24px circle test). An audit can only score "spacing" numerically on Material.
- Body-text anchors differ: 17 pt (iOS) vs 16 sp Body Large on a 14-based scale (Android) vs 16 px web browser default. 14px body on the web reads as sub-convention; 14 sp on Android is spec-sanctioned — identical rendered size, opposite verdicts.
- Primary-nav placement flips by platform: bottom floating tab bar is correct on iPhone but M3 explicitly forbids its equivalent on desktop ("Don't use navigation bars for desktop layouts") and iPadOS now puts the tab bar near the *top* — bottom-nav is a finding on some platforms and idiomatic on others.
- Item-count rules: M3 is normative (bar: 3–5; "Don't use a navigation bar for fewer than three destinations. Instead, use tabs."; rail: 3–7). Current HIG gives no number — only "avoid overflow tabs" and "five or fewer" for customizable iPad tab bars. A 6-tab bottom bar fails Material outright but is only a soft warning under HIG.
- Back navigation: iOS apps must render their own Back button (top toolbar) with edge-swipe supplement; Android back is system-owned (gesture + predictive back), so a missing on-screen back affordance is *not* a defect on Android; web relies on browser back. Never penalize "no back button" without platform context.
- M3's Expressive update deprecated the navigation drawer ("no longer recommended... use an expanded navigation rail") — hamburger-drawer Android apps now diverge from current spec; no analogous deprecation in HIG or web practice. Apple's contrast table exempts *all* bold text at 3:1, more lenient than WCAG 1.4.3 (bold only counts as large at ≥14 pt) — for contrast, WCAG is the stricter and safer rubric on every platform.

## Sources fetched

- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html — SC 2.5.8, Level AA, 24×24 CSS px + 5 exceptions.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html — SC 2.5.5, Level AAA, 44×44 CSS px + 4 exceptions.
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html — SC 1.4.3: 4.5:1 / 3:1 large text; large = 18 pt (~24px) or 14 pt bold (~18.5px); no rounding.
- https://developer.apple.com/design/human-interface-guidelines/layout (rendered in browser) — safe areas; full device logical-dimension table; size classes.
- https://developer.apple.com/design/human-interface-guidelines/typography (rendered) — default/minimum text sizes per platform (17/11 iOS, 13/10 macOS, 16/12 watchOS, 29/23 tvOS, 17/12 visionOS); Dynamic Type tables.
- https://developer.apple.com/design/human-interface-guidelines/accessibility (rendered) — control-size table (44 default / 28 min iOS), 12 pt/24 pt spacing guidance, contrast table, 200% text enlargement.
- https://developer.apple.com/design/human-interface-guidelines/buttons (rendered) — "hit region of at least 44x44 pt — in visionOS, 60x60 pt"; visionOS 60 pt center spacing.
- https://developer.apple.com/design/human-interface-guidelines/tab-bars (rendered) — iOS bottom floating bar; iPadOS top/sidebar-adaptable; overflow More tab; "five or fewer" for customizable tab bars.
- https://developer.apple.com/design/human-interface-guidelines/gestures (rendered) — Back button in top toolbar + side-swipe shortcut.
- https://m3.material.io/foundations/designing/structure (rendered) — 48×48 dp touch targets (~9mm), 44 dp pointer targets, 8 dp target spacing, "iOS recommends 44 x 44dp" note; ARIA landmark roles.
- https://m3.material.io/styles/typography/type-scale-tokens (rendered) — full baseline scale: Display 57/45/36, Headline 32/28/24, Title 22/16/14, Body 16/14/12, Label 14/12/11; Major Second scale, base 14.
- https://m3.material.io/components/navigation-bar/guidelines (rendered) — bottom placement, 3–5 destinations, mobile/tablet only, "Don't use navigation bars for desktop layouts", FAB above bar.
- https://m3.material.io/components/navigation-rail/guidelines (rendered) — leading edge, collapsed 3–7 items, medium+ windows, never rail+bar simultaneously.
- https://m3.material.io/components/navigation-drawer/guidelines (rendered) — deprecated in Expressive update in favor of expanded rail.
- https://developer.mozilla.org/en-US/docs/Web/CSS/font-size — browser default font size 16px.
- https://developer.android.com/design/ui/mobile/guides/patterns/predictive-back — predictive back definition; gesture insets.
- https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma — confirms preset categories exist but publishes no dimensions.

## Unverified/failed

- https://m3.material.io/foundations/accessible-design/accessibility-basics — 404; content moved to /foundations/designing/structure (fetched there).
- https://developer.android.com/design/ui/mobile/guides/patterns/navigation — 404; back-navigation sourced via predictive-back page instead.
- Android back gesture edge specifics (either edge) — not stated on the fetched page; UNVERIFIED.
- Figma frame-preset names and dimensions — not published in Figma help docs; iPhone preset values corroborated only via Apple's device table. All Figma-specific sizes UNVERIFIED.
- A canonical primary source for "web primary nav belongs in a top header" — only indirect ARIA-landmark support; UNVERIFIED as formal standard.
- WCAG SC 1.4.4 Resize Text (200%) — cited from memory in the table; Understanding page not fetched by this agent (NOTE assembler: the accessibility agent DID fetch it — see accessibility.md sources — so this cell can be marked verified at assembly).
- Current HIG contains no explicit "3–5 tabs" rule (verified absent from the Tab bars page) — any audit criterion citing "HIG says 3–5 tabs" would be outdated; the numeric 3–5 rule is Material-only.
# Critique practice (finding/fix wording rules) — agent output, pending Clemens review

## Principles

1. **Critique measures a design against its objectives, not the reviewer's taste.** Connor defines critique as focused analysis of "how a design is or isn't achieving certain goals," distinct from gut-reaction feedback and from approval-driven review. (Adam Connor & Aaron Irizarry, UIE Brainsparks interview "Discussing Design: The Art of Critique," 2012, https://archive.uie.com/brainsparks/2012/07/13/adam-connor-aaron-irizarry-discussing-design-the-art-of-critique/) — *Implication: every finding must name the objective it evaluates against; no judgment may appear without a stated goal.*

2. **Of the three forms of feedback — reaction, direction, critique — only critique is analysis.** The book's framework: reaction-based feedback is visceral and driven by the giver's expectations; direction-based feedback is bare instruction toward the giver's preferred solution; critique applies critical thinking to whether elements achieve the design's objectives (what is the objective, which elements relate, are they effective, why). (Connor & Irizarry, *Discussing Design*, O'Reilly 2015 — framework verified via Stephen P. Anderson, "Three Forms of Feedback...", 2025, https://stephenanderson.medium.com/three-forms-of-feedback-and-my-thoughts-on-design-critique-665179ce17a5, and the 2012 UIE author interview above) — *Implication: audit wording must never be a bare adjective ("cluttered") or a bare command ("make it blue"); each finding must traverse objective → element → effective/not → why.*

3. **A finding is only legitimate if grounded in an established principle, never preference.** NN/g's expert-review guidance: a design element "should never be designated a usability problem because the reviewer personally doesn't like it"; each issue should cite the heuristic or research source violated and explain why it is a problem. (Aurora Harley, "UX Expert Reviews," NN/g, 2018, https://www.nngroup.com/articles/ux-expert-reviews/) — *Implication: every finding carries a criterion/heuristic citation; anything uncitable is dropped or labeled an observation, not a finding.*

4. **Useful feedback describes the effect on the user's task, not the artifact's looks.** NN/g contrasts harmful phrasing ("Yikes… that layout!", "I would have done it differently!") with phrasing tied to goals, e.g. asking how a layout helps users accomplish their task quickly. (Sarah Gibbons, "Design Critiques: Encourage a Positive Culture to Improve Products," NN/g, 2016, https://www.nngroup.com/articles/design-critiques/) — *Implication: the impact clause of a finding is written about the user ("users scanning for X will…"), never about the pixels alone.*

5. **Severity is a composite judgment — frequency × impact × persistence (plus market impact) — reported on one simple scale.** Nielsen combines how often the problem occurs, how hard it is to overcome, and whether it repeatedly bothers users into a single 0–4 rating (cosmetic → catastrophe), and warns ratings from a single evaluator are "too unreliable to be trusted." (Jakob Nielsen, "Severity Ratings for Usability Problems," NN/g, 1994, https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/) — *Implication: the audit rates each finding by explicitly reasoning through frequency, impact, and persistence, outputs one combined severity level, and hedges it as an estimate (single-evaluator caveat).*

6. **Conversation, not command: fixes give a direction and rationale, not a decree.** Gibbons: "Commands, or directives, can very quickly ruin the exact purpose of the critique"; Connor deliberately defers solutions during critique; Harley recommends pairing each issue with a clear recommendation plus real examples — multiple examples, to avoid implying a single "best way." (Gibbons 2016; Connor & Irizarry 2012; Harley 2018 — URLs above) — *Implication: a fix suggestion states the direction and the principle it restores ("increase contrast of X to separate it from Y"), optionally with 1–2 example patterns — never a full prescriptive redesign.*

7. **Intent must be established before evaluation.** Berkun: bad critics assume "one universal and objective measure" of quality; good critics first ask what the creator's intentions and tradeoffs were — "Good criticism serves one purpose: help creators make better choices." (Scott Berkun, "How to Give and Receive Criticism," essay #35, 2004, https://scottberkun.com/essays/35-how-to-give-and-receive-criticism/) — *Implication: when the audit infers the interface's objective (unstated by the user), it must say so and mark dependent findings as conditional on that inference.*

8. **Anchor judgments in conditional, goal-referenced phrasing.** Berkun's critique format replaces absolutes ("this sucks and it's ugly") with goal-conditioned statements — if the goal is to feel friendly, black and flaming red doesn't convey that — and scopes each session to a few explicit questions so it doesn't drift into brainstorm. (Scott Berkun, "How To Run a Design Critique," essay #23, 2003, https://scottberkun.com/essays/23-how-to-run-a-design-critique/) — *Implication: template findings as "If [objective], [element] works against it because [principle]"; the report opens by declaring its scope and the questions it assessed.*

9. **Name what works, not only what fails.** Berkun: good critics spend energy on both strengths and flaws; the d.school's "I Like, I Wish, What If" format leads with positives and phrases requests as first-person wishes rather than accusations, making feedback "reflective, iterative, and conversational" rather than punitive. (Berkun 2004, URL above; Stanford d.school method as reproduced by Harvard GHELI, https://repository.gheli.harvard.edu/repository/14053/) — *Implication: each audited screen/criterion section includes at least one strengths line, and wishes/fixes are framed as improvement direction, not fault attribution.*

10. **Acknowledge tradeoffs.** Berkun: fixing one problem may create vulnerabilities elsewhere, and multiple valid perspectives exist on any design matter. (Berkun 2004, URL above) — *Implication: when a suggested direction could hurt another criterion (e.g. density vs. discoverability), the fix text names the tradeoff instead of presenting the change as free.*

## Finding-wording template

One finding =

1. **Observation** — neutral description of the concrete element and its location ("The primary CTA and the destructive delete action share identical button styling in the header"). No adjectives of taste. *(Principles 2, 4)*
2. **Criterion violated** — the named rubric criterion plus its cited source ("violates: action differentiation — Nielsen heuristic #5 / reference file X"). *(Principles 1, 3)*
3. **User impact, conditioned on objective** — "If the goal is [stated/inferred objective], users doing [task] will [consequence]"; flag when the objective was inferred rather than given. *(Principles 4, 7, 8)*
4. **Severity** — one level from a simple scale, justified in one clause by frequency (how many users/how often), impact (recoverability), persistence (one-time vs. recurring); worded as an estimate. *(Principle 5)*
5. **Suggested direction** — the direction of change plus the principle it restores, optionally one or two example patterns; explicitly not a redesign, and naming any tradeoff the change introduces. *(Principles 6, 10)*
6. Per section, at least one **"what's working"** item precedes the findings list. *(Principle 9)*

Justification: steps 1–3 are exactly the Discussing Design critical-thinking chain (objective → element → effective? → why) fused with NN/g's evidence rule; step 4 operationalizes Nielsen's composite severity; steps 5–6 implement conversation-not-command and strengths-balance.

## Sources fetched

- https://www.nngroup.com/articles/design-critiques/ — Gibbons (NN/g, 2016): scope, agreed objectives, conversation-not-command; harmful vs. useful phrasing examples.
- https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ — Nielsen (NN/g, 1994): frequency/impact/persistence (+ market impact), 0–4 scale, multi-evaluator reliability.
- https://www.nngroup.com/articles/ux-expert-reviews/ — Harley (NN/g, 2018): findings grounded in cited principles, severity per issue, clear recommendation, multiple real examples.
- https://archive.uie.com/brainsparks/2012/07/13/adam-connor-aaron-irizarry-discussing-design-the-art-of-critique/ — Connor & Irizarry author interview (2012): critique defined vs. feedback and design review; goals as centering tool; defer solutions.
- https://scottberkun.com/essays/35-how-to-give-and-receive-criticism/ — Berkun (2004): four bad-critic assumptions; intent, tradeoffs, strengths-and-flaws balance.
- https://scottberkun.com/essays/23-how-to-run-a-design-critique/ — Berkun (2003): goal-conditioned phrasing; scoped questions; critique evaluates, brainstorm generates.
- https://stephenanderson.medium.com/three-forms-of-feedback-and-my-thoughts-on-design-critique-665179ce17a5 — Anderson (2025): secondary verification of the book's reaction/direction/critique framework and critical-thinking questions.
- https://repository.gheli.harvard.edu/repository/14053/ — Harvard GHELI reproduction of the Stanford d.school "I Like, I Wish, What If" method card (I-statements, positives-first).

## Not found/unverified

- **Direct excerpt of *Discussing Design* (O'Reilly 2015) text** — no free author-published excerpt fetchable. Book-specific claims (three forms of feedback; critical-thinking questions) rest on the 2012 author interview (fetched) plus Anderson's 2025 secondary summary, which agree with each other; treat exact book wording as unverified.
- **Original Stanford d.school method-card PDF** — could not be text-extracted; method verified only via the Harvard GHELI reproduction.
- Berkun's criticism essay is now numbered #35, not #23 as commonly linked — the /essays/23-how-to-give-and-receive-criticism/ URL 404s; #23 is "How To Run a Design Critique."
- No IDEO-published critique-format page was located within search budget; nothing IDEO-specific is cited.
