# K-DARI — Korean Digital Asset Research Intelligence

K-DARI는 디지털자산 질문을 유형별 연구 절차로 연결하고, 공식 원문을 우선해 사실·추론·미확인 사항을 구분하는 Agent Skill입니다. 법률·정책, 코인·프로젝트, 네트워크, 백서, 스테이블코인, 토큰증권·RWA, 거래소 정책과 사업모델을 다루며 한국 맥락은 실질적으로 관련될 때만 연결합니다.

> 자연어 질문 → 질문 유형·깊이 선택 → 공식 자료 확인 → 사실·추론·미확인 구분 → 필요한 경우 한국 맥락

법률자문, 세무·회계 자문, 투자 권유 또는 가격 예측 도구가 아닙니다.

## 빠른 시작

Node.js가 설치된 터미널에서 다음 명령을 실행합니다.

```bash
npx skills add junjunny/k-digital-asset-research-intelligence@k-digital-asset-research-intelligence
```

설치 후 지원 에이전트에 자연어로 질문합니다. 스킬을 자동으로 고르지 않으면 현재 식별자를 명시합니다.

```text
Use $k-digital-asset-research-intelligence to explain the current status of the CLARITY Act using official sources.
```

2026-11-21 기준 Skills CLI 1.9.0에서 저장소 탐지와 Codex·Claude Code 대상 격리 설치를 확인했습니다. 설치 성공은 실제 답변에서의 자동 활성화를 보장하지 않습니다. 명시적 호출과 자동 활성화 검증 상태는 [프로젝트 상태](docs/PROJECT_STATUS_2026-11.md)에 따로 기록합니다.

이전 `k-digital-asset-policy-intelligence` 설치본을 사용 중이면 [K-DAPI → K-DARI 마이그레이션](docs/MIGRATION_KDAPI_TO_KDARI.md)을 먼저 읽어 중복 설치를 피하세요.

## 질문 예시

```text
토큰증권이 무엇인지 일반 대학생도 이해할 수 있게 설명해 줘.
```

```text
이더리움 네트워크를 합의 방식, 탈중앙화, 실제 사용과 주요 위험 관점에서 평가해 줘.
```

```text
USDC가 가격을 유지하는 방식과 준비자산·상환·디페깅 위험을 공식 자료로 확인해 줘.
```

```text
이 코인 어떤 거야?
```

마지막 질문처럼 대상이 불명확하면 이름·티커·네트워크를 먼저 확인하며 임의의 프로젝트를 선택하지 않습니다. 매수·매도 요청에는 결론 대신 구조·공급·기술·운영·규제 위험과 확인 체크리스트를 제공합니다.

## 분석 범위

- 12개 질문 유형: 개념, 법률·규제, 규제 비교, 코인·프로젝트, 네트워크·프로토콜, 백서, 스테이블코인, 토큰화 자산·RWA, 거래소 정책, 사업모델, 투자·가격 요청, 모호한 요청
- 3개 답변 깊이: `QUICK`, `STANDARD`, `DEEP_RESEARCH`
- 법률안·공포·시행·입법예고·정책 발표를 구분
- 주요 주장에 Evidence ID와 검증 상태 연결
- HTML·텍스트·PDF 원문과 발췌문 대조 및 해시 기록
- 한국·해외 제도의 비교 가능 항목만 선별

상세 사용법은 [일반 사용자 안내](docs/GENERAL_USER_GUIDE.md), 라우팅 기준은 [질문 라우팅](docs/QUESTION_ROUTING.md), 근거 등급은 [근거 정책](references/evidence-policy.md)을 참고하세요.

## 검증 범위와 한계

`CONTENT_VERIFIED`는 원문 접근과 발췌 일치라는 기술 상태입니다. 법률 해석의 타당성, 출처의 모든 주장, 사업 적법성 또는 투자 안전성을 자동 보증하지 않습니다. 스캔 PDF OCR, 복잡한 표·각주, 비공개 계약과 개별 세무·회계 판단은 전문가 검토가 필요합니다.

EIB와 홍콩 디지털채권 사례는 공식자료 기반 연구 예시이지만 법률·회계·세무 전문가의 최종 검토 전에는 검토용 초안입니다. 시점에 따라 바뀌는 법령·시장·프로젝트 정보는 답변 시점에 공식 원문을 다시 확인해야 합니다.

회사 기밀, 개인정보, 비공개 계약서, API 키를 외부 AI 서비스나 이 저장소의 이슈에 업로드하지 마세요. 허가된 환경과 조직의 데이터 정책을 따르세요.

## 연구·평가 상태

- Phase 8의 독립 설치·질문 실행 자료와 한계는 [평가 패키지](evaluations/phase-8/README.md)에 보존되어 있습니다.
- Phase 9 Claude 코호트는 120/120 답변 생성과 AI 보조 사전검토가 완료됐습니다.
- 120건의 인간 블라인드 검토와 전문가 검토는 아직 완료되지 않았습니다.
- AI 보조점수는 인간 승인이나 조건별 우열의 결론이 아닙니다.
- 블라인드 매핑 적용과 최종 조건별 분석은 인간 검토 후 별도 승인 전까지 수행하지 않습니다.

외부 서비스와의 비교는 공개자료로 확인 가능한 범위만 다루며 내부 구현 부재나 K-DARI의 우월성을 주장하지 않습니다.

## 로컬 검증

Python 3.9 이상이 필요합니다. PDF 추출 기능은 `pypdf`를 사용합니다.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/route_question.py "토큰증권이 뭐야?"
python3 scripts/validate_sources.py examples/tokenization-case-study/evidence.json
python3 scripts/validate_report.py examples/tokenization-case-study/report.json
python3 -m unittest discover -s tests -v
npx skills add . --list
```

실시간 원문 접근은 공식 사이트의 자동 접근 제한에 따라 `ACCESS_RESTRICTED` 또는 `MANUAL_REVIEW_REQUIRED`가 될 수 있습니다.

## 저장소 구조

- `SKILL.md`: 에이전트 실행 진입점
- `references/`: 연구 방법론·근거 정책·규제 프레임워크
- `docs/`: 사용자 안내, 설계 결정, 검증·이관 기록
- `templates/`, `schemas/`: 보고서와 구조화 데이터 형식
- `scripts/`: 라우터·원문·보고서 검증 도구
- `examples/`: 공식자료 기반 연구 예시
- `evaluations/`: 원본 실험·평가 기록
- `tests/`, `.github/workflows/ci.yml`: 회귀 테스트와 CI

## 기여와 라이선스

변경 제안은 분석 기준일, 공식 URL, 법적 상태와 Evidence ID를 보존해야 합니다. 별도 `CONTRIBUTING.md`는 아직 없으므로 이슈나 pull request에 변경 목적과 실행한 테스트를 적어 주세요.

MIT License입니다. 기존 실험 산출물의 K-DAPI 명칭과 이전 식별자는 재현성을 위해 수정하지 않습니다.
