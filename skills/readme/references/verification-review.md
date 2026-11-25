# Verification & Review

## Purpose

Check a README draft, change, or existing file using evidence. Verification is conditional on scope, environment, safety, and authorization; never imply that AI review or a document claim is an executed test.

## Select checks across five layers

### L1 — Structural Validation

Check Markdown structure/render-sensitive syntax, heading hierarchy, fenced code blocks, anchors, relative links, and image/resource paths. Identify target renderer constraints where known. Use static tools only if available and authorized.

### L2 — Factual Verification

Check consequential claims: capabilities, commands, APIs/examples, configuration, dependencies/versions, platforms, project maturity/status, license, performance and release statements. Trace each claim to source/config/docs/user statement or executed evidence. A file existing does not prove a claim; tests existing do not mean tests passed; docs claims do not prove implementation.

### L3 — Functional Verification

When relevant, run only the narrow necessary command if the environment is available, the user authorized execution, side effects are understood, and execution is safe. Prefer an isolated fixture. Never execute destructive or opaque commands to make a Quick Start appear verified. Record exact command, context, exit/result and limitations. If skipped/unavailable, mark **NOT RUN** and explain.

### L4 — Reader Experience Review

Evaluate whether the confirmed Primary Reader can identify the project, find the primary action, understand prerequisites and likely outcome, and reach deeper information. Check terminology, scanability and whether visuals help. An AI reader simulation is not real user research.

### L5 — Change Safety Review

Compare the diff with authorization and approved plan. Check that useful existing information was preserved, moved content has a valid destination, only intended files/resources changed, and no secrets/private paths, dangerous instructions or unrelated edits were introduced. Escalate consequential uncertainty rather than hiding it.

## States and overall delivery

Use one status per applicable check:

- **PASS** — checked and supported evidence satisfies the criterion.
- **FAIL** — checked and a concrete defect exists.
- **UNVERIFIED** — not enough evidence to determine correctness.
- **NOT RUN** — a planned execution/check did not occur; state why.
- **N/A** — not relevant to this task.

Overall state:

- **VERIFIED** — applicable critical checks have evidence and pass, with no material unresolved blocker.
- **CANDIDATE** — useful output is ready but one or more material checks are unverified/not run, or disclosed issues remain.
- **BLOCKED** — required user decision/permission or a blocker prevents a safe, complete result.

Do not mark a check PASS because a test file exists, because an example looks plausible, or because a user approved content. Do not alter criteria or remove important facts merely to turn FAIL into PASS.

## Fix and recheck

Fix only issues within the user's edit authorization and approved structure. Re-run affected checks after a fix; do not claim a full suite unless it ran. If a fix requires broader deletion, migration, changed positioning, a new resource, or a command beyond authorization, pause the dependent change and show the concrete choice. Preserve the original facts and report any remaining defects.

## Verification Report format

```text
Verification Report
- Target and snapshot:
- Scope / authorization:
- L1 Structural: status — evidence/result
- L2 Factual: status — evidence/result
- L3 Functional: status — command/result or NOT RUN reason
- L4 Reader experience: status — review basis (mark simulated)
- L5 Change safety: status — diff/scope result
- Fixes and rechecks:
- Overall: VERIFIED / CANDIDATE / BLOCKED
- Remaining issues and limitations:
```

Omit or combine N/A layers when concise, but disclose all material unrun checks and evidence gaps.
