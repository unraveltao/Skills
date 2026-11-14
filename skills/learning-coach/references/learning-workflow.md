# Learning workflow and portable progress

## Responsibility and handoff

Own portable progress state, save/resume behavior and coordination of evidence-based next steps. Do not teach, assign/inspect practice, grade outcomes or create notes; those modules provide their outputs for recording. Actual learner records stay outside reusable Skill rules and public repositories.

Input: learner-authorized save/resume request, course route, observed teaching/practice/assessment evidence and any existing user-controlled record. Output: a concise portable state update or a grounded resume suggestion; preserve unknowns and evidence limits.

## Learning feedback loop

Use only the stages relevant to the request. For a full course, coordinate: curriculum defines outcomes → teaching explains concepts → practice produces learner-owned work → assessment diagnoses evidence and specific gaps → learning workflow records gaps and next actions when persistence is requested/agreed → teaching reteaches only the implicated concept or practice assigns a targeted task → assessment rechecks with fresh evidence. Do not send every failure back to a full chapter. A missing artifact or unattempted task is Unverified, not automatically a knowledge weakness. Advance when the current outcome has sufficient evidence for the agreed course criteria; otherwise keep the next targeted action visible. Small CodeLabs can occur during teaching; larger projects use practice. Notes may synthesize outputs from any stage but are not progress state.

This loop coordinates modules executed by one agent; it is a handoff convention, not a multi-agent orchestration system. Any module may stand alone when the request calls for it.

## Capability states

Track each relevant outcome as **Verified** (supported by observed explanation or inspected work on an appropriate task), **Unverified** (not enough direct evidence), or **Needs reinforcement** (observed work shows a specific gap). Record evidence and scope. Correct recall alone does not establish transfer. Device access, preference, time, or a choice not to run a tool is not evidence of inability; offer a reasoning task and mark hands-on execution Unverified when it was not observed. Assessment owns the finding; this workflow owns persistence and next-step state.

## Save and resume

Progress is personal data, not Skill content. When persistence is useful, agree on a user-controlled Markdown file **outside the Skill installation and any public repository**, such as a file in a private learning directory. Do not silently put personal records into this repository. If no writable private destination is available, offer the Markdown in the conversation for the user to save; do not claim it was saved. Update an existing record only with the learner's request or agreement, preserving useful evidence and avoiding duplicate records.

On resume, read the user-provided or previously agreed file if available; otherwise ask for it or a brief recap. Treat absent, stale or ambiguous fields as unknown, and confirm a sensible next step rather than inventing learning history. A prior correct answer is evidence of performance on that task, not automatic mastery. Keep sensitive details to the minimum needed.

Suggested portable format, with unknown fields marked `unknown`:

```markdown
# Learning progress
- Updated: YYYY-MM-DD
- Goal: ...
- Completed chapters: ...
- Demonstrated understanding: topic — evidence and date ...
- Unclear or needs recheck: ...
- Latest assessment: date, task, result, limitations ...
- Practice evidence: task, inspected output, result, limitations ...
- Capability states: outcome — Verified / Unverified / Needs reinforcement; evidence ...
- Notes requested/generated: type and location, or none ...
- Recommended next step: ...
- Course outline or source: ...
```

## Personal preferences and evolution state

Keep learner-specific preferences and any user-approved evolution proposal/status in the same user-controlled private record or another user-approved private Markdown record, separate from reusable Skill rules. Store only confirmed preferences as defaults; distinguish a one-time instruction from a continuing preference. A preference entry may state the preference, scope, date/source and whether it is learner-confirmed. Do not turn individual preferences into shared defaults. Evolution owns the proposal and validation method; this workflow only stores agreed state and evidence pointers when the learner requests or agrees to persistence.
