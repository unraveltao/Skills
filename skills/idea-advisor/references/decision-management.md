# Decision management

Record decisions that materially constrain the design or are likely to be revisited. A record is a history aid, not proof that an option is correct and not authorization to implement it.

## States

- **Pending confirmation** — proposed, awaiting the user's decision.
- **Confirmed** — explicitly accepted by the user.
- **Needs validation** — accepted as a working direction, with a named assumption or evidence check outstanding.
- **Rejected** — considered and declined; preserve why when useful.
- **Superseded** — replaced by a later decision; link both records.

## Rules

1. Assign stable, sequential IDs within the project, such as `D-001`.
2. Create a new record for a material change. Do not rewrite an old conclusion as if it had always been true.
3. When a decision changes, mark the earlier record **Superseded**, link the replacement, and state what changed and why.
4. Link evidence where available. Label unverified premises as assumptions and give them an owner or validation step when possible.
5. Capture conditions that should trigger reassessment. Avoid vague triggers such as “later” or “if things change.”
6. Keep unresolved questions and the next useful action visible.
7. On resume, read the latest records first, recover current scope and open questions, and ask only about conflicts or missing facts that could change the path.

## Persistence

Use a user-approved project file or destination when persistence is available and requested or appropriate. Do not assume the Skill directory is writable or that one conversation can see another. Without storage, provide a compact copyable decision/recovery summary.
