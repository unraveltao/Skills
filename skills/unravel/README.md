# Unravel

Unravel helps you build a mental model of a concept, system, process, product, Skill, claim, or design. It explains how relevant parts fit together, what mechanisms or causes matter, and where the available evidence ends.

## When to use it

Use Unravel to understand what something is made of, how it works, why it was designed a certain way, or what evidence supports a claim. It follows conversation context, the user's language, and requested depth.

Do not use it to turn an ordinary execution request, such as editing a file or running a test, into an unsolicited lesson. A direct question should be answered directly rather than forced into an interview or quiz.

## How it explains

Unravel starts with a short overview and a useful map when one helps. It selects a lens suited to the subject: concepts, systems, processes, mechanisms, products/designs, or evidence-based claims. A small diagram, concrete example, or comparison may help explain relationships.

It uses supplied material and conversation context to resolve references before asking the user to repeat information. If ambiguity would materially change the answer, it asks one concise question. For claims about effectiveness or popularity, it separates observed facts from inference and treats correlation or adoption alone as insufficient proof of causation.

The Skill adapts when an explanation does not land and stops when the user has a useful mental model or remaining uncertainty is explicit.

## Evidence and limits

Unravel does not promise complete knowledge of every subject. For current, source-specific, popularity, or causal claims, it should inspect primary material and trustworthy evidence when tools permit, cite claims near sources, and label fact, inference, assumption, or unknown where relevant. If research is unavailable, it should say so instead of inventing evidence.

## Package contents and validation

- [SKILL.md](SKILL.md) defines triggers, workflow, style, and evidence boundaries.
- [Test notes](tests/README.md) describe manual behavior checks and a historical validation note. They are not proof of current routing or runtime behavior.

The test document records static review but says real-agent behavior was Not verified in its 2026-11-15 note. This README does not claim installation, triggering, or behavior has been verified. Manual checks should be run in a session with the Skill loaded and results recorded.

The package declares the unravel Skill name and MIT license in SKILL.md; no bundled runtime or external dependency is declared.

The historical validation notes were reviewed. This pass did not rerun the manual behavior checks in an independently loaded Skill session. See the [repository validation matrix](../../docs/development/skill-validation-matrix.md) for the setup, expected checks, and remaining gaps.
