# Folder rules

Root contains `00-Inbox/`, six category folders `01-Software/` through `06-Others/`, and `99-Review/`. Never derive a root from a drive letter assumption. User chooses it; if unspecified, inspect volumes/free space and offer options. Directory names are stable IDs; labels may be changed only by explicit user configuration. Preserve original basename. Existing destination name is a conflict, never overwrite; route to Review and report both paths. Do not create category subfolders based on untrusted filenames without sanitizing and previewing.
