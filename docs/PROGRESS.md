# Progress

기준일: 2026-11-21

- Phase 0: 완료
- Phase 1: 완료
- Phase 2: 기본 검증 엔진 완료
- Phase 3: EIB 사례 1건 완료
- Phase 4: 로컬 공개 준비, 원격 push, fresh install 검증 완료
- Phase 5: Evidence v2·정규화 규제검증·홍콩 독립 사례·부정 테스트·원격 fresh install·CI 통과
- Phase 6: 인간 검토 패키지, 두 사례 품질감사, 입력 보안 보완, 범용 비전 반영, Phase 7 독립 테스트 설계 완료. 사용자 검토 대기
- Phase 7: 12개 질문 유형 라우터, 3개 응답 모드, 유형별 연구 프레임워크, 모호성·투자안전·한국 맥락 처리, 원격 fresh install·CI 완료
- Phase 8: fresh clone·Skills CLI 설치, 네 필수 질문 A/B 독립 리서치, 사용성·다중턴·오프라인 평가, Evidence v2, 라우터 최소 수정과 63개 회귀 테스트 완료. 인간 평가 대기
- Phase 9: Claude 코호트 120/120 생성 완료. 조건 블라인드 AI 보조평가와 1차 자료 감사 완료, 인간 평가 대기
- Phase 10: K-DARI 명칭·현재 저장소·스킬 식별자 통일, 로컬 격리 설치와 Codex 명시 호출 검증 완료. 인간·전문가 검토와 공개 Release는 대기

## 완료 파일군

초기 산출물에 원문 검증기, Evidence 마이그레이션, claim type 검증, GitHub Actions CI, 홍콩 다중통화 디지털 녹색채권 사례와 부정 테스트를 추가했다. Phase 6에서 K-DAPI를 7개 연구 유형을 지원하는 범용 자연어 스킬로 정의하고, 인간 검토 문서와 Phase 7 독립 자연어 평가 계획을 추가했다.

## Phase 6 완료

- 수동 첨부의 발췌가 일치해도 `CONTENT_VERIFIED`로 올리지 않고 `MANUAL_REVIEW_REQUIRED`로 유지
- 출처 진위, 문서 접근, 발췌 일치, 법률적 의미 검토 상태를 분리
- localhost·사설/내부망·link-local·URL 자격증명·위험한 리다이렉트 차단
- `manual_source_path`와 `evidence_file`의 상위 디렉터리·심볼릭 링크 탈출 차단
- claim/Evidence 호환성은 의미상 증명이 아니라는 validator 경고 추가
- 저장된 홍콩 사례 테스트를 독립 자연어 E2E가 아닌 저장 산출물 회귀검증으로 재분류
- EIB·홍콩 사례를 7개 품질 항목으로 감사하고 사용자 판단 질문을 우선순위화

## Phase 7 완료 범위

- 표준 라이브러리 기반 `route_question.py`와 JSON 출력
- 법률·규제 비교·코인·네트워크·백서·스테이블코인·토큰증권·거래소·사업모델 등 12개 유형
- `QUICK`, `STANDARD`, `DEEP_RESEARCH` 응답 모드
- “이 코인·이 네트워크·이 법안”의 대상 임의 선택 방지와 최소 확인 질문
- 매수·매도·가격 요청을 위험 분석과 체크리스트로 전환
- 명시적 관련성이 없을 때 한국 규제 연결 방지
- 일반 사용자 안내, 라우팅 결정표, 유형별 연구 프레임워크 작성
- 기존 Phase 7 독립 평가 계획을 superseded로 표시하고 Phase 8 후보로 이관
- 원격 fresh clone에서 54개 테스트, Skill Creator, Skills CLI 탐지와 격리 프로젝트 copy 설치 통과

## 미해결

- 최종 하위법규 공포 후 사례의 한국 규제 상태 갱신
- 법률·회계·세무 전문가의 사례 최종 검토
- 스캔 PDF OCR, 표·각주 의미 검증은 미구현
- 최종 하위법규 공포 전 입법예고 수치는 확정 요건으로 사용할 수 없음
- EIB의 룩셈부르크 직접 법적 근거, 홍콩 채권의 개별 적용 법령·법률의견 미확인
- 두 사례의 비용·유동성·수요·수익성 및 국내 사업 기회 미검증
- 라우터는 규칙 기반이므로 새 용어·오탈자·복합 문맥의 의미 판단을 완전히 대체하지 않음
- Phase 8 인간 평가표와 정책·기술·회계 핵심 주장 최종 검토
- Phase 9 인간 검토 120건과 최종 조건 공개·분석
- Claude Code 현재 식별자 명시 호출 재검증(OAuth 만료로 모델 요청 전 차단)
- GitHub Release/tag와 skills.sh 등록·홍보 여부 결정
- CLARITY의 2026년 9월 협상초안과 공식 상원 보고본·별도 S.3755의 절차적 관계 확인
- Chainlink 공급 API·Reserve 시점, Ethereum 동적 지표, USDC 주간 동적 수치 재현 확인

## Phase 8 완료 범위

- 기준선 SHA와 환경·질문·루브릭·치명적 오류를 평가 전에 고정
- 정확한 GitHub Skills CLI 명령으로 격리 소비자 프로젝트 copy 설치
- 네 필수 질문을 K-DAPI 미사용/사용 fresh 독립 세션에서 각각 1회 실행
- 자동 활성화와 명시적 설치본 사용을 구분하고 자동 활성화 미관측을 명시
- 모델 보조평가: CLARITY 94/98, Chainlink 97/98, Ethereum 95/98, USDC 96/98; 인간 점수 아님
- 수정 전 사용성 실패 5건 보존, 최소 라우터 수정, 원 질문·holdout 재검증
- 다중 턴 3개와 웹 미사용 최신상태 질문의 정직한 제한 응답 검증
- 신규 핵심 Evidence 11건: 10건 원문·발췌 일치, 상원 표결 1건 접근 제한


- Phase 9(Claude Code 코호트): 인증 차단 이력 뒤 실행을 재개해 120/120 답변과 blind copy를 완료했다. 2026-11-21 기준 AI 보조평가는 120/120, 공식·관련 근거 URL 969개, 점수 50~87점, `SUPPORTED` 6건·`MIXED` 114건이다. 인간 `reviews.json`은 변경하지 않았고 최종 인간 검토와 조건 공개는 대기 중이다.

## 최종 저장소 정리 (2026-11-21)

- 공개명과 현재 식별자를 K-DARI / `k-digital-asset-research-intelligence`로 통일
- 새 GitHub 주소 기반 설치 명령, 국·영문 README, 이전 식별자 마이그레이션 문서 추가
- Skills CLI 1.9.0에서 현재 식별자 1개 탐지, Codex·Claude Code 격리 copy 설치 확인
- Codex 명시 호출 성공, Claude Code는 스킬 발견 후 OAuth 만료로 실제 모델 호출 미검증
- 과거 실험 코드·기록의 K-DAPI 명칭과 설치 경로는 재현성을 위해 보존
- 인간 검토 파일과 블라인드 매핑은 수정·적용하지 않음
