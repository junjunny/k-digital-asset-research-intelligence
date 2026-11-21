#!/usr/bin/env python3
"""Migrate legacy Evidence records without claiming content verification."""

import argparse
import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path


def migrate_payload(payload, checked_at=None):
    updated = deepcopy(payload)
    records = updated if isinstance(updated, list) else updated["evidence"]
    checked_at = checked_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    for record in records:
        if record.get("schema_version") == "2.0" and record.get("verification"):
            continue
        record["schema_version"] = "2.0"
        record["status_checked_at"] = None
        record["verification_status"] = "NEEDS_REVIEW"
        record["verification"] = {
            "status": "MANUAL_REVIEW_REQUIRED",
            "checked_at": checked_at,
            "method": "URL_ONLY",
            "http_status": None,
            "content_type": None,
            "final_url": record.get("official_url"),
            "document_sha256": None,
            "extracted_text_sha256": None,
            "content_length": None,
            "excerpt_match": None,
            "matched_excerpt": None,
            "source_authenticity": "NOT_VERIFIED",
            "document_access": "NOT_ACCESSED",
            "excerpt_verification": "NOT_CHECKED",
            "legal_meaning_review": "NOT_REVIEWED",
            "warnings": ["MIGRATED_FROM_V1_WITHOUT_CONTENT_VERIFICATION"],
            "error": None
        }
    if isinstance(updated, dict):
        updated["schema_version"] = "2.0"
    return updated


def main():
    parser = argparse.ArgumentParser(description="Migrate K-DARI Evidence v1 to v2")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    updated = migrate_payload(payload)
    records = updated if isinstance(updated, list) else updated["evidence"]
    args.output.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Migrated {len(records)} record(s) to {args.output}")


if __name__ == "__main__":
    main()

