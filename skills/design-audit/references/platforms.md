# Platform classification and thresholds

Used by SKILL.md Step 1. Classify every screen into one bucket, record the
classification + evidence in the report header, and resolve all platform-dependent
thresholds from the table below. Individual criteria reference this file instead of
duplicating numbers.

Buckets: **mobile app (iOS)** · **mobile app (Android)** · **mobile web** ·
**desktop web** · **desktop app** · **responsive pair** (one logical page captured
at two widths).

Units: 1pt (iOS) ≈ 1dp (Android) ≈ 1 CSS px (web) at 1x; WCAG: 1pt = 1.333px.

---

## Classification procedure

Work down the signals; stop when confident. Cite the deciding signals in the
report header.

1. **Exact logical dimensions** (device match ⇒ near-certain). iPhone pt sizes
   (HIG Layout table): 402×874 (17/17 Pro/16 Pro), 393×852 (16/15/14 Pro),
   440×956 (Pro Max), 430×932 (Plus/15 Pro Max), 420×912 (Air), 390×844 (16e/14/13),
   375×812 (X/XS/11 Pro), 360×780 (mini), 375×667 (SE 4.7"), 320×568 (SE 4").
   iPads: 1024×1366, 1032×1376, 834×1194/1210, 820×1180, 810×1080, 768×1024,
   744×1133. A screenshot at exactly 2×/3× these px values is a device screenshot;
   at 1× it's likely a design frame. Common Figma presets (UNVERIFIED — Figma
   doesn't publish them; iPhone values corroborated by Apple's table): Android
   Compact 412×917, Android Medium 700×840, legacy Android 360×800, Desktop
   1440×1024, MacBook Air 1280×832, MacBook Pro 14" 1512×982. Round non-device
   sizes (1440×1024) ⇒ desktop-web design frame.
2. **Aspect ratio (W/H):** 0.42–0.56 portrait ⇒ phone-class; 0.70–0.80 ⇒ tablet
   portrait; ≥1.3 landscape ⇒ desktop-class or tablet landscape.
3. **Status bar:** iOS — time top-left, battery/signal top-right, Dynamic
   Island/notch, home-indicator bar bottom. Android — punch-hole cutout, gesture
   pill or 3-button nav. Either present ⇒ native mobile or mobile web.
4. **Browser chrome:** URL bar + status bar ⇒ mobile web (iOS Safari: bottom URL
   pill by default; Android Chrome: top omnibox). Tab strip + URL bar + window
   controls (traffic lights left / Windows controls right) ⇒ desktop web. Window
   chrome without URL bar ⇒ desktop app.
5. **Nav patterns & widgets:** floating/translucent bottom tab bar, SF-Symbol-style
   icons, back chevron top-leading, large titles, grouped inset lists, iOS
   switches/segmented controls ⇒ iOS. Bottom nav with pill-shaped active
   indicator, FAB, ripple states, Roboto/Google Sans, snackbars ⇒ Android/Material.
   Left rail with icon+label stack ⇒ Material medium+ window. Header logo +
   horizontal links + footer + cookie banner + underlined links ⇒ web.
6. **Responsive pair rule:** same content/brand/URL at one width ≥1024 and one
   ≤480 with reflowed (not scaled) layout ⇒ responsive pair. Audit each screen
   against its own column (desktop web + mobile web) plus cross-breakpoint parity
   (content/feature parity, layout adaptation) in Step 2.

**The one clarifying question** (ask at most once, only when genuinely ambiguous):
phone-sized screen with no status bar and no browser chrome ⇒ "Will this ship as a
native app (iOS/Android) or as a mobile website/PWA?" Also ask when UI style and
dimensions disagree (iOS-style UI at Android dimensions). **Default if
unanswered:** score against WCAG 2.2 AA (24px target floor) and flag anything under
44pt/48dp as platform risk; state the assumption in the report header.

---

## Threshold table

| Property | iOS (HIG) | Android (Material 3) | Web (WCAG + convention) |
|---|---|---|---|
| Touch target minimum | 44×44pt hit region (Buttons); accessibility table: 44pt default, 28×28pt absolute min | 48×48dp (~9mm); icon may draw at 24dp inside the 48dp target | 24×24 CSS px AA floor (SC 2.5.8, with Spacing/Equivalent/Inline/User-agent/Essential exceptions); 44px is AAA (SC 2.5.5) |
| Pointer (desktop) target | macOS 28×28pt default, 20×20pt min | 44×44dp pointer targets | same 24px AA floor (SC 2.5.8 covers all pointer inputs) |
| Spacing between targets | ~12pt around bezeled, ~24pt around non-bezeled edges | ≥8dp between targets | no spacing SC; only the 24px-circle exception test for undersized targets |
| Body text default | 17pt iOS/iPadOS · 13pt macOS | Body Large 16sp (scale base 14; Body Medium 14sp is component default) | 16px browser default (MDN) — convention, not a WCAG rule |
| Minimum text size | 11pt iOS/iPadOS · 10pt macOS | smallest tokens: Label Small 11 / Body Small 12 | none normative; resize-to-200% is SC 1.4.4 (not statically assessable) |
| Text contrast | HIG table exists but is more lenient on bold — **use WCAG on all platforms** (stricter, safer) | follows WCAG; nav icons ≥3:1 vs container | 4.5:1 / 3:1 large (≥18pt or ≥14pt bold); no rounding |
| Primary nav | iPhone: floating bottom tab bar; iPadOS: tab bar near top / sidebar | bottom nav bar (mobile/tablet only); nav rail on medium+ windows; **"Don't use navigation bars for desktop layouts"** | header/banner landmark containing nav; top-header is convention (no single canonical source) |
| Nav item count | no hard number in current HIG ("appropriate number"; customizable iPad tab bars "five or fewer") — **"HIG says 3–5 tabs" is outdated lore** | normative: bar 3–5 destinations (<3 ⇒ tabs; >5 or 2+ levels ⇒ expanded rail); collapsed rail 3–7 | no standard |
| Back navigation | app must provide a Back button in the top toolbar (+ edge-swipe shortcut) | system-owned (gesture + predictive back) — **a missing on-screen back button is NOT a defect on Android** | browser back — no in-page back required |
| Drawer / hamburger | no HIG deprecation | navigation drawer deprecated in M3 Expressive — current spec: expanded nav rail | acceptable convention, esp. mobile web |

## Verdict-changing divergences (keep in mind while scoring)

- A 32px button: passes web AA, fails both native conventions. Always
  platform-conditional.
- Desktop apps do NOT inherit the 44pt rule — macOS default is 28pt (min 20pt).
- Numeric spacing between targets is only scoreable on Material (8dp); iOS gives
  padding guidance; web has none.
- 14sp body on Android is spec-sanctioned; 14px body on web reads sub-convention.
  Same rendered size, opposite verdicts (VD-10).
- Bottom nav: idiomatic on phones, a finding on desktop (M3 explicitly), and
  current iPadOS puts tab bars near the top.
- A 6-item bottom bar fails Material outright; under HIG it's only a soft warning.
- Never penalize "no back button" without platform context (UF-03, UF-08).
- For contrast, WCAG governs everywhere — Apple's bold-text leniency is ignored.

---

Last reviewed: 2026-07

Sources: Apple HIG — "Layout" (device dimension table), "Typography" (defaults/
minimums per platform), "Accessibility" (control-size table, spacing, contrast),
"Buttons" (44pt hit region), "Tab bars", "Gestures" (developer.apple.com/design,
2025) · Material 3 — "Designing > Structure" (48dp/44dp/8dp), "Type scale &
tokens", "Navigation bar/rail/drawer guidelines" (m3.material.io) · W3C —
Understanding SC 2.5.8 Target Size (Minimum), SC 2.5.5 (Enhanced), SC 1.4.3
Contrast (w3.org, 2025–2026 updates) · Android Developers — "Predictive back
design" · MDN — CSS font-size (16px default) · Figma Help — frame presets exist,
dimensions unpublished (preset values marked UNVERIFIED above). Full provenance:
`research/criteria-research.md`.
