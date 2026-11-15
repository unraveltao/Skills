# Source discovery and registration

**Direct:** A browser or app may support a user-configurable download path. Set it to `<root>\00-Inbox` only with authorization, then verify the setting in that app. Examples include Chrome, Edge, Firefox, Internet Download Manager, Xunlei, GitHub Desktop clone locations, and cloud sync clients.

**Registered source:** Register a dedicated download directory for read-only scans. Only complete ordinary files are candidates. Do not recursively scan application databases, caches, or sync-managed internals. Common sources include Baidu Netdisk, WeChat, QQ, Telegram, cloud drives, and tools with fixed paths. Confirm the actual path with the user; do not guess.

**Manual import:** The user names a directory for one scan or plan. Keep the scope inside that directory and do not follow links. Changing the Windows Known Folder for Downloads does not guarantee that other apps will follow it. Check each app's settings individually. Keep registrations in user-local configuration, never in the repository.
