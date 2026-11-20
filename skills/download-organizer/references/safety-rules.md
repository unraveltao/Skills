# Safety rules

- Scan is read-only; plan is read-only; apply requires explicit plan approval.
- No delete feature, overwrite, downloaded program execution, or archive script execution.
- Ignore partial suffixes such as `.crdownload`, `.part`, `.partial`, `.download`, `.tmp`.
- Do not follow symlinks/reparse points. Record access failures and mark results incomplete.
- Exclude app state, caches, databases, and sync internals unless user explicitly scopes a safe dedicated directory.
- Same-volume moves use a no-overwrite rename when possible. For cross-volume moves, copy to an exclusive new path, verify it with SHA-256, then place the verified copy at the destination. Retain the source and report the result as `Copied`; record both paths.
- If destination conflicts, file is locked, space is insufficient, access is denied, or verification fails, keep source and report failure/Review.
- Never claim full scan if errors occurred. Never treat an old report as a live index.
