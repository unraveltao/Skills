# Skill Observability Model

This reference defines what Meta Skill may claim about a Skill's loading, routing, execution, adoption, and quality.

## 1. Evidence levels

Evidence levels describe the strength and kind of evidence available for a specific claim. They are not a universal score for the Skill.

| Level | Name | Evidence | What it supports | What it does not prove |
| --- | --- | --- | --- | --- |
| E0 | Static | Source review, metadata validation, package/link checks, isolated script checks | The package is structurally plausible and declared behavior is inspectable | That an Agent loads, routes to, or follows the Skill |
| E1 | Explicit invocation | A test prompt explicitly names or invokes the Skill in a target client | Behavior after the Skill is deliberately invoked | Automatic selection for natural-language requests |
| E2 | Natural-language routing | A fresh session receives a natural-language request without explicit Skill invocation; observed selection is recorded | Routing behavior for that scenario in that client/session | Universal routing accuracy across models, clients, or prompts |
| E3 | Runtime trace | Independent client/runtime logs, file-read events, tool traces, or equivalent observable evidence tied to the run | Stronger evidence that loading and execution events occurred | That the final result is correct or useful by itself |

Important distinctions:

- An E0 pass is not a behavior pass.
- E1 and E2 answer different questions; do not combine them into one result.
- E3 may strengthen a loading/execution claim, but output quality still needs separate evaluation.
- A message from the Agent saying “I loaded the Skill” is a self-report. Label it as such; do not call it an independent trace.
- If a client exposes no suitable trace, record that limitation. Do not invent one.

## 2. Metric groups

### Adoption

Examples: platform-reported use count, enabled state, or last-used time.

For every automatic metric, record the platform/source, collection time, and observation window. A usage counter is an adoption signal only. It does not prove correct routing, successful completion, or user satisfaction.

### Routing

Use controlled natural-language scenarios to record:

- True positive (TP): an in-scope request correctly selects the Skill.
- False positive (FP): an out-of-scope request incorrectly selects the Skill.
- False negative (FN): an in-scope request fails to select the Skill.
- Borderline: a request where clarification or conservative handling is expected.

When sample size is meaningful, calculate:

- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)

Always include counts and sample size beside rates. Do not report a rate when its denominator is zero. A small hand-authored test set is a regression suite, not a representative estimate of real-world production routing.

### Execution

Examples:

- Scenario completion: passed behavior scenarios / attempted behavior scenarios.
- Tool success or failure, when the tool result is observable.
- Required-step coverage.
- Recovery success after a controlled failure.
- Time or number of turns, only when measured consistently and relevant.

Separate blocked tests from failed tests. A missing tool or unavailable permission is not automatically a Skill instruction defect.

### Quality

Examples:

- User acceptance or rejection of the output.
- Number and type of user corrections.
- Rework required before the result is usable.
- Whether acceptance criteria were met.

Record who or what supplied the assessment and how many outputs were reviewed. Do not infer satisfaction from silence.

### Reliability

Examples:

- Regression results across versions.
- Repeatability across multiple runs.
- Differences across Agent clients, model versions, or runtime configurations.
- Known intermittent tool or environment failures.

Do not generalize a result from one client/version to all environments.

## 3. Metric provenance

Every metric must be labeled:

- **Automatic:** directly returned by an authorized platform metric or runtime API.
- **Manual:** observed and recorded by a person or evaluator.
- **Derived:** calculated from recorded raw observations.

For each value, record:

- Metric name and definition.
- Value and unit.
- Provenance type.
- Source or evidence reference.
- Observation window and sample size.
- Client/model/version when relevant.
- Collection timestamp.
- Known gaps or caveats.

Never fill unavailable metrics with estimates presented as facts. If a platform only shows a cumulative Uses count, record that count as adoption and leave routing, execution, and quality metrics unmeasured.

## 4. Experiment record

A useful minimum experiment record contains:

| Field | Meaning |
| --- | --- |
| Experiment ID | Stable identifier for the run |
| Skill / version | Skill name and version under test |
| Commit | Exact source revision |
| Client / model | Agent client and model/version, if known |
| Date | Run date/time |
| Scenario | Test case ID and prompt |
| Expected | Observable expected behavior |
| Actual | What was observed |
| Result | PASS / FAIL / BLOCKED / NOT RUN |
| Evidence | E0-E3 plus link, log reference, or artifact |
| Metrics | Values with provenance and sample size |
| Findings | Root cause, user correction, or limitation |
| Next action | Keep, fix, add regression case, or investigate |

Use Notion as the experiment and decision log when the workspace and destination are available. Keep the source Skill package and its authoritative version in Git. Link each experiment to the exact commit it evaluates.

## 5. Reporting language

Prefer precise statements:

- “Static package checks passed (E0); natural-language routing was not run.”
- “The Skill was explicitly invoked and completed scenario B (E1); automatic selection remains unverified.”
- “The client trace shows the Skill file was read during this run (E3); output quality was assessed separately.”
- “The platform reports 18 uses in the displayed period; this is an adoption count, not a success rate.”

Avoid unsupported statements:

- “The Skill works perfectly.”
- “It has 18 successful uses” when the platform only reports 18 uses.
- “The Skill auto-triggered” when it was explicitly invoked.
- “The Skill loaded” based only on the Agent's unsupported self-report.
