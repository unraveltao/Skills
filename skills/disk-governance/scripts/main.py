#!/usr/bin/env python3
"""Read-only directory audit with local SQLite storage and HTML reports."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import sqlite3
import sys
import time
import uuid
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


SCHEMA = """
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS batches (
 id TEXT PRIMARY KEY, target TEXT NOT NULL, started TEXT NOT NULL,
 finished TEXT, status TEXT NOT NULL, file_count INTEGER NOT NULL DEFAULT 0,
 dir_count INTEGER NOT NULL DEFAULT 0, total_bytes INTEGER NOT NULL DEFAULT 0,
 error_count INTEGER NOT NULL DEFAULT 0, volume_total INTEGER, volume_free INTEGER
);
CREATE TABLE IF NOT EXISTS entries (
 batch_id TEXT NOT NULL REFERENCES batches(id) ON DELETE CASCADE,
 path TEXT NOT NULL, kind TEXT NOT NULL, size INTEGER NOT NULL DEFAULT 0,
 mtime REAL, extension TEXT NOT NULL DEFAULT '', digest TEXT,
 parent_path TEXT NOT NULL DEFAULT '',
 PRIMARY KEY(batch_id,path)
);
CREATE INDEX IF NOT EXISTS entries_batch_size ON entries(batch_id,size DESC);
CREATE INDEX IF NOT EXISTS entries_batch_digest ON entries(batch_id,digest);
CREATE TABLE IF NOT EXISTS errors (
 id INTEGER PRIMARY KEY AUTOINCREMENT, batch_id TEXT NOT NULL REFERENCES batches(id) ON DELETE CASCADE,
 path TEXT NOT NULL, message TEXT NOT NULL
);
"""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def is_link_or_reparse(path: Path) -> bool:
    try:
        st = path.lstat()
        return path.is_symlink() or bool(getattr(st, "st_file_attributes", 0) & 0x400)
    except OSError:
        return True


def inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except (ValueError, OSError, RuntimeError):
        return False


def record_error(db: sqlite3.Connection, batch: str, path: Path, exc: object) -> None:
    db.execute("INSERT INTO errors(batch_id,path,message) VALUES(?,?,?)",
               (batch, str(path), str(exc)))
    db.execute("UPDATE batches SET error_count=error_count+1 WHERE id=?", (batch,))


def quick_signature(path: Path, size: int) -> str:
    """Read a bounded sample to cheaply reject same-size non-duplicates."""
    sample = 64 * 1024
    h = hashlib.sha256()
    with path.open("rb") as stream:
        h.update(stream.read(sample))
        if size > sample * 2:
            stream.seek(-sample, os.SEEK_END)
            h.update(stream.read(sample))
    return h.hexdigest()


def discover_drives() -> list[str]:
    if os.name == "nt":
        import string
        return [f"{letter}:\\" for letter in string.ascii_uppercase
                if os.path.exists(f"{letter}:\\")]
    return ["/"]


def audit(target: Path, workspace: Path, progress: bool = True, hash_duplicates: bool = False,
          database_path: Path | None = None, logs_dir: Path | None = None) -> str:
    target = target.resolve(strict=True)
    if not target.is_dir():
        raise ValueError(f"扫描目标不是目录: {target}")
    workspace.mkdir(parents=True, exist_ok=True)
    workspace = workspace.resolve()
    if inside(workspace, target):
        # Workspace nested in target is excluded during traversal.
        pass
    (workspace / "logs").mkdir(exist_ok=True)
    db_path = database_path or (workspace / "audit.sqlite3")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(db_path)
    db.executescript(SCHEMA)
    # Additive compatibility for databases created by early v0.1 builds.
    columns = {row[1] for row in db.execute("PRAGMA table_info(entries)")}
    if "parent_path" not in columns:
        db.execute("ALTER TABLE entries ADD COLUMN parent_path TEXT NOT NULL DEFAULT ''")
    batch = uuid.uuid4().hex
    started = now_iso()
    volume_total = volume_free = None
    try:
        usage = os.statvfs(target) if hasattr(os, "statvfs") else None
        if usage:
            volume_total = usage.f_blocks * usage.f_frsize
            volume_free = usage.f_bavail * usage.f_frsize
        elif os.name == "nt":
            import shutil
            du = shutil.disk_usage(target)
            volume_total, volume_free = du.total, du.free
    except OSError:
        pass
    db.execute("INSERT INTO batches(id,target,started,status,volume_total,volume_free) VALUES(?,?,?,?,?,?)",
               (batch, str(target), started, "running", volume_total, volume_free))
    db.commit()
    files = dirs = total = seen = 0
    interrupted = False
    log_root = logs_dir or (workspace / "logs")
    log_root.mkdir(parents=True, exist_ok=True)
    log_path = log_root / f"{batch}.jsonl"
    try:
        with log_path.open("w", encoding="utf-8") as log:
            stack = [target]
            while stack:
                directory = stack.pop()
                try:
                    with os.scandir(directory) as iterator:
                        children = list(iterator)
                except OSError as exc:
                    record_error(db, batch, directory, exc)
                    log.write(json.dumps({"path": str(directory), "error": str(exc)}) + "\n")
                    continue
                for child in children:
                    path = Path(child.path)
                    if path == workspace or inside(path, workspace):
                        continue
                    try:
                        st = child.stat(follow_symlinks=False)
                        if child.is_symlink() or bool(getattr(st, "st_file_attributes", 0) & 0x400):
                            continue
                        if child.is_dir(follow_symlinks=False):
                            dirs += 1
                            db.execute("INSERT OR REPLACE INTO entries(batch_id,path,kind,size,mtime,extension,digest,parent_path) VALUES(?,?,?,?,?,?,?,?)",
                                       (batch, str(path), "dir", 0, st.st_mtime, "", None, str(path.parent)))
                            stack.append(path)
                        elif child.is_file(follow_symlinks=False):
                            size = st.st_size
                            ext = path.suffix.lower() or "[no extension]"
                            db.execute("INSERT OR REPLACE INTO entries(batch_id,path,kind,size,mtime,extension,digest,parent_path) VALUES(?,?,?,?,?,?,?,?)",
                                       (batch, str(path), "file", size, st.st_mtime, ext, None, str(path.parent)))
                            files += 1
                            total += size
                            # Hash only files in a duplicate-size group. Hash in chunks.
                            # We defer candidates until scan completes.
                        seen += 1
                        if progress and seen % 500 == 0:
                            print(f"已检查 {seen} 项…", file=sys.stderr)
                    except OSError as exc:
                        record_error(db, batch, path, exc)
                        log.write(json.dumps({"path": str(path), "error": str(exc)}) + "\n")
                db.commit()
        if hash_duplicates:
            # First compare bounded head/tail samples for same-size files. Only
            # candidates with the same sample receive a full SHA-256 pass.
            candidate_rows = db.execute("""
                SELECT path,size FROM entries
                WHERE batch_id=? AND kind='file' AND size IN (
                    SELECT size FROM entries WHERE batch_id=? AND kind='file'
                    GROUP BY size HAVING COUNT(*)>1
                )
            """, (batch, batch)).fetchall()
            sample_groups: dict[tuple[int, str], list[str]] = defaultdict(list)
            for index, (name, size) in enumerate(candidate_rows, start=1):
                p = Path(name)
                try:
                    sample_groups[(size, quick_signature(p, size))].append(name)
                except OSError as exc:
                    record_error(db, batch, p, exc)
                if progress and index % 10000 == 0:
                    print(f"已筛查重复候选 {index} 项…", file=sys.stderr)
            updates = []
            hashed = 0
            for names in sample_groups.values():
                if len(names) < 2:
                    continue
                for name in names:
                    p = Path(name)
                    try:
                        h = hashlib.sha256()
                        with p.open("rb") as f:
                            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                                h.update(chunk)
                        updates.append((h.hexdigest(), batch, name))
                    except OSError as exc:
                        record_error(db, batch, p, exc)
                    hashed += 1
                    if len(updates) >= 500:
                        db.executemany("UPDATE entries SET digest=? WHERE batch_id=? AND path=?", updates)
                        db.commit()
                        updates.clear()
                    if progress and hashed and hashed % 10000 == 0:
                        print(f"已完整校验重复候选 {hashed} 项…", file=sys.stderr)
            if updates:
                db.executemany("UPDATE entries SET digest=? WHERE batch_id=? AND path=?", updates)
            db.commit()
    except KeyboardInterrupt:
        interrupted = True
    status = "interrupted" if interrupted else ("incomplete" if db.execute("SELECT error_count FROM batches WHERE id=?", (batch,)).fetchone()[0] else "complete")
    finished = now_iso()
    db.execute("UPDATE batches SET finished=?,status=?,file_count=?,dir_count=?,total_bytes=? WHERE id=?",
               (finished, status, files, dirs, total, batch))
    db.commit()
    db.close()
    # Keep CLI output safe for legacy Windows console code pages.
    print(f"Batch {batch}: {status}; files={files}; directories={dirs}; bytes={total}")
    return batch


def generate_report(workspace: Path, batch: str | None = None) -> Path:
    workspace = workspace.resolve()
    db = sqlite3.connect(workspace / "audit.sqlite3")
    db.row_factory = sqlite3.Row
    if batch is None:
        row = db.execute("SELECT id FROM batches ORDER BY started DESC LIMIT 1").fetchone()
        if not row:
            raise ValueError("尚无扫描批次")
        batch = row["id"]
    b = db.execute("SELECT * FROM batches WHERE id=?", (batch,)).fetchone()
    if not b:
        raise ValueError(f"批次不存在: {batch}")
    entries = db.execute("SELECT * FROM entries WHERE batch_id=? AND kind='file' ORDER BY size DESC", (batch,)).fetchall()
    dirs = db.execute("SELECT path FROM entries WHERE batch_id=? AND kind='dir'", (batch,)).fetchall()
    errors = db.execute("SELECT path,message FROM errors WHERE batch_id=? ORDER BY id", (batch,)).fetchall()
    types = Counter()
    for e in entries:
        types[e["extension"]] += e["size"]
    dir_paths = {d["path"] for d in dirs}
    dir_size_map = defaultdict(int)
    # Walk each file's ancestors once. A directory-by-file nested loop becomes
    # quadratic on large volumes and can make report generation appear hung.
    for e in entries:
        parent = str(Path(e["path"]).parent)
        while parent in dir_paths:
            dir_size_map[parent] += e["size"]
            next_parent = str(Path(parent).parent)
            if next_parent == parent:
                break
            parent = next_parent
    dir_sizes = [(path, dir_size_map[path]) for path in dir_paths]
    groups = defaultdict(list)
    for e in entries:
        if e["digest"]:
            groups[e["digest"]].append(e)
    dupes = [g for g in groups.values() if len(g) > 1]
    exact_mode = any(e["digest"] for e in entries)
    if not exact_mode:
        size_groups = defaultdict(list)
        for e in entries:
            size_groups[e["size"]].append(e)
        dupes = [g for g in size_groups.values() if len(g) > 1]
    esc = lambda x: html.escape(str(x), quote=True)
    def table_rows(rows):
        return "".join(f"<tr><td>{esc(a)}</td><td data-n='{int(n)}'>{int(n):,} B</td></tr>" for a,n in rows)
    type_rows = table_rows(sorted(types.items(), key=lambda x:x[1], reverse=True))
    large_rows = table_rows([(e["path"], e["size"]) for e in entries[:100]])
    dir_rows = table_rows(sorted(dir_sizes, key=lambda x:x[1], reverse=True)[:100])
    dupe_html = "".join(
        "<li>" + (f"{g[0]['size']:,} B（{len(g)} 个同大小文件，未验证内容）<br>" if not exact_mode else "")
        + "<br>".join(esc(e["path"]) for e in g[:10])
        + (f"<br>…另有 {len(g)-10} 个" if len(g) > 10 else "") + "</li>"
        for g in dupes[:500]
    )
    if len(dupes) > 500:
        dupe_html += f"<li>其余 {len(dupes)-500} 组已省略</li>"
    err_html = "".join(f"<li>{esc(e['path'])}: {esc(e['message'])}</li>" for e in errors)
    html_doc = f"""<!doctype html><html lang='zh-CN'><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>磁盘审计报告</title>
<style>body{{font:15px system-ui,sans-serif;max-width:1200px;margin:2rem auto;padding:0 1rem;color:#182230}}section{{margin:2rem 0}}table{{border-collapse:collapse;width:100%}}th,td{{padding:.5rem;border-bottom:1px solid #ddd;text-align:left;overflow-wrap:anywhere}}th{{cursor:pointer;background:#f4f6f8}}input{{padding:.6rem;width:min(100%,600px)}}.card{{display:inline-block;padding:1rem;margin:.3rem;background:#eef3f8;border-radius:8px}}</style>
<h1>只读磁盘审计</h1><p>批次 {esc(batch)} · 状态 <b>{esc(b['status'])}</b> · 目标 {esc(b['target'])}</p>
<div class='card'>文件 {b['file_count']:,}</div><div class='card'>目录 {b['dir_count']:,}</div><div class='card'>文件逻辑大小 {b['total_bytes']:,} B</div><div class='card'>异常 {b['error_count']}</div>
<p>卷容量：{(f"{b['volume_total']:,} B，总可用 {b['volume_free']:,} B" if b['volume_total'] is not None else '不可用')}</p>
<label>路径搜索 <input id='q' placeholder='输入路径片段过滤下方结果'></label>
<section><h2>文件类型总大小</h2><table><thead><tr><th>类型</th><th>总大小</th></tr></thead><tbody>{type_rows}</tbody></table></section>
<section><h2>大文件（前 100）</h2><table class='filter'><thead><tr><th>路径</th><th>大小</th></tr></thead><tbody>{large_rows}</tbody></table></section>
<section><h2>大目录（前 100，树内逻辑大小）</h2><table class='filter'><thead><tr><th>路径</th><th>大小</th></tr></thead><tbody>{dir_rows}</tbody></table></section>
<section><h2>{'重复文件候选（SHA-256 已核验）' if exact_mode else '同大小文件候选（未读取文件内容核验）'}</h2><ul>{dupe_html or '<li>未发现候选</li>'}</ul></section><section><h2>异常记录</h2><ul>{err_html or '<li>无</li>'}</ul></section>
<p>候选仅供人工核验。本报告不提供删除或迁移功能。</p><script>const q=document.querySelector('#q');q.addEventListener('input',()=>document.querySelectorAll('table.filter tbody tr').forEach(r=>r.hidden=!r.textContent.toLowerCase().includes(q.value.toLowerCase())));document.querySelectorAll('th').forEach(th=>th.addEventListener('click',()=>{{let t=th.closest('table'),i=[...th.parentNode.children].indexOf(th),body=t.tBodies[0],rows=[...body.rows];rows.sort((a,b)=>{{let x=a.cells[i].dataset.n||a.cells[i].textContent,y=b.cells[i].dataset.n||b.cells[i].textContent;return !isNaN(x)&&!isNaN(y)?Number(x)-Number(y):x.localeCompare(y)}});rows.forEach(r=>body.appendChild(r))}}));</script></html>"""
    (workspace / "reports").mkdir(exist_ok=True)
    out = workspace / "reports" / f"{batch}.html"
    out.write_text(html_doc, encoding="utf-8")
    db.close()
    return out


def main() -> int:
    # Windows PowerShell and legacy consoles may default to cp1252; docs and
    # argparse help are Chinese, so make CLI output deterministic.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="只读磁盘审计工具")
    sub = parser.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("scan", help="扫描指定目录")
    scan.add_argument("--path", type=Path, required=True)
    scan.add_argument("--workspace", type=Path, default=Path(r"E:\DiskAudit"))
    scan.add_argument("--quiet", action="store_true")
    scan.add_argument("--hash-duplicates", action="store_true", help="对同大小候选读取内容并计算完整 SHA-256（大盘可能耗时较长）")
    scan.add_argument("--database", type=Path, help=argparse.SUPPRESS)
    scan.add_argument("--logs-dir", type=Path, help=argparse.SUPPRESS)
    report = sub.add_parser("report", help="生成 HTML 报告")
    report.add_argument("--workspace", type=Path, default=Path(r"E:\DiskAudit"))
    report.add_argument("--batch")
    sub.add_parser("list-drives", help="列出本地卷（不会开始扫描）")
    args = parser.parse_args()
    try:
        if args.command == "scan":
            audit(args.path, args.workspace, not args.quiet, args.hash_duplicates, args.database, args.logs_dir)
        elif args.command == "report":
            print(generate_report(args.workspace, args.batch))
        else:
            print("\n".join(discover_drives()))
        return 0
    except (OSError, ValueError, sqlite3.Error) as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    v02_commands = {"doctor", "status", "open", "serve", "stop"}
    if (len(sys.argv) > 1 and sys.argv[1] in v02_commands) or "--data-dir" in sys.argv:
        runtime = Path(__file__).resolve().parents[1] / "runtime"
        sys.path.insert(0, str(runtime))
        from disk_governance.cli import main as runtime_main
        raise SystemExit(runtime_main())
    raise SystemExit(main())

