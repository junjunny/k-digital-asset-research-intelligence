# Handoff

## 다음 시작점

1. `git status`와 [테스트 보고서](TEST_REPORT.md)를 확인한다.
2. 인간평가 서버를 실행하고 `R001`부터 블라인드 검토를 재개한다.
3. 평가가 120/120 완료된 뒤 사용자가 명시적으로 확정할 때만 blind mapping을 적용한다.
4. 인간평가 완료와 연구 결과 승인은 별도 결정으로 기록한다.

## 인간평가 실행

```bash
python3 scripts/human_review_server.py
```

- 접속: `http://127.0.0.1:8765`
- 저장: `evaluations/controlled-experiment-claude/human-review/reviews.json`
- 절차: [Phase 9 Human Review](PHASE_9_HUMAN_REVIEW.md)

진행 중 평가 데이터는 로컬 파일에 저장되지만 자동 commit·push하지 않는다. 테스트용 가상 평가는 실제 평가 파일과 분리한다.

AI 보조 사전검토는 [별도 보고서](AI_ASSISTED_REVIEW_REPORT.md)와 `evaluations/controlled-experiment-claude/ai-assisted-review/`에 보존되어 있다. 이를 인간 점수나 승인으로 복사하지 않는다.

## 남은 검토

- CLARITY Act 공식 입법기록과 법안 상태
- Chainlink 동적 공급·Reserve·사용 지표
- Ethereum 대시보드 방법론과 운영자 귀속
- USDC 주간 준비자산·상환 수치
- EIB·홍콩 사례의 법률·회계·사업성 전문가 검토

## 불변 주의사항

- 정책 발표·입법예고·법률안·공포·시행을 구분한다.
- `CONTENT_VERIFIED`는 출처 진위나 법률 해석까지 승인했다는 뜻이 아니다.
- 수동 첨부의 발췌가 일치해도 공식 출처 확인 완료로 처리하지 않는다.
- claim/Evidence 구조 호환성은 주장 의미의 증명이 아니다.
- 자동 평가 점수는 인간 승인으로 표현하지 않는다.

Phase 0~8의 당시 판단과 설치 기록은 [`archive/`](archive/)에서 확인한다.
