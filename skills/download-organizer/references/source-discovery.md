# Source discovery and registration

Direct: browser/app supports a user-configurable path; set to `<root>\00-Inbox` only with authorization and verify in that app. Examples: Chrome, Edge, Firefox, IDM, 迅雷, GitHub Desktop (clone location), cloud sync clients.

Registered Source: register a dedicated download directory for read-only scans; only complete ordinary files are candidates. Do not recursively scan application databases, caches, or sync-managed internals. Common sources include 百度网盘, 微信, QQ, Telegram, cloud drives and tools with fixed paths. Confirm actual path with user; do not guess.

Manual Import: user names a directory for one scan/plan. Scope stays within it and does not follow links. Windows Known Folder Downloads changes do not guarantee other apps follow. Check each app's settings individually. Keep registration in user-local config, never repository.
