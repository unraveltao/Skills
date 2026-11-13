# Unimplemented features (boundary reference only)

**None of the capabilities below exist in the current version (v0.2), and no entry point is exposed.** They are recorded here only to define the Skill's boundaries and possible future direction; never use this document as a basis for changing files.

## Cleanup (designed for V0.2, not implemented)

A future cleanup flow would first present exact paths, reasons, impact, and recoverability, then require explicit per-item authorisation; it would re-check file state before acting and record the operation and outcome afterwards. Duplicate candidates would never be treated as automatically deletable. The current version performs no cleanup.

## Planning (designed for V0.2, not implemented)

A future planning flow could suggest grouping by purpose, extension, size, and access recency, and present a target directory structure with conflicts; it would only produce a plan and move nothing. The current version has no planning execution.

## Migration (designed for V0.3, not implemented)

A future migration flow would analyse dependencies and running state, migrate item by item, repair paths, and verify; on failure it would stop the remaining items and restore from a prepared plan. It would never force-close programs by default. Anything touching Codex or the current runtime environment would be handed to a separate executor. The current version moves no files.

