# fixtures

Synthetic inputs for previewing the HTML report. Git-tracked, never loaded by
the skill — same arrangement as `research/`.

## Why this exists

Report styling used to be reviewed by rebuilding a real audit from whatever
happened to be in the session scratchpad. On 2026-07-22 the scratchpad was
cleared mid-review and took three built reports, their `findings.json`, and the
source screenshots with it — none of it recoverable without re-running the
audits. Anything needed to review the template now lives in the repo.

## Preview a template change

```bash
python3 skills/design-audit/scripts/build_report.py fixtures/style-preview.json -o /tmp/preview.html
```

Then open `/tmp/preview.html`.

## What the fixture covers

`style-preview.json` is built to exercise the template in one page, not to be a
plausible audit. It deliberately contains:

- **All five severities** — Critical and Major (red), Minor (orange),
  Cosmetic (purple), Note (blue) — so every tag, marker and card tint renders.
- **All four verdicts** — pass, partial, fail, and an `na` carrying its
  required reason.
- **One dimension per score band** — Visual design 50 (red), Accessibility 75
  and Usability 83.3 (orange), User flow 100 (green), overall 77 / grade B.
- **An unscored dimension** — Consistency, every criterion N/A, to render the
  hatched bar and the redistributed 25% weights.
- **Two screens**, so the multi-screen path and the flow section both render.
- **A region annotation** (finding 3 carries `w`/`h`) alongside point markers.

The numbers are arithmetically consistent — dimension scores match their
points/applicable, and the scored weights sum to 1.0 — so `build_report.py`'s
validation is genuinely exercised rather than bypassed.

## Placeholder screens

`screen-01.png` and `screen-02.png` are flat grey blocks at 390×844, generated
by `make_placeholders.py` (Python 3 stdlib only, matching `build_report.py`):

```bash
python3 fixtures/make_placeholders.py
```

They are not a real interface and are not meant to look like one. The marker
coordinates in the fixture point at their blocks so annotation geometry can be
checked — in particular that the screenshot wrapper matches the rendered image
within the 1px border on each side (evals case R3).

Real screenshots are never committed here; see `.gitignore`.
