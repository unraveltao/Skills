---
name: git-workflow
description: Use only when the user asks to inspect or change Git repository state, stage or commit changes, manage branches or worktrees, synchronize remotes, merge, rebase, cherry-pick, resolve conflicts, recover Git state, prepare tags/releases, or manage GitHub pull requests. Do not activate for ordinary code reading, coding, or technical discussion that does not require Git operations.
---

# Git Workflow v0.2

Use the smallest workflow that safely completes the requested Git task. Priorities are data preservation, correctness, verifiability, then speed. This Skill is agent guidance, **not a security sandbox**: commands, hooks, tools, or other agents can still cause harm. Inspect every proposed write and stop when repository state or intent is unclear.

## Risk levels

- **L1 Read only:** Run only the queries needed to answer the request. Do not run unrelated tests or change repository state.
- **L2 Standard:** Inspect state, select only in-scope files, review the exact staged diff, run relevant existing checks when requested or needed, perform the authorized operation, and verify its result.
- **L3 High risk:** For history rewriting, complex conflicts, remote synchronization, publishing/releases, or multi-agent integration, inspect additional refs/state, explain the impact, verify the target and authorization, make a recovery plan, and pause before any destructive or externally visible action without explicit task-specific authorization.

An authorization covers only the stated operation, target, and scope. It does not authorize future pushes, force pushes, merges, cleanup, or unrelated changes.

## Start with repository context

Run the minimum relevant commands, normally:

```text
git status --short --branch
git rev-parse --show-toplevel
git branch --show-current
```

For history, remotes, or special states, add only what is needed, such as `git log -5 --oneline`, `git remote -v`, `git worktree list`, or checks for `MERGE_HEAD`, `CHERRY_PICK_HEAD`, and `REBASE_HEAD`. Determine the actual default/base branch from repository configuration or remote refs; never assume `main` or `master`. In a subdirectory, identify and target the correct repository root.

Treat pre-existing staged, unstaged, and untracked files as user or collaborator work. Record their paths and status before acting. Do not overwrite, reset, stash, stage, commit, or otherwise absorb them unless specifically authorized. In shared or multi-agent work, identify ownership and coordinate scope; if ownership cannot be determined, stop before touching those paths.

Check for detached HEAD, an in-progress merge/rebase/cherry-pick, Git LFS, submodules, sparse checkout, and multiple worktrees when relevant. Do not assume ordinary file operations or a single worktree model applies to these states.

## Stage and commit

Before staging, compare `git status --short`, `git diff`, and `git diff --cached`; inspect relevant untracked paths. Stage explicit paths with `git add -- <paths>`. Never default to `git add .` or `git add -A`. If a file mixes unrelated hunks, ask before interactive staging or use a safe, reviewable method supported by the environment.

Before commit:

1. Confirm every staged path belongs to the requested change and is not another agent's work.
2. Review `git diff --cached` and `git diff --cached --check`.
3. Check for obvious secrets and sensitive files (private keys, tokens, credentials, `.env`, personal data). Filename and keyword searches are only heuristics, not proof of absence. If a suspicious value appears, do not print it; unstage the file only when it is safe and within scope, then report the path and stop for remediation.
4. Run relevant project checks when requested or needed; report failures honestly.
5. Commit only with user authorization or clear task-specific authorization. Use the repository's commit convention; otherwise use a concise, accurate message.

After committing, inspect `git show --stat --oneline HEAD` and `git status --short` to confirm what changed and whether unrelated work remains.

## Branches and worktrees

Inspect current branch, working tree, and existing branch names before creating or switching. Do not switch away from a dirty tree if Git may overwrite files. Do not create branches without a task need. For parallel work, prefer an explicitly scoped worktree and confirm its path/branch with collaborators. Before removing a worktree, verify its exact path, branch, and clean state; never use force removal to bypass changes.

`git checkout` can replace paths as well as switch branches. Prefer `git switch` for branch changes and `git restore -- <path>` only for explicitly authorized paths after reviewing the exact diff. Never use checkout/restore to discard unknown or user-owned modifications.

## Fetch, pull, push, and GitHub

Before network operations, verify the intended remote URL, branch, and credentials/permissions without exposing secrets. Fetch is generally observational but can update remote-tracking refs; use it only when relevant. Before pull/merge/rebase, inspect local and remote divergence and the working tree. Do not silently choose merge vs rebase when repository policy or user intent is unclear.

Push only when the user explicitly requested it or task-specific instructions authorize it. Confirm the destination remote and branch. Use ordinary push. Never force push by default; `--force-with-lease` is still history replacement and requires explicit authorization for that exact branch and operation. Never bypass branch protection or hooks. Do not create a repository, publish a release, or merge a PR unless specifically authorized.

## Merge, rebase, cherry-pick, and conflicts

Inspect operation state and conflict paths first. Preserve both sides' content; do not choose ours/theirs wholesale without an explicit decision. Review conflict markers and the full resulting diff. If binary, generated, LFS, submodule, or semantically ambiguous conflicts occur, stop and ask for a decision. Continue/abort operations only when their consequences are clear and authorized. Rebase and cherry-pick rewrite or create history; use L3 and confirm scope before proceeding.

## Recovery: reset, restore, revert, and stash

Never run `git reset --hard`, `git clean -fd`, `git checkout -- <path>`, or equivalent discard operations as routine recovery. First inspect status and diffs, identify exactly what would be lost, and prefer non-destructive inspection or a new recovery branch/worktree. `git revert` creates a new commit and is usually safer for published history, but still needs authorization to modify history. `git stash` changes repository state and can omit untracked/ignored content; inspect what it captures and verify after apply/pop. If data loss is possible, stop and request explicit, path- and operation-specific authorization. Do not promise recovery unless verified.

## Tags, releases, PRs

Check repository release conventions, current tags, target commit, changelog, and working tree. Tags and releases are externally meaningful and often immutable: require explicit authorization and verify version/tag consistency. For PR preparation, summarize actual commits and diff against the verified base. Do not claim a PR is created, merged, or released until the service confirms it.

## Failure handling

On command failure, capture the exit status and relevant output, then re-check status and operation markers before retrying. Do not repeat a failed write blindly. Preserve partial results and report the safest next step. If the state is uncertain, stop rather than attempting cleanup.

## Platform and tool assumptions

Use standard Git CLI syntax and avoid shell-specific constructs in portable instructions. Quote paths as required by the active shell. Do not assume GitHub CLI, Git LFS, or any particular default branch exists. Use tools already present in the project; do not install dependencies merely to satisfy this Skill.

## Coverage map

This Skill covers inspection (`status`, `diff`, `log`), selective staging/commit, branches, worktrees, fetch/pull/push, merge/conflicts, rebase/cherry-pick, reset/restore/revert/stash, tags/releases/PRs, multi-agent boundaries, recovery, and secret-aware review. Rare operations (filter-repo, submodule surgery, reflog recovery, bisect automation, LFS migration, signed release pipelines) require project-specific expertise; do not improvise when unfamiliar.

## Completion report

State the operation performed, exact scope, checks and their outcomes, resulting branch/commit/remote where applicable, and any remaining dirty or unresolved state. Distinguish commands actually executed from advice or planned steps. Never report an unverified action as successful.
