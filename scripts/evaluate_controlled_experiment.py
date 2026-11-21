#!/usr/bin/env python3
"""Prepare and run condition-blind, evidence-focused Phase 9 evaluations."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_EXP = ROOT / "evaluations" / "controlled-experiment"
COHORTS = {
    "codex": BASE_EXP,
    "claude": ROOT / "evaluations" / "controlled-experiment-claude",
}
TOPICS = ("clarity_act", "ethereum", "usdc", "chainlink", "upbit", "token_securities")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prepare(exp: Path) -> None:
    manifest = read_json(exp / "manifest.json")
    mapping = read_json(exp / "scores" / "blind-mapping.json")["mapping"]
    by_run = {item["run_id"]: item["blind_id"] for item in mapping}
    prompts = {kind: read_json(BASE_EXP / "prompts" / f"{kind}.json") for kind in ("general", "detailed")}
    slots = {slot["run_id"]: slot for slot in manifest["slots"]}
    out = exp / "scores" / "evaluator-inputs"
    out.mkdir(parents=True, exist_ok=True)
    for topic in TOPICS:
        items = []
        for run_id, blind_id in sorted(by_run.items(), key=lambda pair: pair[1]):
            slot = slots[run_id]
            if slot["topic"] != topic:
                continue
            answer = (exp / "scores" / "blind-inputs" / f"{blind_id}.md").read_text(encoding="utf-8")
            items.append({"blind_id": blind_id, "question": prompts[slot["prompt_kind"]][topic], "answer": answer})
        write_json(out / f"{topic}.json", {"topic": topic, "items": items})
    print("prepared condition-blind evaluator inputs")


def evaluator_prompt(topic: str) -> str:
    return f"""당신은 생성 에이전트와 분리된 증거 검증 평가자다. 현재 기준일은 2026-11-18이다.
현재 디렉터리의 {topic}.json에 있는 모든 답변을 조건을 추측하지 말고 평가하라.
평가 기준은 사실 정확성·최신성 25점, 출처 신뢰도·주장 적합성 20점, 깊이·완전성 15점,
한국 관련성 또는 적절한 생략 15점, 위험·불확실성 10점, 사용자 의도 충족 10점,
실용성·가독성 5점으로 총 100점이다. 각 답변의 중요한 사실을 웹에서 공식 1차 자료로 직접 대조하라.
법률안/현행법, 계획/실제 구현, 파일럿/상용화를 구분한다. 출처가 없거나 접근할 수 없으면 추측하지 않는다.
core claim 수와 VERIFIED/CONTRADICTED/INSUFFICIENT를 세고, 필수 항목 완성도와 표시 URL의 주장 적합성·1차 출처 비율을 기록하라.
비율 분모가 0이면 null을 사용한다. total_score는 7개 항목 합계와 정확히 같아야 한다.
각 답변에 사용한 핵심 공식 URL을 evidence_urls에 기록한다. 인간 승인이나 법률·투자 결론을 내리지 않는다.
출력은 지정된 JSON schema만 따른다."""


def run(topic: str, exp: Path, home: Path | None, model: str | None, reasoning_effort: str, timeout: int) -> None:
    input_dir = exp / "scores" / "evaluator-inputs"
    output = exp / "scores" / "evaluator-outputs" / f"{topic}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "codex", "--search", "exec", "--ephemeral", "--ignore-user-config", "--json",
        "-c", f'model_reasoning_effort="{reasoning_effort}"',
        "--sandbox", "read-only", "--skip-git-repo-check", "-C", str(input_dir),
        "--output-schema", str(BASE_EXP / "scores" / "evaluator-schema.json"),
        "--output-last-message", str(output), evaluator_prompt(topic),
    ]
    if model:
        command[4:4] = ["--model", model]
    environment = os.environ.copy()
    if home is not None:
        environment["HOME"] = str(home)
        environment["CODEX_HOME"] = str(home / ".codex")
    raw = exp / "scores" / "evaluator-outputs" / f"{topic}.jsonl"
    result = subprocess.run(command, text=True, capture_output=True, check=False, timeout=timeout, env=environment)
    raw.write_text(result.stdout, encoding="utf-8")
    (raw.with_suffix(".stderr.txt")).write_text(result.stderr, encoding="utf-8")
    if result.returncode != 0 or not output.exists():
        raise SystemExit(f"evaluator failed for {topic}: exit {result.returncode}")
    print(f"evaluated {topic}", flush=True)


def merge(exp: Path) -> None:
    mapping = read_json(exp / "scores" / "blind-mapping.json")["mapping"]
    by_blind = {item["blind_id"]: item["run_id"] for item in mapping}
    merged = []
    for topic in TOPICS:
        path = exp / "scores" / "evaluator-outputs" / f"{topic}.json"
        data = read_json(path)
        for score in data["scores"]:
            score["run_id"] = by_blind[score["blind_id"]]
            score["topic"] = topic
            score["human_review_status"] = "HUMAN_REVIEW_PENDING"
            merged.append(score)
    write_json(exp / "scores" / "automatic-scores.json", {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "human_review_status": "HUMAN_REVIEW_PENDING",
        "scores": merged,
    })
    print(f"merged {len(merged)} scores")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    prepare_cmd = sub.add_parser("prepare")
    prepare_cmd.add_argument("--cohort", choices=COHORTS, default="codex")
    run_cmd = sub.add_parser("run")
    run_cmd.add_argument("--cohort", choices=COHORTS, default="codex")
    run_cmd.add_argument("--topic", choices=TOPICS)
    run_cmd.add_argument("--all", action="store_true")
    run_cmd.add_argument("--home", type=Path, help="optional isolated HOME/CODEX_HOME; omit to use the current authenticated session")
    run_cmd.add_argument("--model", help="optional model override; omit to use the configured default")
    run_cmd.add_argument("--reasoning-effort", default="medium")
    run_cmd.add_argument("--timeout", type=int, default=1800)
    merge_cmd = sub.add_parser("merge")
    merge_cmd.add_argument("--cohort", choices=COHORTS, default="codex")
    args = parser.parse_args()
    exp = COHORTS[args.cohort]
    if args.command == "prepare":
        prepare(exp)
    elif args.command == "run":
        topics = TOPICS if args.all else (args.topic,)
        if topics == (None,):
            raise SystemExit("choose --all or --topic")
        for topic in topics:
            run(topic, exp, args.home.resolve() if args.home else None, args.model, args.reasoning_effort, args.timeout)
    else:
        merge(exp)


if __name__ == "__main__":
    main()
