# Input capture procedures

Goal: normalize any supported input into **N ordered screenshots on disk** plus
optional structured data. Everything downstream (classification, criteria checks,
annotation) consumes these screens.

## Working directory and naming

- Create a session working directory (use the scratchpad directory if the harness
  provides one; otherwise a temp directory).
- Name screens in flow order: `screen-01.png`, `screen-02.png`, …. Order is the
  order the user gave, or the natural sequence (Figma frame order, video timeline).
- Keep a short capture log (input type, source, viewport/frame, any limitations)
  to include in the report header.

## Downscaling

Downscale any capture whose long edge exceeds **1568px** (keeps images within the
model's effective resolution budget; larger images are resized down anyway, so
oversized captures only cost tokens without adding legibility).

macOS: `sips --resampleHeightWidthMax 1568 in.png --out screen-01.png`
Fallback: any available tool (ImageMagick `magick in.png -resize 1568x1568\> out.png`,
or Python + Pillow). Never upscale.

## Per-input procedures

### 1. Screenshot file(s)

1. Read each file to confirm it is a legible UI screenshot (not corrupt, not blank).
2. Copy into the working directory with ordered names; downscale if needed.
3. If multiple files: ask the user whether they form an ordered flow (unless the
   order is obvious from filenames or the user already said so). This determines
   single-screen vs multi-screen behavior in Step 6.
4. No structured data available — mark DOM/Figma-dependent criteria as
   candidate-N/A for the audit steps.

### 2. URL / localhost / HTML file

Use the in-app browser (Browser pane tools). Local HTML files: navigate to the
`file://` path or serve the directory if the page needs relative assets.

1. Navigate to the URL; wait for load; dismiss cookie/consent banners by choosing
   the most privacy-preserving option.
2. Capture at **two viewports**, each as its own screen:
   - Desktop: resize to 1280 wide, screenshot.
   - Mobile: resize to 375 wide, screenshot.
   The pair is recorded as a **responsive pair** (one logical page, two screens) —
   Step 1 classifies it as such and Step 2 adds cross-breakpoint parity checks.
3. For pages taller than the viewport: capture per-viewport sections as separate
   ordered screens (scroll, screenshot, repeat) — never one tall stitched image.
4. Collect structured data with `read_page` (accessibility tree) at each viewport:
   element roles/names, heading structure, link/button labels, form labels. Save
   alongside the screens; this enables DOM-measured checks (real heading hierarchy,
   accessible names, target sizes) instead of visual estimation.
5. Multiple URLs given as a flow → repeat per URL in the given order.

### 3. Figma link

Use the Figma MCP server (requires the user to be authenticated to it).

1. `get_metadata` on the link target to enumerate frames, their order (canvas
   position: left-to-right, top-to-bottom unless the user specifies), names, and
   bounding boxes.
2. `get_screenshot` per frame → one screen per frame, ordered; downscale if needed.
3. `get_variable_defs` for the file's tokens (colors, type, spacing) when
   available — this powers measured consistency checks.
4. Frame dimensions from metadata feed Step 1 classification (e.g. 393×852 ≈
   iPhone frame preset → mobile app candidate).
5. Node bounding boxes are the preferred source for annotation coordinates —
   more precise than visual estimation.

### 4. Video / prototype recording

1. Confirm `ffmpeg` is available (`ffmpeg -version`); if not, degrade (below).
2. Extract keyframes of distinct screens, e.g.:
   `ffmpeg -i in.mp4 -vf "select='gt(scene,0.3)',scale=1568:-2:force_original_aspect_ratio=decrease" -vsync vfr screen-%02d.png`
3. Review extracted frames; drop mid-transition duplicates/blurs; keep one clean
   frame per distinct screen, in timeline order.
4. If scene detection yields too few/many screens, fall back to sampling
   (`fps=1`) and hand-pick.
5. Treat the result as an ordered multi-screen flow. No structured data.

## Graceful degradation

Never fake a capture. If a needed tool is unavailable:

- **No browser pane** (URL input) → ask the user for manual screenshots of the
  page at desktop and mobile widths; proceed as input type 1.
- **Figma MCP unavailable/unauthenticated** → tell the user, and ask for exported
  frame images (PNG) instead; proceed as input type 1 (no token/geometry data).
- **No ffmpeg** → ask the user for screenshots of each distinct screen from the
  recording; proceed as input type 1.

Record every degradation in the capture log; the report header states what the
audit could and couldn't measure as a result.

---

Last reviewed: 2026-07

Sources (procedure/tooling docs — criteria sources live in the criteria files):
- Anthropic, "Vision" (Claude docs) — image sizing guidance, ~1568px long-edge
  effective maximum, 2024–2025.
- Figma, "Figma MCP server" documentation — get_metadata / get_screenshot /
  get_variable_defs capabilities, 2025.
- FFmpeg documentation — `select` scene-change filter and `fps` sampling.
- WCAG-EM 1.0 (W3C, 2014) — evaluation-scope note: static captures limit which
  accessibility checks are assessable; motivates recording capture limitations.
