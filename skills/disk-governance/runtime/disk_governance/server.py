"""Authenticated loopback-only HTTP workbench server."""
from __future__ import annotations

import json, os, secrets, threading, time, urllib.error, urllib.request, webbrowser
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from .database import DataPaths, Store
from .report_data import build_report_data

UI = Path(__file__).resolve().parents[2] / "ui"
_CHILD_PROCESSES: dict[int, object] = {}

class Server(ThreadingHTTPServer):
    daemon_threads=True
    allow_reuse_address=False


def _acquire_instance_lock(paths:DataPaths):
    """Hold an OS-managed byte lock so parallel starts cannot bind competing services."""
    paths.state.mkdir(parents=True,exist_ok=True)
    handle=(paths.state/"service.lock").open("a+b")
    handle.seek(0,os.SEEK_END)
    if handle.tell()==0: handle.write(b"0");handle.flush()
    handle.seek(0)
    try:
        if os.name=="nt":
            import msvcrt
            msvcrt.locking(handle.fileno(),msvcrt.LK_NBLCK,1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
    except OSError:
        handle.close()
        raise RuntimeError("A Disk Governors service already owns this data directory")
    return handle


def _serve(paths: DataPaths, port: int) -> None:
    lock=_acquire_instance_lock(paths)
    token=secrets.token_urlsafe(32); instance=secrets.token_hex(16)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*_): pass
        def _json(self,obj,status=200):
            raw=json.dumps(obj,ensure_ascii=False).encode(); self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Cache-Control","no-store"); self.send_header("Content-Length",str(len(raw))); self.end_headers(); self.wfile.write(raw)
        def _same_origin_host(self):
            host=self.headers.get("Host","")
            if host not in {f"127.0.0.1:{self.server.server_port}",f"localhost:{self.server.server_port}"}: return False
            origin=self.headers.get("Origin")
            if origin and origin not in {f"http://127.0.0.1:{self.server.server_port}",f"http://localhost:{self.server.server_port}"}: return False
            return True
        def _auth(self):
            return self._same_origin_host() and self.headers.get("X-Disk-Governors-Token")==token
        def do_GET(self):
            u=urlparse(self.path); qs=parse_qs(u.query)
            if u.path=="/session":
                if not self._same_origin_host(): return self._json({"error":"invalid host or origin"},403)
                return self._json({"token":token,"instance":instance})
            if u.path.startswith("/api/") or u.path.startswith("/download/"):
                if not self._auth(): return self._json({"error":"unauthorized"},403)
            elif not self._same_origin_host(): return self._json({"error":"invalid host or origin"},403)
            if u.path.startswith("/download/"):
                name=u.path.removeprefix("/download/")
                if not re.fullmatch(r"[a-f0-9]{32}(?:-offline)?\.html",name): return self._json({"error":"not found"},404)
                file=paths.reports/name
                if not file.is_file(): return self._json({"error":"report not found"},404)
                body=file.read_bytes(); self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Disposition",f'attachment; filename="{name}"'); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body); return
            if u.path.startswith("/api/v1/"):
                try:
                    with Store.open(paths,read_only=False,migrate=True) as db:
                        batch=(qs.get("batch_id") or [None])[0]
                        if u.path=="/api/v1/batches": data=db.list_batches(500)
                        else:
                            batch=batch or ((db.list_batches(1) or [{}])[0].get("id"))
                            if not batch: return self._json({"error":"no batches"},404)
                            cached=int(db.conn.execute("SELECT COUNT(*) FROM directory_stats WHERE batch_id=?",(batch,)).fetchone()[0])
                            if cached==0 and int(db.get_batch(batch)["dir_count"] or 0): db.rebuild_directory_stats(batch)
                            if u.path=="/api/v1/overview": data=build_report_data(db,batch)
                            elif u.path=="/api/v1/files": data=db.search_files(batch,query=(qs.get("q") or [""])[0],extension=(qs.get("extension") or [""])[0],sort_by=(qs.get("sort") or ["size"])[0],order=(qs.get("order") or ["desc"])[0],page=int((qs.get("page") or [1])[0]),page_size=int((qs.get("page_size") or [50])[0]))
                            elif u.path=="/api/v1/directories": data=db.list_directories(batch,(qs.get("parent") or [""])[0])
                            elif u.path=="/api/v1/file": data=db.get_file(batch,(qs.get("path") or [""])[0])
                            elif u.path=="/api/v1/errors": data={"items":db.get_errors(batch,500),"total":db.get_batch(batch)["error_count"]}
                            elif u.path=="/api/v1/candidates":
                                from .candidates import generate_candidates
                                generate_candidates(db,batch)
                                data=db.get_candidates(batch,query=(qs.get("q") or [""])[0],risk=(qs.get("risk") or [""])[0],category=(qs.get("category") or [""])[0],status=(qs.get("status") or [""])[0],page=int((qs.get("page") or [1])[0]),page_size=int((qs.get("page_size") or [50])[0]))
                            elif u.path=="/api/v1/history": data=db.review_history((qs.get("candidate_id") or [""])[0])
                            elif u.path=="/api/v1/reviews/history": data=db.review_events_for_batch(batch,limit=int((qs.get("limit") or [100])[0]),offset=int((qs.get("offset") or [0])[0]))
                            else: return self._json({"error":"not found"},404)
                    return self._json(data)
                except (ValueError,KeyError) as exc: return self._json({"error":str(exc)},400)
                except Exception: return self._json({"error":"request failed"},500)
            allowed={"/":"index.html","/index.html":"index.html","/styles.css":"styles.css","/app.js":"app.js"}
            name=allowed.get(u.path)
            if not name: return self._json({"error":"not found"},404)
            body=(UI/name).read_bytes(); mime="text/html; charset=utf-8" if name.endswith("html") else "text/javascript; charset=utf-8" if name.endswith("js") else "text/css; charset=utf-8"
            self.send_response(200); self.send_header("Content-Type",mime); self.send_header("X-Content-Type-Options","nosniff"); self.send_header("Content-Security-Policy","default-src 'self'; connect-src 'self'; style-src 'self'; script-src 'self'; img-src 'self' data:"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
        def do_POST(self):
            if not self._auth(): return self._json({"error":"unauthorized"},403)
            if self.path=="/api/v1/stop":
                try: body=json.loads(self.rfile.read(min(int(self.headers.get("Content-Length","0")),65536)))
                except Exception: return self._json({"error":"invalid body"},400)
                if body.get("instance")!=instance: return self._json({"error":"instance mismatch"},409)
                self._json({"stopping":True}); threading.Thread(target=self.server.shutdown,daemon=True).start(); return
            if self.path=="/api/v1/report":
                try:
                    body=json.loads(self.rfile.read(min(int(self.headers.get("Content-Length","0")),65536)))
                    from .offline import generate_offline
                    from .candidates import generate_candidates
                    with Store.open(paths,read_only=False,migrate=True) as db:
                        batch=body.get("batch_id")
                        if not isinstance(batch,str) or not re.fullmatch(r"[a-f0-9]{32}",batch) or not db.get_batch(batch): return self._json({"error":"batch not found"},404)
                        if int(db.conn.execute("SELECT COUNT(*) FROM directory_stats WHERE batch_id=?",(batch,)).fetchone()[0])==0 and int(db.get_batch(batch)["dir_count"] or 0): db.rebuild_directory_stats(batch)
                        generate_candidates(db,batch); data=build_report_data(db,batch)
                        file=generate_offline(data,paths.reports/f"{batch}-offline.html")
                    return self._json({"name":file.name,"url":f"/download/{file.name}"})
                except Exception: return self._json({"error":"report generation failed"},500)
            if self.path!="/api/v1/reviews": return self._json({"error":"not found"},404)
            try:
                body=json.loads(self.rfile.read(min(int(self.headers.get("Content-Length","0")),65536)))
                with Store.open(paths,read_only=False,migrate=True) as db: result=db.update_review(**body,actor="local-workbench")
                return self._json(result)
            except (ValueError,KeyError,PermissionError) as exc: return self._json({"error":str(exc)},400)
            except Exception: return self._json({"error":"request failed"},500)

    server=Server(("127.0.0.1",port),Handler)
    actual=server.server_port
    state={"pid":os.getpid(),"instance":instance,"token":token,"port":actual,"started":time.time()}
    paths.state.mkdir(parents=True,exist_ok=True); tmp=paths.state/"service.json.tmp"; tmp.write_text(json.dumps(state),encoding="utf-8"); tmp.replace(paths.state/"service.json")
    try: server.serve_forever(poll_interval=.25)
    finally:
        server.server_close()
        try:
            current=json.loads((paths.state/"service.json").read_text(encoding="utf-8"))
            if current.get("instance")==instance: (paths.state/"service.json").unlink()
        except (OSError,ValueError): pass
        lock.close()


def _request(state:dict, path:str, method="GET", body=None):
    url=f"http://127.0.0.1:{state['port']}{path}"
    req=urllib.request.Request(url,data=json.dumps(body).encode() if body is not None else None,method=method,headers={"X-Disk-Governors-Token":state["token"],"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=2) as r: return json.load(r)

def start_or_open(paths:DataPaths,port:int=0)->str:
    statefile=paths.state/"service.json"
    if statefile.exists():
        try:
            state=json.loads(statefile.read_text(encoding="utf-8")); identity=_request(state,"/session")
            if identity.get("instance")!=state.get("instance"): raise RuntimeError("service identity mismatch")
            webbrowser.open(f"http://127.0.0.1:{state['port']}/"); return f"http://127.0.0.1:{state['port']}/"
        except Exception: pass
    import subprocess,sys
    flags=(getattr(subprocess,"CREATE_NO_WINDOW",0)|getattr(subprocess,"DETACHED_PROCESS",0)) if os.name=="nt" else 0
    env=os.environ.copy(); runtime=str(Path(__file__).resolve().parents[1]); env["PYTHONPATH"]=runtime+(os.pathsep+env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
    child=subprocess.Popen([sys.executable,"-m","disk_governance.server_worker",str(paths.root),str(port)],creationflags=flags,close_fds=True,env=env)
    _CHILD_PROCESSES[child.pid]=child
    for _ in range(60):
        time.sleep(.2)
        try:
            state=json.loads(statefile.read_text(encoding="utf-8")); identity=_request(state,"/session")
            if identity.get("instance")!=state.get("instance"): continue
            webbrowser.open(f"http://127.0.0.1:{state['port']}/"); return f"http://127.0.0.1:{state['port']}/"
        except Exception: continue
    raise RuntimeError("工作台启动超时；查看本地 logs 目录")

def stop_service(paths:DataPaths)->bool:
    f=paths.state/"service.json"
    try:
        state=json.loads(f.read_text(encoding="utf-8")); _request(state,"/api/v1/stop","POST",{"instance":state["instance"]})
        child=_CHILD_PROCESSES.pop(int(state["pid"]),None)
        if child is not None: child.wait(timeout=5)
        return True
    except Exception: return False

if __name__=="__main__":
    import sys
    _serve(DataPaths(Path(sys.argv[1])),int(sys.argv[2]))

