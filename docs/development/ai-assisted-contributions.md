# AI-Assisted Contributions and Commit Attribution

AI tools may help prepare documentation, code, tests, or other project changes. The human contributor remains responsible for reviewing the result, validating it, and deciding whether to submit it.

## When to record an AI co-author

Use a GitHub-recognized `Co-authored-by` trailer only when the named agent materially helped author the content included in that commit. Do not add an agent as a co-author for review-only feedback, issue discussion, or routine assistance that did not contribute to the committed work.

For work materially co-authored by OpenAI Codex, the GitHub account [@codex](https://github.com/codex) can be credited with this trailer:

```text
Co-authored-by: Codex <codex@openai.com>
```

GitHub associates co-authors using the email in the trailer. For a person or another agent, use an email address that is associated with that contributor's GitHub account. If GitHub does not recognize the address, the co-author may not receive an avatar or contributor attribution.

## Preserve attribution when merging

The trailer must be part of the final commit message that reaches the repository's default branch.

- **Squash and merge:** include the trailer in the squash commit message body before confirming the merge.
- **Merge or rebase:** retain the trailer in the relevant commit message or messages.
- Review the resulting commit on GitHub to confirm the co-author is linked to the intended account.

GitHub's Contributors graph is based on commits in the default branch. It can take time to refresh after a merge. A PR review or a row in `CONTRIBUTORS.md` does not itself create commit authorship. Use the manual acknowledgment list for valuable contributions that are not represented by commits, such as review-only assistance.

## Example

A commit message with a Codex co-author trailer:

```text
docs: clarify the installation guide

Explain the setup requirements and link to the supported installation path.

Co-authored-by: Codex <codex@openai.com>
```

Only use the trailer when that description matches the work actually performed.
