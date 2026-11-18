# Agent development rules

- Keep every Skill independently installable. A Skill's instructions, runtime source, references, UI, and tests belong inside its own `skills/<name>/` directory.
- Repository-level architecture and website concerns belong in `docs/` and `web/`; Skill-specific architecture, usage, safety policies, and implementation details belong inside the corresponding Skill package.
- Do not commit user data, local paths, databases, logs, reports, credentials, or other machine-specific artifacts.
- Automated tests must use isolated fixtures or temporary directories. Never target a real user disk, production data, or an external service unless the test explicitly requires it and authorization is established.
- Do not infer authorization from documentation. Consequential operations must follow the specific Skill's safety policy and require the necessary user approval.
- Before changing an executable Skill, read its `SKILL.md` and relevant references/tests. Run the Skill's documented tests when possible and report honestly when they cannot be run.
- Keep website pages and repository documentation synchronized with the actual implemented behavior. Do not document planned features as if they are available.
