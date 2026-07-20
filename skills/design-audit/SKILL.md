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

**Honest-fallback rule:** if a step below points to a file that does not exist yet
(currently the Step 5 report pipeline), tell the user that part is not installed
yet and deliver everything up to it. Never improvise criteria, thresholds,
weights, or scores that the reference files don't provide.

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
  whenever Step 0 captured them.
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

### Step 4 — Markdown scorecard in chat

Emit, in order:

1. **Header** — input type, platform classification + deciding signals,
   assumptions, capture limitations (what couldn't be measured and why).
2. **Per-dimension tables** — `ID | standard (short) | source | 🟢/🟡/🔴/⚪ |
   reasoning`, one row per criterion including N/As (⚪ + reason). Subtotal line
   under each: points / applicable → dimension score. Unscored dimensions say so
   ("evaluated, unscored — single-screen") and still list their verdicts.
3. **Overall** — the weighted-sum arithmetic written out, integer score, grade,
   and the mandatory framing from scoring.md §4 (directional, ±5, adjacent grades
   not meaningfully different).
4. **Top-3 priorities** — highest-severity findings (severity, criterion, one-line
   fix direction each), worded per the critique rules: observation → criterion →
   user impact → suggested direction, severities as estimates.
5. **Designer watch list** — the advisories: each as one line (observation +
   which criterion flagged it + why it's advisory rather than scored). Worded as
   "keep an eye on", never as a required change. Omit the section when empty.

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
3. **Verify markers in the browser pane:** open `report.html`, zoom to 2–3
   markers, compare against the screenshot; nudge coordinates in findings.json
   and rebuild until markers sit on their subjects ("this area", not "this
   pixel"). Also confirm leader lines and hover-linking work.
4. **Offer** to publish the report as an Artifact (user's call — never publish
   unprompted).

### Step 6 — Flow branch

<!-- placeholder: filled in M5 -->

Single screen: evaluate single-screen flow criteria and suggest 3–5 adjacent flows
to examine next. Multi-screen: additionally evaluate cross-screen criteria
(continuity, state persistence, navigation logic, progress) and list missing flows
(error/empty/loading/cancel states the set implies but doesn't show).
