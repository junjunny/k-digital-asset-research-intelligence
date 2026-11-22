# Phase 0 — Foundation

## 환경 확인

- 원격 GitHub 저장소는 존재했으나 2026-11-16 clone 당시 빈 저장소였다.
- Python 3.9.6, Node.js 26.8.1, Skills CLI 1.8.1을 확인했다.
- 필수 런타임은 Python 표준 라이브러리만 사용하도록 결정했다.

## 공개 스킬 조사

skills.sh와 `npx skills find 'regulatory research'`를 확인했다. 일반 연구에는 `mattpocock/skills@research`, deep research에는 `samber/cc-skills@deep-research`, 규제 연구에는 설치 수가 매우 적은 `hardyfu/ai-tools@regulatory-research` 등이 검색됐다. legal verified memo, financial research 계열도 확인했다.

평가 결과, 검색·자료 합성·PDF 처리의 일반 패턴은 참고할 수 있지만 다음 요구는 별도 구현이 필요했다.

- 한국 법률의 공포·시행·입법예고 상태 분리
- 증권의 법적 내용과 토큰 형식 구분
- 해외 모델에서 한국 적용 조건으로 이어지는 고정 분석 체계
- Evidence ID와 날짜·법적 상태를 기계 검증하는 스키마

외부 스킬은 설치·복제하지 않았고 필수 의존성으로 두지 않았다.

## 아키텍처 결정

`SKILL.md`는 라우팅과 불변 규칙만 유지한다. 상세 지침은 `references/`, 출력 골격은 `templates/`, 구조화 계약은 `schemas/`, 반복 검증은 `scripts/`로 분리한다. 웹·Python이 없는 환경에서도 자료 기반 분석은 가능하되 최신성·자동 검증 제한을 고지하도록 설계했다.

## 공식 출처 접근성

국가법령정보센터, 금융위원회, EIB, ESMA, EUR-Lex의 관련 문서를 실제 조회했다. 검색 결과의 존재만 가정하지 않고 사례에 사용한 URL을 `evidence.json`에 기록했다.

## 테스트 전략

자동: 구조, JSON 구문, 필수 필드, 날짜, URL 형식, Evidence ID 연결, 법률/정책/입법예고 상태 충돌. 수동: 법적 해석, 인용 문맥, 최신 하위법규, 사업 실행 가능성과 전문가 최종 검토.

