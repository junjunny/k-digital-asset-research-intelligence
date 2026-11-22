#!/usr/bin/env python3
"""K-DARI evidence records validator (standard library only)."""

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from verify_evidence import build_safe_opener, validate_remote_url

REQUIRED = {
    "evidence_id", "source_title", "publisher", "jurisdiction", "source_type",
    "legal_status", "official_url", "publication_date", "retrieved_at",
    "effective_date", "relevant_excerpt", "page_or_section", "verification_status",
}
SOURCE_TYPES = {
    "LAW", "REGULATION", "OFFICIAL_POLICY", "LEGISLATIVE_MATERIAL",
    "REGULATORY_GUIDANCE", "OFFICIAL_DISCLOSURE", "PRIMARY_BUSINESS_SOURCE",
    "SECONDARY_SOURCE", "USER_PROVIDED",
}
LEGAL_STATUSES = {
    "IN_FORCE", "ENACTED_NOT_EFFECTIVE", "PROPOSED_BILL",
    "PASSED_NOT_PROMULGATED", "DRAFT_REGULATION", "POLICY_ANNOUNCEMENT",
    "GUIDANCE", "REPEALED", "NOT_APPLICABLE",
}
VERIFICATION_STATUSES = {"VERIFIED", "PARTIALLY_VERIFIED", "UNVERIFIED", "NEEDS_REVIEW"}
CONTENT_STATUSES = {"URL_REACHABLE", "CONTENT_VERIFIED", "CONTENT_MISMATCH", "ACCESS_RESTRICTED", "MANUAL_REVIEW_REQUIRED"}
AUTHENTICITY_STATUSES = {"OFFICIAL_URL_FETCHED", "NOT_VERIFIED"}
ACCESS_STATUSES = {"REMOTE_FETCHED", "LOCAL_ATTACHMENT_LOADED", "NOT_ACCESSED"}
EXCERPT_STATUSES = {"MATCHED", "NOT_MATCHED", "NOT_CHECKED"}
MEANING_REVIEW_STATUSES = {"MANUAL_REVIEWED", "NOT_REVIEWED"}


def parse_date(value, field, evidence_id, errors, nullable=False):
    if value is None and nullable:
        return None
    if not isinstance(value, str):
        errors.append(f"{evidence_id}: {field} must be YYYY-MM-DD")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{evidence_id}: {field} is not a valid YYYY-MM-DD date")
        return None


def extract_records(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and "evidence" in payload:
        return payload["evidence"]
    if isinstance(payload, dict):
        return [payload]
    raise ValueError("input must be an evidence object, list, or report containing evidence")


def check_url(url, timeout):
    try:
        validate_remote_url(url)
        request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "K-DARI-source-validator/0.1"})
        with build_safe_opener().open(request, timeout=timeout) as response:
            validate_remote_url(response.geturl())
            return 200 <= response.status < 400, str(response.status)
    except urllib.error.HTTPError:
        # Some official sites return an error for HEAD while serving the same URL via GET.
        request = urllib.request.Request(url, method="GET", headers={"User-Agent": "K-DARI-source-validator/0.1"})
        try:
            with build_safe_opener().open(request, timeout=timeout) as response:
                validate_remote_url(response.geturl())
                return 200 <= response.status < 400, str(response.status)
        except Exception as retry_exc:  # network result, reported rather than hidden
            return False, str(retry_exc)
    except Exception as exc:
        return False, str(exc)


def validate_records(records, check_urls=False, timeout=10):
    errors, warnings = [], []
    seen = set()
    if not isinstance(records, list) or not records:
        return ["evidence list must contain at least one record"], warnings

    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"record {index}: must be an object")
            continue
        evidence_id = record.get("evidence_id", f"record {index}")
        missing = sorted(REQUIRED - set(record))
        if missing:
            errors.append(f"{evidence_id}: missing fields: {', '.join(missing)}")
            continue
        if not isinstance(evidence_id, str) or not evidence_id.startswith("EV-"):
            errors.append(f"{evidence_id}: evidence_id must start with EV-")
        if evidence_id in seen:
            errors.append(f"{evidence_id}: duplicate evidence_id")
        seen.add(evidence_id)
        for field in ("source_title", "publisher", "jurisdiction", "relevant_excerpt", "page_or_section"):
            if not isinstance(record[field], str) or not record[field].strip():
                errors.append(f"{evidence_id}: {field} must be a non-empty string")
        if record["source_type"] not in SOURCE_TYPES:
            errors.append(f"{evidence_id}: invalid source_type")
        if record["legal_status"] not in LEGAL_STATUSES:
            errors.append(f"{evidence_id}: invalid legal_status")
        if record["verification_status"] not in VERIFICATION_STATUSES:
            errors.append(f"{evidence_id}: invalid verification_status")
        verification = record.get("verification")
        if record.get("schema_version") == "2.0":
            if not isinstance(verification, dict):
                errors.append(f"{evidence_id}: schema v2 requires verification metadata")
            elif verification.get("status") not in CONTENT_STATUSES:
                errors.append(f"{evidence_id}: invalid content verification status")
            else:
                dimensions = {
                    "source_authenticity": AUTHENTICITY_STATUSES,
                    "document_access": ACCESS_STATUSES,
                    "excerpt_verification": EXCERPT_STATUSES,
                    "legal_meaning_review": MEANING_REVIEW_STATUSES,
                }
                for field, allowed in dimensions.items():
                    if verification.get(field) not in allowed:
                        errors.append(f"{evidence_id}: invalid or missing verification.{field}")
            if "status_checked_at" not in record:
                errors.append(f"{evidence_id}: schema v2 requires status_checked_at")
        if record["verification_status"] == "VERIFIED":
            if not isinstance(verification, dict) or verification.get("status") != "CONTENT_VERIFIED":
                errors.append(f"{evidence_id}: VERIFIED requires CONTENT_VERIFIED, not URL reachability alone")

        publication_date = parse_date(record["publication_date"], "publication_date", evidence_id, errors, nullable=True)
        retrieved_at = parse_date(record["retrieved_at"], "retrieved_at", evidence_id, errors)
        effective_date = parse_date(record["effective_date"], "effective_date", evidence_id, errors, nullable=True)
        if publication_date and retrieved_at and publication_date > retrieved_at:
            errors.append(f"{evidence_id}: publication_date is later than retrieved_at")
        if record["legal_status"] == "ENACTED_NOT_EFFECTIVE" and not effective_date:
            errors.append(f"{evidence_id}: ENACTED_NOT_EFFECTIVE requires effective_date")
        if record["legal_status"] == "IN_FORCE" and effective_date and retrieved_at and effective_date > retrieved_at:
            errors.append(f"{evidence_id}: IN_FORCE conflicts with future effective_date")
        if record.get("status_checked_at") is not None:
            parse_date(record.get("status_checked_at"), "status_checked_at", evidence_id, errors)
        provisions = record.get("provisions", [])
        if not isinstance(provisions, list):
            errors.append(f"{evidence_id}: provisions must be a list")
        else:
            provision_ids = set()
            for provision in provisions:
                if not isinstance(provision, dict):
                    errors.append(f"{evidence_id}: every provision must be an object")
                    continue
                provision_id = provision.get("provision_id")
                if not provision_id or provision_id in provision_ids:
                    errors.append(f"{evidence_id}: provision_id must be non-empty and unique")
                provision_ids.add(provision_id)
                parse_date(provision.get("effective_date"), "provision.effective_date", evidence_id, errors, nullable=True)
                parse_date(provision.get("expiry_date"), "provision.expiry_date", evidence_id, errors, nullable=True)

        url = record["official_url"]
        parsed = urlparse(url) if isinstance(url, str) else None
        if not parsed or parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"{evidence_id}: official_url must be an absolute HTTP(S) URL")
        else:
            if record["source_type"] != "SECONDARY_SOURCE" and parsed.scheme != "https":
                warnings.append(f"{evidence_id}: primary/official source should use HTTPS where available")
            if check_urls:
                ok, detail = check_url(url, timeout)
                if not ok:
                    errors.append(f"{evidence_id}: URL check failed: {detail}")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validate K-DARI evidence JSON")
    parser.add_argument("path", type=Path)
    parser.add_argument("--check-urls", action="store_true", help="perform live HTTP checks")
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()
    try:
        payload = json.loads(args.path.read_text(encoding="utf-8"))
        records = extract_records(payload)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    errors, warnings = validate_records(records, args.check_urls, args.timeout)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"OK: {len(records)} evidence record(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

