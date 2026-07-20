# User flow criteria (UF) — 11 criteria

Dimension scope: entry clarity, next-step obviousness, cross-screen continuity,
state persistence, navigation logic, progress indication, empty/loading/cancel
paths, dead ends, completion feedback. Not here: single-screen action design
(usability.md), nav styling (consistency.md), error-message craft and recovery
(US-08 — old UF-04 folded there per Clemens ruling #6).

**Applies flags matter most in this dimension.** Single-screen audits score only
`single`/`both` criteria; multi-screen audits score everything. SKILL.md Step 6
redistributes flow's weight when too few criteria apply.

**Walkthrough engine (multi-screen):** before scoring, reconstruct the implied task
and its subtask order (informal hierarchical task analysis — Rosala/NN/g 2020),
then at every screen transition ask the cognitive-walkthrough questions (Lewis,
Polson, Wharton & Rieman, via Flaherty/NN/g 2022): right goal? action noticeable?
action connected to result? progress visible? UF-09/11/12 operationalize these.

Verdicts: pass = 1, partial = 0.5, fail = 0, N/A excluded from the denominator.

---

### UF-01 Next-step obviousness
- **Standard:** From any screen, a first-time user can identify the action that advances the implied goal — the gulf of execution is bridged.
- **Source:** Whitenton, "The Two UX Gulfs: Evaluation and Execution", NN/g, 2018.
- **Check:** Name the screen's implied goal; locate the advancing control(s); would a user who understands the state know what to do next? Flag competing CTAs, buried primary actions, ambiguous outcomes. (Whether controls are individually well-designed is usability's business.)
- **Pass:** one clear forward path, prominent, predictable. **Partial:** forward path competes with 2+ equal-weight actions or its outcome is ambiguous. **Fail:** no discernible advance, or the apparent primary action leads away from the goal.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### UF-02 Orientation and progress indication
- **Standard:** Multi-step processes show where the user is, what steps exist, which is current.
- **Source:** Budiu, "Wizards: Definition and Design Recommendations", NN/g, 2017; Harley, "Visibility of System Status", NN/g, 2018.
- **Check:** If the screen belongs to a wizard/checkout/onboarding: step list or diagram with current highlighted, or an equivalent cue ("Step 2 of 4"). Multi-screen: indicator advances correctly between screens.
- **Pass:** steps enumerated + current highlighted (or genuinely single-step). **Partial:** some position cue but no view of remaining steps, or indicator on some screens only. **Fail:** multi-step process with no position cue.
- **Applies:** both · **Platforms:** all · **Needs:** screenshot-only

### UF-03 Exit and cancel paths
- **Standard:** Every screen in a flow offers a clearly marked way out, with data-loss exits guarded.
- **Source:** Rosala, "User Control and Freedom", NN/g, 2020.
- **Check:** Back/Cancel/Close in expected positions on every step; confirmation guarding destructive mid-task exits; flows that fight back navigation flagged. (Modal exit *labeling* craft is US-05 — here the flow-level presence per step.)
- **Pass:** marked exit on every step, conventionally placed, guarded where destructive. **Partial:** exit obscure/mislabeled or missing on some steps. **Fail:** a step traps the user.
- **Applies:** both · **Platforms:** all — back-affordance expectations differ per platform, see `platforms.md` (iOS app-provided Back; Android system back; web browser back) · **Needs:** screenshot-only

### UF-05 Empty-state guidance
- **Standard:** An empty container communicates status, cause, and a next action.
- **Source:** Kaplan, "Designing Empty States in Complex Applications: 3 Guidelines", NN/g, 2021.
- **Check:** Any contentless container: (1) status distinguishing "no data" from loading/error, (2) cue explaining what would populate it, (3) direct action to start. Blank region with none = the failure signature.
- **Pass:** all three present. **Partial:** status text only ("no results"). **Fail:** blank container indistinguishable from a loading failure.
- **Applies:** single (scored per screen whenever an empty container is visible; N/A otherwise) · **Platforms:** all · **Needs:** screenshot-only

### UF-06 Wait-state feedback
- **Standard:** Visible wait states use feedback matched to duration — looped animation for ~2–10s operations, percent-done/step progress for longer — with text naming the operation.
- **Source:** Sherwin, "Progress Indicators Make a Slow System Less Insufferable", NN/g, 2014.
- **Check:** If a loading state is captured: animated indicator + label ("Loading comments…"); bare spinner on an obviously long operation (bulk upload, export) flagged.
- **Pass:** indicator type fits operation class and is labeled. **Partial:** unlabeled indicator, or bare spinner on a long operation. **Fail:** no feedback for a visible wait, or a static indicator that could mask a hang.
- **Applies:** single (N/A when no wait state captured) · **Platforms:** all · **Needs:** screenshot-only

### UF-07 In-form flow sequencing
- **Standard:** Form steps run in logical single-column order with requirements disclosed up front — users move forward, not back to fix surprises.
- **Source:** Whitenton, "Website Forms Usability: Top 10 Recommendations", NN/g, 2016.
- **Check:** Fields in conventional order (name before address); requirements at the field, not deferred to errors; nothing demanding data a later step provides. (Form *structure* — columns, grouping, Reset — is US-12; here the progression logic.)
- **Pass:** conventional order, requirements visible before submit. **Partial:** logical order but requirements hidden until errors. **Fail:** scrambled order or undisclosed format rules forcing error loops.
- **Applies:** single · **Platforms:** all · **Needs:** screenshot-only

### UF-08 Dead-end avoidance
- **Standard:** No state leaves the user without a productive option — a forward action, a way back, or both.
- **Source:** Rosala, "User Control and Freedom", NN/g, 2020 (dead-end framing is our synthesis of its emergency-exit guidance, flagged as derived).
- **Check:** Single: at least one enabled action exists (terminal confirmations count if they link onward). Multi: trace for reachable-but-not-leavable states — final screens without navigation, error/empty screens without exits, overlays without close.
- **Pass:** every state has an onward or backward path. **Partial:** a state relies on browser/OS chrome as its only escape. **Fail:** any state with no visible way forward or back.
- **Applies:** both · **Platforms:** all (system-back conventions per `platforms.md` inform the Partial band) · **Needs:** screenshot-only

### UF-09 Action-result continuity
- **Standard:** Each screen visibly confirms the previous action succeeded and moved toward the goal (walkthrough Q4: "will users see that progress is made?").
- **Source:** Flaherty, "Evaluate Interface Learnability with Cognitive Walkthroughs", NN/g, 2022 (method: Lewis, Polson, Wharton & Rieman).
- **Check:** Per consecutive screen pair: carried-over context (added item visible in cart, chosen plan echoed at payment), advanced progress indicator, or acknowledging header. Flag screens that could equally follow success or failure.
- **Pass:** every transition shows the prior action took effect. **Partial:** one ambiguous transition. **Fail:** any transition with no evidence the previous action worked.
- **Applies:** multi · **Platforms:** all · **Needs:** screenshot-only

### UF-10 State persistence across steps
- **Standard:** Provided information persists: later steps echo earlier choices; going back doesn't destroy work; long flows offer save/resume.
- **Source:** Budiu, "Wizards", NN/g, 2017 (exit midway, save state, self-sufficient steps); Rosala 2020 (Back without data loss).
- **Check:** Earlier selections echoed where relevant (summaries, "plan: Pro" headers); revisited steps still populated if captured; save-draft/finish-later affordances in long flows. Static screens only show echoes — absence of any echo is the detectable failure.
- **Pass:** prior inputs visibly persist; long flows offer save/resume. **Partial:** some carried state but no summary step where entries span many screens, or no save/resume in a long flow. **Fail:** a later screen contradicts/ignores earlier input, or a revisited step is empty.
- **Applies:** multi · **Platforms:** all · **Needs:** DOM/Figma preferred (prototype/DOM materially improves this check)

### UF-11 Step-order logic
- **Standard:** Screen sequence follows predictable task logic: each step needs only information already available; dependent steps follow their prerequisites; forward labels describe the next step.
- **Source:** Budiu, "Wizards", NN/g, 2017; Rosala, "Task Analysis", NN/g, 2020.
- **Check:** Decompose the implied goal into subtasks (the walkthrough-engine step above); diff the captured order against it. Any screen demanding not-yet-available data (shipping method before address)? Generic Next/Previous where descriptive labels fit?
- **Pass:** order matches decomposition; labels descriptive. **Partial:** workable order with one misplaced step or generic labels. **Fail:** a step requiring unavailable information or forcing obvious backtracking.
- **Applies:** multi · **Platforms:** all · **Needs:** screenshot-only

### UF-12 Completion feedback
- **Standard:** The flow ends with an explicit plain-language confirmation: outcome stated, summary shown (order number, saved item), what happens next, an onward action.
- **Source:** Harley, "Visibility of System Status", NN/g, 2018; Rosala, "Status Trackers and Progress Updates", NN/g, 2019.
- **Check:** On the final/confirmation screen: success in user language (not "fulfilled"), outcome summary, next-step statement, onward path. Flows whose last captured screen is the action button get flagged as unverifiable completion.
- **Pass:** clear success + summary + onward path. **Partial:** success stated but jargon-y, or missing summary/next step. **Fail:** no completion state — success indeterminable.
- **Applies:** both (single only when the audited screen IS a confirmation state; otherwise multi) · **Platforms:** all · **Needs:** screenshot-only

---

## Flow outputs beyond scoring (feeds SKILL.md Step 6)

- **Single screen:** after scoring `single`/`both` criteria, infer 3–5 adjacent
  flows worth auditing next (where does the primary action lead; what
  error/empty/loading states does this screen imply).
- **Multi screen:** list **missing flows** — states the set implies but doesn't
  show (error, empty, loading, cancel/abandon, back-navigation) — as report
  suggestions, not scored verdicts. Scope boundary: the screen set is treated as a
  candidate wireflow (one task, one product — Kaplan/NN/g 2023); journey-level
  concerns (multi-channel, emotion) are out of scope.

## Severity guidance (annotation only — never in score math)

Rate findings 0–4 by frequency × impact × persistence. Flow failures compound:
trapped states and dead ends on the task path trend 3–4 (abandonment); missing
progress indication or unlabeled spinners trend 1–2; an ambiguous
action-result transition trends 2–3 because users repeat or abandon actions they
can't confirm.

---

Last reviewed: 2026-07

Sources: Whitenton, "The Two UX Gulfs" (2018), "Website Forms Usability" (2016),
nngroup.com · Budiu, "Wizards" (2017) · Rosala, "User Control and Freedom" (2020),
"Task Analysis" (2020), "Status Trackers and Progress Updates" (2019) · Kaplan,
"Designing Empty States" (2021), "User Journeys vs. User Flows" (2023) · Sherwin,
"Progress Indicators" (2014) · Harley, "Visibility of System Status" (2018) ·
Flaherty, "Evaluate Interface Learnability with Cognitive Walkthroughs" (2022),
crediting Lewis, Polson, Wharton & Rieman (1990/1994). Full provenance:
`research/criteria-research.md`. (UF-04 was folded into US-08 — ID intentionally
unused so digest references stay valid.)
