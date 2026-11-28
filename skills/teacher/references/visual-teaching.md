# Visual Teaching

## D-T005 — Purposeful and adaptive visualization

Use visuals proactively when they make a mechanism, comparison, relationship, sequence or change easier to understand. Do not require a visual for each unit or response. A simple explanation may be clearer in text.

| Teaching need | Preferred representation |
| --- | --- |
| Components and relationships | Structure or knowledge map |
| Steps, branching or interaction | Flowchart or sequence diagram |
| Change, scale or quantitative comparison | Chart with units and assumptions |
| Feedback, causality or mechanism | Labeled schematic or cycle |
| Dynamic behavior | Interactive simulation, animation or prediction experiment |
| Concrete unfamiliar object or interface | Relevant verified image or actual screenshot |
| Exact values or alternatives | Table |

Use available host capabilities only. Prefer exact structured diagrams (SVG, Mermaid or equivalent) for precise relationships and programmatically derived charts for numerical data. If interactive visualization is supported, optionally let the learner change a parameter, predict an outcome and verify it; do not assume the model receives client-only state. If interactivity, rendering, image generation or external imagery is unavailable, degrade to a static diagram, table, ASCII/Markdown representation or concise prose. A visual is not required to answer a learner who prefers speech or plain text.

## Design and validation

- Choose the simplest accurate representation; place it near its explanation. Use concise, meaningful labels, clear arrows and a short caption stating what the diagram demonstrates. Include accessible text alternatives where appropriate.
- Check relationships, ordering, branches, units, calculations and assumptions against the source or example. Mark hypothetical data and simplified diagrams. Avoid invented measurements, misleading scales, decorative clutter, or depicting proposed implementation as real.
- Connect the visual to a teaching action when useful: ask the learner to predict a missing step, compare curves, trace a request, explain an arrow, or identify a failure. Do not supply a revealing diagram before a recall question unless it is a deliberate hint.
- Keep visual output proportional to the goal. In learner-first review, prefer natural conversation and use a visual for a real gap or final synthesis, not automatically after every answer. If the learner cannot see the visual, describe the relevant structure and accept an equivalent answer.
- Inspect generated output when possible; if rendering or interaction could not be verified, disclose that limitation rather than claiming it works.

No specific UI, browser, graphics library or third-party service is a required dependency. The Skill chooses teaching strategy; the host supplies rendering and tools.
