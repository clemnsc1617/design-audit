# Scoring — verdicts, weights, grades, severity

The complete scoring contract. Decided by Clemens 2026-07-19 after the weighting
research (`research/weighting-memo.md`); every rule here traces to that memo.

## 1. Verdicts

Per criterion, per audit: **pass = 1.0 · partial = 0.5 · fail = 0 · N/A = excluded.**

N/A is honest, never lazy — it requires a stated reason from one of:
- **Applies mismatch:** multi-only criterion on a single-screen audit (or vice versa).
- **Needs unmet:** criterion requires DOM/Figma data that wasn't available
  (accessibility.md Assessability tags; consistency.md measured-check rule).
- **Condition absent:** conditional criteria whose trigger state isn't captured
  (error state → US-08/AC-11; focus state → AC-09; empty container → UF-05;
  wait state → UF-06; destructive control → US-07; confirmation screen → UF-12).
- **Platform-inapplicable:** per `platforms.md` (e.g., on-screen back affordance
  on Android).

The scorecard prints every N/A with its reason — an N/A without a reason is a bug.

## 2. Dimension scores

For each dimension: **score = 100 × Σ points / Σ applicable criteria**, reported to
one decimal. A dimension with zero applicable criteria is **unscored** (dropped
from the overall, weight redistributed — §3), never shown as 0 or 100.

## 3. Weights and the overall score

**Equal weights.** Multi-screen audits: five dimensions × 20%. No dimension is
more important than another by fiat — the research found no citable basis for
fixed unequal weights (weighting-memo §4); severity handles importance per finding
(§5).

**Single-screen audits: user flow is evaluated but unscored.** Its single-screen
criteria (UF-01/02/03/08, plus conditionals) still get verdicts — they feed
findings and Step 6's suggestions — but the flow dimension drops out of the math
and the remaining four dimensions carry 25% each.

**General redistribution rule:** any unscored dimension (zero applicable criteria)
drops out and its weight spreads equally over the scored dimensions. With k scored
dimensions, each carries 100/k %.

**Overall = weighted mean of scored dimension scores, rounded to the nearest
integer.** Report both the unweighted per-dimension scores and the overall, plus
the arithmetic itself — the reader must be able to recompute the number from the
scorecard table alone.

## 4. Grade bands

| Grade | Overall |
|---|---|
| A | 90–100 |
| B | 75–89 |
| C | 60–74 |
| D | 40–59 |
| F | 0–39 |

Mandatory framing wherever a grade appears: these bands are **directional
conventions** (letter-grading a 0–100 usability score has precedent — Bangor,
Kortum & Miller 2009 — but no norm database underlies these particular cut
points), and run-to-run variance is roughly ±5 points, so **adjacent grades are
not meaningfully different**. A 74 vs a 76 is noise, not a verdict.

## 5. Severity (annotation only — never in the score)

Every fail and partial gets a Nielsen 0–4 severity: **0** not a problem ·
**1** cosmetic · **2** minor · **3** major · **4** catastrophe. Reason through
frequency (how many users, how often) × impact (recoverable?) × persistence
(once vs every time); each reference file's severity-guidance section calibrates
its dimension. Severity drives the Top-3 priorities and annotation colors.

It is NEVER folded into the 0–100 math (weighting-memo: single-evaluator severity
ratings are "too unreliable to be trusted" — Nielsen 1994 — and this audit is one
evaluator). Reports word severities as estimates and carry that caveat once.

## 6. Worked example (hand-checkable)

Hypothetical single-screen, desktop-web screenshot, no DOM data, no error/focus/
wait states captured, no destructive controls visible.

**Applicability:**
- Usability: 14 − 3 N/A (US-06 needs-DOM-partial → still judgeable visually, keep;
  US-07 no destructive control; US-08 no error state; US-11 kept — labels visible) = **11 applicable**
- Visual design: 12 − 0 = **12 applicable**
- Accessibility: 14 − 7 N/A (AC-04/05/14 DOM required; AC-09 no focus state;
  AC-11 no error state; AC-12/13 multi-only) = **7 applicable**
- Consistency: 12 − 4 N/A (CO-02 multi-only; CO-05/06/07 no DOM/Figma) = **8 applicable**
- User flow: single-screen → **evaluated, unscored**

**Verdicts → dimension scores:**

| Dimension | pass | partial | fail | points | applicable | score |
|---|---|---|---|---|---|---|
| Usability | 7 | 3 | 1 | 7 + 1.5 + 0 = 8.5 | 11 | 100×8.5/11 = **77.3** |
| Visual design | 8 | 3 | 1 | 9.5 | 12 | **79.2** |
| Accessibility | 4 | 2 | 1 | 5.0 | 7 | **71.4** |
| Consistency | 6 | 2 | 0 | 7.0 | 8 | **87.5** |
| User flow | (4 verdicts recorded, unscored) | | | — | — | — |

**Overall:** 4 scored dimensions → 25% each.
0.25 × (77.3 + 79.2 + 71.4 + 87.5) = 0.25 × 315.4 = 78.85 → **79 · Grade B**
(with the framing note: 79 sits within ±5 of the B/C boundary, so "high C / low B"
is the honest reading).

**Top-3** come from severity, not score: the accessibility fail (body-text
contrast 3.8:1, severity 3) outranks the visual-design fail (no focal point,
severity 2) even though visual design scored lower overall.

## 7. Reporting rules

- Show the math: points, applicable counts, redistribution, the weighted sum.
- Emoji key in tables: 🟢 pass · 🟡 partial · 🔴 fail · ⚪ N/A (with reason).
- State capture limitations next to the scores (what the audit could not measure
  and why) — scores are only as strong as the evidence class behind them.
- Never present the overall as more precise than it is: integer score,
  directional grade, ±5 variance note.

---

Last reviewed: 2026-07

Sources: decision + derivation in `research/weighting-memo.md` (equal weights:
SUS/UMUX construction precedent, Lewis & Sauro 2017 unidimensionality; severity:
Nielsen 1994 severity ratings; bands: Bangor, Kortum & Miller 2009 precedent with
curved-scale caveat per Sauro–Lewis). Criteria provenance:
`research/criteria-research.md`.
