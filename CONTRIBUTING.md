# Contributing to Unravel Skills

Thank you for contributing. Unravel Skills is a collection of independently installable Agent Skills, so contributions should keep the repository understandable both to people and to compatible Agents.

## Before you change anything

1. Read the root [AGENTS.md](AGENTS.md).
2. Identify whether your change is **repository-level** or **Skill-specific**.
3. For a Skill-specific change, read that Skill's `SKILL.md` and relevant references before editing it.
4. Keep unrelated changes out of the same change set.

## Skill changes

A Skill should remain self-contained under `skills/<name>/`.

- Keep `SKILL.md` as the authoritative Agent-facing entry point.
- Put human-facing explanation in that Skill's `README.md` when useful.
- Keep detailed behavior, policies, examples, and implementation notes in the Skill's `references/`.
- Put executable helpers in `scripts/` only when they are required by the Skill.
- Put fixtures and verification in `tests/` when applicable.
- Do not move Skill-specific architecture into the repository-wide `docs/concepts/architecture.md`.

## Documentation changes

Repository-wide documentation belongs under `docs/` and should describe the repository as a whole.

Use the existing sections:

- `getting-started/` — onboarding and installation.
- `guides/` — task-oriented usage.
- `concepts/` — repository-wide concepts and architecture.
- `reference/` — stable formats and interfaces.
- `development/` — contribution, validation, planning, and historical engineering records.

Skill-specific documentation stays with the Skill. Do not duplicate it in the global Docs unless it describes a repository-wide contract.

## Website changes

The website in `web/` is a static catalog and documentation reader.

When changing Docs navigation or pages:

1. Add or update the Markdown under `docs/`.
2. Update `web/src/lib/docs.ts` when a page is added or removed.
3. Verify the generated route and navigation.
4. Run the repository's relevant checks before proposing the change.

## Validation

Do not claim a Skill is fully verified unless the corresponding checks have actually been run. Distinguish:

- structural validation;
- automated tests;
- isolated fixture tests;
- real-Agent behavior testing.

For safety-sensitive Skills, prefer isolated fixtures and read-only validation where possible.

## Pull requests

Use a focused branch and a descriptive commit or PR title.

A PR description should state:

- **What changed**
- **Why it changed**
- **How it was tested**
- **Known limitations or unverified behavior**

If the change affects installation, public documentation, or Skill metadata, include the user-visible impact.

## License

By contributing, you agree that your contribution is provided under the repository's [MIT License](LICENSE), unless a different written agreement applies.
