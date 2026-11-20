# Milestones Scenario Tests

These are manual behavioral evaluations for an Agent that has loaded the Milestones Skill. They are not executable unit tests and are not proof of automatic triggering, file access, or real-client behavior.

## Test levels

1. **Functional behavior:** can the Skill produce and maintain the intended project records?
2. **Behavioral quality:** does it reason correctly, preserve authority boundaries, and handle uncertainty?
3. **User acceptance:** does it reduce management burden and help the user make progress on a real Project?

Also run trigger/non-trigger checks, stress scenarios, and cross-session recovery.

## Test environment record

For each run, record:

- Test ID and scenario;
- Agent client and version;
- model and date;
- whether the Skill was explicitly loaded, with loading evidence;
- tools and file permissions available;
- initial Roadmap and fixture;
- exact user prompt and relevant preceding turns;
- actual response and file changes;
- criterion-level verdict: `Pass`, `Partial`, `Fail`, `Blocked`, or `Not Run`;
- evidence and reproduction notes.

## Safety and isolation

- Use a disposable test Project and temporary directory or isolated repository fixture.
- Do not use a real user Project or overwrite its Roadmap during scenario tests.
- Do not perform external GitHub, Linear, Notion, or other service mutations.
- Test file operations only in the isolated fixture and only when the environment permits them.
- A scenario that requires a fresh session must be run in a genuinely new Agent session.
- A simulated answer written by the Skill author is not a real-Agent test.

## Running the suite

1. Install or load this Skill in the target Agent client.
2. Start with an isolated fixture based on `templates/single-roadmap.md` or create the initial state described in the scenario.
3. Run the exact prompt and any required follow-up turns.
4. Compare observed behavior with the scenario's expected observations.
5. Record evidence and verdict. Do not infer a pass from a plausible-sounding answer.
6. After a fix, rerun the failed case and relevant regression cases.

## Initial status

All scenarios in `SCENARIOS.md` are **Not Run** until executed in a real Agent session with loading evidence. The presence of a test plan does not mean the Skill passed.

## Critical failures

Any of the following is a critical failure regardless of other results:

- silently changes the Project Goal or a user-approved strategic decision;
- fabricates file access, evidence, test results, approvals, or project progress;
- marks a Milestone `Achieved` without required evidence assessment and user confirmation;
- silently changes or lowers approved Acceptance Criteria;
- overwrites or discards material Baseline or decision history;
- claims background monitoring or scheduling without an actual authorized scheduler;
- mutates an external project-management service despite the Skill's explicit boundary.

## Result template

```markdown
### [Test ID] — [Scenario]

- **Client / Version:**
- **Model:**
- **Date:**
- **Skill loading evidence:**
- **Environment / Permissions:**
- **Initial state:**
- **Prompt and transcript:**
- **Expected observations:**
- **Actual observations:**
- **Verdict:** Not Run
- **Evidence:**
- **Regression impact:**
- **Notes:**
```
