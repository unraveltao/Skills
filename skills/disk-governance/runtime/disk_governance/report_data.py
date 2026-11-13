"""Versioned, presentation-neutral report data contract."""
from __future__ import annotations

from datetime import datetime, timezone

from .classification import RULE_VERSION
from .database import Store

REPORT_SCHEMA_VERSION = 1


def build_report_data(store: Store, batch_id: str) -> dict:
    batch = store.get_batch(batch_id)
    if batch is None:
        raise KeyError(f"Batch not found: {batch_id}")
    categories=store.get_categories(batch_id)
    errors_total=int(batch["error_count"] or 0)
    errors=store.get_errors(batch_id,limit=500)
    candidates=store.get_candidates(batch_id,page=1,page_size=200)
    return {
        "schema_version": REPORT_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "classification_rule_version": RULE_VERSION,
        "batch": {
            "id": batch["id"], "target": batch["target"], "started": batch["started"],
            "finished": batch["finished"], "status": batch["status"],
            "file_count": batch["file_count"], "dir_count": batch["dir_count"],
            "logical_bytes": batch["total_bytes"], "error_count": errors_total,
        },
        "volume": {
            "total_bytes": batch["volume_total"], "free_bytes": batch["volume_free"],
            "used_bytes": (batch["volume_total"]-batch["volume_free"])
                if batch["volume_total"] is not None and batch["volume_free"] is not None else None,
        },
        "categories": categories,
        "file_types": store.file_types(batch_id,100),
        "top_files": store.largest_files(batch_id,100),
        "top_directories": store.top_directories(batch_id,100),
        "candidates": {"total":candidates["total"],"items":candidates["items"],"truncated":candidates["total"]>len(candidates["items"])},
        "errors": {"total":errors_total,"items":errors,"truncated":len(errors)<errors_total},
    }

