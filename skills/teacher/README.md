# Teacher

> Experimental · V0.1 — candidate for controlled trials. The instructions and validation scenarios are present; independent client loading and full behavioral acceptance remain unverified.

Teacher is a focused instruction-based Agent Skill for explaining concepts, leading coherent interactive lessons, adapting to learner feedback, and conducting learner-led review. It can be installed independently; it does not create a separate GPT or require a runtime program.

## When to use it

- Learn a concept, continue a lesson or resolve a specific misunderstanding.
- Request a small guided experiment, diagram or reasoning challenge.
- Review a unit with your own explanation, Feynman-style role reversal or a milestone synthesis.

Learning Coach is the broader companion for curriculum planning, project practice, formal assessment, knowledge notes and private progress management. Teacher is not a replacement for that workflow. If both are installed, explicitly request Teacher for lesson interaction and Learning Coach for learning-path coordination.

## Install and try

Copy the entire `skills/teacher/` directory into a Skill-compatible client's configured location; reload if required and verify discovery. Exact installation and available rendering vary by client. No API keys, external services, scripts or personal learning records are required.

Example requests: "Use Teacher to explain HTTP proxying with one coherent example"; "Review today's lesson with me using role reversal; don't give away the answers"; "Explain a feedback loop using a diagram, or a text alternative if diagrams are unavailable."

## Package

- [SKILL.md](SKILL.md) — authoritative routing and teaching loop; D-T001 and D-T002.
- [Review and assessment](references/review-and-assessment.md) — D-T003, D-T006, D-T007.
- [Visual teaching](references/visual-teaching.md) — D-T005.
- [Evolution](references/evolution.md) — D-T004.
- [Behavior scenarios](tests/scenarios.md) — reproducible manual acceptance plan, not passed tests.

## Limits and validation

Personal learning records are private and separate. Teacher does not silently save notes or change its own rules, run background work, grant tool permissions or guarantee mastery. Visuals and runnable code depend on actual tools. This V0.1 is an implementation candidate based on approved design; the scenarios still need independent real-client execution. See [LICENSE](LICENSE).
