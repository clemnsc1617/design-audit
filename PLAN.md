# Plan: `design-audit` — a standalone Claude Code plugin for design critiques

## Context

Clemens wants a reusable SKILL that performs rigorous, research-backed design audits of any interface. Existing skills (`design:design-critique`, `design:accessibility-review`, `ui-ux-pro-max`, `web-design-guidelines`) produce text-only scorecards or code-level findings; **none produce an annotated illustration**, none carry literature citations per criterion, and none are flow-aware. This plugin fills that gap.

**Decisions confirmed with Clemens:**
- **Standalone plugin** (own repo, installable via local marketplace) — not project- or user-scoped skills dir.
- **The HTML artifact is the full audit report**: heading → executive summary → score overview + per-dimension scorecard tables → annotated illustration(s) (screenshot + numbered markers + leader lines + fix text) → flow section. Publishable as an Artifact; the same scorecard also appears in chat as markdown.
- **Platform-aware**: the skill classifies each screen (mobile app / mobile web / desktop web / desktop app / responsive pair) and applies platform-specific guidelines (Apple HIG, Material, web conventions) — thresholds like touch-target size differ per platform.
- **Deep-research pass during the build** to compile a cited criteria corpus into `references/` — including the **dimension weights themselves**, which must be derived from published evaluation methodology (not guessed) and approved by Clemens.
- **Scoring = per-criterion pass/partial/fail + weighted 0–100 overall with grade bands.**
- **Per-milestone testing with Clemens**: every milestone ends with a concrete test the two of us run together before moving on.
- **A working agreement (CLAUDE.md) for the plugin repo**, adapted from the portfolio's — created and approved in M0 before any code.

## What gets built

### Plugin location & structure

Source lives at `/Users/clemnsc/Desktop/Vibe Coding/design-audit-plugin/` (sibling of the portfolio repo, own git repo):

```
design-audit-plugin/
├── .claude-plugin/
│   ├── plugin.json           # name, version, description, author
│   └── marketplace.json      # self-listing → repo doubles as local marketplace
├── README.md
├── CLAUDE.md                 # working agreement (M0)
├── research/
│   ├── criteria-research.md  # deep-research provenance (git-tracked, not loaded by skill)
│   └── weighting-memo.md     # weight-derivation options + recommendation, for Clemens's decision
└── skills/design-audit/
    ├── SKILL.md              # <500 lines, orchestration only
    ├── references/
    │   ├── usability.md        # ~14 criteria (Nielsen 10 heuristics, Laws of UX, Krug)
    │   ├── visual-design.md    # ~12 (Gestalt, NN/g hierarchy, typography norms)
    │   ├── accessibility.md    # ~12 (WCAG 2.2 AA, POUR-structured)
    │   ├── consistency.md      # ~10 (Nielsen #4, token discipline, Jakob's Law, HIG/Material)
    │   ├── user-flow.md        # ~10 (Norman action cycle, NN/g journeys, Discussing Design)
    │   ├── platforms.md        # platform classification rules + per-platform threshold table
    │   ├── scoring.md          # weights, math, grade bands, worked example
    │   └── input-capture.md    # per-input capture procedures
    ├── scripts/build_report.py       # findings.json + shots → self-contained annotated HTML
    ├── assets/
    │   ├── report-template.html      # annotation shell (markers, leader lines, themes)
    │   └── findings.schema.json
    └── evals/evals.json
```

**Local dev loop:** `claude plugin validate <path>` → `claude --plugin-dir <path>` (session-only) → once stable, `claude plugin marketplace add <path>` + `claude plugin install design-audit@design-audit-plugin`.

### Skill behavior (SKILL.md outline)

1. **Step 0 — Input detection & capture.** Dispatch on input type; normalize everything to *N ordered screenshots on disk* + optional structured data:
   - Screenshot file(s) → read directly. **URL / localhost / HTML file** → in-app browser (navigate, resize to 1280 desktop / 375 mobile, screenshot; `read_page` for DOM-measured a11y checks). **Figma link** → Figma MCP (`get_screenshot` per frame, `get_metadata` for frame order/bounding boxes, `get_variable_defs` for measured tokens). **Video/prototype recording** → ffmpeg keyframes. Downscale captures to ≤1568px long edge. Degrade gracefully if a capture tool is unavailable (ask for manual screenshots).
2. **Step 1 — Classify platform & context.** Per screen, classify as **mobile app (iOS/Android) / mobile web / desktop web / desktop app / responsive pair** using `references/platforms.md` (signals: aspect ratio, status bar, browser chrome, nav patterns; Figma frame presets; URL inputs captured at both 1280 and 375 count as a responsive pair). The classification selects which convention set applies (Apple HIG, Material 3, web) and which threshold values criteria use (e.g. touch targets: 44pt HIG / 48dp Material / 24px WCAG minimum). Also infer audience/product type; ≤1 clarifying question (e.g. ambiguous mobile-web vs native); record classification + assumptions in the report header.
3. **Step 2 — Audit one dimension at a time** (load one reference file, evaluate all its criteria, record verdict + evidence + coordinates, then next — progressive disclosure). Criteria with platform-dependent thresholds resolve them via the Step 1 classification; platform-inapplicable criteria are marked N/A (e.g. hover-state checks on mobile app screens). For responsive pairs, additionally check cross-breakpoint parity (content/feature parity, layout adaptation). Prefer *measured* checks (DOM/Figma data) over visual estimation when available.
4. **Step 3 — Score.** pass=1 / partial=0.5 / fail=0; N/A excluded from denominator. Dimension = 100×Σpoints/Σapplicable. **Weights: TBD — derived in the deep-research pass** (see below) from published evaluation methodology, then approved by Clemens; whatever they are, flow's weight is redistributed for single-screen audits, and `scoring.md` documents the derivation with citations. The report always shows unweighted per-dimension scores alongside the weighted overall so the weighting is transparent. Grade bands: A 90–100, B 75–89, C 60–74, D 40–59, F <40 (also subject to what grading-scale literature supports).
5. **Step 4 — Markdown scorecard** in chat: per-dimension tables (criterion ID | standard | source | 🟢/🟡/🔴 | reasoning), subtotals, weighted overall + grade, Top-3 priorities (matches design-critique conventions Clemens knows).
6. **Step 5 — Full HTML report.** Model writes `findings.json`; `build_report.py` fills the template → single self-contained HTML (base64-inlined images) structured as: **① heading** (title, date, input type, platform classification, assumptions) → **② executive summary** (overall score dial + grade, dimension bar chart, 2–3 sentence verdict, top-3 priorities) → **③ scorecard tables** (per-dimension, same content as the chat markdown) → **④ annotated screens** (markers + leader lines + fix cards) → **⑤ flow section**. Verify marker placement in the browser pane (zoom 2–3 markers, nudge coords, rebuild). Offer to publish as Artifact.
7. **Step 6 — Flow branch.** Single screen → evaluate single-screen flow criteria + output "flows to examine next" (3–5 inferred adjacent flows). Multi-screen → additionally evaluate cross-screen criteria (continuity, state persistence, navigation logic, progress) using screen order + output "missing flows" (error/empty/loading/cancel states the set implies but doesn't show).

### Criteria format (uniform block, per reference file)

Each criterion: `ID` (VD/CO/US/UF/AC prefix), `Standard`, `Source` (author/org + work + year), `Check` (concrete procedure), `Pass/Partial/Fail` anchors, `Applies` (single/multi/both), `Platforms` (all, or a subset like mobile-only/web-only, with per-platform threshold values where they differ), `Needs` (screenshot-only vs DOM/Figma data — enables honest N/A). ~58 criteria total. `references/platforms.md` holds the classification signals and one consolidated per-platform threshold table (touch targets, type minimums, nav conventions per HIG / Material 3 / web) so individual criteria reference it instead of duplicating numbers. Each file ends with "Last reviewed: YYYY-MM" + source list. `ui-ux-pro-max`'s `data/ux-guidelines.csv` (99 rows) is a mining source, but every borrowed check gets re-grounded to a primary source.

### Annotation mechanics

- **findings.json schema:** meta (title, date, input type, overall score, grade, summary text, assumptions), platform (per-screen classification + convention set applied), dimensions (id/weight/score), scorecard (per-criterion rows: id, standard, source, verdict, reasoning — drives the report's tables), screens (id/label/platform/image), findings ({id, screen, x%, y%, optional w/h region box, severity, criterionId, title, evidence, fix, source}), flow (observed/missing/suggested_next).
- **Template (full report shell):** heading block → executive summary (score dial, grade band, dimension bar chart, top-3 priorities) → per-dimension scorecard tables → annotated screens: per-screen section with screenshot + absolutely-positioned numbered markers (percent coords) + optional region rectangles on the left, finding cards on the right, SVG leader lines recomputed on resize, hover linking → flow section. Severity colors (fail red / partial amber / note green); light/dark themes.
- **build_report.py:** Python 3 stdlib only; validates findings against the schema; fails loudly.
- **Coordinate accuracy caveat:** visual estimation is ±3–5%; mitigate with region boxes > point markers, browser-pane verification loop, DOM-derived geometry for URLs, Figma node bounds for Figma.

### Deep-research pass (feeds the criteria)

One deep-research run answering: (1) the 10–15 most defensible, operationalizable criteria per dimension + the primary source stating each standard; (2) concrete numeric thresholds (4.5:1/3:1 contrast, WCAG 2.2 24px vs HIG 44pt vs Material 48dp targets, 45–75 char line length, Doherty threshold); (3) what critique-practice literature says separates actionable critique from opinion (shapes fix wording); (4) published frameworks for multi-screen flow evaluation; (5) which WCAG criteria are legitimately assessable from a static screenshot vs. requiring DOM/interaction; (6) **where platform guidelines diverge**: HIG vs Material 3 vs web conventions for navigation, touch/click targets, typography minimums, and gestures — the per-platform threshold table for `references/platforms.md`; (7) **how to weight the dimensions**: what published evaluation frameworks say about relative importance and aggregation — Nielsen's severity-rating methodology (frequency × impact × persistence), how heuristic-evaluation and expert-review practice aggregate findings, standardized instruments (SUS, UMUX) and their construction, weighted-scorecard/multi-criteria methods (e.g. AHP) and their known critiques, and whether the literature supports fixed weights at all vs. context-dependent ones. Deliverable: cited draft criterion blocks + threshold table + a **weighting recommendation memo** (options with evidence, one recommended scheme), kept in `research/`, edited into `references/` after Clemens approves.

## Milestones (each ends with a test Clemens runs with me; nothing advances without his sign-off)

| # | Milestone | Files | Test with Clemens (the gate) |
|---|---|---|---|
| M0 | Working agreement + repo init | CLAUDE.md (plugin repo), git init | Clemens approves the working-agreement draft (see section below) |
| M1 | Scaffold + SKILL.md skeleton | plugin.json, marketplace.json, SKILL.md, input-capture.md | `plugin validate` passes; Clemens opens a `--plugin-dir` session, types "audit this screenshot", confirms the skill triggers and asks for the right inputs |
| M2a | Deep research (criteria + **weights**) | research/criteria-research.md, research/weighting-memo.md | Clemens reads the criteria drafts + weighting memo; we discuss, he picks/adjusts the weighting scheme and cuts/keeps criteria |
| M2b | References batch 1 | usability.md, accessibility.md, visual-design.md | Clemens spot-reads ~5 criteria per file: standard clear? source real? rubric judgeable? |
| M2c | References batch 2 | consistency.md, user-flow.md, platforms.md | Same spot-read; plus Clemens supplies 3 screenshots of known platforms and we verify the classification rules bucket them correctly |
| M3 | Scoring + scorecard | scoring.md, SKILL.md steps 1–4 | Live test: Clemens picks one screenshot; we run the audit together; he judges whether verdicts and reasoning are fair, and hand-checks the math against scoring.md's worked example |
| M4 | Report pipeline | report-template.html, findings.schema.json, build_report.py | Live test: build a report from a fixture findings.json; Clemens reviews all 5 sections in the browser and judges marker accuracy and visual quality — his designer eye is the gate |
| M5 | Flow-awareness | SKILL.md step 6, template flow section, user-flow Applies flags | Live test: one single-screen run + one 3-screen run on Clemens's own screens; he judges whether the flow suggestions are ones a design lead would actually raise |
| M6 | Evals + shakedown | evals.json, README.md | Dress rehearsal on 3 real inputs spanning platforms (his portfolio URL desktop-web, his mobile Figma frames, a raw screenshot); Clemens scores the skill's usefulness; we iterate on his fix list until he'd use it on real work; then persistent install |

M4 (net-new, riskiest) lands after the scorecard already works, so the skill is useful even if annotation needs iteration.

## Working agreement (M0 — a CLAUDE.md in the plugin repo, drafted for Clemens's approval)

Adapted from the portfolio's; portfolio-specific rules (copy porting, asset slots, reference sites) swapped for skill-building equivalents:

- **Address me as Clemens.** Begin every reply with "Clemens".
- **Permission first** — propose the approach and wait for explicit approval before any change (code, files, commits, installs). Reading, inspecting, and researching to inform a proposal is fine.
- **Brief updates.** Short status notes and results over narration.
- **Finish a milestone, then pause** — each milestone ends with its "Test with Clemens" gate; never start the next milestone without sign-off on the current one.
- **Research-backed, never guessed** — every criterion, threshold, and weight in the skill traces to a cited source; Clemens approves the research digest before it becomes reference files.
- **Clemens tests as the user** — skill quality is judged by him running real audits on his own work, not by synthetic examples passing.
- **Report wording is reviewable** — templates and user-facing text in the skill's output get Clemens's review before shipping.
- **Small, reviewable commits** with clear messages. Git + GitHub.

## Risks

- **Marker precision:** "this area", not "this pixel" — region boxes + verification loop + DOM/Figma geometry.
- **Long pages:** capture per-viewport sections as separate screens, not one tall image; `--no-inline` flag beyond ~10 screens.
- **Score variance:** ±5 points run-to-run; rubric anchors with numeric thresholds; report frames scores as directional.
- **Platform misclassification** would apply the wrong threshold set (e.g. judging a mobile-web page against HIG). Mitigate with explicit classification signals in platforms.md, stating the classification in the report header, and the single allowed clarifying question for ambiguous cases.
- **Trigger collision** with design-critique/web-design-guidelines: description owns "audit / score / grade / annotated report"; M6 includes a trigger eval.
- **Staleness:** "Last reviewed" line per reference file; refresh is a per-file re-research task.

## Verification

Verification is the per-milestone "Test with Clemens" gates in the milestones table — every milestone ends with a joint test (trigger check, research review, live audits, report review in the browser pane, and the M6 dress rehearsal on three real inputs spanning platforms). Nothing advances without Clemens's sign-off, and M6 loops until he'd use the skill on real work.
