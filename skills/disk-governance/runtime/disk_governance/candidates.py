"""Conservative metadata-only audit candidates; never claim deletion safety."""
from __future__ import annotations
import hashlib
from datetime import datetime, timezone
from .classification import RULE_VERSION, candidate_risk, classify_path
from .database import Store

def generate_candidates(store:Store,batch_id:str)->int:
    marker=f"candidates-generated:{batch_id}:{RULE_VERSION}"
    if store.conn.execute("SELECT 1 FROM app_meta WHERE key=?",(marker,)).fetchone(): return 0
    rows=[]; now=datetime.now(timezone.utc).isoformat()
    for row in store.conn.execute("SELECT path,extension,size FROM entries WHERE batch_id=? AND kind='file' AND size>=104857600 ORDER BY size DESC LIMIT 10000",(batch_id,)):
        path=row["path"]; cl=classify_path(path,row["extension"]); risk,reason,evidence=candidate_risk(path,"large_file")
        key="large:"+path; cid=hashlib.sha256(f"{batch_id}|{RULE_VERSION}|{key}".encode()).hexdigest()
        rows.append(dict(candidate_id=cid,rule_version=RULE_VERSION,kind="large_file",subject_key=key,path=path,category=cl.category,risk_level=risk,confidence=cl.confidence,size_bytes=int(row["size"]),reason="大文件元数据候选；大小不代表可清理。"+reason,evidence={"rule_id":"size-over-100MiB","signals":[f"size_bytes:{row['size']}",*evidence],"classification":cl.as_dict()},created_at=now))
    for row in store.conn.execute("SELECT path,parent_path,total_bytes,file_count FROM directory_stats WHERE batch_id=? ORDER BY total_bytes DESC LIMIT 10000",(batch_id,)):
        parts={p.casefold() for p in str(row["path"]).replace("/","\\").split("\\")}
        if not parts.intersection({"cache",".cache","tmp","temp","build","dist","node_modules","__pycache__"}): continue
        path=row["path"]; risk,reason,evidence=candidate_risk(path,"cache_or_build_directory")
        key="directory:"+path; cid=hashlib.sha256(f"{batch_id}|{RULE_VERSION}|{key}".encode()).hexdigest()
        rows.append(dict(candidate_id=cid,rule_version=RULE_VERSION,kind="cache_or_build_directory",subject_key=key,path=path,category="缓存与构建",risk_level=risk,confidence="低",size_bytes=int(row["total_bytes"]),reason=reason,evidence={"rule_id":"directory-name-heuristic","signals":evidence,"file_count":row["file_count"]},created_at=now))
    # Equal-size groups are candidates only; no content hashes are read in v0.2.
    for row in store.conn.execute("SELECT size,COUNT(*) AS n FROM entries WHERE batch_id=? AND kind='file' GROUP BY size HAVING COUNT(*) BETWEEN 2 AND 100 ORDER BY n DESC LIMIT 500",(batch_id,)):
        size=int(row["size"]); key=f"same-size:{size}"; risk,reason,evidence=candidate_risk(key,"same_size_group")
        cid=hashlib.sha256(f"{batch_id}|{RULE_VERSION}|{key}".encode()).hexdigest()
        rows.append(dict(candidate_id=cid,rule_version=RULE_VERSION,kind="same_size_group",subject_key=key,path=None,category="重复候选（未验证）",risk_level=risk,confidence="低",size_bytes=size*int(row["n"]),reason=reason,evidence={"rule_id":"same-size-only","signals":evidence,"file_count":int(row["n"]),"content_verified":False},created_at=now))
    store.replace_candidates(batch_id,rows)
    with store.transaction() as conn: conn.execute("INSERT OR REPLACE INTO app_meta(key,value) VALUES(?,?)",(marker,now))
    return len(rows)

