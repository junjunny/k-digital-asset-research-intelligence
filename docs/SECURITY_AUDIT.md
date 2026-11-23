# K-DARI 보안 감사

기준일: 2026-11-23 (Asia/Seoul)  
대상: skills.sh Snyk MEDIUM WARN `W011`, `W012`와 K-DARI 공개 설치·외부 자료 검증 경로

## 결론

두 경고는 알려진 악성 코드나 이미 악용된 취약점을 확인한 결과가 아니다. 그러나 오탐으로 폐기할 수도 없다.

- `W011`은 에이전트가 외부 백서·웹페이지·PDF를 읽는 연구 기능에 수반되는 **간접 프롬프트 인젝션 위험**이다. 기존 코드가 외부 명령을 실행하지는 않지만, 에이전트가 읽는 콘텐츠와 지시의 신뢰 경계를 더 명확하게 고정할 필요가 있었다.
- `W012`는 간편 설치가 기본 브랜치의 최신 내용을 가져오는 **가변 공급망 위험**이다. 저장소가 검증되지 않았다는 의미라기보다, 미래 설치 결과가 현재 감사본과 달라질 수 있다는 뜻이다.

따라서 웹 연구 기능과 간편 설치는 유지하되, 콘텐츠 격리 규칙·기계 판독 가능한 경고·자격증명 URL 차단·해시 고정 의존성·태그/커밋 고정 설치 경로를 추가했다. Snyk PASS 전환은 보장하거나 주장하지 않는다. 2026-11-23 커밋 고정 설치 시 Skills CLI 1.9.0도 여전히 Snyk를 `Med Risk`로 표시했다.

## W011 — Third-party content exposure

### 원인

K-DARI는 법령, 규제기관 문서, 프로젝트 백서와 웹페이지를 읽어야 한다. 공식 도메인도 침해되거나 사용자 생성 콘텐츠를 포함할 수 있고, PDF·HTML 본문에 “이전 지시를 무시하라”, “도구를 실행하라”, “비밀을 전송하라” 같은 문자열이 들어갈 수 있다. 정적 감사 도구는 이 외부 콘텐츠 노출을 간접 프롬프트 인젝션 가능성으로 본다.

### 위험 수준

**구조적 MEDIUM 위험, 알려진 악용 증거 없음.** 외부 텍스트가 에이전트의 권한으로 이어질 수 있는 환경에서는 영향이 크지만, 현재 검증기는 문서를 실행하지 않고 텍스트와 발췌문만 비교한다. 위험은 에이전트가 콘텐츠 속 지시를 신뢰하거나 별도 도구로 옮겨 실행할 때 현실화한다.

### 기존 방어

- 외부 콘텐츠를 데이터로만 처리하고 문서 명령을 실행하지 않는 `SKILL.md` 규칙
- HTML의 `script`, `style`, `noscript`, `svg` 본문 억제
- PDF는 텍스트 추출만 수행하고 첨부 코드·매크로·링크를 실행하지 않음
- 내부망·localhost·자격증명 포함 URL, HTTPS→HTTP 리다이렉트, 작업 디렉터리 밖 파일 접근 차단
- 매 리다이렉트 대상 재검증, 문서 크기 상한, 공식 URL과 수동 첨부 상태 분리
- 일부 인젝션 문구 탐지와 `UNTRUSTED_INSTRUCTION_PATTERN` 경고

### 추가 개선

- `SKILL.md`에 외부 콘텐츠 신뢰 경계를 별도 절로 추가했다.
- 역할 변경, 지시 무시, 프롬프트·비밀 공개, 데이터 유출, 도구·코드 실행의 영문·국문 패턴을 규칙 ID로 탐지한다.
- 검증 결과에 `content_trust=UNTRUSTED_EXTERNAL_DATA`, `untrusted_instruction_detected`, `detected_instruction_patterns`를 기록한다. 탐지된 원문 자체는 로그에 복제하지 않는다.
- 외부 문서의 링크는 자동 추적하지 않으며, 인젝션 문구가 포함돼도 발췌 일치와 보안 경고를 서로 다른 차원으로 보존한다.
- `token`, `api_key`, `password`, 서명 값 등 자격증명형 쿼리 키가 있는 URL은 네트워크 요청 전에 거부한다.
- 의심 문서는 독립 공식 출처로 교차검증하고, 확인할 수 없으면 `NEEDS_REVIEW`로 남기도록 근거 정책을 보강했다.

### 테스트 결과

- 인젝션 문구가 있는 문서를 한 번만 조회하고 외부 지시 URL을 추가 호출하지 않음
- 비밀·로컬 파일 업로드 요구를 `DATA_EXFILTRATION`으로 표시
- 역할·지시 무시와 시스템 프롬프트 공개 요구를 별도 규칙으로 표시
- 자격증명형 쿼리 문자열을 요청 전에 차단
- 기존 localhost·내부망·리다이렉트·파일 경로 방어 회귀 유지

### 잔여 위험

- 휴리스틱은 변형·난독화·이미지 속 지시를 모두 탐지하지 못하며 오탐도 가능하다.
- `pypdf`가 처리하는 악성 PDF의 파서 취약점과 자원 고갈 가능성을 완전히 제거하지 못한다. 파일 크기 제한과 버전·해시 고정은 완화책이다.
- DNS 재바인딩, 프록시 계층, 브라우저/에이전트 자체 검색 도구의 구현 차이는 이 Python 검증기만으로 완전히 통제할 수 없다.
- 보안 경고가 없다는 사실은 문서가 안전하거나 주장이 사실임을 보증하지 않는다.

## W012 — Unverifiable external dependency

### 원인

간편 설치 명령의 `@k-dari`는 버전이 아니라 스킬 이름 필터다. 따라서 설치 시점의 기본 브랜치에서 `k-dari`를 찾는다. 기본 브랜치가 바뀌면 미래 설치본도 바뀐다. 외부 공식 URL 역시 연구 시점에 내용과 가용성이 변할 수 있다.

```bash
npx skills add junjunny/k-digital-asset-research-intelligence@k-dari
```

### 위험 수준

**공급망·재현성 MEDIUM 위험, 임의 런타임 제어 증거 없음.** 현재 저장소와 CI는 공개적으로 감사할 수 있지만, 기본 브랜치 설치는 특정 감사를 재현하지 않는다. GitHub 계정·저장소 또는 의존 배포 경로가 침해되면 후속 설치에 영향을 줄 수 있다.

### 기존 방어

- 공개 Git 이력, 최소권한 GitHub Actions(`contents: read`), 독립 `skills/k-dari/` 패키지
- Skill Creator 검증, 전체 회귀 테스트, 격리 copy 설치와 설치본 파일 확인
- skills.sh에서 소스 저장소와 스킬 경로 공개
- URL 원문 해시와 추출문 해시 기록

### 추가 개선과 검증된 설치 방식

Skills CLI 공식 문서와 1.9.0 동작을 함께 확인했다. 버전 형태의 `owner/repo@v1.0.0` 또는 40자리 전체 커밋 SHA는 Git ref로 해석되며, `--skill k-dari`로 스킬을 선택한다. GitHub Release 객체 자체가 설치 대상을 고정하는 것은 아니고, 연결된 **Git 태그 또는 커밋**이 실제 설치 기준이다.

최신 기능을 받는 간편 설치는 그대로 유지한다.

```bash
npx skills add junjunny/k-digital-asset-research-intelligence@k-dari
```

검증 기준 릴리스 설치:

```bash
npx skills add junjunny/k-digital-asset-research-intelligence@v1.0.0 --skill k-dari
```

감사 구현 커밋 고정 설치:

```bash
npx skills add junjunny/k-digital-asset-research-intelligence@7bd5ce84825ee4e678e17d8ecd33a41cfd394ebb --skill k-dari
```

전체 SHA 설치는 Skills CLI 1.9.0의 격리 프로젝트에서 실제 실행해 `ref`, 설치 파일 25개와 보안 지침 포함 여부를 확인했다. 태그는 저장소 관리자가 이동할 수 있으므로 편의성과 재현성의 절충안이며, 전체 커밋 SHA가 더 강한 고정 수단이다.

또한 PDF 의존성을 범위 지정에서 다음 정확한 버전과 PyPI 배포 SHA-256으로 변경했다.

- `pypdf==6.21.4`
- Python 3.9·3.10용 `typing_extensions==4.16.0`

CI와 설치 검증은 `pip --require-hashes`를 사용한다.

### 잔여 위험

- 태그는 암호학적으로 불변이 아니며 GitHub 계정·저장소 신뢰가 필요하다.
- 커밋 SHA도 GitHub·Git·Skills CLI·npm 전달 경로의 가용성과 구현을 신뢰한다. 서명된 배포물과 완전한 재현 빌드는 아직 제공하지 않는다.
- 간편 설치는 의도적으로 최신 기본 브랜치를 사용하므로 W012의 근본 신호가 남을 수 있다.
- 연구 대상 공식 URL은 동적 외부 의존성이다. 이를 제거하면 최신성 검증 기능이 사라지므로 해시·조회시각·상태 기록으로 관리한다.

## 변경하지 않은 연구 자료

이번 감사는 기존 120개 답변, 자동·AI 보조평가, 인간 검토 상태, blind mapping과 과거 실행 로그를 수정하지 않는다. 인간 검토는 계속 `0/120` 대기 상태이며, 보안 보강은 기존 실험 결과를 재채점하거나 승인하지 않는다.

감사 시작 시 보존 확인 SHA-256:

- `human-review/reviews.json`: `7eb166dac6920b67a0cd300262988c0639f811cc68153476d4687983a4ae2c2b`
- `results/aggregate.json`: `2e638b97815f0d0abbd3dff5d0f64fb774cebd58211c4aed40ed0c1dc888b923`
- `scores/blind-mapping.json`: `a2e519638d0a9a4b16321c2d9ca719fa2da39c1ce7f6d14aaa122f5a8bbc41fa`

## 외부 근거

- [Skills CLI source formats and pinned refs](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#source-formats)
- [Skills CLI source parser](https://github.com/vercel-labs/skills/blob/main/src/source-parser.ts)
- [skills.sh security notice](https://www.skills.sh/docs)
