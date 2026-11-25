An evaluator reports that the hypothetical Issue-to-PR Skill called the table-of-contents fix verified even though the browser never started. The build had passed. Three explanations are plausible: the workflow accepts a build as sufficient evidence, the instructions mix two kinds of checks, or the runner never reported that it failed to start.

A durable fix begins by locating the first point where the run diverged from the expected path.

## Keep the failed run intact

Record the request, target revision, Skill revision, fixture, and available permissions. Keep the tool responses and the point at which the workflow made its claim. A later rerun may succeed and still leave the first failure unexplained.

For this case, the expected result is a scoped diff and an explicit statement that scroll behavior remains unverified when the browser is unavailable. The observed result is a passing build plus an unsupported claim about the interaction.

## Locate the first wrong decision

<figure>
  <img src="/@blog-assets/skill-failure-regression.svg" alt="A failed run goes through trace inspection, a focused correction, and a case pair that checks both the failure and normal path." loading="lazy">
  <figcaption>Diagnose from the first observable divergence, then test both sides of the decision.</figcaption>
</figure>

| Layer | Diagnostic question | Candidate correction |
| --- | --- | --- |
| Task model | Does the verification stage represent different types of evidence? | Give each claim its required evidence and separate the outcomes |
| Instructions | Is the rule available at the point where the Skill makes the claim? | Move or clarify the rule at the verification step |
| Tool or integration | Does the runner distinguish failure to start, test failure, and a passing result? | Preserve the runner status and map it explicitly |
| Environment | Could this client execute the intended check on this fixture? | Restore the environment or report that the check could not run |

Change one relevant condition at a time. Run the same fixture with and without the browser available. If the tool records that launch failed and the Skill still claims success, the failure lies after the tool response. If that status is missing from the output, inspect the integration before rewriting instructions.

## Fix the decision rule

A rule about a specific error phrase will fail as soon as the environment reports a different message. Express the underlying decision in terms of observable state: “Claim scroll behavior was verified only if a relevant browser case actually ran and passed. If it did not run, report the build outcome separately.”

The patch should reach the faulty layer. Adding two paragraphs to the prompt leaves the underlying ambiguity in place if the runner outputs a single generic success flag for every build and browser check.

## Keep two sides of the regression

| Scenario | Expected result |
| --- | --- |
| Build passes and browser launch fails | Build reported as passed. Scroll behavior remains unverified |
| Build passes and relevant browser case passes | Scroll behavior reported as observed, with the revision and fixture |
| Browser starts and the case detects incorrect highlighting | Report the observed behavior as a test failure and return to investigation |
| A different Issue has no interactive behavior to verify | Use the checks relevant to the claim, without requiring a browser by default |

Review the first case that failed, an adjacent case, and the normal path. This catches a correction that unconditionally reports “unverified” or makes every task depend on a browser.

Overfitting means shaping the correction around incidental details of the failing example. Hold back a few cases when designing the fix. For example, after correcting a browser launch failure, try a runner that opens the page but times out before the assertion. In a fresh, different fixture, try a successful browser run with a skipped related test. The Skill should report the evidence its claim actually requires without relying on the original error message or fixture name.

## What you should leave with

Write a failure record with the first divergent decision, its evidence, the smallest correction, and a regression set that shows when the corrected rule applies.

## Next

Part 08 turns those cases and the remaining limitations into release and maintenance criteria.
