"""Unified command line entry for the Disk Governors Skill."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import webbrowser
from pathlib import Path

from .database import DataPaths, Store
from .report_data import build_report_data


def _paths(value: str | None) -> DataPaths:
    if value:
        return DataPaths(Path(value))
    env = os.environ.get("DISK_GOVERNORS_DATA_DIR")
    return DataPaths(Path(env)) if env else DataPaths.default()


def _scan(target: Path, paths: DataPaths, quiet: bool) -> int:
    script = Path(__file__).resolve().parents[2] / "scripts" / "main.py"
    paths.prepare()
    # Keep v0.1 scanner semantics and its tested reparse-point handling.
    proc = subprocess.run([sys.executable, str(script), "scan", "--path", str(target),
                           "--workspace", str(paths.root), "--database", str(paths.database),
                           "--logs-dir", str(paths.logs), *( ["--quiet"] if quiet else [])])
    return proc.returncode


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="disk-governors", description="只读磁盘治理工作台")
    p.add_argument("--data-dir", help="用户数据目录；默认 %LOCALAPPDATA%\\DiskGovernors")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor", help="检查 Python、SQLite 与运行目录")
    sub.add_parser("status", help="显示本地数据与最近批次")
    scan = sub.add_parser("scan", help="只读扫描用户指定目录")
    scan.add_argument("--path", type=Path, required=True); scan.add_argument("--quiet", action="store_true")
    report = sub.add_parser("report", help="生成只读离线 HTML 报告"); report.add_argument("--batch")
    op = sub.add_parser("open", help="生成并打开离线报告"); op.add_argument("--batch")
    serve = sub.add_parser("serve", help="按需启动本机工作台"); serve.add_argument("--port", type=int, default=0)
    sub.add_parser("stop", help="停止已验证的本机工作台实例")
    # Accept the data path both before and after the subcommand.
    for command_parser in sub.choices.values():
        command_parser.add_argument("--data-dir", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    args = p.parse_args(argv); paths = _paths(args.data_dir)
    try:
        if args.command == "doctor":
            import sqlite3
            from . import __version__,MIN_PYTHON
            python_ok=sys.version_info[:2]>=MIN_PYTHON;sqlite_ok=sqlite3.sqlite_version_info>=(3,24,0)
            print(json.dumps({"runtime":__version__,"python":sys.version.split()[0],"python_supported":python_ok,
                              "sqlite":sqlite3.sqlite_version,"sqlite_supported":sqlite_ok,
                              "data_dir":str(paths.root),"database_exists":paths.database.exists()},ensure_ascii=False,indent=2))
            return 0 if python_ok and sqlite_ok else 2
        if args.command == "scan": return _scan(args.path, paths, args.quiet)
        if args.command == "status":
            if not paths.database.exists(): print(f"尚无数据库：{paths.database}"); return 0
            with Store.open(paths,read_only=True) as db: print(json.dumps(db.list_batches(20),ensure_ascii=False,indent=2))
            return 0
        if args.command in {"report","open"}:
            from .offline import generate_offline
            from .candidates import generate_candidates
            paths.prepare()
            with Store.open(paths,read_only=False,migrate=True) as db:
                batches=db.list_batches(1); batch=args.batch or (batches[0]["id"] if batches else None)
                if not batch: raise ValueError("尚无扫描批次")
                if not re.fullmatch(r"[a-f0-9]{32}",batch): raise ValueError("批次 ID 格式无效")
                if int(db.conn.execute("SELECT COUNT(*) FROM directory_stats WHERE batch_id=?",(batch,)).fetchone()[0])==0 and int(db.get_batch(batch)["dir_count"] or 0): db.rebuild_directory_stats(batch)
                generate_candidates(db,batch)
                data=build_report_data(db,batch)
                out=generate_offline(data,paths.reports / f"{batch}-offline.html")
            print(out)
            if args.command=="open": webbrowser.open(out.as_uri())
            return 0
        from .server import start_or_open, stop_service
        if args.command=="serve":
            paths.prepare(); print(start_or_open(paths,args.port)); return 0
        if args.command=="stop": print("stopped" if stop_service(paths) else "not running"); return 0
    except (OSError,ValueError,RuntimeError,KeyError) as exc:
        print(f"Error: {exc}",file=sys.stderr); return 2
    return 2


if __name__ == "__main__": raise SystemExit(main())

