# Phase 9 — K-DARI Controlled Evaluation & Portfolio Validation

## 범위

Phase 9는 공개 명칭을 K-DARI로 정리하고 120개 통제 실험을 실행했다. 최종 저장소 정리에서 현재 설치 식별자는 `k-digital-asset-research-intelligence`로 변경했으며, 이 Phase의 이전 설치 슬러그와 경로는 재현성을 위해 그대로 보존한다. 외부 네이버 사례, 포트폴리오 문서, 자동 보조평가와 인간 검토를 서로 분리한다.

## 상태

| 구성요소 | 상태 |
|---|---|
| K-DARI 공개명·기존 슬러그 호환 | COMPLETE |
| 프로토콜·프롬프트·rubric·manifest 동결 | COMPLETE |
| GitHub 원격 fresh install | COMPLETE |
| 120개 생성 실행 | COMPLETE — Claude 코호트 120/120 |
| condition-blind 자동 근거 검증·평가 | COMPLETE — AI 보조 120/120, 인간 평가와 분리 |
| 결과 집계·통계 | PARTIAL — 자동점수 병합 완료, 인간 검토 후 조건별 최종분석 대기 |
| 네이버 외부 E군 공식 근거 대조 | PARTIAL |
| Corporate 포트폴리오 | DRAFT_COMPLETE — 최종 수치·전문가 검토 반영 대기 |
| 인간 검토 | HUMAN_REVIEW_PENDING |

120개 생성과 AI 보조평가는 완료됐지만 인간 비교 검증은 완료되지 않았다. 따라서 “인간 검증 완료” 또는 “최종 비교 검증 완료”라고 표현하지 않는다. Phase 10은 사용자 별도 승인 전 시작하지 않는다.

## 격리 문제와 조치

초기 파일럿에서 사용자 전역에 설치된 스킬이 대조군에 유입될 수 있음을 실제 로그로 발견했다. 해당 시도는 삭제하지 않고 `GLOBAL_SKILL_CONTAMINATION_OR_PRE_ISOLATION_PILOT`로 분석 제외했다. 이후 조건별 임시 `HOME`·`CODEX_HOME`과 작업 디렉터리를 분리하고, 대조군에 스킬 읽기가 관측되면 자동으로 `BLOCKED` 처리하도록 수정했다.


## Claude Code 이관 (2026-11-18)

개발 도구가 Codex에서 Claude Code로 바뀌었다(D-012). 저장소 확인 결과 Codex는 이미 manifest·프롬프트·루브릭·harness·Codex 코호트 실행 일부(완료 21 슬롯, 99 실패 시도, 모두 미커밋)를 만들었으므로 재작성하지 않고 보존 커밋한다. 신규 요구에 따라 동일 모델·환경의 **Claude 코호트**를 `evaluations/controlled-experiment-claude/`에 별도 구성했다(합산 금지).

| 구성요소 | 상태 |
|---|---|
| Claude 런타임 harness(`--runtime claude`, stream-json 파서, 사용량 중복 방지, AUTH/한도 BLOCKED·재개) | COMPLETE (단위 테스트) |
| Claude Code 원격 npx 설치(`--agent claude-code`) | COMPLETE (SHA 일치) |
| 자동 활성화(implicit) 관측 | COMPLETE — C/D 60/60에서 Skill 도구 호출 관측, A/B 오염 0건 |
| Claude 120회 실행 | COMPLETE — 120/120 슬롯 정상 완료(모델 claude-sonnet-5-5, 재시도 없음 제외 초기 AUTH 차단 2건 보존) |
| Codex 코호트 | PARTIAL — 21/120 완료(사용량 제한), 별도 보존 |
| 근거검증·평가·통계·E군·포트폴리오 | AI 보조평가 완료, E군·인간검토·최종통계 일부 대기 |
| 인간 검토 | HUMAN_REVIEW_PENDING |

재개: `evaluations/controlled-experiment-claude/reproduce.md`. Phase 10은 시작하지 않았다.

원시 사용량 요약: 평균 output 토큰 A 1148 / B 6941 / C 2159 / D 7687, 평균 소요 A 13s / B 83s / C 25s / D 93s. 블라인드 사본 120개와 AI 보조평가는 완료됐다. AI 점수만으로 조건 우열이나 최종 합격을 확정하지 않으며, 인간 검토 완료 뒤에만 blind mapping을 적용한다.
