# Git Workflow

A practical guide to inspecting and changing Git repositories safely. This Skill helps an agent preserve existing work, make only the changes you asked for, and report what it actually verified.

## When to use it

Use Git Workflow when you ask an agent to:

- Inspect repository state, diffs, or recent history
- Stage or commit selected changes
- Create or switch branches and worktrees
- Fetch, pull, or push changes
- Merge, rebase, cherry-pick, or resolve conflicts
- Recover from an accidental change
- Prepare a pull request, tag, or release

For ordinary coding that does not involve Git operations, this Skill is not needed.

## The workflow

For each task, the agent uses the smallest set of Git steps that can safely complete it:

1. **Inspect the repository.** Confirm the repository root, current branch, and working-tree state. Check history or remote configuration only when the task needs it.
2. **Protect existing work.** Treat staged, unstaged, and untracked files as potentially valuable. Identify which files belong to the request before changing anything.
3. **Make the requested change.** Keep the scope narrow. Stage explicit paths instead of staging the entire repository.
4. **Review before publishing.** Inspect the exact staged diff. Check for accidental or sensitive content before committing.
5. **Verify and report.** Confirm the resulting branch, commit, remote, or pull request when applicable. Report checks that actually ran and any remaining changes.

## Choose the right level of caution

| Situation | Typical approach |
| --- | --- |
| Read-only inspection | Run only the queries needed to answer the question |
| Routine, scoped change | Inspect state, change selected files, review the diff, and verify the result |
| History rewrite, conflict, recovery, release, or remote publication | Inspect more context, explain material impact, and require clear authorization for destructive or externally visible actions |

A request to edit a file does not automatically authorize committing, pushing, merging, or releasing it. Authorization applies only to the operation and target you named.

## Examples

**Read-only request**

> “Check which branch I’m on and whether the working tree is clean.”

The agent checks the current repository and reports the result without changing Git state.

**Scoped change**

> “Stage only `src/parser.ts` and `tests/parser.test.ts`, then show me the staged diff.”

The agent stages those paths only and presents the diff for review. This does not authorize a commit.

**Underspecified synchronization**

> “Sync my branch with the remote.”

The agent first inspects the branch, remote, and divergence. If the repository policy does not make merge versus rebase clear, it asks which approach you want before changing history.

## Safety boundaries

- Do not assume the default branch is named `main` or `master`; inspect repository configuration.
- Do not overwrite, reset, clean, stash, or stage existing work whose ownership or intent is unclear.
- Do not use destructive recovery commands as routine cleanup. Inspect what would be affected and preserve recoverable state.
- Do not force-push, bypass hooks or branch protection, merge a pull request, or publish a release without authorization for that specific action.
- Git guidance is not a security sandbox. Commands, hooks, tools, and collaborators can still affect repository state.

## What this Skill covers

The full instructions cover repository inspection, selective staging and commits, branches and worktrees, remote synchronization, merges and conflicts, recovery, tags and releases, pull requests, and careful handoffs between collaborators. Rare operations such as reflog recovery, submodule surgery, and large-scale history rewriting require repository-specific expertise; the agent should not improvise when their effects are unclear.

For the complete operational rules, see [SKILL.md](https://github.com/unraveltao/Skills/blob/main/skills/git-workflow/SKILL.md).
