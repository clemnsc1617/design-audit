# Scoring — worked example (hand-checkable)

Moved out of `references/scoring.md` so the skill doesn't load the full arithmetic
every run. This is the recompute-by-hand check for the §1–§5 rules. Never loaded
by the skill.

## Worked example

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

