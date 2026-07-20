# Weighting memo — how the design-audit scorecard should aggregate to 0–100

Status: **DECIDED — Clemens, 2026-07-19.** Adopted: the recommendation (Option A —
equal dimension weights, 20% × 5, redistributed 25% × 4 for single-screen audits;
Nielsen 0–4 severity rated per finding for prioritization/annotation only, never
folded into the score; grade bands A 90–100 / B 75–89 / C 60–74 / D 40–59 / F < 40,
framed as directional conventions). Option C (AHP elicitation) stays available as a
later upgrade if M6's dress rehearsal shows equal weights misranking real audits.
This decision is binding input for `references/scoring.md` (M3).

## The decision needed

The audit produces per-criterion pass (1) / partial (0.5) / fail (0) verdicts in five
dimensions (usability, visual design, accessibility, consistency, user flow), N/A
excluded from denominators. Two open choices:

1. **Weights** — how the five dimension scores combine into one 0–100 overall.
2. **Grade bands** — how that number maps to a letter grade.

## How this was researched and verified

Deep-research pass (2026-07-18/19): fan-out searches → claim extraction from fetched
sources → adversarial 3-voter verification panels. Usage limits killed ~2/3 of the
panels, so remaining claims were verified directly in-session against each source
(W3C-style: quote located in the fetched page/PDF). Verification depth is labeled
per claim:

- **[panel]** — survived a 3-0 adversarial verification panel.
- **[verified]** — quote/number located directly in the fetched source this session.
- **[title-only]** — paper's existence/title/venue confirmed; specific figures not
  independently re-checked (extracted by one researcher from a successful fetch).

## What the literature actually says

### 1. Nielsen severity & heuristic-evaluation practice

- Nielsen's severity rating is a **single 0–4 ordinal scale per problem** (0 = not a
  problem … 4 = usability catastrophe) — a prioritization device, not a
  dimension-weighted score. [panel] (Nielsen, NN/g 1994)
- Severity combines **frequency + impact + persistence** (+ market impact). [panel]
- **Single-evaluator severity ratings are "too unreliable to be trusted"**; Nielsen
  recommends the mean of ≥3 evaluators. [panel] Empirically, inter-rater agreement on
  severity is weak-to-moderate: κ = 0.580 / 0.216 / 0.336 across rater groups in a
  published clinical HE. [verified] (PMC6436963)
- Published HE practice aggregates with **unweighted descriptive statistics** (mean/SD
  of severity per heuristic) — no weighted 0–100 composite. [verified] (PMC9090311)
- Herr, Müller & Gross (CHI 2016): practitioners collapse severity to one rating
  despite its acknowledged multidimensionality [panel]; a decomposed multi-factor
  scale beat Nielsen's single scale on accuracy (mean deviation 23.4 vs 28.1 vs 39.3;
  H(2)=49.6, p<.001) [panel]; and — key for us — **"the weighting of individual
  factors might differ for different product areas and purposes and should be
  investigated"** — i.e., factor weighting is an open research question. [verified,
  quote extracted from the paper PDF]

### 2. How standardized instruments weight things

- **SUS**: 10 items, each 0–4, sum × 2.5 → 0–100. **Equal item weights by
  construction.** [verified] (Lewis & Sauro, HCII 2009, PDF fetched)
- Lewis & Sauro 2017, from >9,000 questionnaires: **"treat the SUS as a unidimensional
  measure of perceived usability, and no longer routinely compute Usability and
  Learnability subscales."** [verified, ACM abstract] — the field's flagship
  instrument deliberately refuses sub-dimension weighting.
- Weighted (factor-loading) scores correlated r = .993/.997 with unweighted scores —
  differential weighting adds complexity for almost no information. [title-only]
  (Lewis & Sauro 2009)
- **UMUX** (4 items, equal-weight rescale to 0–100; parallel analysis supports one
  latent factor) and **UMUX-Lite** (2 items, equal-weight linear rescale, calibrated
  to SUS by regression 0.65x + 22.9) follow the same pattern. [title-only]
  (Finstad 2010; Lewis, Utesch & Maher CHI 2013)

### 3. AHP / weighted scorecards applied to heuristics

- Talero-Sarmiento et al. 2024 (Big Data Cogn. Comput. 8:69): argues equal /
  question-count-derived weighting (Granollers) "may not align with the relevance of
  heuristics in specific systems"; an expert (Usability Testing Leader) derives
  weights via AHP pairwise comparisons — producing **strongly unequal weights
  (18.06% → 1.45%, consistency ratio 0.044)**; applying them moved the mean score
  78.12% → 80.97% and cut between-evaluator SD 8.94 → 6.61. Weights are framed as
  **per-system, per-phase (context-dependent)**; "pre-configured set[s] of weights
  for various software families" are future work, and reliance on expert judgment
  "may limit the inclusiveness" of the process. [verified, full text via browser]
- Corroborating precedent: a 2025 IJHCI paper integrates Nielsen's 10 heuristics with
  AHP — weights from ~30 experts' pairwise comparisons, validated against 200 user
  surveys with strong correlation [verified, abstract]; Benaida 2023 (Soft Computing)
  does AHP-weighted heuristics for UI design. [title-only]
- Critique: rank reversal — rankings changing when an alternative is added/removed —
  afflicts AHP and also simple additive weighting (the weighted-sum model under any
  fixed-weight scorecard), Borda–Kendall, TOPSIS, DEA. [title-only] (Wang & Luo 2009,
  "On rank reversal in decision analysis", Math. Comput. Modelling — title/DOI
  verified; method list not independently re-checked. Less damaging for us than for
  MCDM selection: an audit scores one artifact, it doesn't rank alternatives.)

### 4. Fixed vs context-dependent weights

No fetched source supports **universal fixed unequal weights**. The three positions
actually found: (a) equal weights by construction (SUS/UMUX family); (b)
context-dependent weights elicited per system by an expert via AHP; (c) open research
question (Herr et al.). What the literature does NOT contain: any published,
validated weight set for dimensions like ours that we could cite and adopt.
A hard-coded "usability 30%, accessibility 25%…" would be **invented, not sourced**.

### 5. Grade bands

- **Sauro–Lewis curved grading scale** (SUS-specific, percentile-anchored): A+ 84.1+,
  A 80.8–84.0, A− 78.9–80.7, B+ 77.2–78.8, B 74.1–77.1 … C 65.0–71.0, D 51.7–62.6,
  F below 51.7. Mean SUS = 68 = 50th percentile; the curve deliberately matches the
  normal distribution of a large SUS database. [verified] (measuringu.com)
- **Bangor, Kortum & Miller 2009** (JUS 4(3), 114–123): added a 7-point adjective
  scale to ~1,000 SUS surveys, r = 0.822 with SUS [verified, ACM abstract]; anchor
  values ≈ OK 51, Good 71, Excellent 85+ [verified via measuringu recap; exact table
  values title-only]; they also read SUS against the traditional US school scale
  (90s=A, 80s=B, 70s=C…) — under which the average product grades a C/D. [title-only]
- Implication: **percentile-curved bands require a norm database we don't have.** Our
  instrument (pass/partial/fail against strict criteria) has no score distribution
  yet; borrowing SUS's curve would be false precision. Criterion-referenced
  (absolute) bands with disclosed conventionality are the honest option, with
  Bangor's school-scale reading as precedent for letter-grading a 0–100 usability
  number at all.

## Options

### Option A — Equal dimension weights (default 20% each)

Overall = mean of the five dimension scores. Single-screen audits: flow's weight
redistributed equally (25% × 4), per PLAN.

- **Basis:** instrument-construction practice (SUS/UMUX equal weights,
  unidimensionality recommendation [verified]); HE practice aggregates unweighted
  [verified]; differential weighting ≈ no information gain (r=.993/.997
  [title-only]); no citable weight set exists to do otherwise (§4).
- **Weaknesses:** treats a contrast failure and a line-length quibble's *dimensions*
  as equal stakes; ignores that dimensions have different criteria counts (mitigated:
  each dimension is normalized to 100 before averaging); genuinely different products
  (a medical form vs a portfolio) get identical emphasis.

### Option B — Severity-weighted scoring (no dimension weights)

Each failed/partial criterion gets a Nielsen 0–4 severity (frequency × impact ×
persistence); the overall score is deduction-based, weighted by severity rather than
by dimension.

- **Basis:** severity methodology is the best-verified machinery in this space
  [panel ×3]; Herr et al. show decomposed judgments are *more* accurate [panel].
- **Weaknesses:** single-evaluator severity is explicitly untrustworthy [panel], and
  this skill IS a single evaluator — the exact failure mode Nielsen warns about;
  score becomes opaque (can't recompute from the scorecard table alone); run-to-run
  variance increases (each finding adds a judged multiplier).

### Option C — AHP-elicited fixed weights (one-time expert session)

Clemens (as the expert) does pairwise comparisons across the five dimensions once; I
compute the eigenvector weights + consistency ratio (the MDPI paper's exact
procedure, CR < 0.1 acceptance); the derived weights are hard-coded into scoring.md
with the derivation documented.

- **Basis:** published, peer-reviewed precedent for AHP-weighted heuristic scoring
  [verified ×2]; produces defensible, documented, *non-arbitrary* unequal weights;
  the MDPI result suggests weighting can reduce between-evaluator variance
  [verified].
- **Weaknesses:** the literature frames such weights as context-dependent (per
  system/phase) [verified], so one fixed set contradicts its own methodology when the
  skill audits everything from portfolios to checkout flows; single-expert
  elicitation inherits the inclusiveness caveat the MDPI authors themselves state
  [verified]; weighted-sum models carry known aggregation critiques [title-only].

### Option D — Context-dependent weight presets

Different weight sets per product type/platform (e.g., accessibility ↑ for public
services, flow ↑ for transactional apps), selected during Step 1 classification.

- **Basis:** directionally what Herr et al. and the MDPI authors point at
  [verified] — weights *should* vary by product area.
- **Weaknesses:** no published preset values exist for any product taxonomy (§4) —
  every number in every preset would be invented, multiplying arbitrariness by the
  number of presets; harder to explain in a report; preset choice becomes a new
  failure mode stacked on platform classification.

## Recommendation

**Option A for the score, plus Option B's machinery as annotation, with Option C
available as an upgrade if you want unequal weights.**

Concretely:

1. **Equal weights (20/20/20/20/20; 25×4 single-screen) compute the 0–100 overall.**
   It is the only scheme every verified source family actually practices, it is
   transparent (a reader can recompute it from the scorecard), and it avoids
   inventing numbers the research says don't exist. The report states the weighting
   in one line and shows unweighted per-dimension scores alongside (per PLAN), so
   nothing is hidden.
2. **Every finding still carries a Nielsen 0–4 severity** (reasoned through
   frequency/impact/persistence) — used for the Top-3 priorities and annotation
   colors, NOT folded into the score. This keeps the best-verified prioritization
   tool where it's reliable (ordering findings) and out of where it's unreliable
   (single-evaluator numeric aggregation). The report carries the single-evaluator
   caveat verbatim.
3. **If you want unequal weights**, we run the 10-comparison AHP session (Option C)
   at any point; scoring.md then documents the derivation and CR. I'd hold off until
   M6's dress rehearsal shows equal weights actually misranking real audits.

### Grade bands (recommended)

Criterion-referenced bands, framed in the report as directional conventions (not
percentile claims): **A 90–100 · B 75–89 · C 60–74 · D 40–59 · F < 40** (PLAN's
bands). Rationale: letter-grading a 0–100 usability score has published precedent
(Bangor et al. 2009 [verified]); a Sauro–Lewis-style curve is unavailable to us
without a norm database for this instrument [verified reasoning, §5]; and PLAN's
thresholds are stricter than school bands in the middle (C starts at 60, D at 40),
which suits a strict-rubric audit where partials drag scores down. The scoring.md
will state explicitly that bands are conventions and that ±5 run-to-run variance
means adjacent grades are not meaningfully different (per PLAN's risk note).

## Sources

- Nielsen, "Severity Ratings for Usability Problems", NN/g, 1994. nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/ [panel]
- Herr, Müller & Gross, "An Empirical Comparison of Severity Rating Scales…", CHI 2016. cml.hci.uni-bamberg.de PDF [panel + verified]
- Khowaja et al. (clinical HE), PMC9090311 [verified]; Cho et al. (kappa study), PMC6436963 [verified]
- Lewis & Sauro, "The Factor Structure of the System Usability Scale", HCII 2009. measuringu.com PDF [verified: scoring; title-only: r=.993/.997]
- Lewis & Sauro, "Revisiting the Factor Structure of the SUS", JUS 12(4), 2017. dl.acm.org/doi/10.5555/3190867.3190870 [verified]
- Finstad, "The Usability Metric for User Experience", Interact. Comput. 22(5), 2010 [title-only]
- Lewis, Utesch & Maher, "UMUX-LITE: When There's No Time for the SUS", CHI 2013 [title-only]
- Talero-Sarmiento, Gonzalez-Capdevila, Granollers, Lamos-Diaz & Pistili-Rodrigues, "Towards a Refined Heuristic Evaluation…", Big Data Cogn. Comput. 8(6):69, 2024. doi.org/10.3390/bdcc8060069 [verified]
- "Fundamental Usability Evaluation in Visualization: Integrating Nielsen's Principles and the AHP", IJHCI, 2025. doi.org/10.1080/10447318.2025.2467455 [verified, abstract]
- Benaida, "Developing and extending usability heuristics evaluation for user interface design via AHP", Soft Computing, 2023 [title-only]
- Wang & Luo, "On rank reversal in decision analysis", Math. Comput. Modelling, 2009. doi.org/10.1016/j.mcm.2008.06.019 [title-only]
- Bangor, Kortum & Miller, "Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale", JUS 4(3), 2009. dl.acm.org/doi/10.5555/2835587.2835589 [verified: abstract, r=0.822; title-only: exact table values]
- Sauro, "5 Ways to Interpret a SUS Score", MeasuringU. measuringu.com/interpret-sus-score/ [verified]

Last reviewed: 2026-07
