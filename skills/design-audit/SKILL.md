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

**Honest-fallback rule:** if a step below points to a reference file that does not
exist yet, stop and tell the user that part of the audit is not installed yet
(this plugin is under construction, milestone by milestone). Never improvise
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

### Step 1 — Classify platform & context

<!-- placeholder: filled in M2c (references/platforms.md) -->

Per screen, classify as mobile app (iOS/Android) / mobile web / desktop web /
desktop app / responsive pair using `references/platforms.md`, and record which
convention set (Apple HIG, Material 3, web) and threshold values apply. Infer
audience and product type. At most one clarifying question for ambiguous cases.
The classification and assumptions go in the report header.

### Step 2 — Audit, one dimension at a time

<!-- placeholder: filled in M2b/M2c (references/usability.md, visual-design.md,
accessibility.md, consistency.md, user-flow.md) -->

For each dimension: load that dimension's reference file, evaluate every criterion
against every screen, record verdict (pass/partial/fail/N-A) + evidence +
approximate coordinates for visual findings, then unload and move to the next
dimension. Resolve platform-dependent thresholds via Step 1. Prefer measured checks
(DOM/Figma data) over visual estimation when available.

### Step 3 — Score

<!-- placeholder: filled in M3 (references/scoring.md) -->

Apply the scoring math from `references/scoring.md`: pass = 1, partial = 0.5,
fail = 0, N/A excluded from the denominator; per-dimension scores; weighted
0–100 overall; grade band.

### Step 4 — Markdown scorecard in chat

<!-- placeholder: filled in M3 -->

Emit the scorecard as chat markdown: per-dimension tables
(criterion ID | standard | source | 🟢/🟡/🔴 | reasoning), dimension subtotals,
weighted overall + grade, and Top-3 priorities.

### Step 5 — Annotated HTML report

<!-- placeholder: filled in M4 (assets/report-template.html,
assets/findings.schema.json, scripts/build_report.py) -->

Write `findings.json` (validated against `assets/findings.schema.json`), run
`scripts/build_report.py` to produce a single self-contained HTML report, verify
marker placement in the browser pane, and offer to publish it as an Artifact.

### Step 6 — Flow branch

<!-- placeholder: filled in M5 -->

Single screen: evaluate single-screen flow criteria and suggest 3–5 adjacent flows
to examine next. Multi-screen: additionally evaluate cross-screen criteria
(continuity, state persistence, navigation logic, progress) and list missing flows
(error/empty/loading/cancel states the set implies but doesn't show).
