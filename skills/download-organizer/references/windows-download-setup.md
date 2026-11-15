# Windows Downloads setup

Distinguish organizer root from the Windows Known Folder: the latter should be `<root>\00-Inbox`.

Read-only sequence: query Known Folder Downloads through Windows Known Folder API (`FOLDERID_Downloads`, `SHGetKnownFolderPath`); inspect target volume filesystem/free bytes and directory access; show layout and current-file count/size; produce a plan. If no target was specified, recommend only, never choose/change silently.

Mutation is out of scope for unattended V0.1. After explicit authorization, a capable Windows setup action must use `IKnownFolder::SetPath`/`SHSetKnownFolderPath` and verify by querying the API again. Registry text editing alone is not completion. Setting Known Folder and migrating existing files are separate approvals/steps. Migration copies first without overwrite, handles conflicts by preserving both and asking, verifies content (size and hash), and retains originals until verification and separate source-removal authorization. Any failure leaves old path and originals intact. This release ships only `inspect` and `init-preview`; it does not change OS settings or migrate existing Downloads.
