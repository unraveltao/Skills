# Idea Advisor

Idea Advisor helps turn an unclear idea for a Skill, product, tool, or technical project into a considered design and a useful next step. It advises on design decisions; it does not implement the product.

## When to use it

Use this Skill to shape an unclear idea, compare building with adopting an existing solution, research relevant projects or constraints, define scope and acceptance criteria, prepare an implementation handoff, or revisit a design decision as requirements change.

A direct tool explanation, tutorial, or implementation task is a different request. The Skill uses context to distinguish those tasks from designing a product or Skill.

## What it can produce

Depending on the decision, it may provide a problem definition, research findings with sources and limitations, a comparison and recommendation, a scoped requirement document, acceptance criteria, a decision record, or an implementation handoff. A small question may need only a concise recommendation; not every task needs every artifact.

## How it works

The Skill uses an adaptive loop:

1. Explore goals, context, constraints, and desired outcome.
2. Research when external facts could change the recommendation.
3. Compare viable alternatives against the user's priorities.
4. Recommend a direction while making assumptions and uncertainty visible.
5. Deliver the smallest useful answer or handoff.

It reuses context and asks questions only when an answer could materially change the design. It may skip, combine, or revisit stages.

## Boundaries and limitations

- It advises on design; it does not implement a product or manage its delivery.
- Research depends on available browsing and connected tools; unavailable evidence should be disclosed.
- Decision records require an available, user-approved place to save them. The Skill does not assume persistent memory or filesystem access.
- Recommendations depend on available evidence and context; users should review consequential decisions.

## Supporting files

- [Skill instructions](SKILL.md)
- [Adaptive workflow](references/workflow.md)
- [Research guidelines](references/research-guidelines.md)
- [Decision management](references/decision-management.md)
- [Deliverables](references/deliverables.md)
- [Decision record template](templates/decision-record.md)
- [Design handoff template](templates/design-handoff.md)

## Validation status

The repository includes [manual scenario evaluations](tests/README.md). These are behavioral evaluation scenarios, not executable unit tests. They were not run for this README update; their presence does not show that the Skill passed real-Agent testing. Record the client, session, scenario, and evidence that the Skill was loaded when reporting behavior results.

See the repository [Installation guide](../../docs/getting-started/installation.md); installation and discovery vary by client. MIT licensed; see [LICENSE](../../LICENSE).

The T1–T8 scenario specifications were identified. They were not run in an independently loaded Skill session. See the [repository validation matrix](../../docs/development/skill-validation-matrix.md) for the setup, expected checks, and remaining gaps.
