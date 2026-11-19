# Reader & Product Understanding

## Purpose and inputs

Choose a clear reader priority before designing a complete README. Use the confirmed Project Understanding Brief, existing README/docs, explicit user intent, and evidence. This module is unnecessary for a trivial targeted edit unless the reader decision materially affects wording.

## Separate three views

- **Current Reality** — capabilities and behavior supported by implementation/configuration and actual verification evidence. Distinguish implemented, partial/in development, and unverified.
- **Creator Intent** — purpose, audience, and value the user says they intend. Label user-provided statements; do not present them as implemented facts.
- **Future Vision** — desired future capabilities, explicitly marked as future if included. Do not let it dominate current onboarding unless the user confirms that emphasis.

## Recommend a reader model

Recommend, then let the user decide:

- one **Primary Reader**;
- one **Primary Reader Goal**;
- relevant secondary readers and their likely needs;
- concise product positioning and value proposition;
- main use cases and a reader journey from discovery to first useful outcome.

Ground the recommendation in product type, actual entrypoints, existing documentation and user intent. Separate a **Feature** (what the product does) from a **Benefit** (why that matters to a reader); do not invent either.

## Reality and intent conflicts

Rate material conflicts:

- **P0** — blocks the affected decision/claim. Pause only that decision; independent work may continue.
- **P1** — needs resolution or careful qualification before publishing affected wording.
- **P2** — non-blocking; document as an assumption or candidate wording.

Give the evidence on each side, likely reader impact, and a recommendation. Ask one focused question when a user decision changes the outcome. Do not force a complete interview for facts already established.

## QD and approval

Use Question-Driven interaction: analyze first, recommend, and ask only about important uncertainty. Ask one key question at a time. Bundle only independent low-cost questions when useful; never ask the user to repeat known information. Make assumptions explicit and revisable.

For complete CREATE/REWRITE flows, present the Reader & Product Brief and wait for explicit confirmation before architecture. A user's correction updates the brief; do not silently override it. Confirmation accepts the reader/product direction, not permission to modify files.

## Brief format

```text
Reader & Product Brief
- Current Reality:
- Creator Intent:
- Future Vision (if relevant):
- Primary Reader / Goal:
- Secondary readers:
- Positioning / value (evidence and inference distinguished):
- Use cases and reader journey:
- Conflicts and P0/P1/P2 status:
- Assumptions / open decision:
```

Include only material details, and identify user-confirmed decisions.
