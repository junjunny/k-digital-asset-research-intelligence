#!/usr/bin/env python3
"""Build a condition-blind AI-assisted pre-review package without altering human review data."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "evaluations" / "controlled-experiment-claude" / "scores" / "automatic-scores.json"
DEFAULT_OUTPUT = ROOT / "evaluations" / "controlled-experiment-claude" / "ai-assisted-review" / "reviews.json"
HUMAN_REVIEWS = ROOT / "evaluations" / "controlled-experiment-claude" / "human-review" / "reviews.json"
SCORE_FIELDS = (
    "factual_currentness",
    "source_claim_fit",
    "depth_completeness",
    "korean_relevance",
    "risk_uncertainty",
    "intent",
    "usability",
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    source = read_json(args.input)
    human_before = HUMAN_REVIEWS.read_bytes()
    reviews = {}
    for score in sorted(source["scores"], key=lambda item: item["blind_id"]):
        reviews[score["blind_id"]] = {
            "blind_id": score["blind_id"],
            "review_type": "AI_ASSISTED_PRE_REVIEW",
            "status": "NEEDS_HUMAN_VERIFICATION",
            "scores": {field: score[field] for field in SCORE_FIELDS},
            "total_score": score["total_score"],
            "status_classification": score["status_classification"],
            "claim_counts": {
                "core": score["core_claims_total"],
                "verified": score["verified_core_claims"],
                "contradicted": score["contradicted_core_claims"],
                "insufficient": score["insufficient_core_claims"],
            },
            "required_items": {
                "total": score["required_items_total"],
                "completed": score["required_items_completed"],
            },
            "citation_claim_fit": score["citation_claim_fit"],
            "first_party_url_ratio": score["first_party_url_ratio"],
            "evidence_urls": score["evidence_urls"],
            "notes": score["notes"],
        }

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    output = {
        "schema_version": 1,
        "review_type": "AI_ASSISTED_PRE_REVIEW",
        "generated_at": now,
        "source_generated_at": source["generated_at"],
        "human_review_status": "HUMAN_REVIEW_PENDING",
        "disclosure": "AI가 공식 원문 검색과 블라인드 루브릭으로 생성한 사전검토이며 인간 평가·승인·서명이 아니다.",
        "reviews": reviews,
    }
    if len(reviews) != 120:
        raise SystemExit(f"refusing incomplete AI-assisted review: {len(reviews)}/120")
    write_json(args.output, output)
    if HUMAN_REVIEWS.read_bytes() != human_before:
        raise SystemExit("human review data changed unexpectedly")
    print(args.output)


if __name__ == "__main__":
    main()
