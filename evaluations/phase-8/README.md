# Phase 8 Evaluation

Phase 7 기준선을 fresh clone·격리 설치한 뒤 일반 에이전트와 K-DAPI 사용 에이전트의 실제 답변을 비교한다. 평가 자료는 수행 사실을 보존하며, 인간 승인과 모델 보조 평가는 구분한다.

- 기준선: `ba7734ed6e6b3b0483313d0564b12374b1d273f4`
- 평가일: 2026-11-17 (Asia/Seoul)
- 필수 사례: CLARITY Act, Chainlink, Ethereum, USDC
- 사용자 평가: `../../docs/archive/PHASE_8_HUMAN_REVIEW.md`

민감한 세션 정보, 인증정보와 절대 로컬 경로는 저장하지 않는다.

## 구성

- `evaluation-plan.md`: 고정 기준선·환경·질문·변경 통제
- `rubric.md`: 100점 기준과 치명적 오류
- `cases/`: 네 질문의 대조군·K-DAPI 답변, 핵심 Evidence v2, 검증·평가
- `usability/`: 수정 전 독립 평가와 수정 후 열 문항·holdout 결과
- `multi-turn/`: 세 대화 흐름의 문맥 유지 결과
- `offline/`: 웹 미사용 최신 법안 질문
- `comparison/`: 모델 보조 A/B 평가 원문
- `results.json`: 모델 보조 점수. 인간 평가가 아님
- `failure-log.md`: 실패를 삭제하지 않은 수정 전후 기록

모든 정책·준비금·네트워크 지표는 평가일의 스냅샷이다. 일반 사용 시 질문 시점의 공식 원문을 다시 확인한다.

