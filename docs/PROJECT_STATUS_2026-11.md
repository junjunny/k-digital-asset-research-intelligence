# K-DARI 프로젝트 상태 — 2026-11

기준일: 2026-11-23 (Asia/Seoul)

이 문서는 개발, 설치, 평가, 검토와 공개 상태를 서로 섞지 않기 위한 현재 상태표다.

| 상태 | 판정 | 근거와 한계 |
|---|---|---|
| `DEVELOPMENT_COMPLETE` | 완료 | 12개 질문 유형, 3개 응답 깊이, 근거·보고서 검증기와 회귀 테스트 구현 |
| `INSTALL_VERIFIED` | 완료 | 원격 `9e5b1a7`에서 `@k-dari` 격리 copy 설치, 25파일·152KB 패키지와 `SKILL.md` 설명 확인 |
| `SKILL_DISCOVERY_VERIFIED` | 완료 | `skills/k-dari/`에서 `k-dari` 1개만 탐지; 저장소 루트 중복 스킬 없음 |
| `EXPLICIT_ACTIVATION_VERIFIED` | 부분 완료 | Codex 0.169.0에서 현재 식별자 명시 호출 확인; Claude Code 2.1.327은 스킬 발견 후 OAuth 만료로 모델 요청 전 차단 |
| `AUTO_ACTIVATION_VERIFIED` | 미검증 | 에이전트별 자동 선택을 일반화할 독립 관측이 없음 |
| `AI_EVALUATION_COMPLETE` | 완료 | Claude 코호트 120/120 생성과 AI 보조 사전검토 완료 |
| `HUMAN_REVIEW_PENDING` | 대기 | 120건 인간 블라인드 검토 미실시; 매핑 적용·최종 조건별 분석 금지 |
| `EXPERT_REVIEW_PENDING` | 대기 | 사례의 법률·회계·세무·기술 핵심 판단 최종 검토 미실시 |
| `RELEASE_PREPARATION_COMPLETE` | 완료 | 명칭·README·마이그레이션·보안·원격 설치·Actions CI 점검 완료 |
| `SKILLS_SH_INDEXING` | 완료 | 상세 페이지가 `SKILL.md` 설명·본문·설치 명령을 표시하고 대소문자 CLI 검색에서 새 항목이 첫 번째로 노출됨 |
| `SECURITY_HARDENING` | 완료(잔여 위험 있음) | W011·W012 분석, 인젝션 신뢰 경계·URL 차단·해시 의존성·v1.0.0/전체 SHA 설치 검증; Snyk PASS 미주장 |

## 이번 정리의 경계

- 현재 공개명: K-DARI
- 현재 정식명: Korean Digital Asset Research Intelligence
- 현재 저장소: `junjunny/k-digital-asset-research-intelligence`
- 현재 스킬 식별자: `k-dari`
- 이전 K-DAPI 명칭과 식별자는 과거 실험 재현 기록에서만 유지

이번 정리는 새 연구 기능, 재실험 또는 인간 평가가 아니다. 기존 결과·원문·점수·블라인드 상태를 변경하지 않는다.

## 공개 전 남은 게이트

1. 인간 검토자가 블라인드 상태에서 Phase 9의 120건을 직접 평가한다.
2. 별도 승인 후에만 매핑 적용과 조건별 최종 분석을 수행한다.
3. 법률·회계·세무·기술 전문가가 사례의 핵심 판단을 검토한다.
4. 동적 법령·정책·프로젝트 지표를 제출 또는 배포 시점에 다시 확인한다.
5. skills.sh 인덱스는 외부 서비스이므로 향후 구조·표시 변경 시 설치 가능 여부와 별도로 재확인한다.
6. 외부 콘텐츠와 최신 브랜치 설치의 구조적 위험은 제거 완료로 보지 않고 [보안 감사](SECURITY_AUDIT.md)에 따라 관리한다.

## 블라인드·공개 저장소 위험

블라인드 매핑 원본은 이미 Git 이력에 추적되어 있어 공개 저장소 접근 권한이 있는 평가자가 의도치 않게 조건을 확인할 수 있다. 연구 원본과 재현성을 보존하기 위해 이번 정리에서 삭제하거나 다시 쓰지 않았다. 인간 검토자는 평가 완료 전 공개 저장소·커밋 이력·매핑 파일에 접근하지 않고, 조건 메타데이터가 없는 로컬 검토 화면이나 별도 블라인드 내보내기만 사용해야 한다. 최종 매핑 적용은 인간 검토 완료와 사용자의 별도 승인 후에만 실행한다.

## GitHub 메타데이터 점검

- 공개 저장소, 기본 브랜치 `main`, MIT License, Actions CI를 확인했다.
- 2026-11-23 저장소 description, skills.sh homepage와 `k-dari`, `agent-skills`, `digital-assets`, `cryptocurrency`, `blockchain`, `research`, `korea` topics를 반영했다.
- skills.sh의 `k-dari` 상세 페이지는 HTTP 200이며 `SKILL.md`의 K-DARI 설명·본문과 설치 명령을 표시한다.
- `npx skills find k-dari`와 대문자 `K-DARI` 모두 `junjunny/k-digital-asset-research-intelligence@k-dari`를 첫 번째로 반환한다. 과거 식별자는 역사적 설치 수 때문에 하위 결과에 남아 있다.
- 권장 description: `Evidence-led digital asset research Agent Skill with Korean regulatory context`
- 권장 topics: `agent-skills`, `digital-assets`, `cryptocurrency`, `blockchain`, `research`, `korea`

