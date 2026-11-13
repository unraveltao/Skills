"""SQLite store. Legacy v0 databases are backed up before additive migration."""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

CURRENT_SCHEMA_VERSION = 1
LEGACY_REQUIRED = {"batches", "entries", "errors"}
LEGACY_CORE = (
    "CREATE TABLE IF NOT EXISTS batches ("
    "id TEXT PRIMARY KEY, target TEXT NOT NULL, started TEXT NOT NULL, finished TEXT, status TEXT NOT NULL, "
    "file_count INTEGER NOT NULL DEFAULT 0, dir_count INTEGER NOT NULL DEFAULT 0, total_bytes INTEGER NOT NULL DEFAULT 0, "
    "error_count INTEGER NOT NULL DEFAULT 0, volume_total INTEGER, volume_free INTEGER)"
)
LEGACY_ENTRIES = (
    "CREATE TABLE IF NOT EXISTS entries (batch_id TEXT NOT NULL REFERENCES batches(id) ON DELETE CASCADE, "
    "path TEXT NOT NULL, kind TEXT NOT NULL, size INTEGER NOT NULL DEFAULT 0, mtime REAL, "
    "extension TEXT NOT NULL DEFAULT '', digest TEXT, PRIMARY KEY(batch_id,path))"
)
LEGACY_ERRORS = (
    "CREATE TABLE IF NOT EXISTS errors (id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "batch_id TEXT NOT NULL REFERENCES batches(id) ON DELETE CASCADE, path TEXT NOT NULL, message TEXT NOT NULL)"
)
APP_TABLES = (
    "CREATE TABLE IF NOT EXISTS directory_stats (batch_id TEXT NOT NULL REFERENCES batches(id) ON DELETE CASCADE, path TEXT NOT NULL, parent_path TEXT NOT NULL, total_bytes INTEGER NOT NULL DEFAULT 0, file_count INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(batch_id,path))",
    "CREATE TABLE IF NOT EXISTS candidates ("
    "candidate_id TEXT PRIMARY KEY, batch_id TEXT NOT NULL REFERENCES batches(id) ON DELETE CASCADE, "
    "rule_version TEXT NOT NULL, kind TEXT NOT NULL, subject_key TEXT NOT NULL, path TEXT, "
    "category TEXT NOT NULL, risk_level TEXT NOT NULL, confidence TEXT NOT NULL, size_bytes INTEGER NOT NULL, "
    "reason TEXT NOT NULL, evidence_json TEXT NOT NULL, created_at TEXT NOT NULL, "
    "UNIQUE(batch_id,rule_version,kind,subject_key))",
    "CREATE TABLE IF NOT EXISTS reviews ("
    "candidate_id TEXT PRIMARY KEY REFERENCES candidates(candidate_id) ON DELETE CASCADE, "
    "status TEXT NOT NULL, note TEXT NOT NULL DEFAULT '', version INTEGER NOT NULL, "
    "updated_at TEXT NOT NULL)",
    "CREATE TABLE IF NOT EXISTS review_events ("
    "event_id INTEGER PRIMARY KEY AUTOINCREMENT, candidate_id TEXT NOT NULL REFERENCES candidates(candidate_id) ON DELETE CASCADE, "
    "request_id TEXT UNIQUE, actor TEXT NOT NULL, action TEXT NOT NULL, from_status TEXT, to_status TEXT NOT NULL, "
    "note TEXT NOT NULL, version INTEGER NOT NULL, created_at TEXT NOT NULL)",
    "CREATE TABLE IF NOT EXISTS app_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)",
)
INDEXES = (
    "CREATE INDEX IF NOT EXISTS entries_batch_kind_size ON entries(batch_id,kind,size DESC)",
    "CREATE INDEX IF NOT EXISTS entries_batch_extension_size ON entries(batch_id,extension,size DESC)",
    "CREATE INDEX IF NOT EXISTS entries_batch_parent ON entries(batch_id,parent_path,kind)",
    "CREATE INDEX IF NOT EXISTS errors_batch_id ON errors(batch_id,id)",
    "CREATE INDEX IF NOT EXISTS candidates_batch_risk ON candidates(batch_id,risk_level,created_at)",
    "CREATE INDEX IF NOT EXISTS review_events_candidate_id ON review_events(candidate_id,event_id)",
)


class DataPaths:
    """Separate install files from user data and preserve legacy workspace layout."""
    def __init__(self, root: Path):
        self.root = root.expanduser().resolve()
        nested = self.root / "database" / "audit.sqlite3"
        legacy = self.root / "audit.sqlite3"
        self.database = legacy if legacy.exists() and not nested.exists() else nested
        self.reports = self.root / "reports"
        self.logs = self.root / "logs"
        self.backups = self.root / "backups"
        self.state = self.root / "state"
        self.config = self.root / "config"

    @classmethod
    def default(cls) -> "DataPaths":
        local = os.environ.get("LOCALAPPDATA")
        root = Path(local) / "DiskGovernors" if local else Path.home() / "AppData" / "Local" / "DiskGovernors"
        return cls(root)

    def prepare(self) -> None:
        for path in (self.database.parent, self.reports, self.logs, self.backups, self.state, self.config):
            path.mkdir(parents=True, exist_ok=True)


def _schema(conn: sqlite3.Connection) -> tuple[int, set[str], set[str]]:
    version = int(conn.execute("PRAGMA user_version").fetchone()[0])
    tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    columns = {r[1] for r in conn.execute("PRAGMA table_info(entries)")} if "entries" in tables else set()
    return version, tables, columns


def _legacy_backup(conn: sqlite3.Connection, paths: DataPaths) -> Path:
    paths.backups.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate = paths.backups / f"audit-before-schema-v{CURRENT_SCHEMA_VERSION}-{stamp}.sqlite3"
    suffix = 1
    while candidate.exists():
        candidate = paths.backups / f"audit-before-schema-v{CURRENT_SCHEMA_VERSION}-{stamp}-{suffix}.sqlite3"
        suffix += 1
    backup = sqlite3.connect(candidate)
    try:
        conn.backup(backup)
    finally:
        backup.close()
    return candidate


def _migrate(conn: sqlite3.Connection, paths: DataPaths) -> None:
    version, tables, columns = _schema(conn)
    if version > CURRENT_SCHEMA_VERSION:
        raise RuntimeError(f"Database schema {version} is newer than supported schema {CURRENT_SCHEMA_VERSION}")
    if version == CURRENT_SCHEMA_VERSION:
        return
    if version == 0 and tables:
        if not LEGACY_REQUIRED.issubset(tables):
            raise RuntimeError("Unrecognized schema v0; refusing to modify this database")
        required_cols = {"batch_id", "path", "kind", "size", "mtime", "extension", "digest"}
        if not required_cols.issubset(columns):
            raise RuntimeError("Unrecognized v0 entries schema; refusing to modify this database")
        backup = _legacy_backup(conn, paths)
    else:
        backup = None

    if conn.in_transaction:
        conn.rollback()
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("BEGIN IMMEDIATE")
    try:
        for statement in (LEGACY_CORE, LEGACY_ENTRIES, LEGACY_ERRORS):
            conn.execute(statement)
        version, tables, columns = _schema(conn)
        if "parent_path" not in columns:
            conn.execute("ALTER TABLE entries ADD COLUMN parent_path TEXT NOT NULL DEFAULT ''")
            rows = conn.execute("SELECT batch_id,path FROM entries").fetchall()
            conn.executemany(
                "UPDATE entries SET parent_path=? WHERE batch_id=? AND path=?",
                [(str(Path(path).parent), batch_id, path) for batch_id, path in rows],
            )
        for statement in APP_TABLES + INDEXES:
            conn.execute(statement)
        conn.execute(f"PRAGMA user_version={CURRENT_SCHEMA_VERSION}")
        conn.commit()
    except Exception:
        conn.rollback()
        if backup is not None:
            raise RuntimeError(f"Schema migration failed; original database is unchanged and backup is at {backup}")
        raise


class Store:
    """Deep SQLite interface for batches, report queries, candidates and decisions."""
    def __init__(self, paths: DataPaths, conn: sqlite3.Connection, read_only: bool):
        self.paths, self.conn, self.read_only = paths, conn, read_only
        self.conn.row_factory = sqlite3.Row

    @classmethod
    def open(cls, paths: DataPaths, *, read_only: bool = False, migrate: bool = False) -> "Store":
        path = paths.database
        if not path.exists() and read_only:
            raise FileNotFoundError(f"Database does not exist: {path}")
        if not read_only:
            paths.prepare()
        if read_only:
            uri = "file:" + path.as_posix() + "?mode=ro"
            conn = sqlite3.connect(uri, uri=True, timeout=5.0)
        else:
            conn = sqlite3.connect(path, timeout=5.0, isolation_level=None)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys=ON")
        conn.execute("PRAGMA busy_timeout=5000")
        if read_only:
            conn.execute("PRAGMA query_only=ON")
            version, tables, columns = _schema(conn)
            if version > CURRENT_SCHEMA_VERSION or not LEGACY_REQUIRED.issubset(tables):
                conn.close()
                raise RuntimeError("Database schema is not readable by this Runtime")
        elif migrate:
            _migrate(conn, paths)
        return cls(paths, conn, read_only)

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "Store":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def list_batches(self, limit: int = 100) -> list[dict]:
        limit = max(1, min(int(limit), 500))
        rows = self.conn.execute("SELECT * FROM batches ORDER BY started DESC LIMIT ?", (limit,))
        return [dict(row) for row in rows]

    def get_batch(self, batch_id: str) -> dict | None:
        row = self.conn.execute("SELECT * FROM batches WHERE id=?", (batch_id,)).fetchone()
        return dict(row) if row else None

    def count_entries(self, batch_id: str, kind: str | None = None) -> int:
        if kind:
            row = self.conn.execute("SELECT COUNT(*) FROM entries WHERE batch_id=? AND kind=?", (batch_id, kind)).fetchone()
        else:
            row = self.conn.execute("SELECT COUNT(*) FROM entries WHERE batch_id=?", (batch_id,)).fetchone()
        return int(row[0])

    def get_errors(self, batch_id: str, limit: int = 500, offset: int = 0) -> list[dict]:
        limit = max(1, min(int(limit), 500))
        offset = max(0, int(offset))
        rows = self.conn.execute(
            "SELECT id,batch_id,path,message FROM errors WHERE batch_id=? ORDER BY id LIMIT ? OFFSET ?",
            (batch_id, limit, offset),
        )
        return [dict(row) for row in rows]

    def search_files(self, batch_id: str, *, query: str = "", extension: str = "", sort_by: str = "size",
                     order: str = "desc", page: int = 1, page_size: int = 100) -> dict:
        sort_map = {"size": "size", "mtime": "mtime", "name": "path"}
        if sort_by not in sort_map:
            raise ValueError("Unsupported sort field")
        if order not in {"asc", "desc"}:
            raise ValueError("Sort order must be asc or desc")
        page = max(1, int(page))
        page_size = max(1, min(int(page_size), 500))
        where = ["batch_id=?", "kind='file'"]
        args: list[object] = [batch_id]
        if query:
            where.append("path LIKE ? ESCAPE '\\' COLLATE NOCASE")
            escaped = query.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
            args.append("%" + escaped + "%")
        if extension:
            where.append("extension=?")
            args.append(extension.casefold())
        clause = " AND ".join(where)
        total = int(self.conn.execute(f"SELECT COUNT(*) FROM entries WHERE {clause}", args).fetchone()[0])
        sort = sort_map[sort_by]
        rows = self.conn.execute(
            f"SELECT batch_id,path,kind,size,mtime,extension,digest,parent_path FROM entries WHERE {clause} "
            f"ORDER BY {sort} {order.upper()},path ASC LIMIT ? OFFSET ?",
            args + [page_size, (page - 1) * page_size],
        )
        return {"items": [dict(row) for row in rows], "total": total, "page": page, "page_size": page_size}

    def get_file(self, batch_id: str, path: str) -> dict | None:
        row = self.conn.execute(
            "SELECT batch_id,path,kind,size,mtime,extension,digest,parent_path FROM entries "
            "WHERE batch_id=? AND path=? AND kind='file'", (batch_id, path),
        ).fetchone()
        return dict(row) if row else None

    def list_directories(self, batch_id: str, parent_path: str, limit: int = 500) -> list[dict]:
        limit = max(1, min(int(limit), 1000))
        rows = self.conn.execute(
            "SELECT path,parent_path,total_bytes,file_count FROM directory_stats "
            "WHERE batch_id=? AND parent_path=? ORDER BY total_bytes DESC,path LIMIT ?",
            (batch_id, parent_path, limit),
        )
        return [dict(row) for row in rows]

    def top_directories(self, batch_id: str, limit: int = 100) -> list[dict]:
        limit = max(1, min(int(limit), 500))
        rows = self.conn.execute(
            "SELECT path,parent_path,total_bytes,file_count FROM directory_stats "
            "WHERE batch_id=? ORDER BY total_bytes DESC,path LIMIT ?", (batch_id, limit),
        )
        return [dict(row) for row in rows]

    def get_categories(self, batch_id: str) -> list[dict]:
        from .classification import classify_path
        totals: dict[str, int] = {}
        counts: dict[str, int] = {}
        for row in self.conn.execute("SELECT path,extension,size FROM entries WHERE batch_id=? AND kind='file'", (batch_id,)):
            category = classify_path(row["path"], row["extension"]).category
            totals[category] = totals.get(category, 0) + int(row["size"])
            counts[category] = counts.get(category, 0) + 1
        return [{"category": key, "bytes": value, "file_count": counts[key]}
                for key, value in sorted(totals.items(), key=lambda item: (-item[1], item[0]))]

    def file_types(self, batch_id: str, limit: int = 100) -> list[dict]:
        limit = max(1, min(int(limit), 500))
        rows = self.conn.execute(
            "SELECT extension,COUNT(*) AS file_count,COALESCE(SUM(size),0) AS bytes "
            "FROM entries WHERE batch_id=? AND kind='file' GROUP BY extension ORDER BY bytes DESC LIMIT ?",
            (batch_id, limit),
        )
        return [dict(row) for row in rows]

    def largest_files(self, batch_id: str, limit: int = 100) -> list[dict]:
        limit = max(1, min(int(limit), 500))
        rows = self.conn.execute(
            "SELECT batch_id,path,size,mtime,extension,digest,parent_path FROM entries "
            "WHERE batch_id=? AND kind='file' ORDER BY size DESC,path LIMIT ?", (batch_id, limit),
        )
        return [dict(row) for row in rows]

    @contextmanager
    def transaction(self) -> Iterator[sqlite3.Connection]:
        if self.read_only:
            raise PermissionError("Read-only store cannot start a write transaction")
        self.conn.execute("BEGIN IMMEDIATE")
        try:
            yield self.conn
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    def replace_candidates(self, batch_id: str, rows: list[dict]) -> None:
        if self.read_only:
            raise PermissionError("Read-only store cannot persist candidates")
        with self.transaction() as conn:
            # Upsert immutable evidence without deleting review history or decisions.
            conn.executemany(
                "INSERT INTO candidates(candidate_id,batch_id,rule_version,kind,subject_key,path,category,risk_level,"
                "confidence,size_bytes,reason,evidence_json,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) "
                "ON CONFLICT(candidate_id) DO NOTHING",
                [(r["candidate_id"],batch_id,r["rule_version"],r["kind"],r["subject_key"],r.get("path"),
                  r["category"],r["risk_level"],r["confidence"],r["size_bytes"],r["reason"],
                  json.dumps(r["evidence"],ensure_ascii=False,separators=(",",":")),r["created_at"]) for r in rows],
            )

    def rebuild_directory_stats(self, batch_id: str) -> None:
        """Compute logical tree sizes bottom-up; directory bytes are not physical allocation."""
        with self.transaction() as conn:
            conn.execute("DELETE FROM directory_stats WHERE batch_id=?", (batch_id,))
            dirs = conn.execute("SELECT path,parent_path FROM entries WHERE batch_id=? AND kind='dir'", (batch_id,)).fetchall()
            files = conn.execute("SELECT path,parent_path,size FROM entries WHERE batch_id=? AND kind='file'", (batch_id,)).fetchall()
            stats: dict[str, list[int]] = {str(r[0]): [0, 0] for r in dirs}
            for row in files:
                parent = str(row[1])
                while parent in stats:
                    stats[parent][0] += int(row[2]); stats[parent][1] += 1
                    next_parent = str(Path(parent).parent)
                    if next_parent == parent: break
                    parent = next_parent
            conn.executemany("INSERT INTO directory_stats(batch_id,path,parent_path,total_bytes,file_count) VALUES(?,?,?,?,?)",
                [(batch_id, path, str(Path(path).parent), vals[0], vals[1]) for path, vals in stats.items()])

    def get_candidates(self, batch_id: str, *, query: str = "", risk: str = "", category: str = "",
                       status: str = "", page: int = 1, page_size: int = 50) -> dict:
        page = max(1, int(page)); page_size=max(1,min(int(page_size),200))
        where=["c.batch_id=?"]; args: list[object]=[batch_id]
        if query:
            where.append("(c.path LIKE ? ESCAPE '\\' COLLATE NOCASE OR c.subject_key LIKE ? ESCAPE '\\' COLLATE NOCASE)")
            escaped=query.replace("\\","\\\\").replace("%","\\%").replace("_","\\_")
            args.extend([f"%{escaped}%",f"%{escaped}%"])
        if risk: where.append("c.risk_level=?"); args.append(risk)
        if category: where.append("c.category=?"); args.append(category)
        if status:
            where.append("COALESCE(r.status,'untracked')=?"); args.append(status)
        clause=" AND ".join(where)
        total=int(self.conn.execute(f"SELECT COUNT(*) FROM candidates c LEFT JOIN reviews r ON r.candidate_id=c.candidate_id WHERE {clause}",args).fetchone()[0])
        rows=self.conn.execute(
            f"SELECT c.*,COALESCE(r.status,'untracked') AS review_status,COALESCE(r.note,'') AS review_note,COALESCE(r.version,0) AS review_version "
            f"FROM candidates c LEFT JOIN reviews r ON r.candidate_id=c.candidate_id WHERE {clause} "
            "ORDER BY c.size_bytes DESC,c.candidate_id LIMIT ? OFFSET ?", args+[page_size,(page-1)*page_size])
        items=[]
        for row in rows:
            item=dict(row); item["evidence"]=json.loads(item.pop("evidence_json")); items.append(item)
        return {"items":items,"total":total,"page":page,"page_size":page_size}

    def candidate_by_id(self, candidate_id: str) -> dict | None:
        row=self.conn.execute("SELECT * FROM candidates WHERE candidate_id=?",(candidate_id,)).fetchone()
        if not row: return None
        item=dict(row); item["evidence"]=json.loads(item.pop("evidence_json")); return item

    def review_history(self, candidate_id: str) -> list[dict]:
        rows=self.conn.execute("SELECT * FROM review_events WHERE candidate_id=? ORDER BY event_id",(candidate_id,))
        return [dict(row) for row in rows]

    def review_events_for_batch(self, batch_id: str, limit: int = 100, offset: int = 0) -> dict:
        limit=max(1,min(int(limit),500));offset=max(0,int(offset))
        total=int(self.conn.execute("SELECT COUNT(*) FROM review_events e JOIN candidates c ON c.candidate_id=e.candidate_id WHERE c.batch_id=?",(batch_id,)).fetchone()[0])
        rows=self.conn.execute("SELECT e.*,c.kind,c.path,c.subject_key FROM review_events e JOIN candidates c ON c.candidate_id=e.candidate_id WHERE c.batch_id=? ORDER BY e.event_id DESC LIMIT ? OFFSET ?",(batch_id,limit,offset))
        return {"items":[dict(row) for row in rows],"total":total,"limit":limit,"offset":offset}

    def update_review(self, candidate_id: str, status: str, note: str, expected_version: int,
                      request_id: str, actor: str = "local-workbench") -> dict:
        if self.read_only: raise PermissionError("Read-only store cannot update reviews")
        if not self.candidate_by_id(candidate_id): raise KeyError("Candidate not found")
        if len(note)>2000: raise ValueError("Review note exceeds 2000 characters")
        if not request_id or len(request_id)>100: raise ValueError("A request_id of 1-100 characters is required")
        if actor not in {"local-workbench","runtime-cli"}: raise ValueError("Unsupported actor")
        with self.transaction() as conn:
            prior=conn.execute("SELECT candidate_id,version,to_status FROM review_events WHERE request_id=?",(request_id,)).fetchone()
            if prior:
                if prior["candidate_id"]!=candidate_id: raise ValueError("request_id was already used for another candidate")
                current=conn.execute("SELECT * FROM reviews WHERE candidate_id=?",(candidate_id,)).fetchone()
                return {"candidate_id":candidate_id,"status":current["status"],"version":current["version"],"idempotent":True}
            current=conn.execute("SELECT * FROM reviews WHERE candidate_id=?",(candidate_id,)).fetchone()
            current_version=int(current["version"]) if current else 0
            if current_version!=int(expected_version):
                raise ReviewConflict({"candidate_id":candidate_id,"version":current_version,
                                      "status":current["status"] if current else "untracked"})
            previous=current["status"] if current else None
            if status not in {"pending","verified","keep","deferred","needs_assessment"}:
                raise ValueError("Unsupported review status")
            if previous==status:
                return {"candidate_id":candidate_id,"status":status,"version":current_version,"idempotent":True}
            version=current_version+1
            stamp=datetime.now(timezone.utc).isoformat()
            if current:
                changed=conn.execute("UPDATE reviews SET status=?,note=?,version=?,updated_at=? WHERE candidate_id=? AND version=?",
                                     (status,note,version,stamp,candidate_id,current_version)).rowcount
                if changed!=1: raise ReviewConflict({"candidate_id":candidate_id,"version":current_version})
            else:
                conn.execute("INSERT INTO reviews(candidate_id,status,note,version,updated_at) VALUES(?,?,?,?,?)",
                             (candidate_id,status,note,version,stamp))
            conn.execute("INSERT INTO review_events(candidate_id,request_id,actor,action,from_status,to_status,note,version,created_at) "
                         "VALUES(?,?,?,?,?,?,?,?,?)",
                         (candidate_id,request_id,actor,"status_changed",previous,status,note,version,stamp))
        return {"candidate_id":candidate_id,"status":status,"version":version,"idempotent":False}


class ReviewConflict(Exception):
    def __init__(self, current: dict):
        super().__init__("Review was updated by another caller")
        self.current=current

