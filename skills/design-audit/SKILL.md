---
name: design-audit
description: Run a design audit of an interface — score and grade it against cited usability, visual-design, accessibility, consistency, and user-flow criteria, and produce an annotated HTML report. Use when the user asks to audit, score, grade, or formally evaluate a design/screen/UI from a screenshot, URL, Figma link, or prototype recording. Not for casual feedback ("what do you think?") — that's design-critique territory.
---

# Design Audit

Perform a rigorous, research-backed audit of an interface. Every criterion, threshold,
and weight traces to a published source (cited in `references/`). The audit produces:

1. A **markdown scorecard** in chat — per-dimension tables with verdicts, reasoning,
   and sources, plus a weighted 0–100 overall score and grade.
2. A **self-contained annotated HTML report** — executive summary, scorecard tables,
   screenshot(s) with numbered markers and fix cards, and a flow section.

Five dimensions: **usability, visual design, accessibility, consistency, user flow.**

**Progressive disclosure rule:** load exactly one reference file at a time, use it,
move on. Never load all references up front.

**Honest-fallback rule:** if a step's reference file, template, or script is
missing or fails, say so and deliver everything up to that point. Never improvise
criteria, thresholds, weights, or scores that the reference files don't provide.

## Workflow

### Step 0 — Input detection & capture

Read `references/input-capture.md` and follow its procedure for the input type
(screenshot files, URL/localhost/HTML, Figma link, or video/prototype recording).

The outcome of this step, regardless of input type:

- **N ordered screenshots on disk** (the "screens"), each ≤1568px on the long edge,
  in a session working directory.
- **Optional structured data** alongside each screen when the source provides it
  (DOM measurements for URLs, Figma node geometry/variables for Figma links).
- A recorded note of the input type and any capture limitations (e.g. a capture tool
  was unavailable and the user supplied manual screenshots).

If the user gave no input at all, ask for one — accept a screenshot path, a URL,
a Figma link, or a screen recording. Ask whether multiple screens form an ordered
flow; order matters for Step 6.

**Pasted image with no file path:** you can still audit it, and the report needs
it as a file. Offer to find it in the usual places (Downloads, Desktop, the
project) rather than making the user hunt, confirm the specific file before using
it, and never let a missing file block the report — see input-capture.md's
pasted-image rule for the exact wording and the permission boundary.

### Step 1 — Classify platform & context

Read `references/platforms.md`. Per screen, work down its classification procedure
(exact dimensions → aspect ratio → status bar → browser chrome → nav patterns →
responsive-pair rule) and record:

- **Bucket** (mobile app iOS/Android / mobile web / desktop web / desktop app /
  responsive pair) + the deciding signals, verbatim enough to be checkable.
- **Convention set** now in force (HIG / Material 3 / web) — this resolves every
  platform-dependent threshold in Step 2.
- **Inferred audience and product type** (one line each, labeled as inferred).

Ask **at most one** clarifying question, only in the cases platforms.md enumerates
(native-vs-web ambiguity; style/dimension mismatch; OS-indeterminate native app).
If unanswered, apply its stated default (WCAG floor + platform-risk flags) and say
so. Everything recorded here goes in the report header as classification +
assumptions.

### Step 2 — Audit, one dimension at a time

Fixed order: `usability.md` → `visual-design.md` → `accessibility.md` →
`consistency.md` → `user-flow.md`. For each: load that one file, evaluate every
criterion against every screen, then move on. Never load two dimension files at
once.

Record per criterion:
- **Verdict** — pass / partial / fail / N/A, judged strictly against the file's
  Pass/Partial/Fail anchors. Every N/A carries a reason from scoring.md §1's list.
- **Evidence** — the concrete observation (what, where, measured value when the
  check is measured). Prefer DOM/Figma-measured values over visual estimation
  whenever Step 0 captured them. **For raw screenshots, use `scripts/measure.py`
  to get exact numbers — but only for the findings that hinge on one** (contrast
  AC-01/AC-02, target size AC-07, grid keylines VD-06). Read everything else
  visually; do not measure what a number won't change. On a device screenshot,
  pass `--scale` (e.g. 3 for a 3× capture) so pixels convert to points. Do not
  re-implement pixel sampling inline — the shipped script is the tool.
- **Coordinates** — for visual findings: screen id + approximate x%/y% (region box
  when the issue covers an area). These feed the Step 5 annotations.
- **Severity** — for every fail/partial: 0–4 per the file's severity-guidance
  section, with a one-clause frequency/impact/persistence justification.
- **Advisories** — a separate channel for "worth a designer's eye, not a defect":
  deliberate patterns serving a purpose (e.g., fade-truncation before Show more),
  findings conditional on an *inferred* objective/audience, and
  ecosystem-convention cases the criterion marks advisory (e.g., tier-2 icons).
  Advisories never change a verdict or the score; they surface in Step 4's watch
  list, phrased as observations to monitor, not changes to make.

Thresholds with platform variants resolve through the Step 1 classification and
`platforms.md` — never from memory. Honor the cross-reference rules (one flaw,
one criterion — see accessibility/consistency files) and each criterion's
Needs/Assessability tags. Responsive pairs: audit each screen against its own
column, plus cross-breakpoint parity checks under consistency.

### Step 3 — Score

Read `references/scoring.md` and apply it exactly: pass 1 / partial 0.5 / fail 0,
N/A excluded; dimension = 100 × points/applicable (one decimal); equal weights
with the redistribution rule (single-screen: flow evaluated but unscored, 25% × 4;
any zero-applicable dimension drops out, 100/k each); overall rounded to integer;
grade from the band table. Show the arithmetic — the scorecard must let the reader
recompute the overall by hand. Never fold severity into the score.

### Report voice (applies to Step 4 chat text and the Step 5 report)

Write for a busy designer who should get each point at a glance. Not an essay.

- **Finding pattern:** state → problem → number → threshold it misses → source.
  E.g. "Unselected labels (the category tabs and the whole bottom nav) sit at a
  2.12:1 contrast ratio, less than half the 4.5:1 that text this size needs
  (WCAG 1.4.3)."
- **Lead with the fact, not a windup.** Cut filler adjectives (confident,
  disciplined, thoughtful, clean, elegant, seamless) and any sentence that only
  restates the obvious. If a summary sentence could describe any decent screen,
  delete it.
- **Punctuation:** don't reach for the em dash. Use a colon to introduce, "e.g."
  in parentheses for examples, and commas. An occasional em dash is fine; a
  paragraph built on them is not.
- **Inferred priority/audience/goal:** when a finding depends on one, say so in
  the finding itself and give advice that helps whichever way it turns out — not
  a verdict that assumes your read is right (see the $500-promo example: if the
  promo is the campaign's primary funnel the order is deliberate; if the goal is
  getting this account to trade, it can't until it verifies). This is the same
  discipline as the advisory channel, applied inside a scored finding.

### Step 4 — Chat summary (short)

The chat carries only the frame; the full scorecard, priorities, and watch list
live in the HTML report (Step 5), which keeps chat output — and tokens — small.
Emit, in order:

1. **Input** — type and source.
2. **Platform + deciding signals** — the bucket, convention set, and the signals
   that decided it.
3. **Assumptions** — everything inferred (audience, product type, any inferred
   priority), stated plainly.
4. **What this audit could not measure** — the capture limitations and why.
5. **Overall** — integer score and grade, with the scoring.md §4 framing
   (directional, ±5, adjacent grades not meaningfully different), and the
   coverage line (measured N of 63).

Then point to the report for the per-criterion tables, the priorities, and the
watch list. Do not reproduce those in chat.

### Step 5 — Annotated HTML report

1. **Write `findings.json`** in the session working directory, following the
   contract in `assets/findings.schema.json` exactly: all Step 1–4 outputs (meta,
   platform + signals, dimensions with scored/weight/score, full scorecard incl.
   N/A reasons, advisories, flow) plus located **findings** — marker id, screenId,
   criterionId, severity, title, evidence, fix direction, source, and coordinates
   as percentages (x/y point, or x/y/w/h region box — prefer region boxes; visual
   estimation is ±3–5%, use DOM/Figma geometry when Step 0 captured it).
2. **Build:** `python3 scripts/build_report.py findings.json -o report.html`
   (add `--no-inline` beyond ~10 screens). The script validates first and fails
   loudly — fix the named field, don't bypass.
3. **Verify markers with `scripts/preview_markers.py findings.json`:** it draws
   every marker onto the screenshot and writes one `*-markers.png` per screen.
   Read that image once, check each marker sits on its subject ("this area", not
   "this pixel"), nudge coordinates in findings.json, and rebuild. This replaces
   the browser-pane loop for the common case and costs one image Read instead of
   a screenshot-per-nudge cycle. Only open `report.html` in the browser when you
   need to check something the flat image can't show (leader lines, hover-linking,
   a layout regression).
4. **Offer** to publish the report as an Artifact (user's call — never publish
   unprompted).

### Step 6 — Flow synthesis

Step 2 already produced the user-flow verdicts (via `references/user-flow.md`,
including its walkthrough engine for ordered sets). Step 6 turns them into the
flow outputs — the report's flow section and the `flow` object in findings.json.

**Single screen** (flow evaluated, unscored — scoring.md §3):
- `observed`: 1–2 sentences on the interaction loop the screen supports.
- `suggestedNext`: 3–5 adjacent flows worth auditing next, inferred from the
  screen itself — where each primary action leads, and which error/empty/loading/
  confirmation states the screen references but doesn't show. Word each as a
  concrete audit target ("Cart (13 items) → checkout, including error and empty
  states"), not a vague theme.
- `missing`: leave empty — a single screen can't owe states to a sequence.

**Multi screen (ordered flow)** — user flow is the fifth scored dimension (20%):
- `observed`: the reconstructed task and how the sequence serves it (from the
  walkthrough: goal → step order → per-transition continuity).
- `missing`: states the sequence implies but never shows — error paths, empty
  states, loading, cancel/abandon routes, back-navigation behavior. Each entry
  names the screen pair that implies it ("payment → confirmation implies a
  declined-card path; not shown"). These are report suggestions, not scored
  verdicts.
- `suggestedNext`: flows adjacent to the audited one, same concreteness rule.

Flow outputs are conversation, not verdicts: no invented severities, no scores —
they answer "what would a design lead ask to see next?"
