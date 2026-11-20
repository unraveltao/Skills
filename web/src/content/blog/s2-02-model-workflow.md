The previous article helped us identify stages, decisions, and states in a complex task. That task map shows what can change; it does not yet say how the Skill should move through those changes.

Now we will turn the map into a workflow: where the work begins, how each result leads to the next step, and when to continue, recover, or stop.

We will keep using the hypothetical GitHub Issue-to-PR workflow as a teaching example. This article is about the design method, not implementing that Skill.

## A task map is not yet a workflow

A task map helps us inventory the work:

- What stages are involved?
- Which decisions can change the next step?
- What blocked or failure states can occur?

A workflow goes further:

- What state is required to enter each stage?
- What result should the stage produce?
- Which observable condition selects the next route?
- Where should the work go if that condition is not met?

For example, “verify the fix” is a stage. The workflow must distinguish its possible outcomes:

- Verification passes: review the change.
- Verification fails and the change may be responsible: investigate, adjust, and verify again.
- The verification tool is unavailable: record the limitation; do not claim the fix was verified.
- The failure is outside the task scope: stop and report the evidence and blocker.

These routes cannot be captured by “handle problems as appropriate.” The Skill needs a basis for deciding what to do and a clear handoff when it cannot proceed.

## Write the normal path first

Describe the most common route when the task is clear and the required information is available. This is the main path; other routes branch from it.

For the Issue-to-PR example, the main path might be:

1. Understand the reported problem and expected behavior.
2. Inspect the relevant code and confirm that the problem still exists.
3. Find a cause that explains the observed behavior.
4. Plan a focused fix.
5. Run checks relevant to the change.
6. Review the change and prepare the authorized handoff.

This is not complete until each stage has an **observable exit condition**.

For example, “find the root cause” should not mean that the Skill has a plausible theory. A stronger condition is that the cause explains the report and is supported by code, reproduction, or other evidence.

Clear exit conditions make the next step easier to choose. Vague exit conditions let the Skill move forward without enough evidence.

## Branch when a decision changes what happens next

Not every unusual event needs its own elaborate route. Add a branch when different outcomes require different next actions.

| Decision | Condition | Next route |
|---|---|---|
| Is the report actionable? | Key reproduction details are missing and cannot be confirmed from the available context | Ask a focused question or report the blocker |
| Does the problem still occur? | Current code already matches the expected behavior | Gather evidence and report; avoid a duplicate change |
| Is the cause supported? | The explanation is only a guess | Investigate or report uncertainty |
| Did verification pass? | Relevant checks passed | Review the change |
| Can the failure be recovered? | A transient tool failure may succeed on a bounded retry | Retry safely and record the result |
| Is the next action within scope? | Work would expand the change or exceed authorization | Stop and ask for direction |

A useful test is: **if the condition changes but the next action stays the same, it may not need to be a separate branch.** Keep the workflow focused on decisions that change the route.

<figure>
  <img src="/@blog-assets/series-02/s2-02-workflow-branches.svg" alt="Issue-to-PR workflow showing the main route and branches for clarification, an already-fixed issue, uncertain root cause, failed verification, and user handoff.">
  <figcaption>Figure 1. A workflow makes the normal route and its decision branches visible.</figcaption>
</figure>

## Design stop and handoff routes

A workflow does not always continue. Sometimes the right next step is to ask the user, report a blocker, or return control.

For this example, stop when:

- The Issue lacks key context and the available materials cannot fill the gap.
- The cause is not supported by evidence, so further edits would be guesses.
- The fix would expand beyond the requested scope.
- Verification cannot run or cannot support a completion claim.
- The next action is outside the user’s authorization.

Stopping is not a workflow failure. Continuing without evidence is what makes the result unreliable.

A stop route should specify what to hand back: what was inspected, what is known, what remains uncertain, and what decision is needed. This makes it possible for the user or another agent to resume the task.

## Add bounded recovery paths

Some failures can be recovered from; others cannot be fixed by repeating the same action. The workflow should distinguish them.

A bounded recovery can make sense when an external tool has a temporary error, a command times out without an uncertain side effect, or verification reveals a focused defect in the current change.

Repeated failure without new evidence is different. So is an incomplete tool result that leaves it unclear whether an operation already happened. In those cases, blindly retrying can make the situation worse.

A recovery route can follow this sequence:

1. Classify the failure.
2. Record the evidence that supports the classification.
3. Choose a limited recovery action.
4. Check whether recovery worked.
5. Stop and report if the task still cannot proceed.

The goal is not to make the Skill continue forever. Each attempt should have a reason; when the evidence runs out, the Skill should stop safely.

## Make the workflow inspectable

A compact text flow can connect the normal route, branches, and recovery paths:

```text
Start
  → Understand the Issue
      → Not enough context: ask a focused question or report the blocker
      → Enough context: inspect the repository
  → Does the problem still occur?
      → No: report the evidence; do not make a duplicate change
      → Yes: investigate the cause
  → Is the cause supported by evidence?
      → No: investigate further or report uncertainty
      → Yes: make a focused change
  → Run relevant verification
      → Pass: review the change and prepare the handoff
      → Fail: classify the failure; recover safely or stop
  → Deliver within the user's authorized scope
End
```

Each arrow should correspond to a condition someone can check. “Continue when it seems appropriate” does not help because “appropriate” has no observable meaning.

## Check the workflow for gaps

Walk through the design using several different scenarios:

- The Issue is clear, the problem reproduces, and verification passes.
- Reproduction details are missing.
- The repository already contains a fix.
- The cause cannot yet be confirmed.
- Verification fails after the change.
- The verification tool is unavailable.
- The work would need to expand beyond the requested scope.

For each scenario, ask:

1. What state will the Skill recognize?
2. What will it do next, and what evidence supports that choice?
3. If it stops, what information will it hand back?

If any scenario has no clear answer, the workflow has a gap. If many scenarios lead to the same action, simplify the design rather than adding branches for every minor variation.

## What you should leave with

After this article, you should be able to turn a task map into a reviewable workflow that includes:

- A normal path with exit conditions for each stage
- Branches for decisions that change the next action
- Clear stop, clarification, and handoff routes
- Limited recovery steps for recoverable failures
- Representative scenarios for finding workflow gaps

You still do not need to write the complete `SKILL.md`. Design the workflow first; it will make the required inputs, context, and clarification rules easier to define.

## Next

In the next article, we will define the input and context contract: what the Skill should read, what it should ask for, and how it should avoid treating unknown information as fact.
