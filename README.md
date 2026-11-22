# K-DARI — Korean Digital Asset Research Intelligence

[English](README.en.md) · [사용 가이드](docs/GENERAL_USER_GUIDE.md) · [연구 방법론](references/research-methodology.md) · [검증 결과](docs/TEST_REPORT.md) · [프로젝트 상태](docs/PROJECT_STATUS_2026-11.md)

K-DARI(`k-dari`)는 일반 사용자의 자연어 질문을 공식 자료에 근거해 조사하는 오픈소스 디지털자산 Agent Skill입니다. 법률·정책, 코인·프로젝트, 블록체인 네트워크, 백서, 스테이블코인, RWA·토큰증권, 거래소 정책과 사업모델을 질문별 방법론으로 분석합니다. 한국 규제·정책·시장 맥락은 실제 관련성이 있을 때만 연결합니다.

> 자연어 질문 → 질문 유형과 깊이 선택 → 공식 자료 확인 → 사실·추론·미확인 구분 → 필요한 경우 한국 맥락

이 스킬은 법률자문, 투자 권유, 가격 예측을 제공하지 않습니다.

## 설치

```bash
npx skills add junjunny/k-digital-asset-research-intelligence --skill k-dari
```

설치 가능한 스킬을 먼저 확인하려면 다음 명령을 사용합니다.

```bash
npx skills add junjunny/k-digital-asset-research-intelligence --list
```

## 질문 예시

```text
미국 CLARITY Act가 무엇인지 현재 법안 상태와 함께 간단히 알려줘.
```

```text
이더리움 네트워크를 합의 방식, 탈중앙화, 실제 사용과 주요 위험 관점에서 평가해 줘.
```

```text
USDC가 가격을 유지하는 방식과 준비자산·상환·디페깅 위험을 알려줘.
```

```text
이 코인 어떤 거야?
```

마지막 질문처럼 대상이 불명확하면 이름·티커·네트워크를 먼저 확인하며 임의로 프로젝트를 선택하지 않습니다.

## 무엇이 다른가

- 12개 질문 유형과 `QUICK`·`STANDARD`·`DEEP_RESEARCH` 응답 깊이
- 법률안·공포·시행 예정·현행법·정책 발표·입법예고의 상태 구분
- 프로젝트 주장, 독립 검증 사실, 분석자의 추론과 미확인 사항 분리
- 핵심 주장별 Evidence ID, 원문 위치, 분석 기준일 기록
- 질문과 무관한 한국 규제 또는 토큰증권 분석을 억지로 추가하지 않음
- PDF 업로드나 외부 API 키 없이 시작 가능

웹 검색이 불가능하거나 공식 사이트가 자동 접근을 제한하면 최신 검증 불가 또는 수동 확인 필요 상태를 명시합니다.

## 구성

| 경로 | 역할 |
|---|---|
| `SKILL.md` | 에이전트가 읽는 실행 진입점 |
| `references/` | 연구 방법론, 근거 정책, 국내외 규제 프레임워크 |
| `templates/` | 브리프·비교·보고서 템플릿 |
| `schemas/` | Evidence·Finding·Report JSON Schema |
| `scripts/` | 질문 라우터와 출처·보고서 검증 도구 |
| `examples/` | EIB·홍콩 디지털채권 재현 사례 |
| `evaluations/` | 독립 평가와 통제 실험의 감사 자료 |
| `docs/` | 설계·품질 기준·진행 기록 |

`evaluations/`의 원본 실행 기록은 용량이 크지만 통제 실험의 재현성과 불리한 결과까지 보존하기 위한 연구 자료입니다.

## 검증

Python 3.9 이상이 필요합니다. PDF 추출 기능은 `requirements.txt`의 선택 의존성을 사용합니다.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/route_question.py "토큰증권이 뭐야?"
python3 scripts/validate_sources.py examples/tokenization-case-study/evidence.json
python3 scripts/validate_report.py examples/tokenization-case-study/report.json
python3 -m unittest discover -s tests -v
```

실시간 URL 접근까지 확인하려면 `validate_sources.py`에 `--check-urls`를 추가합니다. 자동 접근 제한은 검증 성공으로 간주하지 않습니다.

## 사례와 평가

- [EIB 디지털 채권과 한국 적용 조건](examples/tokenization-case-study/report-ko.md)
- [홍콩 다중통화 디지털 녹색채권](examples/hong-kong-digital-green-bond/report-ko.md)
- [Phase 8 독립 평가](evaluations/phase-8/README.md)
- [Phase 9 인간 검토 절차](docs/PHASE_9_HUMAN_REVIEW.md)
- [AI 보조 사전검토 보고서](docs/AI_ASSISTED_REVIEW_REPORT.md)

자동 평가 점수는 인간 승인이나 법률·회계·기술 전문가 검토를 대신하지 않습니다. 인간 평가 입력은 로컬에 저장되며 사용자의 검토 없이 공개 저장소로 자동 전송되지 않습니다.

## 명칭과 라이선스

K-DARI는 **Korean Digital Asset Research Intelligence**의 약칭입니다. 검색과 설치 식별자는 소문자 `k-dari`이며, 문서의 이전 개발명 `K-DAPI`는 과거 실험 기록을 정확히 보존하기 위해 일부 남아 있습니다. 기존 설치본은 [마이그레이션 안내](docs/MIGRATION_KDAPI_TO_KDARI.md)에 따라 중복을 정리할 수 있습니다.

MIT License. 규제 정보는 시간에 따라 바뀌므로 기여 시 분석 기준일, 공식 URL, 법적 상태와 Evidence ID를 함께 갱신해 주세요.
