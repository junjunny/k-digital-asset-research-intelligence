# Decisions

## D-001 Skill-first

웹사이트나 별도 백엔드를 필수로 만들지 않는다. 핵심 산출물은 설치 가능한 폴더형 Agent Skill이다.

## D-002 Progressive disclosure

`SKILL.md`에는 라우팅과 규제 정확성 규칙만 두고, 상세 방법론·관할권·용어는 references로 분리한다.

## D-003 Dependency-light validation

기본 검증기는 Python 표준 라이브러리만 사용한다. JSON Schema는 상호운용을 위해 제공하되 실행에 `jsonschema`를 강제하지 않는다.

## D-004 Legal status as data

법률/정책의 차이를 서술 규칙에만 맡기지 않고 `legal_status` 필드와 시간 검증으로 표현한다.

## D-005 First case

공식 발행인 자료가 있고 한국 정책의 초기 사모사채 범위와 비교하기 좋은 EIB sterling digital bond를 선택했다. EU DLT Pilot 적용 사례라고 오인하지 않도록 발행일과 적용일을 분리했다.

## D-006 MIT

재사용과 공개 배포 목적에 맞춰 MIT License를 채택했다. 보고서의 제3자 원문은 복제하지 않고 짧은 발췌와 링크만 저장한다.

## D-007 Evidence v2

URL 접근과 내용 검증을 분리한다. 원문 추출과 발췌문 일치가 확인된 경우에만 `CONTENT_VERIFIED`를 부여하고, 문서와 추출문 해시를 기록한다. 동적 웹페이지는 문서 전체 해시가 바뀔 수 있으므로 해시만으로 의미 동일성을 단정하지 않는다.

## D-008 Normalized claims

한국어 키워드 대신 `claim_type`과 `legal_status` 호환성, `analysis_date`, 관할권, 공식 출처 유형을 검증한다. 의미적·법률적 정당성 전체를 자동화했다고 주장하지 않는다.

## D-009 Untrusted sources

다운로드한 HTML·PDF·텍스트는 신뢰하지 않는 데이터다. 스크립트·매크로·문서 속 명령을 실행하지 않고, 지시문 패턴은 경고만 기록한다. 접근 제한을 우회하지 않는다.

## D-010 Independent case

EIB와 다른 홍콩 정부 다중통화 디지털 녹색채권을 신규 연구질문으로 선택했다. 한국 공식 자료는 비교 기준으로 재사용하되 해외 사례·규제·분석은 새로 조사했다.

## D-011 Deterministic question routing

일반 사용자 질문은 표준 라이브러리 기반 규칙으로 12개 유형과 3개 응답 깊이 중 하나를 선택한다. 라우터는 사실을 생성하거나 모호한 대상을 추정하지 않는다. 새 용어·복합 문맥은 에이전트가 검토하고, 한국 맥락은 명시적 관련성 또는 근거가 있을 때만 추가한다.


## D-012 Phase 9 개발 도구 전환: Codex → Claude Code (2026-11-18)

Codex 사용량 제한으로 Phase 9 후속 작업을 Claude Code가 이어받는다. 변경 범위는 (1) `scripts/controlled_experiment.py`의 `--runtime claude` 실행기, `setup-claude`, `K_DARI_EXP_DIR` 코호트 분리, (2) 동일 모델·환경 Claude 코호트 `evaluations/controlled-experiment-claude/`, (3) `CLAUDE.md`(AGENTS.md를 가리키는 얇은 포인터)와 문서 갱신이다. 기존 Codex 코호트(`evaluations/controlled-experiment/`, 완료 21 슬롯·실패 99 시도)는 수정·삭제·합산하지 않고 보존한다. 분석 엔진, 라우터, 스키마, 동결 프롬프트·루브릭은 변경하지 않았다. Codex와 Claude 결과는 모델·도구·검색이 달라 서로 합산하거나 인과 비교하지 않는다.

## D-013 현재 식별자를 K-DARI로 통일 (2026-11-21)

현재 공개 저장소와 스킬 식별자를 `junjunny/k-digital-asset-research-intelligence`, `k-digital-asset-research-intelligence`로 통일한다. 별도 legacy alias skill은 만들지 않는다. 두 식별자를 함께 배포하면 자동 발견 후보가 중복되고 실험 격리가 약해질 수 있기 때문이다. 이전 K-DAPI 명칭·저장소·설치 경로는 당시 실행을 재현하는 실험 코드와 기록에서만 보존하며, 현재 사용자 안내에는 마이그레이션 경계를 명시한다.
