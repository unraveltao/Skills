# Learning Coach V0.1

An Agent Skill for learning across many fields: plan courses when useful, teach interactively, assign practice, review results, address gaps, and reassess. It can organize different kinds of learning notes when the user asks. Its guidance is written in Markdown and requires no external service or runtime program.

## Install and use

Copy the entire `learning-coach` directory into Codex's user Skills directory. PowerShell example (run from the repository root):

```powershell
Copy-Item -Recurse -LiteralPath .\skills\learning-coach -Destination "$env:USERPROFILE\.codex\skills\learning-coach"
```

If the destination already exists, inspect and resolve conflicts first to avoid overwriting it. Start a new Codex session after installation so it can discover the Skill again. Enter `$learning-coach` and describe a task, or describe a learning need directly and let Codex choose it. Actual discoverability depends on the target client's configuration and must be checked after installation. Other clients that support the open Agent Skills format should place the full directory in the location they specify; follow their documentation for discovery.

Examples: `$learning-coach Teach me instance attributes and class attributes`; `$learning-coach Create a Git learning path`; `$learning-coach Test my understanding of attribute lookup`.

## Progress and privacy

Progress is saved in a private Markdown file chosen by the user, outside the Skill installation directory. To resume, provide its path or contents; if no record is available, provide the record or a brief recap. There is no database, cloud synchronization, or automatic long-term memory. The user chooses where to store notes.

## Development and verification

The entry point is `SKILL.md`; mode details are in `references/`. When editing, keep relative links and independent distribution intact, and do not commit personal learning data. Practice records and Verified / Unverified / Needs reinforcement statuses must be tied to actual evidence. Codex skill-creator's `quick_validate.py` can check structure; it cannot prove teaching behavior.

Manual checks in a new session: request a Python object-oriented course plan; learn instance and class attributes and check that the Skill waits after asking a question; organize learned material into a separate note; assess attribute lookup with a new question and identify gaps based on the answer; try resuming with both an existing progress file and a missing record. Use a non-Python topic to check range, and verify that a request for one task does not force the full workflow. Record actual results; do not treat structural checks as multi-turn behavior validation.

MIT licensed; see [LICENSE](LICENSE).
