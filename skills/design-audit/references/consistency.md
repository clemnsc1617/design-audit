# Consistency criteria (CO) — 12 criteria

Dimension scope: internal consistency (same thing looks/reads the same everywhere)
and external consistency (platform and web conventions). Not here: whether a
convention is itself usable (usability.md), aesthetics (visual-design.md), WCAG
conformance (accessibility.md), navigation logic (user-flow.md).

Cross-reference rule (Clemens ruling #4): AC-12/AC-13 score the WCAG floor
(relative order, same identification, multi-screen); CO-02/CO-03 score the stricter
craft bar. One observed flaw counts against ONE layer — the one it actually
violates — never both.

Measured-check rule (ruling #7): CO-05, CO-06, CO-07 are auto-N/A without DOM or
Figma data; without measured values they would only re-score visual judgments that
VD-02/VD-06/VD-07 already made.

Verdicts: pass = 1, partial = 0.5, fail = 0, N/A excluded from the denominator.

---

### CO-01 Uniform styling of repeated elements
- **Standard:** An element playing the same role (primary button, link, card, field) looks identical everywhere it appears.
- **Source:** Nielsen heuristic #4, "Consistency and Standards", NN/g.
- **Check:** Inventory each recurring element class across the input; compare fill/border, radius, typography, padding across instances (state variants excepted). Figma component data reveals detached/overridden instances directly.
- **Pass:** one treatment per class. **Partial:** one class has a stray unmotivated variant. **Fail:** multiple classes with unexplained variants, or one class with 3+ treatments.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma preferred)

### CO-02 Cross-screen structural stability
- **Standard:** Persistent chrome — header, nav, logo, page-title placement, recurring actions — keeps identical position and contents on every screen.
- **Source:** Nielsen heuristic #4; Material 3, "Grids & spacing" (consistent cross-page placement).
- **Check:** Multi-screen: overlay/compare screens; nav placement + item order, logo position, header height, recurring action locations identical. (Relative-order-only violations belong to AC-12.)
- **Pass:** all persistent regions identical. **Partial:** one region shifts without a mode-change reason. **Fail:** nav or primary-action placement moves between screens.
- **Applies:** multi · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma for pixel diffs)

### CO-03 Terminology consistency
- **Standard:** One term per concept everywhere; no term meaning two things.
- **Source:** Nielsen heuristic #4; Apple HIG, "Writing".
- **Check:** Extract visible labels/headings/buttons/messages; build a concept→term table; flag synonym pairs and overloaded terms. (Cross-screen same-function labeling floor is AC-13.)
- **Pass:** one term per concept. **Partial:** one synonym pair on a peripheral concept. **Fail:** core objects/actions with multiple names, or one word with two meanings.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only (DOM widens the inventory)

### CO-04 Capitalization and label style
- **Standard:** Each element type uses one capitalization style (title case or sentence case) and one punctuation pattern throughout.
- **Source:** Apple HIG, "Writing" ("Choose a style for each UI element type and use it consistently").
- **Check:** Group visible text by element type (buttons, menus, headings, field labels, tabs); classify case per string; check terminal punctuation and label suffixes.
- **Pass:** every type internally uniform. **Partial:** one type mixes styles in 1–2 spots. **Fail:** multiple types mixed, or sibling elements on one screen differing.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### CO-05 Color token discipline — measured
- **Standard:** Every UI color resolves to a defined palette role or token; no ad-hoc near-duplicates.
- **Source:** Material 3, "Design tokens" ("Use design tokens instead of hardcoded values"); NN/g, "Design Systems 101".
- **Check:** From Figma variables/styles: count colors not bound to any token and distinct raw values per role. From DOM: cluster computed colors per role. Flag near-duplicate grays/brand hues serving one role. No numeric color budget exists in sources — judge role-mapping and duplication, not a count.
- **Pass:** colors map to a small role-based palette; no unbound fills on repeated elements. **Partial:** 1–2 near-duplicates or a handful of unbound fills. **Fail:** same-role elements visibly differ, or widespread hard-coded colors bypass defined tokens.
- **Applies:** both · **Platforms:** all · **Needs:** DOM/Figma required (auto-N/A otherwise)

### CO-06 Type scale discipline — measured
- **Standard:** All text maps to a small deliberate set of type styles; no one-off size/weight combos. (M3's full scale is 15 styles; real products use a subset — more ad-hoc combos than a full scale is the defensible ceiling.)
- **Source:** Material 3, "Typography — type scale & tokens".
- **Check:** From Figma: distinct text styles in use + text nodes unbound to any style. From DOM: distinct computed (size, weight, family) tuples vs declared styles. Same role → same style everywhere. (Per-screen emphasis legibility is VD-02.)
- **Pass:** clear scale, same role = same style, text style-bound. **Partial:** 1–2 orphan combos or minor unbound text. **Fail:** same-role text varying across screens, or ad-hoc combos rivaling the defined styles.
- **Applies:** both · **Platforms:** all · **Needs:** DOM/Figma required (auto-N/A otherwise)

### CO-07 Spacing scale adherence — measured
- **Standard:** Padding/gaps/margins come from one consistent scale (M3's system: multiples of 8dp) applied equally to equivalent pairs.
- **Source:** Material 3, "Spacing" (8dp scale, space100 = 8dp). The criterion requires *a* scale, not specifically 8.
- **Check:** From Figma auto-layout / DOM computed style: gaps between repeated siblings and padding inside repeated containers — equivalent pairs equal, values clustering on a scale. (Within-screen rhythm/crowding is VD-07.)
- **Pass:** equivalent gaps equal, values on a scale. **Partial:** isolated off-scale values or one unequal sibling gap. **Fail:** repeated structures with visibly unequal spacing, no scale evident.
- **Applies:** both · **Platforms:** all · **Needs:** DOM/Figma required (auto-N/A otherwise)

### CO-08 Icon family and weight
- **Standard:** All icons share one family: stroke weight, fill style, corner style, optical size matched to adjacent text.
- **Source:** Material 3, "Applying icons" ("Apply weights consistently" / "Don't mix different weights"); Apple HIG, "SF Symbols" (custom symbols consistent with system detail/weight).
- **Check:** Collect visible icons; compare weight, filled-vs-outlined (selected-state fills excepted), corner style, size relative to paired text. On iOS check custom icons against SF Symbols weight; on Android against one Material Symbols style.
- **Pass:** one family, uniform weight/style/sizing. **Partial:** one deviating icon. **Fail:** mixed families or filled/outlined mixing without state semantics.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only (Figma reveals mixed libraries)

### CO-09 Collection uniformity and alignment
- **Standard:** Same-kind items in a collection (thumbnails, avatars, cards, leading icons) share identical size and a common alignment line.
- **Source:** Material 3, "Grids & spacing" (similar elements same spacing/sizing; leading elements always aligned).
- **Check:** Per collection (list, grid, toolbar): item dimensions match; leading elements on one line; inter-item spacing constant per axis. (The page grid itself is VD-06.)
- **Pass:** all collections uniform. **Partial:** one collection with one misaligned/missized item. **Fail:** mixed sizes or broken alignment in multiple collections.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only (DOM/Figma for exact coordinates)

### CO-10 External convention adherence (Jakob's Law)
- **Standard:** Standardized patterns work the way the ecosystem taught users: logo top-left linking home, cart top-right, magnifier = search, links look like links. ("Users spend most of their time on other sites.")
- **Source:** Laws of UX, "Jakob's Law"; Nielsen, "The Need for Web Design Standards", NN/g (80%+ adoption = standard; placements from 2004 — still dominant practice, exact current rates unverified).
- **Check:** Identify each standardized pattern the screen participates in; judge against the dominant convention; flag reinvented solved patterns.
- **Pass:** all standards followed. **Partial:** one convention bent discoverably. **Fail:** a standard element repurposed/relocated so its learned meaning breaks.
- **Applies:** both · **Platforms:** all (web conventions for web; ecosystem conventions for mobile) · **Needs:** screenshot-only

### CO-11 Platform-native pattern adherence
- **Standard:** The interface uses its platform's native components and structures — or customs that respect documented platform anatomy.
- **Source:** Apple HIG, "Designing for iOS"; Material 3 components. Platform selected by Step 1 classification (`platforms.md`).
- **Check:** Compare visible controls against the classified platform's standard set: iOS tab bars/nav bars/SF-style symbols/sheet anatomy; Android Material components/Symbols; web per CO-10. Divergences that change verdicts (nav placement, back affordance, item counts) are tabled in `platforms.md`.
- **Pass:** native or anatomy-respecting customs. **Partial:** one isolated foreign-platform component. **Fail:** wholesale foreign or invented chrome.
- **Applies:** both · **Platforms:** per classification · **Needs:** screenshot-only

### CO-12 Data and format consistency
- **Standard:** Dates, times, numbers, currency, phone numbers, units formatted one way throughout, in locale-standard formats.
- **Source:** Nielsen heuristic #4 (lists standard formats among consistency's objects).
- **Check:** Extract visible formatted values; group by type; one format per type ("Jan 5, 2026" vs "05/01/26" mixing fails; consistent decimals, currency placement, relative-vs-absolute time per context).
- **Pass:** one format per type. **Partial:** two formats for one type across clearly different contexts. **Fail:** same type formatted differently within a screen or arbitrarily across screens.
- **Applies:** both · **Platforms:** all (locale sets the expected format) · **Needs:** screenshot-only (DOM for datetime attributes)

---

## Severity guidance (annotation only — never in score math)

Rate findings 0–4 by frequency × impact × persistence. Consistency failures are
high-frequency by nature (every occurrence retrains the user) but individually
low-impact: broken external conventions (CO-10) and cross-screen chrome jumps
(CO-02) trend 2–3 because they defeat learned behavior; case mixing and format
drift trend 1. Reserve 4 for a repurposed standard element that actively misleads
(a magnifier that isn't search on the primary path).

---

Last reviewed: 2026-07

Sources: see `research/reference-sources.md` (kept out of the skill's load path).
