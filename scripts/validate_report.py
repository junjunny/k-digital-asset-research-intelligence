#!/usr/bin/env python3
"""Validate K-DARI report evidence, legal status, dates, and claim types."""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from validate_sources import validate_records

CLASSIFICATIONS = {"VERIFIED_FACT", "SUPPORTED_INFERENCE", "UNVERIFIED", "NEEDS_REVIEW"}
CONFIDENCE = {"HIGH", "MEDIUM", "LOW"}
CLAIM_COMPATIBILITY = {
    "LAW_EFFECTIVE": {"IN_FORCE"},
    "LAW_PROMULGATED_NOT_EFFECTIVE": {"ENACTED_NOT_EFFECTIVE"},
    "BILL_PROPOSED": {"PROPOSED_BILL", "PASSED_NOT_PROMULGATED"},
    "REGULATION_DRAFT": {"DRAFT_REGULATION"},
    "POLICY_ANNOUNCEMENT": {"POLICY_ANNOUNCEMENT"},
    "REGULATORY_GUIDANCE": {"GUIDANCE"},
    "BUSINESS_MODEL_FACT": {"NOT_APPLICABLE", "IN_FORCE", "GUIDANCE"},
    "BUSINESS_APPLICABILITY_INFERENCE": {
        "IN_FORCE", "ENACTED_NOT_EFFECTIVE", "PROPOSED_BILL", "PASSED_NOT_PROMULGATED",
        "DRAFT_REGULATION", "POLICY_ANNOUNCEMENT", "GUIDANCE", "NOT_APPLICABLE",
    },
    "OTHER_FACT": {
        "IN_FORCE", "ENACTED_NOT_EFFECTIVE", "PROPOSED_BILL", "PASSED_NOT_PROMULGATED",
        "DRAFT_REGULATION", "POLICY_ANNOUNCEMENT", "GUIDANCE", "REPEALED", "NOT_APPLICABLE",
    },
}
LEGAL_CLAIMS = {
    "LAW_EFFECTIVE", "LAW_PROMULGATED_NOT_EFFECTIVE", "BILL_PROPOSED",
    "REGULATION_DRAFT", "POLICY_ANNOUNCEMENT", "REGULATORY_GUIDANCE",
}
OFFICIAL_LEGAL_SOURCE_TYPES = {"LAW", "REGULATION", "OFFICIAL_POLICY", "LEGISLATIVE_MATERIAL", "REGULATORY_GUIDANCE"}


def valid_date(value):
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def jurisdiction_matches(finding_jurisdiction, evidence_jurisdiction):
    left = finding_jurisdiction.strip().casefold()
    right = evidence_jurisdiction.strip().casefold()
    return left == right or left in right or right in left


def provision_effective_date(linked, provision_refs, errors, finding_id):
    if not provision_refs:
        return None
    provision_map = {}
    for item in linked:
        for provision in item.get("provisions", []):
            provision_map[provision.get("provision_id")] = provision
    unknown = sorted(set(provision_refs) - set(provision_map))
    if unknown:
        errors.append(f"{finding_id}: unknown provision refs: {', '.join(unknown)}")
        return None
    dates = {valid_date(provision_map[ref].get("effective_date")) for ref in provision_refs}
    dates.discard(None)
    if len(dates) > 1:
        errors.append(f"{finding_id}: referenced provisions have different effective dates; split the finding")
        return None
    return next(iter(dates), None)


def validate_report(report, base_dir=None):
    errors, warnings = [], []
    required = {"report_id", "title", "analysis_date", "jurisdictions", "research_question", "findings", "limitations"}
    missing = sorted(required - set(report))
    if missing:
        return [f"report: missing fields: {', '.join(missing)}"], warnings
    analysis_date = valid_date(report["analysis_date"])
    if not analysis_date:
        errors.append("report: analysis_date must be YYYY-MM-DD")
    if not isinstance(report["limitations"], list) or not report["limitations"]:
        errors.append("report: limitations must contain at least one item")
    evidence_records = report.get("evidence")
    if evidence_records is None and report.get("evidence_file") and base_dir:
        evidence_ref = Path(report["evidence_file"])
        root = base_dir.resolve()
        try:
            if evidence_ref.is_absolute():
                raise ValueError("evidence_file must be relative to the report directory")
            evidence_path = (root / evidence_ref).resolve()
            if not evidence_path.is_relative_to(root):
                raise ValueError("evidence_file escapes the report directory")
            evidence_records = json.loads(evidence_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"report: cannot load evidence_file: {exc}")
            evidence_records = []
    if evidence_records is None:
        errors.append("report: evidence or resolvable evidence_file is required")
        evidence_records = []
    source_errors, source_warnings = validate_records(evidence_records)
    errors.extend(source_errors)
    warnings.extend(source_warnings)
    evidence = {item.get("evidence_id"): item for item in evidence_records if isinstance(item, dict)}

    findings = report.get("findings")
    if not isinstance(findings, list) or not findings:
        errors.append("report: findings must contain at least one item")
        return errors, warnings
    seen = set()
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            errors.append(f"finding {index}: must be an object")
            continue
        finding_id = finding.get("finding_id", f"finding {index}")
        for field in ("statement", "claim_type", "classification", "evidence_ids", "confidence", "jurisdiction", "as_of_date"):
            if field not in finding:
                errors.append(f"{finding_id}: missing {field}")
        if finding_id in seen:
            errors.append(f"{finding_id}: duplicate finding_id")
        seen.add(finding_id)
        claim_type = finding.get("claim_type")
        if claim_type not in CLAIM_COMPATIBILITY:
            errors.append(f"{finding_id}: invalid claim_type")
        classification = finding.get("classification")
        if classification not in CLASSIFICATIONS:
            errors.append(f"{finding_id}: invalid classification")
        if finding.get("confidence") not in CONFIDENCE:
            errors.append(f"{finding_id}: invalid confidence")
        evidence_ids = finding.get("evidence_ids", [])
        if not isinstance(evidence_ids, list):
            errors.append(f"{finding_id}: evidence_ids must be a list")
            continue
        if classification in {"VERIFIED_FACT", "SUPPORTED_INFERENCE"} and not evidence_ids:
            errors.append(f"{finding_id}: {classification} requires evidence")
        unknown = sorted(set(evidence_ids) - set(evidence))
        if unknown:
            errors.append(f"{finding_id}: unknown evidence IDs: {', '.join(unknown)}")
        as_of = valid_date(finding.get("as_of_date"))
        if not as_of:
            errors.append(f"{finding_id}: as_of_date must be YYYY-MM-DD")
        elif analysis_date and as_of != analysis_date:
            errors.append(f"{finding_id}: as_of_date must equal report analysis_date")

        linked = [evidence[eid] for eid in evidence_ids if eid in evidence]
        compatible_statuses = CLAIM_COMPATIBILITY.get(claim_type, set())
        if linked and claim_type != "BUSINESS_APPLICABILITY_INFERENCE":
            if not any(item.get("legal_status") in compatible_statuses for item in linked):
                errors.append(f"{finding_id}: claim_type {claim_type} is incompatible with linked legal_status values")

        if claim_type in LEGAL_CLAIMS and linked:
            if not any(jurisdiction_matches(finding.get("jurisdiction", ""), item.get("jurisdiction", "")) for item in linked):
                errors.append(f"{finding_id}: legal claim jurisdiction does not match linked evidence")
            if not any(item.get("source_type") in OFFICIAL_LEGAL_SOURCE_TYPES for item in linked):
                errors.append(f"{finding_id}: legal claim requires an official legal or regulatory source")

        if classification == "VERIFIED_FACT" and linked:
            if not any(item.get("verification", {}).get("status") == "CONTENT_VERIFIED" for item in linked):
                errors.append(f"{finding_id}: VERIFIED_FACT requires at least one CONTENT_VERIFIED source")

        if claim_type == "BUSINESS_APPLICABILITY_INFERENCE" and classification == "VERIFIED_FACT":
            errors.append(f"{finding_id}: business applicability must be an inference or review item")

        if linked and classification in {"VERIFIED_FACT", "SUPPORTED_INFERENCE"}:
            warnings.append(
                f"{finding_id}: structural evidence compatibility does not prove that the source "
                "semantically or legally supports the statement; manual meaning review remains required"
            )

        provision_date = provision_effective_date(linked, finding.get("provision_refs", []), errors, finding_id)
        effective_dates = [valid_date(item.get("effective_date")) for item in linked]
        effective_dates = [item for item in effective_dates if item]
        effective_date = provision_date or (effective_dates[0] if len(set(effective_dates)) == 1 else None)
        if analysis_date and effective_date:
            if claim_type == "LAW_EFFECTIVE" and effective_date > analysis_date:
                errors.append(f"{finding_id}: LAW_EFFECTIVE conflicts with effective date after analysis_date")
            if claim_type == "LAW_PROMULGATED_NOT_EFFECTIVE" and effective_date <= analysis_date:
                errors.append(f"{finding_id}: law is effective by analysis_date")

        for item in linked:
            checked_at = valid_date(item.get("status_checked_at") or item.get("retrieved_at"))
            if analysis_date and checked_at and (analysis_date - checked_at).days > 365 and claim_type in LEGAL_CLAIMS:
                errors.append(f"{finding_id}: regulatory status check is older than 365 days at analysis_date")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validate a K-DARI report JSON")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        report = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if not isinstance(report, dict):
        print("ERROR: report must be a JSON object", file=sys.stderr)
        return 2
    errors, warnings = validate_report(report, args.path.parent)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    evidence_count = len(report.get("evidence", []))
    if not evidence_count and report.get("evidence_file"):
        evidence_count = len(json.loads((args.path.parent / report["evidence_file"]).read_text(encoding="utf-8")))
    print(f"OK: report validated ({evidence_count} evidence, {len(report['findings'])} findings)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
