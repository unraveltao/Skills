# Using Skills

Skills provide guidance and optional scripts for compatible agents. They do **not** bypass tool permissions, provide automatic memory, or guarantee an Agent will consistently follow instructions.

## Match a Skill to a task

Choose by the user's goal and the Skill's declared scope. For example, `git-workflow` guides Git operations; `learning-coach` guides interactive learning; `disk-governance` only audits disks, and **does not perform cleanup or deletion**.

## Read before invoking

Check `SKILL.md` for triggers, workflow and restrictions. If available, consult `README.md`, `references/`, and tests. The [Skill Structure](/Skills/docs/reference/skill-structure/) reference explains these resources.

## Invoke and validate

Different clients have different Skill discovery, invocation, and reload behavior. A directory being present is not evidence that an Agent actually loaded it. A safe test is a harmless, read-only example where the Agent explains its selection.

## Authorization matters

Do not interpret Skill instructions as permission for file modifications, system administration, external publishing, or unapproved installations. Obtain approval for the specific action.

## Troubleshooting

If a Skill is not recognized, verify the full installed directory, client configuration, platform requirements, and reload procedure. See [Skill Readiness](/Skills/docs/development/skill-readiness/) for historical validation limits.