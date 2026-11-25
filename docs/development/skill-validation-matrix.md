# Skill validation matrix

This pass tracks the evidence required by [Issue #71](https://github.com/unraveltao/Skills/issues/71). It keeps executable checks, source inspection, historical results, and live Agent behavior distinct. **Not run** means there is no execution result for this pass.

| Skill | Check type and setup | Expected observable result | Actual and evidence |
| --- | --- | --- | --- |
| [Disk Governance](../../skills/disk-governance/README.md) | SQLite regression in disposable directories with `#`, `%`, and a space. Python 3.13.17, SQLite 3.50.4. | Open the intended database read-only, read a seeded row, deny writes, and leave the file unchanged. | Passed for all three paths. Previous isolated scan, status, and offline report evidence is recorded in [PR #72](https://github.com/unraveltao/Skills/pull/72). Live activation not run. |
| [Download Organizer](../../skills/download-organizer/README.md) | Contract suite using temporary fixtures on Windows PowerShell 5.1.26100.9818. Static inspection of the cross-volume branch. | Preserve command envelopes, perform the authorized fixture move, reject unapproved and outside-root operations. Cross-volume handling should hash-check the copy, keep the source, and report `Copied`. | 19 passed, 0 failed, 0 skipped. Runtime and safety documentation agree on cross-volume handling. Actual transfer across volumes and live activation not run. See the [test script](../../skills/download-organizer/tests/test-organizer.ps1). |
| [Git Workflow](../../skills/git-workflow/README.md) | Historical guide validation in [PR #56](https://github.com/unraveltao/Skills/pull/56). Live routing would require an isolated repository and a separately loaded Skill. | Select the appropriate read-only or explicitly authorized Git workflow for the request. | Historical evidence identified. Commands and live routing not rerun during this pass. |
| [GitHub Project Coach](../../skills/github-project-coach/README.md) | Manual behavior check in a separately loaded Skill session with a fixed public repository or Gist. | Ground the explanation in accessible source and give a usable first step. | No package suite found. Manual behavior not run. |
| [Idea Advisor](../../skills/idea-advisor/README.md) | Manual cases T1–T8 in a separately loaded Skill session. | Clarify meaningful uncertainty and present grounded options and a recommendation. | [Scenario definitions](../../skills/idea-advisor/tests/README.md) inspected. Behavior not run. |
| [Learning Coach](../../skills/learning-coach/README.md) | README scenarios in a separately loaded Skill session with a disposable progress record. | Teach, assess observable evidence, and distinguish resuming with a record from starting fresh. | Suggested scenarios identified. No package suite or current behavior result found. |
| [QD Meta-Skill](../../skills/qd-meta-skill/README.md) | Manual cases T1–T13, including trigger and scope cases. | Recognize eligible Skill design requests and produce a bounded design with a validation plan. | [Scenario definitions](../../skills/qd-meta-skill/tests/README.md) and [status record](../../skills/qd-meta-skill/tests/REPORT.md) inspected. Independent behavior not run. |
| [README Skill](../../skills/readme/README.md) | Manual cases T01–T14 against controlled fixture repositories. | Base README recommendations and edits on repository evidence, with verification gaps stated. | [Scenario definitions](../../skills/readme/tests/scenarios.md) inspected. Behavior not run. |
| [Unravel](../../skills/unravel/README.md) | Manual checks using the package's examples and historical validation record. | Explain a system with an appropriate level of depth and state what the evidence supports. | [Historical notes](../../skills/unravel/tests/README.md) identified. Live behavior not rerun. |

## Reproduction

- **Disk Governance:** From the package directory run `python -B -m unittest discover -s tests -v`. The SQLite regression covers paths containing `#`, an escaped percent sequence, and a space. The stored marker remains readable, writes are denied, and database bytes are unchanged.
- **Download Organizer:** From the package directory run `powershell -NoProfile -ExecutionPolicy Bypass -File .\tests\test-organizer.ps1`. The checked-in suite verifies the fixture path before recursive cleanup. The 19 contract assertions and their fixtures are unchanged.

## Remaining validation

For live behavior, capture the client version, evidence that the Skill loaded, the prompt and fixture, and the observed result for each case. Validate the cross-volume path separately with disposable fixtures on two writable volumes.
