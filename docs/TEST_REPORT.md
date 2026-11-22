# Test Report

최종 갱신: 2026-11-21 (Asia/Seoul)

## 결과 요약

| 검증 | 결과 |
|---|---|
| Python unittest | 통과: 85건 (2026-11-21 전체 재실행) |
| 질문 라우터 | 통과: 26건 — 기존 17건 + 실제 실패 5건 + holdout·복합 유형 4건 |
| 부정 테스트 | 통과: 인용 불일치, 다른 문서, 404, 접근 제한, 오프라인, 시행 전 오인, 정책·입법예고 오인, 오래된 자료, 관할권 혼동, 근거 불일치, 사용자 오정보, 악의적 지시문 |
| EIB 저장 Evidence | 통과: 6/6 `CONTENT_VERIFIED`; 최신 live 재조회는 아래 제한 참조 |
| 홍콩 신규 사례 live content verification | 통과: 6/6 `CONTENT_VERIFIED` |
| HTML 추출 | 통과 |
| PDF 추출 | 통과: 홍콩 SFC circular (`pypdf`) |
| Report validator | 통과: EIB 6 findings, 홍콩 7 findings |
| JSON Schema 3종과 사례 2건 | 통과 |
| Skill Creator `quick_validate.py` | 통과 |
| 원격 fresh clone | 통과: commit `9b29d56` |
| Skills CLI 탐지·격리 설치 | 통과: Codex project scope, copy mode |
| GitHub Actions CI | 통과: Phase 6 run `43823538012` (`2305f3d`) |
| Python 문법 컴파일·CI YAML | 통과 |
| 일반적 API 키·개인키 패턴 검색 | 발견 없음 |
| 수동 첨부 진위 분리 | 통과: 발췌 일치 시에도 `MANUAL_REVIEW_REQUIRED` |
| URL·파일 입력 보안 | 통과: localhost, 사설·loopback·link-local, 자격증명, HTTPS downgrade, 리다이렉트 재검증, 디렉터리 탈출 차단 |
| 의미 검토 경계 | 통과: 구조적 claim/Evidence 호환성이 의미 증명이 아니라는 경고 출력 |
| Phase 6 격리 validator | 통과: 임시 venv에서 Skill Creator, Evidence 12건·Report 2건 JSON Schema 검증 |
| Skills CLI 탐지 | 통과: 범용 자연어 설명으로 스킬 1개 탐지 |
| Phase 7 로컬 Skill Creator·Skills CLI | 통과: 새 라우터·네트워크 설명 포함 스킬 1개 탐지 |
| Phase 7 원격 fresh clone·격리 설치 | 통과: commit `9e8f1ab`, copy mode, 설치본 라우터·Skill Creator 검증 |
| Phase 7 GitHub Actions CI | 통과: run `44027593383` (`9e8f1ab`) |
| Phase 8 fresh clone·Skills CLI 설치 | 통과: 기준선 `ba7734e`, GitHub source, Codex copy mode |
| Phase 8 독립 A/B 리서치 | 수행: CLARITY, Chainlink, Ethereum, USDC 각 대조군·설치본 사용군 1회 |
| Phase 8 모델 보조평가 | 94/98, 97/98, 95/98, 96/98; 치명적 오류 0 판단, 인간 평가 아님 |
| Phase 8 신규 Evidence v2 | 11건 schema 통과; 10 `CONTENT_VERIFIED`, 1 `ACCESS_RESTRICTED` |
| Phase 8 사용성·다중턴·오프라인 | 10개 수정 전/후, holdout 3개, 다중턴 3개, 웹 미사용 1개 기록 |
| Phase 8 GitHub Actions CI | 통과: run `44071185525` (`fec3258`) |
| Phase 9 Claude 코호트 | 완료: 120/120 답변·blind copy |
| Phase 9 AI 보조평가 | 통과: 120/120 고유 ID, 점수 합계 일치, 공식·관련 URL 969개 |
| AI 사전검토 분리 | 통과: 120개 모두 `NEEDS_HUMAN_VERIFICATION`, 인간 `reviews.json` 해시 불변 |
| K-DARI 현재 식별자 로컬 탐지 | 통과: Skills CLI 1.9.0, 1개 스킬 탐지 |
| 격리 copy 설치 | 통과: Codex·Claude Code 대상, 현재 식별자·references·scripts 확인 |
| Codex 명시 호출 | 통과: Codex CLI 0.169.0, 현재 식별자와 투자추천 금지 규칙 응답 |
| Claude Code 명시 호출 | 미검증: 2.1.327에서 스킬 발견, OAuth 만료로 모델 요청 전 차단 |
| 자동 활성화 | 미검증: 현재 식별자에 대한 일반화 가능한 관측 없음 |
| Markdown 상대 링크 | 통과: 깨진 링크 0건 |
| 공개 파일 보안 패턴 | 통과: 개인 절대경로·키·개인키·서명 URL 경계 패턴 0건; URL 단어 조각 오탐은 제외 |
| 최종 원격 fresh clone·설치 | 통과: `8ffdc23`, 85 tests, README 명령, Codex·Claude Code 설치본 SHA-256 일치 |
| 최종 GitHub Actions CI | 통과: run `44905235685` (`8ffdc23`) |

## 실행한 주요 명령

```bash
python3 -m py_compile scripts/*.py
python3 -m unittest discover -s tests -v
python3 scripts/route_question.py "CLARITY Act가 뭐야?"
python3 scripts/route_question.py "이 코인 어떤 거야?"
python3 scripts/validate_sources.py examples/tokenization-case-study/evidence.json
python3 scripts/validate_report.py examples/tokenization-case-study/report.json
python3 scripts/validate_sources.py examples/hong-kong-digital-green-bond/evidence.json
python3 scripts/validate_report.py examples/hong-kong-digital-green-bond/report.json
python3 scripts/verify_evidence.py examples/hong-kong-digital-green-bond/evidence.json --output /tmp/kdapi-hk-live-verification.json --timeout 25
python3 scripts/verify_evidence.py examples/tokenization-case-study/evidence.json --output /tmp/kdapi-eib-live-verification.json --timeout 25
npx skills add . --list
```

## Phase 8 독립 평가

기준선 `ba7734ed6e6b3b0483313d0564b12374b1d273f4`을 GitHub에서 fresh clone하고 다음 명령으로 설치했다.

```bash
npx --yes skills add junjunny/k-digital-asset-policy-intelligence@k-digital-asset-policy-intelligence --agent codex --copy -y
```

설치본은 격리 소비자 프로젝트의 `.agents/skills/k-digital-asset-policy-intelligence`에 생성됐다. 탐지·설치와 명시적 설치본 사용은 성공했다. 자동·암묵 활성화는 관측 가능한 이벤트가 없어 검증 완료로 표시하지 않았다.

네 질문의 A/B 원문은 `evaluations/phase-8/cases/`에 보존했다. 별도 모델 보조평가의 대조군/사용군 점수는 CLARITY 94/98, Chainlink 97/98, Ethereum 95/98, USDC 96/98이었다. 네 사례 모두 치명적 오류 0으로 보았으나, 각 1회 표본이고 최종 인간 평가는 미완료다.

핵심 출처 표본 11건을 Evidence v2로 검증했다. Chainlink 3건, Ethereum 2건, USDC 4건, CLARITY 상원 보고본 1건은 원격 원문과 발췌가 일치했다. 미국 상원 표결 페이지 1건은 HTTP 403으로 `ACCESS_RESTRICTED`이며 사람이 직접 확인해야 한다. 이 표본은 장문 답변의 모든 주장을 완전 매핑한 것은 아니다.

## Phase 8 라우터 회귀

수정 전 열 문항에서 실제로 관찰된 다섯 실패를 보존했다. 법률 의도와 스테이블코인, 거래소명과 네트워크, 국가명과 기술 비교, 한글 CLARITY 음역, 명시된 백서 대상의 충돌만 최소 수정했다. 수정 후 원 문항 10개와 별도 holdout 3개가 통과했다. 국내 토큰증권 현재 발행 가능성 질문은 `TOKENIZED_ASSET_OR_RWA`와 보조 `LAW_AND_REGULATION`을 함께 유지한다.

다중턴 3개는 독립 대화 평가로 통과했으나 자동화된 상태 서버 시험이 아니다. 웹 미사용 평가는 도구를 제공하지 않은 조건에서 최신 입법상태 단정을 거부했지만 OS 네트워크 차단 통합시험은 아니다.

## Phase 7 라우터 검증

- CLARITY Act 질문은 `LAW_AND_REGULATION`, 한국 규제 비교는 `REGULATORY_COMPARISON`
- 토큰증권의 간단한 정의는 `CONCEPT_EXPLANATION` + `TOKENIZED_ASSET_OR_RWA`
- 이더리움은 네트워크 평가, USDC는 스테이블코인 평가로 분리
- 대상 없는 코인·네트워크는 `AMBIGUOUS_REQUEST`와 확인 질문
- 백서는 공식 URL·파일·프로젝트명을 요청하되 백서 프레임워크 유지
- 투자 요청은 `INVESTMENT_OR_PRICE_REQUEST`로 분류하고 추천 대신 위험 검토로 전환
- 해외 네트워크 질문에는 한국 맥락을 자동 추가하지 않음
- 단순 질문에는 `DEEP_RESEARCH`를 강제하지 않음

라우터는 질문의 방법론을 선택할 뿐 실제 법안 상태, 프로젝트 안전성, 네트워크 품질을 증명하지 않는다. 이 부분은 Phase 8의 독립 리서치 대상이다.

## Phase 7 fresh installation

GitHub 원격을 `/tmp/kdapi-phase7-fresh-20261117/repo`에 새로 clone하고 별도 venv에 의존성을 설치했다. 54개 테스트, CLARITY Act 라우팅, Skill Creator 검증과 Skills CLI 탐지를 통과했다. 별도 git 프로젝트인 `/tmp/kdapi-phase7-fresh-20261117/consumer`에 copy mode로 설치하고, 설치본의 실행 권한·`SKILL.md`·모호한 코인 확인 질문·Skill Creator 검증을 확인했다.

PDF나 외부 API 키 없이 질문 라우팅은 시작할 수 있다. 다만 실제 최신 법률·프로젝트·네트워크 분석에는 웹 검색 또는 사용자가 제공한 공식 원문이 필요하며, 이것은 이번 Phase에서 독립 수행하지 않았다.

## Evidence 원문 검증

`verify_evidence.py`는 응답 코드·콘텐츠 유형·최종 URL·조회시각·문서 SHA-256·추출문 SHA-256을 기록하고, 정규화된 `relevant_excerpt`가 추출 원문에 포함되는지 확인했다.

실제 검증한 출처:

- EIB sterling digital bond 발표
- EUR-Lex Regulation (EU) 2022/858
- ESMA DLT Pilot Regime
- 국가법령정보센터 개정 전자증권법
- 금융위원회 2026-09 토큰증권 정책방향
- 금융위원회 2026-10 하위법규 입법예고
- HKMA 2024 multi-currency digital green bond 발표
- 홍콩 SFC tokenised securities circular PDF
- HKMA 2026 Tokenised Bond Expert Group 발표

같은 동적 웹페이지도 조회 시점에 HTML 전체 해시가 달라질 수 있다. 따라서 해시 변경만으로 의미 변경을 단정하지 않고 발췌문 일치·발행기관·날짜·법적 상태를 함께 본다.

## Fresh installation

GitHub 원격을 `/tmp/kdapi-fresh.ZWUF4g/repo`에 새로 clone하고 별도 venv에 의존성을 설치했다. 27개 테스트와 홍콩 보고서 검증을 통과한 뒤, Skills CLI가 1개 스킬을 탐지했고 `/tmp` 격리 프로젝트의 `.agents/skills/k-digital-asset-policy-intelligence`에 copy mode로 설치했다. 설치본에 대해 Skill Creator validator와 사례 파일 존재를 확인했다.

## 저장된 연구 산출물 회귀검증

Phase 5의 실제 자연어 요구를 기준으로 홍콩 다중통화 디지털 녹색채권을 조사했고, `tests/test_e2e_workflow.py`는 커밋된 산출물과 Evidence 상태를 재검증한다. 테스트 클래스는 실제 범위를 반영해 `StoredResearchArtifactTests`로 명명했다.

별도 에이전트가 격리 설치본에서 처음 보는 자연어 입력을 받아 출처 탐색부터 보고서 생성까지 실행한 blind E2E는 아니다. 당시 독립 평가 계획은 `docs/archive/PHASE_7_TEST_PLAN.md`에 보존한다.

## Phase 6 live 확인

- 홍콩 사례: 6/6 `CONTENT_VERIFIED`
- EIB 사례: 5/6 `CONTENT_VERIFIED`; EUR-Lex가 HTTP 200의 AWS WAF challenge를 반환하여 `ACCESS_RESTRICTED`

EUR-Lex 결과는 발췌 불일치로 잘못 분류하지 않고 접근 제한으로 처리하도록 검증기를 보완했다. 저장된 이전 원문 해시·발췌 기록은 삭제하지 않았지만, 이번 조회에서 원문을 재확인하지 못했으므로 사람이 브라우저에서 직접 확인해야 한다.

## 자동 검증할 수 없는 부분

- 인용문의 법률적 의미와 전체 문맥
- 비공개 계약서·법률의견서
- 개별 사업의 최종 인허가·세무·회계·외국환 적법성
- 스캔 PDF OCR, 복잡한 표·각주
- 기존 방식 대비 실제 비용·시간 절감과 사업 수익성
- 향후 공포될 한국 하위법규의 최종 내용
- CLARITY 2026년 9월 협상초안의 절차적 지위와 공식 상원 보고본·S.3755 관계
- Chainlink 계약매출·LINK 전환액·온체인 CCIP 사용량과 공급 API의 경제적 의미
- Ethereum 동적 대시보드·entity tagging의 실제 운영자 귀속
- USDC 동적 주간 수치, 은행별 익스포저와 한국 개별 거래의 외국환·세무 적용
- 지원 에이전트의 자동·암묵 스킬 활성화 이벤트

이 항목은 검증 완료로 표시하지 않고 보고서 한계 또는 `NEEDS_REVIEW`로 남겼다.

## 공개 패키징 재검증 (2026-11-23)

- `python3 -m unittest discover -s tests -v`: 88 tests OK
- Skill Creator `quick_validate.py`: valid
- `npx skills add . --list`: `k-dari` 1개 탐지
- 격리 로컬 copy 설치: 25파일·152KB, 프로젝트 전용 `evaluations/`, `tests/`, `docs/` 제외 확인
- 원격 `npx skills add junjunny/k-digital-asset-research-intelligence@k-dari --agent codex --copy -y`: 설치 성공
- 원격 `9e5b1a7` 설치본: 25파일·152KB, `SKILL.md` SHA-256 `95ce9d2983e14e9000b4b0d1fc6938d4194b6d851e078b78b30c583506913a23`
- skills.sh `junjunny/k-digital-asset-research-intelligence/k-dari`: HTTP 200, 설명·본문·설치 명령 표시
- `npx skills find k-dari`와 `npx skills find K-DARI`: 새 `@k-dari` 항목이 모두 첫 번째
- GitHub Actions run `45082535500` (`9e5b1a7`): success
- Markdown 상대 링크 검사: 누락 0건
- 추적 JSON 전체 파싱: 오류 0건
- 경계를 적용한 GitHub·OpenAI·AWS 키와 개인키 패턴 검사: 0건

이전 식별자 두 개는 과거 설치 기록 때문에 검색 하위 결과에 남아 있다. 현재 저장소에서는 `k-dari` 하나만 발견되며, 별도 alias를 제공하지 않는다. 인간평가 0/120과 전문가 검토 대기는 공개 패키징 완료와 별개의 상태다.


## Phase 9 Claude Code 이관 (2026-11-18)

- `python3 -m unittest discover -s tests`: 78 tests OK (신규 harness 6개: stream-json 사용량 중복 방지·N/A, 활성화 판정, 인증/한도 분류, 재개 대상 선별, 코호트 경로). 이전 54/63개는 역사적 수치.
- 실제 `npx --yes skills add junjunny/k-digital-asset-policy-intelligence@k-digital-asset-policy-intelligence --agent claude-code --yes` exit 0, SKILL.md SHA-256 로컬 일치.
- 실제 `claude -p` 1회 시도: AUTH_REQUIRED(OAuth 만료)로 실패 → 생성 답변 0개, 결과 없음.

위 0/120은 최초 차단 이력이다. 이후 재개되어 현재 Claude 코호트는 120/120 완료됐다.

## Phase 9 AI 보조 검토 (2026-11-21)

- `python3 scripts/evaluate_controlled_experiment.py prepare --cohort claude`: 6개 주제 × 20개 입력 생성
- 주제별 조건 블라인드 공식 원문 평가: 120/120, 누락·중복 없음
- 7개 항목 점수 합계와 `total_score`: 120/120 일치
- 결과 범위 50~87점, `SUPPORTED` 6건, `MIXED` 114건
- 핵심 주장 집계: 반박 169건, 근거 부족 502건
- `python3 scripts/build_ai_assisted_review.py`: 별도 AI 사전검토 120건 생성
- 생성 전후 `human-review/reviews.json` SHA-256 동일

AI 점수와 메모는 인간 검토를 대체하지 않으며, 최종 blind mapping 적용도 실행하지 않았다.

## K-DARI 최종 설치·명칭 검증 (2026-11-21)

환경은 Node.js 26.8.1, npm 11.19.0, Skills CLI 1.9.0, Codex CLI 0.169.0-alpha.11.1, Claude Code 2.1.327이었다.

```bash
npx --yes skills --version
npx --yes skills --help
npx --yes skills add --help
npx --yes skills add . --list
npx --yes skills add <local-repository> --skill k-digital-asset-research-intelligence --agent codex claude-code --copy -y --json
```

격리된 새 Git 프로젝트에서 `.agents/skills/k-digital-asset-research-intelligence`와 `.claude/skills/k-digital-asset-research-intelligence`를 생성했다. `SKILL.md` frontmatter, `references/evidence-policy.md`, `scripts/route_question.py`를 확인했고 Skills CLI 목록에는 현재 식별자 1개만 표시됐다.

Codex에는 `$k-digital-asset-research-intelligence`를 명시해 웹 검색과 파일 수정을 금지한 최소 호출을 실행했다. 에이전트가 현재 frontmatter 이름과 투자 추천 금지 규칙을 응답해 명시 호출을 확인했다. Claude Code 초기화 로그에도 현재 스킬이 발견됐지만 OAuth 세션 만료로 모델 요청 전 종료되어 명시 활성화 성공으로 기록하지 않는다. 자동 활성화는 이번 정리에서 검증하지 않았다.

전체 회귀는 `python3 -m unittest discover -s tests -v` 85건, Python 문법 컴파일, 두 사례 Evidence·Report validator, JSON 스키마 4종, Skills CLI 탐지와 `git diff --check`를 통과했다.

원격 커밋 `8ffdc23d736ea8e967f0c3ac52196f55e1a15094`을 새 디렉터리에 clone해 85개 테스트를 다시 통과했다. README의 정확한 명령으로 GitHub source를 설치했고 Codex·Claude Code 설치본의 `SKILL.md`가 원격 clone과 동일한 SHA-256 `73a190bb2199b114c31a4d5923f7e8b761714b838f367586ba01a5c301321de0`임을 확인했다. GitHub Actions run `44905235685`도 성공했다.

공개 추적 파일에서 개인 절대경로, 개인키, GitHub/AWS/Anthropic 키, 경계를 갖춘 OpenAI 키, 서명 URL 패턴을 검사했다. `sk-` 정규식의 초기 결과는 URL 내부의 일반 영단어 조각이었으며 토큰 경계를 적용하면 0건이다. 블라인드 매핑 원본은 이미 Git 이력에 추적되어 있어 내용은 열지 않고 공개 평가 오염 위험으로 별도 기록했다.
