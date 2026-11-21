# Handoff

## 다음 시작점

1. `git status`, `docs/AI_ASSISTED_REVIEW_REPORT.md`, `docs/TEST_REPORT.md`를 확인한다.
2. `evaluations/controlled-experiment-claude/ai-assisted-review/reviews.json`의 저점·반박·근거 부족 항목부터 사람이 검토한다.
3. 로컬 검토 화면에서 R001~R120을 직접 확인하고 인간 의견만 `human-review/reviews.json`에 저장한다.
4. Phase 8은 `docs/PHASE_8_HUMAN_REVIEW.md`, EIB·홍콩은 `HUMAN_REVIEW_GUIDE.md`와 `ANALYST_REVIEW.md`를 계속 사용한다.
5. 120개 인간 검토 완료 전에는 blind mapping 적용과 조건별 최종 분석을 실행하지 않는다.

## 사용자 작업

- MIT License의 저작권자 표기 확인
- 실제 포트폴리오 제출 전 사례의 전문가 검토
- 최종 하위법규 공포 후 규제 상태·수치 재검증
- `OPEN_QUESTIONS.md`의 평가 관련 항목 결정
- Phase 8 인간 채점표 작성 및 승인 여부 결정
- Phase 9 블라인드 답변 120건의 인간 채점·승인

## 주의

2026-10-01 금융위원회 자료는 입법예고다. 예고 내용의 숫자와 요건을 확정 규정으로 바꾸지 않는다. EIB sterling bond는 EU DLT Pilot 적용 전 발행이다.

`CONTENT_VERIFIED`는 원격 원문 접근과 발췌문 일치를 뜻하며 출처의 실질적 진위, 법률 해석, 주장의 의미상 충분성, 사업 적법성을 검증했다는 의미가 아니다. 수동 첨부는 발췌가 일치해도 공식 출처 확인 완료로 처리하지 않는다. validator의 claim/Evidence 호환성도 구조 검사일 뿐 의미 증명이 아니다.

Phase 8에서 자연어 입력부터 최신 공식자료 탐색과 답변 생성까지 네 사례를 독립 실행했다. Phase 9 Claude 코호트는 120/120 생성과 AI 보조평가가 끝났지만, 자동 점수는 인간 승인이나 전문가 법률·회계·기술 검토가 아니다. 라우터 통과, 설치 성공, Evidence 발췌 일치도 실제 리서치 정확성과 각각 구분한다. skills.sh 등록·릴리스·홍보는 계속 제외한다.

프로젝트는 Phase 10에서 신규 기능 개발을 종료한다. Phase 9는 자동으로 시작하지 않는다.



## Phase 9 인간 검토 재개

1. `python3 scripts/human_review_server.py`를 실행하고 `http://127.0.0.1:8765`에서 blind ID만 보고 평가한다.
2. AI 보조 사전검토는 확인 경로로만 사용하고, 사람이 실제로 확인한 주장·의견·날짜만 인간 검토 파일에 입력한다.
3. 120개 완료 뒤 사용자가 명시적으로 승인한 경우에만 `python3 scripts/finalize_human_review.py --confirm APPLY_BLIND_MAPPING`을 실행한다.
