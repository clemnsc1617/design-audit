# Accessibility criteria (AC) — 14 criteria, WCAG 2.2 Level AA

Dimension scope: WCAG 2.2 AA conformance signals, POUR-organized. Every criterion
carries an **Assessability** tag — the audit only scores what the available
evidence honestly supports; everything else is N/A with an explicit reason.

Standing disclosure (include in every report): SC 1.4.4 Resize Text, 1.4.10 Reflow,
2.1.1 Keyboard, 3.2.1/3.2.2 On Focus/On Input are **not statically assessable** and
are never scored; they're listed as "needs manual test." Units: 1pt = 1.333px
(WCAG); establish CSS-px scale from DOM viewport or Figma frame before measuring —
state the assumption if estimating from a raw screenshot.

Verdicts: pass = 1, partial = 0.5, fail = 0, N/A excluded from the denominator.

---

## Perceivable

### AC-01 Text contrast (SC 1.4.3, AA)
- **Standard:** Text ≥4.5:1 against background; ≥3:1 for large text (≥18pt / ≥14pt bold). No rounding — 4.499:1 fails.
- **Check:** Sample body text, secondary text, button labels, links, placeholders; ratio = (L1+0.05)/(L2+0.05). Text over images: sample the worst-case region. Exempt: inactive controls, decoration, logotypes.
- **Pass:** all sampled pairs meet threshold. **Partial:** only secondary/caption text fails, or failures within 0.3 where anti-aliasing muddies sampling. **Fail:** body text, labels, or primary actions below threshold. **Deliberate-pattern exception (Clemens ruling 2026-07):** low-contrast text that is a recognized disclosure device (fade-truncation teaser before a "Show more", scrim-faded preview) where the full-contrast content is one interaction away → **advisory**, not a verdict hit — unless the faded rendering is the content's only instance.
- **Applies:** both · **Platforms:** all (Apple's more lenient bold-text rule is ignored; WCAG is stricter and governs) · **Needs:** screenshot-only (DOM/Figma preferred for exact values) · **Assessability:** screenshot

### AC-02 Non-text contrast (SC 1.4.11, AA)
- **Standard:** Visual information required to identify UI components and states, and meaning-bearing graphics, ≥3:1 against adjacent colors.
- **Check:** Sample input borders/fills, checkboxes, toggles, icon buttons, state indicators (selected tab, toggle-on), chart elements. Boundaries need contrast only when no other cue identifies the control.
- **Pass:** all identification-critical visuals meet 3:1. **Partial:** isolated failures on non-primary controls, or another passing cue identifies the component. **Fail:** primary controls indistinguishable at 3:1 (e.g., pale input borders on white, no other cue).
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only · **Assessability:** screenshot

### AC-03 Use of color (SC 1.4.1, A)
- **Standard:** Color is never the only means of conveying information or distinguishing elements.
- **Check:** Hunt color-only patterns: hue-only links, red-only required/error fields, color-legend-only charts, status dots without text/shape. Mentally grayscale the screen.
- **Pass:** every color signal has a redundant cue. **Partial:** isolated color-only instances in secondary content. **Fail:** any primary signal is color-only.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only · **Assessability:** screenshot

### AC-04 Text alternatives (SC 1.1.1, A)
- **Standard:** Meaningful non-text content has purpose-equivalent text alternatives; decoration is hidden from assistive tech.
- **Check:** With DOM: audit img/SVG/canvas/icon fonts for non-empty, purpose-equivalent alt/aria-label; decorative images empty-alt or aria-hidden. With Figma: check alt-text annotations. Judge equivalence, not presence.
- **Pass:** all meaningful content covered, decoration suppressed. **Partial:** alternatives exist but some generic ("image", filename). **Fail:** meaningful images or icon-only controls lack alternatives.
- **Applies:** both · **Platforms:** all (web alt/ARIA; iOS accessibilityLabel; Android contentDescription) · **Needs:** DOM/Figma required · **Assessability:** DOM/Figma — N/A on raw screenshots

### AC-05 Structure and relationships (SC 1.3.1, A)
- **Standard:** Visually conveyed structure (headings, labels, lists, tables) is programmatically determinable.
- **Check:** With DOM: whatever looks like a heading/label/list/data table is marked up as one (h1–h6 in sane hierarchy, label/for, ul/ol, th+scope). Cross-reference against the screenshot.
- **Pass:** visual and programmatic structure match. **Partial:** mostly present, isolated gaps (one skipped level, one loose label). **Fail:** styled-text headings, unassociated labels, layout tables for data.
- **Applies:** both · **Platforms:** all · **Needs:** DOM/Figma required · **Assessability:** DOM/Figma — N/A on raw screenshots

### AC-06 Text spacing (SC 1.4.12, AA) — measured assessment + risk flags
- **Standard:** SC 1.4.12 requires no loss of content when users override to line height ≥1.5×, paragraph spacing ≥2×, letter spacing ≥0.12×, word spacing ≥0.16×. Shipping tighter values is *not* a failure by itself — the audit measures shipped spacing against these anchors and flags breakage risk.
- **Check:** Measure body line-height (exact from DOM/Figma; baseline-to-baseline from pixels) and paragraph spacing. Then flag override-breakage risks: fixed-height text containers, overflow clipping, buttons/badges with zero vertical slack.
- **Pass:** shipped spacing at/near the SC anchors and no breakage-risk patterns. **Partial:** spacing well below anchors but flexible containers, or one risk pattern. **Fail:** tight spacing inside fixed/clipping containers — likely breakage under user overrides. Verdict wording must say "risk assessment — full SC 1.4.12 conformance requires the override test."
- **Applies:** both · **Platforms:** web primarily; native analog is Dynamic Type resilience · **Needs:** DOM/Figma preferred (screenshot: careful measurement) · **Assessability:** screenshot (as measured risk assessment; full conformance = manual test)

## Operable

### AC-07 Target size (SC 2.5.8, AA) + placement
- **Standard:** Pointer targets ≥24×24 CSS px, unless exempt (Spacing: 24px circles centered on undersized targets don't intersect; Equivalent control; Inline; User-agent; Essential). Platform conventions are stricter — flag <44pt (iOS) / <48dp (Android) as platform risk via `platforms.md` even when 24px passes.
- **Check:** Establish px scale; measure icon buttons, close buttons, checkboxes, pagination, row actions; apply the circle test before failing undersized ones. Also note placement: destructive actions crowding constructive ones, primary targets small/remote relative to secondary (Fitts).
- **Pass:** all ≥24px or exempt; no hazardous adjacency. **Partial:** a few undersized-but-nearly-spaced targets, scale uncertainty, or one adjacency hazard. **Fail:** clearly undersized packed targets, or destructive/constructive abutting on the task path.
- **Applies:** both · **Platforms:** all — thresholds per `platforms.md` (WCAG 24px floor; HIG 44pt; Material 48dp + 8dp gaps) · **Needs:** screenshot-only (DOM/Figma preferred for scale) · **Assessability:** screenshot

### AC-08 Descriptive headings and labels (SC 2.4.6, AA)
- **Standard:** Headings and labels, where present, describe their topic or purpose. (Existence is US-11/SC 3.3.2's job; markup is AC-05's.)
- **Check:** Read each visible heading/label against what it governs: topic inferable from heading alone? Labels disambiguate similar fields/actions?
- **Pass:** all descriptive. **Partial:** isolated vague ones. **Fail:** misleading or generic headings/labels leaving purpose unclear.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only · **Assessability:** screenshot

### AC-09 Focus visible (SC 2.4.7, AA) — conditional
- **Standard:** A visible keyboard-focus indicator exists in some mode of operation.
- **Check:** Scoreable only when the input shows a focused state (a captured focus screenshot, prototype/recording frame, or explicit focus-state design). Then: indicator present and perceivable (its contrast belongs to AC-02). Otherwise N/A "needs keyboard test" — plus CSS risk flags when DOM available (`outline: none` without replacement :focus styles).
- **Pass:** captured focus states all show an indicator. **Partial:** indicator on some captured states only. **Fail:** a captured focused control shows no indicator.
- **Applies:** both — N/A without a captured focus state · **Platforms:** web/desktop primarily · **Needs:** focus-state capture or DOM (risk flags) · **Assessability:** conditional screenshot; otherwise interaction-required

## Understandable

### AC-10 Labels or instructions (SC 3.3.2, A)
- **Standard:** Required input has visible labels/instructions: persistent labels, required-field marking, format hints for non-customary formats.
- **Check:** Per input: persistent visible label (placeholder-only fails once filled)? Required marked? Unusual formats hinted? (Overlaps US-11 mechanics; here the test is the WCAG floor — presence — while US-11 scores the placement craft.)
- **Pass:** every input labeled persistently, cues present where needed. **Partial:** placeholder reliance or missing format hints on some fields. **Fail:** unlabeled inputs or placeholder-only forms.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only · **Assessability:** screenshot

### AC-11 Error identification in text (SC 3.3.1, A) — conditional
- **Standard:** Detected input errors are identified and described in visible text; color/style may supplement, never replace text. (Message craft is US-08; this is the normative text-presence floor.)
- **Check:** Only when an error state is captured: is each errored field named and the problem described in text — not just a red border/icon?
- **Pass:** all captured errors named + described in text. **Partial:** text present but vague or unanchored to a field. **Fail:** color/icon-only errors.
- **Applies:** both — N/A when no error state captured (same trigger as US-08) · **Platforms:** all · **Needs:** screenshot-only · **Assessability:** conditional screenshot

### AC-12 Consistent navigation (SC 3.2.3, AA) — multi-screen only
- **Standard:** Navigation repeated across screens keeps the same relative order (insertions allowed).
- **Check:** Diff repeated nav structures across the screen set: same items, same relative order. Position identity and craft-level stability are CO-02's job — do not double-penalize one flaw under both.
- **Pass:** relative order preserved everywhere. **Partial:** order preserved but grouping shifts oddly. **Fail:** reordered nav between screens.
- **Applies:** multi (single-screen: N/A — SC scopes to sets of pages) · **Platforms:** all · **Needs:** screenshot-only · **Assessability:** screenshot

### AC-13 Consistent identification (SC 3.2.4, AA) — multi-screen only
- **Standard:** Same-function components are identified consistently across screens (labels; icon text alternatives).
- **Check:** Match same-function controls across screens (search, save, delete, back); compare labels/icons. Terminology craft within a screen is CO-03's job — don't double-penalize.
- **Pass:** same function, same identification. **Partial:** minor wording drift without ambiguity. **Fail:** same function identified differently enough to suggest different functions.
- **Applies:** multi (single-screen: N/A) · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma for icon alternatives) · **Assessability:** screenshot

## Robust

### AC-14 Name, role, value (SC 4.1.2, A)
- **Standard:** All UI components expose programmatic name, role, and state to assistive technologies.
- **Check:** With DOM: native semantic elements used per spec, or ARIA supplies role + accessible name + state (aria-expanded, aria-checked…); flag div/span click targets without role/name. Figma cannot answer this — N/A with note.
- **Pass:** all controls expose name/role/state. **Partial:** names/roles present, some states missing. **Fail:** unnamed or role-less custom controls.
- **Applies:** both · **Platforms:** web (DOM); native platforms' APIs usually unavailable to the audit — N/A with note · **Needs:** DOM required · **Assessability:** DOM only

---

## Severity guidance (annotation only — never in score math)

Rate findings 0–4 by frequency × impact × persistence. In this dimension impact
dominates: a contrast or target-size failure on the primary action excludes users
outright every time (persistence = always) → trend 3–4. Color-only signals with
partial redundancy, or generic alt text on secondary imagery → 1–2. Word severity
as an estimate; note that WCAG conformance itself is binary per SC — severity ranks
the finding's user cost, not its normative status.

---

Last reviewed: 2026-07

Sources: W3C, WCAG 2.2 (Recommendation 2023, upd. 2024), w3.org/TR/WCAG22/ · W3C
Understanding WCAG 2.2 pages for SC 1.4.3, 1.4.11, 1.4.1, 1.1.1, 1.3.1, 1.4.12,
2.5.8, 2.4.6, 2.4.7, 3.3.2, 3.3.1, 3.2.3, 3.2.4, 4.1.2 (2025–2026 updates) · W3C
WAI, "Easy Checks" · W3C, WCAG-EM 1.0 (2014). Full provenance and the
assessability derivation: `research/criteria-research.md`.
