# Visual design criteria (VD) — 12 criteria

Dimension scope: hierarchy, layout/grid/alignment, typography quality,
spacing/whitespace, Gestalt grouping, imagery quality. Not here: contrast ratios
and text-size accessibility minimums (accessibility.md), content relevance and
decoration-as-noise (US-14), icon labels (US-10), cross-screen token discipline
(consistency.md).

Where a Partial/Fail band edge is our operationalization rather than a sourced
number, the criterion says so — report wording must not present those edges as
literature values.

Verdicts: pass = 1, partial = 0.5, fail = 0, N/A excluded from the denominator.

---

### VD-01 Visual hierarchy and scan order
- **Standard:** The most important element attracts the eye first; emphasis descends in order of intended importance (scale, value/contrast, grouping, whitespace, placement).
- **Source:** Kelley Gordon, "Visual Hierarchy in UX: Definition", NN/g, 2021.
- **Check:** Blur/squint the screenshot; record the 2–3 dominant elements; compare against the screen's purpose. Unblurred, trace eye-landing order vs importance. (Figure-ground failures — background swallowing foreground — surface here too.)
- **Pass:** blurred view surfaces exactly what matters; clear 1st–2nd–3rd order. **Partial:** hierarchy exists but a secondary/decorative element competes with the primary. **Fail:** near-uniform blur (no focal point) or the dominant element is irrelevant to the purpose.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### VD-02 Emphasis economy
- **Standard:** Emphasis is rationed: ~≤3 size levels, ~≤3 emphasis treatments, palette reading as ~2 primary + 2 secondary hues. (NN/g rules of thumb, not empirical thresholds — treat as heuristic bands.)
- **Source:** Gordon, "5 Principles of Visual Design in UX", NN/g, 2020; Gordon 2021 (above).
- **Check:** Count visible size steps, strong-emphasis treatments (bold, accent, badge, oversized), and UI hue families (exclude photography). Per-screen judgment; token/scale discipline across screens is CO-06's job.
- **Pass:** within bands; emphasized items actually stand out. **Partial:** 4–5 sizes or treatments, or one stray accent hue. **Fail:** >5 sizes, emphasis everywhere (nothing stands out), or an uncontrolled palette.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma preferred for exact counts)

### VD-03 Proximity grouping
- **Standard:** Space encodes relatedness: within-group gaps visibly smaller than between-group gaps; related pairs read as units without boxes.
- **Source:** Aurora Harley, "Proximity Principle in Visual Design", NN/g, 2020.
- **Check:** Sample 3–5 label/control or heading/content pairs; compare partner-gap vs nearest-unrelated-gap (measure when DOM/Figma available). Check no action sits buried among unrelated controls; long forms/lists chunked.
- **Pass:** every sampled pair closer to its partner; content chunked. **Partial:** one ambiguous pairing. **Fail:** 2+ false groupings, uniform spacing everywhere, or a control nearer a stranger group than its own.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma preferred)

### VD-04 Similarity coding
- **Standard:** Same function = shared visual traits; different function = visibly different. Link/accent color reserved for interactive elements; primary CTA distinct from secondary actions.
- **Source:** Harley, "Similarity Principle in Visual Design", NN/g, 2020.
- **Check:** Inventory same-function families (nav links, cards, buttons, tags); verify internal uniformity within this screen. Hunt false similarity: non-interactive text in link color, promos styled as content, secondary buttons identical to primary. (Cross-screen uniformity is CO-01.)
- **Pass:** families uniform; accent only on interactive; primary/secondary distinguishable at a glance. **Partial:** one false-similarity or one drifting family member. **Fail:** multiple false similarities or indistinguishable primary/secondary actions.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### VD-05 Container restraint (common region)
- **Standard:** Borders/background containers appear only where whitespace can't do the grouping; each encloses genuinely related items; no clutter-nesting; no full-width band reading as a false end-of-page.
- **Source:** Harley, "The Principle of Common Region", NN/g, 2020.
- **Check:** Count containers; verify each earns its keep; flag box-in-box with one child, chrome/content confusion, false floors near the fold.
- **Pass:** every container motivated; no false floor. **Partial:** one redundant container or heavy-but-legible banding. **Fail:** boxes around everything, mixed-content containers, or a false floor above real content.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### VD-06 Grid and alignment
- **Standard:** Content sits on a consistent column grid (12-col desktop norm, fewer at smaller sizes); block edges share keylines; nothing lives in gutters/margins.
- **Source:** Gordon, "Using Grids in Interface Designs", NN/g, 2022.
- **Check:** Trace major left edges; count distinct alignment positions in the content area; flag stragglers aligning to nothing; confirm even outer margins. (Item uniformity inside collections is CO-09.)
- **Pass:** edges resolve to few shared keylines; margins even. **Partial:** 1–2 slightly off-grid elements or one self-aligned section. **Fail:** 3+ unexplained alignment positions, ragged edges across sections, content in gutters.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma preferred for pixel-exact edges)

### VD-07 Spacing rhythm and whitespace
- **Standard:** Spacing follows a consistent rhythm (8px base grid is the cited convention) with adequate micro whitespace (lines, paragraphs, neighbors) and macro whitespace (around blocks); no crowding.
- **Source:** Gordon, "Using Grids…", NN/g, 2022 (8px); IxDF, "The Power of White Space", 2015/2020 (micro/macro; qualitative).
- **Check:** Sample 6–10 gaps; equivalent relationships get equal spacing, values cluster on one scale (measure when DOM/Figma available). Scan for crowding: text touching edges, abutting targets, dense clusters without breathing room. (Token adherence across screens is CO-07.)
- **Pass:** consistent rhythm, everything breathes. **Partial:** 1–2 arbitrary gaps or one crowded region. **Fail:** effectively random gaps or widespread crowding.
- **Applies:** both · **Platforms:** all · **Needs:** DOM/Figma preferred; crowding judgeable from screenshot

### VD-08 Body text line length
- **Standard:** Body measure 45–90 characters per line (Butterick); 45–75 satisfactory, ~66 ideal (Bringhurst); 40–50 for multi-column.
- **Source:** Butterick, *Practical Typography*, "Line length"; Rutter (Bringhurst), *Elements of Typographic Style Applied to the Web* §2.1.2, 2005.
- **Check:** Average character count across 2–3 full lines of the widest body paragraph (~2–3 alphabets per line as shortcut). Skip paragraphs whose measure is forced by a narrow viewport rather than designed.
- **Pass:** 45–90 (40–50 multi-column). **Partial:** ~35–45 or ~90–105. **Fail:** <~35 or >~105. (35/105 edges are our operationalization.)
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### VD-09 Line spacing (leading)
- **Standard:** Body line-height 120–145% of type size.
- **Source:** Butterick, *Practical Typography*, "Line spacing".
- **Check:** line-height ÷ font-size from DOM/Figma; or baseline-to-baseline ÷ apparent size on a 3+-line paragraph. Body text only — heading leading is not covered by the source.
- **Pass:** 1.2–1.45. **Partial:** 1.0–1.2 or 1.45–1.7. **Fail:** <1.0 (collisions) or ≥~1.8. (Out-of-band edges are our operationalization.)
- **Applies:** both · **Platforms:** all · **Needs:** DOM/Figma preferred

### VD-10 Body type size
- **Standard:** Web/desktop body text 15–25px (reading-comfort norm, distinct from accessibility minimums). Native mobile: judge against platform defaults via `platforms.md` (iOS 17pt body default / min 11pt; Material Body Large 16sp / smallest tokens 11–12).
- **Source:** Butterick, *Practical Typography*, "Point size"; platform values per `platforms.md` (HIG Typography; M3 type scale).
- **Check:** Computed body font-size from DOM/Figma; from pixels only when the scale factor is known.
- **Pass:** in the platform's comfort band. **Partial:** 13–15px or 25–30px web (or one step under platform default). **Fail:** <~13px or >~30px web running text (or below platform minimum). (Web partial/fail edges are our operationalization.)
- **Applies:** both · **Platforms:** per `platforms.md` · **Needs:** DOM/Figma preferred

### VD-11 Typeface restraint
- **Standard:** One or two families, each with a stable role; "Most documents can tolerate a second font. Few can tolerate a third." (Butterick)
- **Source:** Butterick, *Practical Typography*, "Mixing fonts".
- **Check:** Count families (exclude logos, embeds, icon fonts); verify role mapping; no family-mixing within a paragraph/element.
- **Pass:** 1–2 families, consistent roles. **Partial:** 3 with clearly distinct roles. **Fail:** 4+, or 3 without role separation, or mixing inside one element.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma to distinguish families from weights)

### VD-12 Imagery quality
- **Standard:** Prominent images are informative (product detail, real people, data) rather than stock filler — users scrutinize informative images and skip decorative ones — and render cleanly (no upscaling, stretching, pixelation).
- **Source:** Jakob Nielsen, "Photos as Web Content", NN/g, 2010; Harley, "Icon Usability", NN/g, 2014 (icon salience note).
- **Check:** Classify each image informative vs decorative/stock; check rendering quality at display size. (Icon labeling is US-10; decoration-as-noise competition is US-14 — here only informativeness and rendering.)
- **Pass:** prominent images informative and clean. **Partial:** one large stock/filler image, rest fine. **Fail:** multiple stock images in prime space or visibly degraded imagery.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

---

## Severity guidance (annotation only — never in score math)

Rate findings 0–4 by frequency × impact × persistence. Visual-design failures are
persistent (every view) but usually recoverable, so impact drives the split: a
missing focal point or false floor that hides content trends 3; a stray accent hue
or slightly loose leading trends 1. Reserve 4 for hierarchy failures that actively
misdirect users away from the screen's purpose.

---

Last reviewed: 2026-07

Sources: Gordon, "Visual Hierarchy in UX" (2021), "5 Principles of Visual Design"
(2020), "Using Grids in Interface Designs" (2022), nngroup.com · Harley, "Proximity"
(2020), "Similarity" (2020), "Common Region" (2020), "Icon Usability" (2014),
nngroup.com · Nielsen, "Photos as Web Content" (2010) · Butterick, *Practical
Typography* (practicaltypography.com): "Line length", "Line spacing", "Point size",
"Mixing fonts" · Rutter, webtypography.net §2.1.2 (2005), citing Bringhurst ·
Soegaard/IxDF, "The Power of White Space" (2015/2020). Full provenance:
`research/criteria-research.md`.
