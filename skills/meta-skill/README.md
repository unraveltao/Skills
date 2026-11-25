# Meta Skill

Meta Skill is a personalized, evidence-driven workflow for engineering reusable Agent Skills across compatible Agent environments.

It covers the full lifecycle: **Discover → Design → Build → Test → Observe → Evolve**. It starts from real user work, makes important design trade-offs explicit, builds a bounded package after design approval, and improves it using test results and observed feedback.

## When to use it

Use Meta Skill when you want to create a new Skill, substantially improve an existing Skill, investigate incorrect activation or execution, or establish a repeatable testing and evaluation process.

Do not use it for general explanations about Skills or to execute an ordinary task with an existing Skill.

## What it does

1. Discovers reusable steps and stable decision rules from real examples.
2. Checks whether a Skill is the right artifact and looks for overlap with existing solutions.
3. Classifies the design as platform-agnostic, platform-specific, or hybrid.
4. Separates portable core behavior from tool adapters and runtime-specific requirements when useful.
5. Produces a user-reviewable behavior specification and acceptance criteria.
6. Builds an independently installable package after the design is approved.
7. Separates static checks, routing tests, scope tests, behavior tests, and regression tests.
8. Records evidence, metrics, failures, user corrections, and version changes.
9. Proposes focused improvements and re-tests the affected behavior.

## Design principles

- Prefer the smallest useful Skill over a large framework.
- Material decisions include meaningful options, benefits, downsides/risks, and a reasoned recommendation.
- Confirmed facts, assumptions, inferences, and unresolved questions remain distinct.
- Platform portability is never assumed; tool and runtime dependencies are explicit.
- Usage counts are adoption signals, not quality scores.
- Git is the source of truth for authored Skill packages. Notion is used for experiment records and decision history when available.
- Tests that cannot be run in a real target client remain **NOT RUN** or **UNVERIFIED**.

## Safety boundaries

Meta Skill does not grant tool access or permissions. It does not silently modify production Skills, install, enable, publish, distribute, merge, delete, or change access. These actions require explicit user approval.

A new package may be built in an isolated branch or workspace after its design is approved. Existing production Skills remain unchanged until the user approves a specific change.

## Package contents

- [SKILL.md](SKILL.md) — authoritative workflow and safety boundaries.
- [Observability Model](references/observability.md) — evidence levels, metric definitions, and provenance.
- [Manual validation scenarios](tests/README.md).
- [Experiment report template](tests/REPORT_TEMPLATE.md).
- [Package validator](tests/validate_package.py) — local structural/link checks; it does not test Agent routing or runtime behavior.
- [OpenAI Agent metadata](agents/openai.yaml).

## Validation status

Initial V0.1 package. The bundled validator is intended to check package structure and local references. Real-Agent routing and post-trigger behavior have not yet been tested in an independent client session.

## Version

0.1.0 — initial full-lifecycle implementation.
