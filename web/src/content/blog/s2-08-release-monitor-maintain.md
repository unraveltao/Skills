A Skill is ready for people to rely on when its supported behavior can be explained, observed, and maintained. A polished entry point and one successful demonstration are useful evidence for particular claims. A release decision has to account for the boundaries of that evidence.

For the hypothetical Issue-to-PR Skill, the release candidate claims that it can assess a scoped Issue and prepare a reviewable handoff after appropriate checks. Publishing and merging depend on the user's authority and the repository policy.

## Write down the supported promise

Name the client or clients whose behavior you actually checked. State which modes were exercised. For example, “Explicitly selected in Client A, with local edits and a draft review description tested” leaves room to identify automatic routing, network access, and remote writes as separate capabilities.

Keep configuration and version information with the evidence. A changed client, tool schema, or repository policy can alter behavior without a change to the Skill's instructions.

## Use a release checklist that cites evidence

| Check | Evidence to inspect | Decision if evidence is missing |
| --- | --- | --- |
| Installation and discovery | Client version, installation path, and observable load or invocation | Limit the compatibility claim to the tested installation and client |
| Main workflow | Representative case with target revision, scoped diff, checks, and handoff | Hold the behavior claim until the run exists |
| Stops and permission boundaries | Negative cases and observed tool actions | Fix the boundary or limit the supported scope before release |
| Known failures | Regression set and open limitations | Record the remaining risk and choose an owner for the follow-up |
| Package and documentation | Entry point, referenced resources, scripts, examples, and change notes | Correct broken paths and stale claims |
| Authority to publish | Approval or policy applicable to the specific release | Prepare a version and review material for the authorized decision |

Test the package that will be shipped. A run against an older checkout can support a historical claim. Tie present release claims to the candidate revision and environment.

## Set a maintenance trigger and a response

Feedback should come with enough context to reproduce the issue. Request the client and Skill version, a redacted prompt, the task state, the expected outcome, and what happened. Collect only the information needed for the follow-up.

Suppose a new client version stops exposing a routing signal. The Skill may still work when selected explicitly. Update the compatibility record, rerun explicit and automatic cases independently, and mark automatic routing unverified where evidence is unavailable. If a permission boundary changes or a write happens unexpectedly, pause the affected use and recheck the relevant negative cases before expanding usage.

Use a change log that records behavior differences, migrations or configuration changes, and the test evidence for published claims. Keep the last known usable revision identifiable so a maintainer can evaluate restoring it if a release causes a regression.

## Close the loop from Issue to release

The first part of this series mapped decisions hidden inside a checklist. Our Issue-to-PR example now has an input contract, a permissions matrix, a package map, an evaluation matrix, and a regression process. The release checklist ties each supported promise back to one of those artifacts.

In your own Skill, identify one consequential claim you plan to make. Find the run that supports it and the regression that would detect if it stopped being true. Where evidence is missing, narrow the claim or complete the missing check.

## What you should leave with

A release decision with the supported scope, evidence, limitations, and approval, plus a maintenance record with clear triggers for reevaluation.
