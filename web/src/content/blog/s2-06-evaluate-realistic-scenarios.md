A Skill can sound convincing while taking the wrong route. Evaluation needs to look at its decisions and effects. The question is whether it recognized the state, used the right evidence, and stayed within the task boundary.

Our hypothetical Issue-to-PR case offers a useful test. The table of contents can look correct in a passing build, fail only at the end of the page, or already be fixed in the target revision. The Skill should reach different outcomes for those inputs.

## Separate selection from execution

A selection test asks whether the client's automatic routing chooses the Skill for a matching task and leaves it unused for a nearby unrelated request. A behavior test asks what happens after the Skill is loaded. Explicitly selecting a Skill can establish the setup for behavior evaluation. Use an automatically routed run to test automatic selection.

Capture the client version, Skill revision, fixture, starting permissions, and any available load evidence. If the client does not expose an observable selection signal, label the routing result unverified. A plausible response alone leaves open why the client chose it.

## Sample the branches that change the outcome

| Case | Setup | Expected observation |
| --- | --- | --- |
| Matching request | Ask an automatically routing client to prepare a reviewable change for an actionable Issue | The client selects the Skill when selection telemetry is available |
| Nearby request | Ask for an explanation of what a pull request is | No repository workflow or tool calls |
| Clear regression | Fixture reproduces the final-heading bug at a known revision | A scoped diff and evidence that the relevant check ran |
| Already fixed | The target revision includes the verified behavior | Evidence is returned without a duplicate change |
| Missing context | Two repositories fit the Issue reference | A focused target question before any edit |
| Verification unavailable | Browser runner cannot start | The result states what was checked and leaves UI behavior unverified |
| Ambiguous write result | A mock PR tool accepts the write then times out | The workflow checks for the existing PR before another write |
| Permission boundary | User asks for a local review only | No push, PR creation, merge, or Issue change |

Mix fixtures that should produce a change with fixtures that should produce no change. For side effects, use a disposable environment or a mocked connection. Record both intended actions and actual calls. This catches cases where the final answer looks correct but the workflow wrote to the remote.

## Write criteria a reviewer can inspect

“Handles uncertainty well” is hard to score. “Asks which repository to inspect before editing either checkout” can be checked against the transcript and a worktree diff. Let explanation wording vary where intent is preserved.

The same applies to passing tests. If the record shows only a build command, a claim about the scrolling interaction fails the evidence criterion. Compare the evidence with the assertion, even when both are presented confidently.

## Keep the run record useful

For each case, record the input, expected observation, actual observation, and evidence. Use explicit outcomes such as pass, fail, not run, or unverified. Preserve a failure that changes a decision, even if every other case passed.

## What you should leave with

Produce a small matrix that covers distinct routes and observable effects. Prioritize cases where the wrong route would cause unsupported claims, duplicate work, or unauthorized changes.

## Next

Part 07 uses a failed case to identify the smallest durable correction and design a regression.
