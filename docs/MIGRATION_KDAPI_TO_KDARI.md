# K-DAPI에서 K-DARI로 이전

## 변경 배경

프로젝트 범위가 정책 분석을 넘어 코인·프로젝트, 네트워크, 백서, 스테이블코인, RWA, 거래소 정책과 사업모델 리서치까지 확장되어 공개 명칭을 **K-DARI (Korean Digital Asset Research Intelligence)**로 통일했다.

현재 저장소와 스킬 식별자는 다음과 같다.

- 저장소: `junjunny/k-digital-asset-research-intelligence`
- 현재 식별자: `k-dari`
- 이전 식별자: `k-digital-asset-policy-intelligence`

이전 GitHub 저장소 주소는 GitHub 리디렉션이 동작할 수 있지만 영구 호환성을 보장하는 설치 인터페이스로 간주하지 않는다. 새 설치와 문서 링크에는 현재 주소를 사용한다.

## 새로 설치

```bash
npx skills add junjunny/k-digital-asset-research-intelligence --skill k-dari
```

특정 에이전트에 비대화식 copy 설치를 하려면 다음처럼 대상 에이전트를 지정할 수 있다.

```bash
npx skills add junjunny/k-digital-asset-research-intelligence --skill k-dari --agent codex --copy -y
```

## 기존 설치 이전

프로젝트에서 이전 식별자를 제거한 뒤 현재 식별자를 설치한다.

```bash
npx skills remove k-digital-asset-policy-intelligence -y
npx skills add junjunny/k-digital-asset-research-intelligence --skill k-dari
```

전역 설치였다면 두 명령에 `--global`을 함께 사용한다. 제거 전에 `npx skills list`와 `npx skills list --global`로 설치 범위를 확인한다.

`npx skills update`는 같은 식별자의 업데이트에 적합하다. 이번 변경은 식별자 자체가 달라졌으므로 이전 항목을 남긴 채 새 항목만 추가하면 중복 설치가 될 수 있다.

## 중복 설치와 호환성

두 식별자가 동시에 있으면 에이전트가 이전 지침과 현재 지침을 함께 발견하거나, 명시 호출이 서로 다른 파일을 가리킬 수 있다. 이전 폴더를 수동으로 복사한 경우에도 해당 에이전트의 프로젝트·사용자 skills 디렉터리를 확인해 하나만 남긴다. 삭제 대상 경로가 불명확하면 재귀 삭제를 사용하지 말고 Skills CLI의 목록과 제거 명령을 사용한다.

이 저장소는 이전 식별자를 가리키는 별도 alias skill을 제공하지 않는다. alias를 추가하면 자동 발견 시 중복 후보가 되고 실험 격리를 약화시킬 수 있기 때문이다.

## 에이전트별 사용

- 설치는 Skills CLI가 지원하는 에이전트 대상에 배치할 수 있다.
- 설치 성공, 스킬 발견, 명시적 호출, 자동 활성화는 서로 다른 검증 상태다.
- 자동 활성화가 관측되지 않으면 `$k-dari`를 명시한다.
- 각 에이전트의 버전·권한·도구 설정에 따라 웹 검색과 원문 접근 결과가 달라질 수 있다.

현재 확인된 상태는 [프로젝트 상태](PROJECT_STATUS_2026-11.md)와 [테스트 보고서](TEST_REPORT.md)에 기록한다.

## 과거 연구 결과

기존 Phase 8·9 실험 코드, 입력, 로그와 산출물의 K-DAPI 명칭·이전 저장소·이전 설치 경로는 당시 실행을 재현하기 위한 역사적 기록이다. 이를 현재 명칭으로 일괄 치환하지 않는다. 과거 기록의 이전 명칭은 현재 설치를 권장한다는 뜻이 아니다.

이름 변경은 기존 실험 결과를 다시 채점하거나 우열 결론을 바꾸지 않는다. 120건의 인간 블라인드 검토와 전문가 검토는 별도 게이트로 계속 대기한다.

