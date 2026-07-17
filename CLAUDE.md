# design-audit plugin — working agreement

A standalone Claude Code plugin by Clemens Chen: research-backed design audits of any
interface (screenshots, URLs, Figma, prototypes) producing a cited scorecard and an
annotated HTML report.

## How we work together

- **Address me as Clemens.** Begin every reply with "Clemens".
- **Permission first** — propose the approach and wait for explicit approval before any
  change (code, files, commits, installs). Reading, inspecting, and researching to
  inform a proposal is fine.
- **Brief updates.** Short status notes and results over narration.
- **Finish a milestone, then pause** — each milestone ends with its "Test with Clemens"
  gate; never start the next milestone without sign-off on the current one.
- **Research-backed, never guessed** — every criterion, threshold, and weight in the
  skill traces to a cited source; Clemens approves the research digest before it
  becomes reference files.
- **Clemens tests as the user** — skill quality is judged by him running real audits on
  his own work, not by synthetic examples passing.
- **Report wording is reviewable** — templates and user-facing text in the skill's
  output get Clemens's review before shipping.
- **Small, reviewable commits** with clear messages. Git + GitHub.

## Milestones

| # | Milestone | Gate (test with Clemens) |
|---|---|---|
| M0 | Working agreement + repo init | Clemens approves this document |
| M1 | Scaffold + SKILL.md skeleton | Skill validates and triggers in a `--plugin-dir` session |
| M2a | Deep research (criteria + weights) | Clemens reviews criteria drafts + weighting memo, picks the scheme |
| M2b | References: usability, accessibility, visual-design | Clemens spot-reads ~5 criteria per file |
| M2c | References: consistency, user-flow, platforms | Spot-read + platform classification check on 3 known screenshots |
| M3 | Scoring + scorecard | Live audit of a screenshot Clemens picks; he checks fairness + math |
| M4 | Report pipeline (template, schema, build script) | Clemens reviews the full HTML report in the browser |
| M5 | Flow-awareness | Single-screen + 3-screen runs on Clemens's screens |
| M6 | Evals + shakedown | Dress rehearsal on 3 real inputs; iterate until Clemens would use it on real work |

## Conventions

- Skill content follows skill-creator conventions: SKILL.md < 500 lines, heavy rubrics
  in `references/`, executable helpers in `scripts/`, templates in `assets/`.
- Research provenance lives in `research/` (git-tracked, never loaded by the skill).
- Every reference file ends with a "Last reviewed: YYYY-MM" line and its source list.
- `scripts/build_report.py` is Python 3 stdlib only.
