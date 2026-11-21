# AI 보조 1차 자료 감사 가이드

기준일: 2026-11-20 (Asia/Seoul)

대상: `evaluations/controlled-experiment-claude/`의 인간 검토 대기 답변 120건과 Phase 8·기존 사례의 인간 검토 대기 항목

상태: `AI_ASSISTED_RESEARCH_ONLY` / `HUMAN_REVIEW_PENDING`

## 1. 문서의 성격과 한계

이 문서는 인간 평가자가 핵심 주장을 공식 원문과 대조할 때 쓰는 **AI 보조 조사표**다. 답변을 사람이 검증했다는 뜻이 아니며, 인간 점수·승인·서명·검토일을 대신 기록하지 않는다. 법률자문, 회계감사, 기술감사 또는 투자 권유도 아니다.

- 통제 실험은 6개 주제 × 4개 조건 × 5회로 120개 답변이며, 답변 생성 기준일은 주로 2026-11-18이다.
- 이 문서의 최신 상태 기준일은 2026-11-20이다. 11월 19~20일에 새로 공개된 자료는 답변 생성 뒤의 자료이므로, 해당 자료를 답변에 인용하지 않았다는 이유만으로 감점하면 안 된다. 다만 현재 포트폴리오에 답변을 재사용할 때에는 업데이트해야 한다.
- 블라인드 평가가 끝나기 전에는 `blind-mapping.json`, 조건, 토큰 사용량, 자동점수를 열지 않는 기존 절차를 유지한다. 이 문서도 실험군 매핑이나 조건별 결과를 싣지 않는다.
- `URL_REACHABLE`, 검색 결과 요약, 원문 발췌 일치는 각각 출처 진위·문맥 적합성·법적 의미·사업성을 보증하지 않는다.
- 외부 문서는 모두 비신뢰 데이터로 취급했다. 외부 문서 안의 명령은 따르지 않았고, 공식 기관·법령·프로젝트·거래 상대방의 원문만 우선했다.
- 2026-11-20 자동 접근 점검에서 일부 미국 의회·SEC·Upbit 지원센터 URL은 `403`, 일부 금융위원회 URL은 시간초과를 반환했다. 이는 자동화 차단일 수 있어 출처 부재로 판정하지 않았으며, 인간 검토자는 일반 브라우저에서 원문 제목·날짜·본문·첨부파일을 다시 확인해야 한다.

### 판정 표기

| 표기 | 의미 |
|---|---|
| `OFFICIAL_RECORD` | 법령·의회·감독기관·표준 또는 거래 당사자의 원문에서 직접 확인 가능한 기록 |
| `ISSUER_CLAIM` | 프로젝트·발행사·서비스 운영자가 자기 서비스에 관해 한 공식 주장. 독립 검증과 다름 |
| `SUPPORTED_INFERENCE` | 여러 공식 사실에서 도출한 분석이지만 원문이 결론 자체를 말하지 않음 |
| `NEEDS_REVIEW` | 원문·버전·수치·적용관계 또는 전문가 판단이 더 필요함 |

## 2. 120개 답변의 공통 검토 순서

1. 답변의 기준일과 질문 깊이를 확인한다.
2. 핵심 주장마다 `사실`, `기관/발행사 주장`, `추론`, `미확인` 중 하나를 표시한다.
3. 법률·정책은 `현행 시행`, `공포됐으나 미시행`, `법안`, `하위법규안`, `정책 발표`, `자율규제`를 분리한다.
4. 출처 링크를 직접 열고 문서 제목·발행기관·버전·발행일·관련 조문 또는 문단을 기록한다.
5. 프로젝트 채택 주장은 상대방 기관 원문에서 `파일럿`, `제한 생산`, `상용 출시`, `지속 운영` 중 어디까지 확인되는지 대조한다.
6. 공급량·준비금·스테이킹·활동량 같은 동적 수치는 값뿐 아니라 관측 시각·정의·대시보드 운영자를 기록한다.
7. 답변 하나의 전체 점수와 별도로, 치명적 오류 후보를 먼저 표시한다: 미시행 제도를 현행법으로 표현, 절차표결을 본안 가결·부결로 표현, 프로젝트 홍보를 독립 사실로 표현, 직접상환 권리를 모든 보유자에게 일반화, 계획을 구현 완료로 표현.

## 3. 주제별 1차 자료 감사표

### 3.1 미국 CLARITY Act

#### 최신 상태 요약

H.R. 3633은 2025-07-17 하원을 294–134로 통과했다. 상원 은행위원회는 2026-05-14 수정안을 15–9로 의결했고, 2026-07-22에는 은행위·농업위 작업을 합친 업데이트 텍스트가 공개됐다. 그러나 2026-09-15 상원 본회의에서 **법안 본안 표결이 아니라 motion to proceed에 대한 cloture**가 49–50으로 부결됐다. 상원 농업위원회 위원장의 2026-11-17 공식 발언도 “full Senate를 통과하지 못했다”고 확인한다. 따라서 기준일 현재 **미제정 법안**이며 현행법이 아니다.

| Evidence ID | 핵심 검증 주장 | 1차 자료 | 현재 판정·검토 포인트 |
|---|---|---|---|
| AUD-CLA-01 | 법안 번호·하원 통과본의 조문과 버전 | [GovInfo H.R. 3633 Engrossed in House](https://www.govinfo.gov/content/pkg/BILLS-119hr3633eh/html/BILLS-119hr3633eh.htm), [Congress.gov bill page](https://www.congress.gov/bill/119th-congress/house-bill/3633) | `OFFICIAL_RECORD`. SEC/CFTC 역할·정의·예외는 반드시 이 버전을 인용했다고 밝혀야 한다. |
| AUD-CLA-02 | 하원 통과 294–134 | [House Financial Services Committee 발표](https://financialservices.house.gov/news/documentsingle.aspx?DocumentID=410815) | `OFFICIAL_RECORD`. 위원회 표결 32–19와 하원 본회의 표결을 혼동하지 않는다. |
| AUD-CLA-03 | 상원 은행위 15–9 및 수정본 | [Senate Banking Committee 표결 발표](https://www.banking.senate.gov/newsroom/majority/chairman-scott-senate-banking-committee-advance-clarity-act-in-historic-bipartisan-vote), [상원 은행위 텍스트 PDF](https://www.banking.senate.gov/imo/media/doc/ehf26374.pdf) | `OFFICIAL_RECORD`. 하원 통과본과 조문이 다를 수 있으므로 혼합 요약 금지. |
| AUD-CLA-04 | 2026-07-22 합본 업데이트 텍스트의 존재 | [Sen. Lummis 공식 발표](https://www.lummis.senate.gov/press-releases/lummis-releases-updated-clarity-act-text/) | `OFFICIAL_RECORD`. “최신 상원안”이라고 할 때 PDF 버전·공개일을 함께 적는다. |
| AUD-CLA-05 | 2026-09-15 표결은 motion to proceed에 대한 cloture이며 49–50 부결 | [U.S. Senate Roll Call Vote 234](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00234.htm) | `OFFICIAL_RECORD`. “상원이 법안을 49–50으로 부결했다”는 표현은 부정확하다. 3/5가 필요한 절차표결이다. |
| AUD-CLA-06 | 기준일 현재 full Senate 미통과 | [Senate Agriculture Committee 2026-11-17 발언](https://www.agriculture.senate.gov/newsroom/rep/press/release/chairman-boozman-opening-statement-in-hearing-to-consider-cftc-nominees) | `OFFICIAL_RECORD`. 재고동의 가능성과 법률 제정 여부를 분리한다. |
| AUD-CLA-07 | 하원안의 SEC/CFTC 분담에 대한 중립 요약 | [Congressional Research Service IN12583](https://www.congress.gov/crs_external_products/IN/PDF/IN12583/IN12583.1.pdf) | 의회 소속 1차 분석 자료. CFTC의 디지털 상품·중개자 역할과 SEC의 1차 발행·증권 권한을 설명하지만, 상원 수정본의 최종 내용으로 일반화하지 않는다. |

#### 오류 위험 포인트

- `BILL_PROPOSED`를 `LAW_EFFECTIVE`처럼 표현하는 오류.
- 하원 본회의, 하원 위원회, 상원 위원회, 상원 cloture 표결을 하나의 “통과/부결”로 합치는 오류.
- 하원 EH 버전의 정의·면제와 2026년 상원 수정본을 섞으면서 단일 법안 내용처럼 쓰는 오류.
- 법안이 제안하는 SEC/CFTC 권한을 현재 기관 권한이라고 표현하는 오류.
- 법안 지지 위원회 보도자료의 효과 주장을 중립적·독립적으로 입증된 결과로 취급하는 오류.
- 한국 비교에서 토큰증권 시행 예정법, 가상자산이용자보호법, 아직 입법 중인 디지털자산 2단계 제도를 혼합하는 오류.

### 3.2 Chainlink와 LINK

#### 최신 상태 요약

Chainlink는 오라클·데이터·상호운용성 서비스이고 LINK는 그 네트워크의 지불·보상·스테이킹 자산이다. 공식 페이지는 총공급 10억 LINK, 현재 연 7% 토큰 방출 일정을 밝힌다. 2026-11-20 조회 시 공식 대시보드는 약 7.67억 유통량, Community staking 40,875,000 LINK가 꽉 찬 상태, Reserve 약 6.57M LINK를 표시했다. 이 값들은 계속 변하므로 답변의 관측일 값과 현재 값을 직접 비교해야 한다.

CCIP 2.0은 2026-09-28 출시됐지만, Chainlink의 자체 채택·TVE·TVS 수치는 `ISSUER_CLAIM`이다. DTCC는 2026-07-15 제한 생산 거래 후 2026-10-28 Tokenization Service를 상용 출시했다. 다만 DTCC가 Chainlink를 참여사로 열거한 사실과 “DTCC 전체 서비스가 Chainlink로 구동된다”는 주장은 같지 않다.

| Evidence ID | 핵심 검증 주장 | 1차 자료 | 현재 판정·검토 포인트 |
|---|---|---|---|
| AUD-LINK-01 | DON·Data Feed의 구조 | [Chainlink Decentralized Data Model](https://docs.chain.link/architecture-overview/architecture-decentralized-model) | `ISSUER_CLAIM`이지만 기술 구조의 소유 문서. “완전한 탈중앙화” 같은 평가로 확대하지 않는다. |
| AUD-LINK-02 | CCIP 기능·보안 구조·현재 버전 | [CCIP overview](https://docs.chain.link/ccip/overview), [CCIP 2.0 changelog](https://docs.chain.link/changelog/announcing-ccip-2-0-8b9be), [CCIP architecture](https://docs.chain.link/ccip/concepts/architecture/offchain/overview) | `ISSUER_CLAIM`. v1 문서와 v2 구조, RMN의 과거·현재 역할을 섞지 않는다. |
| AUD-LINK-03 | LINK 역할과 Payment Abstraction | [Chainlink Economics](https://chain.link/economics), [Payment Abstraction mainnet 발표](https://chain.link/blog/payment-abstraction-svr-fee-conversion) | 사용자는 법정화폐·다른 토큰으로 낼 수 있고 일부 수익이 LINK로 전환되는 구조. 기관 채택 건수를 LINK 매수액·가격으로 바로 환산할 수 없다. |
| AUD-LINK-04 | 총공급·유통량·방출 일정 | [공식 circulating supply](https://chain.link/circulating-supply) | 총공급 10억, 현행 방출 일정 연 7%. 유통량은 API·대시보드 관측 시각을 기록한다. 초기 배분과 현재 통제지갑을 별도로 검토한다. |
| AUD-LINK-05 | Staking v0.2 범위 | [Staking v0.2 설명](https://chain.link/economics/staking), [실시간 staking dashboard](https://staking.chain.link/) | 총 cap 45M, community allotment 40.875M, 28일 cooldown. v0.2에서 slashing은 서비스 대상 Node Operator stake에 적용되고 community stake는 현재 대상이 아니다. |
| AUD-LINK-06 | Reserve 현재 규모와 Q3 증가 | [Reserve dashboard](https://metrics.chain.link/reserve), [Q3 2026 review](https://chain.link/blog/quarterly-review-q3-2026) | 대시보드는 약 6.57M LINK, Q3 말 자체 보고는 6,047,498.3150 LINK. 온체인 주소·시점 대조 전에는 독립 검증으로 표시하지 않는다. |
| AUD-LINK-07 | 네트워크 사용 지표 | [Chainlink Metrics](https://metrics.chain.link/) | TVE·TVS·CCIP volume은 Chainlink가 정의·제공한 지표. 산식, 중복, 이상치 제거, 업데이트 월을 함께 확인한다. |
| AUD-LINK-08 | DTCC의 실제 운영 단계 | [2026-07-15 제한 생산 거래](https://www.dtcc.com/press-releases/2026/dtcc-turns-tokenization-into-reality), [2026-10-28 서비스 출시](https://www.dtcc.com/press-releases/2026/dtcc-tokenization-service-goes-live) | `OFFICIAL_RECORD`인 상대방 자료. 7월 거래와 10월 출시를 구분하고, Chainlink의 구체 역할은 거래별 상대방 문구로 제한한다. |
| AUD-LINK-09 | Swift 상호운용성 실험 | [Swift interoperability experiments report](https://www.swift.com/sites/default/files/files/results_report_swift_interoperability_experiments_final_310823.pdf) | `OFFICIAL_RECORD`. 실험 결과이지 Swift의 독점적·전면 상용 채택 증명은 아니다. |

#### 오류 위험 포인트

- Chainlink 플랫폼 채택, CCIP 채택, LINK 보유·구매를 동일시하는 오류.
- 파트너 로고·보도자료를 계약 매출·사용량·상용 지속성으로 바꾸는 오류.
- 공식 대시보드의 동적 수치를 기준일 없이 고정 사실처럼 쓰는 오류.
- Staking 전체 cap, community cap, 실제 stake를 혼동하거나 v0.2 slashing 범위를 과장하는 오류.
- Chainlink가 산출한 TVE·TVS를 감사된 재무지표처럼 표현하는 오류.
- DTCC의 제한 생산 거래와 상용 출시를 혼합하거나, 참여사인 Chainlink가 전체 서비스를 “powered”한다고 확대하는 오류.

### 3.3 Ethereum 네트워크

#### 최신 상태 요약

Ethereum은 execution client와 consensus client가 Engine API로 연결되는 PoS 네트워크다. Pectra는 2025-05-07, Fusaka는 2025-12-03 mainnet에 적용됐다. EIP-7702는 Pectra에 포함됐지만 이것이 모든 계정의 완전한 native account abstraction을 뜻하지는 않는다. ERC-4337은 별도 mempool·EntryPoint 계약 기반 방식이다.

Glamsterdam은 2026-11-20 현재 devnet/testnet 단계이며 ethereum.org는 mainnet을 “Q4 2026, date not yet confirmed”로 표시한다. Hegotá는 2027 계획이고 범위가 확정되지 않았다. 따라서 예정 기능을 현재 mainnet 기능으로 쓰면 오류다.

| Evidence ID | 핵심 검증 주장 | 1차 자료 | 현재 판정·검토 포인트 |
|---|---|---|---|
| AUD-ETH-01 | 실행 계층·합의 계층·Engine API | [ethereum.org node architecture](https://ethereum.org/developers/docs/nodes-and-clients/node-architecture/) | `OFFICIAL_RECORD` 성격의 프로젝트 기술문서. EL이 거래·EVM·상태, CL이 PoS 합의·fork choice를 맡는다는 구분을 확인한다. |
| AUD-ETH-02 | PoS 구조 | [ethereum.org Proof-of-Stake](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) | 보상·슬래싱·finality 설명은 “12초 슬롯”과 “경제적 finality”를 같은 개념으로 쓰지 않는다. |
| AUD-ETH-03 | EVM 사양 | [Ethereum Yellow Paper](https://ethereum.org/content/developers/tutorials/yellow-paper-evm/yellow-paper-berlin.pdf), [execution specs repository](https://github.com/ethereum/execution-specs) | Yellow Paper 버전이 최신 fork 전체를 반영하는지 확인한다. 구현 현황은 specs·client release와 대조한다. |
| AUD-ETH-04 | L2와 L1 보안 관계 | [ethereum.org scaling](https://ethereum.org/developers/docs/scaling/), [Ethereum security challenges](https://ethereum.org/reports/trillion-dollar-security/) | L2는 설계별 보안·bridge·sequencer·security council 위험이 다르다. L1과 L2 거래량·수수료를 단순 합산하지 않는다. |
| AUD-ETH-05 | Pectra와 EIP-7702 | [Pectra EIP-7702 guide](https://ethereum.org/roadmap/pectra/7702/), [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) | 이미 구현됨. 단, 기존 EOA private key 통제가 남고 wallet·delegate contract·relayer 위험이 있다. |
| AUD-ETH-06 | ERC-4337 방식 | [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) | 계약·bundler 기반 account abstraction. EIP-7702와 목적이 겹쳐도 동일 구현은 아니다. |
| AUD-ETH-07 | Fusaka mainnet 상태 | [Ethereum Foundation Fusaka announcement](https://blog.ethereum.org/2025/11/06/fusaka-mainnet-announcement), [Ethereum roadmap](https://ethereum.org/roadmap/) | 2025-12-03 적용, PeerDAS와 후속 BPO를 확인. 발표 당시의 “예정” 문구와 현재 완료 상태를 구분한다. |
| AUD-ETH-08 | Glamsterdam·Hegotá 상태 | [Glamsterdam roadmap](https://ethereum.org/roadmap/glamsterdam/), [Glamsterdam testnet announcement](https://blog.ethereum.org/en/2026/09/17/glamsterdam-testnet-announcement), [전체 roadmap](https://ethereum.org/roadmap/) | Glamsterdam mainnet 날짜 미확정, Hegotá 2027 계획. scope와 EIP status는 변동 가능하다. |

#### 오류 위험 포인트

- 슬롯 시간, finality, 처리량 상한, 실제 평균 처리량을 같은 성능 수치로 쓰는 오류.
- Ethereum L1과 여러 L2의 거래를 중복·비교 불가능한 정의로 합산하는 오류.
- Pectra·Fusaka 완료, Glamsterdam 테스트, Hegotá 계획을 모두 “도입”으로 표현하는 오류.
- ERC-4337과 EIP-7702를 동일시하거나 EIP-7702가 EOA 키 위험을 제거했다고 표현하는 오류.
- validator 수를 독립 운영자 수로, client share를 entity share로, builder 집중을 consensus client 집중으로 바꾸는 오류.
- “가장 큰 개발자 생태계”, TPS, 수수료 같은 동적·비교 주장을 ethereum.org만으로 독립 입증했다고 보는 오류.

### 3.4 USDC

#### 최신 상태 요약

Circle의 2026-10-15 약관에 따르면 USDC는 분리된 준비자산으로 1:1 뒷받침된다고 Circle이 약속하지만, Circle에 직접 상환하려면 적격 Circle Mint 계정이 필요하다. 일반 보유자(User Type B)는 계정을 개설해 적격성을 충족하기 전에는 직접 상환할 수 없다. USDC는 예금보험·SIPC 보호 대상이 아니고, Circle은 주소 차단·동결 및 유효한 정부 명령에 따른 준비자산 반환 권한을 보유한다.

2026-11-16 Circle 자체 공시는 약 680억 USDC 유통을 표시했다. 주간 공시는 회사 자료이고, 월간 examination은 특정 기준일의 준비자산·유통량 진술에 대한 독립 회계사 보증이며 회사 전체 재무제표 audit와 다르다. GENIUS Act와 OCC 최종규칙은 제정·공포됐지만 2027-01-18 시행 예정이므로, 기준일 현재 새 연방 체계가 이미 시행 중이라고 쓰면 안 된다.

| Evidence ID | 핵심 검증 주장 | 1차 자료 | 현재 판정·검토 포인트 |
|---|---|---|---|
| AUD-USDC-01 | 발행사·보유자 유형·직접상환·동결·무보험 | [Circle USDC Terms, 2026-10-15](https://www.circle.com/legal/usdc-terms) | `OFFICIAL_RECORD`인 계약 원문. 1 USDC=1 USD 상환은 약관·적격성·법률·수수료 조건부다. |
| AUD-USDC-02 | 준비자산 구성·주간 공시·월간 examination | [Circle transparency](https://www.circle.com/transparency) | Circle 자체 공시. 수치의 기준시각과 월간 보고서의 report date를 별도로 기록한다. |
| AUD-USDC-03 | attestation/examination과 audit 차이 | [Circle의 설명](https://www.circle.com/blog/how-to-build-trust-usdc-audits-and-attestations), [Circle SEC 10-Q, 2026-09-30](https://www.sec.gov/Archives/edgar/data/1876042/000187604226000311/crcl-20260930.htm) | 용어 설명은 발행사 자료, 재무제표와 위험요인은 SEC filing에서 대조. 월간 examination을 회사 전체 audit로 부르지 않는다. |
| AUD-USDC-04 | 준비금 집중·유동성·운영·depeg 위험 | [Circle 2026 Q2 results/risk factors](https://www.circle.com/pressroom/circle-reports-second-quarter-2026-results), [SEC filings](https://www.sec.gov/edgar/browse/?CIK=1876042) | 발행사 스스로 bank counterparty, fund manager/custodian, run, redemption delay, 기술·시장 위험을 공시한다. “100% backed”가 무위험을 뜻하지 않는다. |
| AUD-USDC-05 | 스마트계약·지원 네트워크 | [Circle USDC contracts](https://developers.circle.com/stablecoins/usdc-contract-addresses), [Circle blocklisting 설명](https://help.circle.com/support/en/understand-circle-s-stablecoin-blocklisting-process?id=support_article_view&sysparm_article=KB0011513) | native USDC, bridged USDC, USDC-backed token의 계약·상환 경로를 구분한다. |
| AUD-USDC-06 | GENIUS Act와 연방규칙 시행일 | [U.S. Treasury enactment statement](https://home.treasury.gov/news/press-releases/sb0197), [OCC Final Rule](https://occ.gov/news-issuances/bulletins/2026/bulletin-2026-50.html), [Federal Register final rule](https://www.occ.gov/news-issuances/federal-register/2026/91fr67000.pdf) | 법률·OCC 최종규칙은 2027-01-18 시행 예정. 다른 감독기관의 규칙 상태와 Circle의 실제 허가 상태는 별도 확인한다. |

#### 오류 위험 포인트

- “항상 1달러로 상환”을 모든 한국 개인의 Circle 직접상환권으로 일반화하는 오류.
- 발행사 주간 자체공시, 월간 examination, 연간 재무제표 audit, 예금보험을 혼동하는 오류.
- 준비금이 있다는 사실을 시장가격 고정·즉시 유동성·파산 시 완전 회수의 보장으로 바꾸는 오류.
- native USDC와 제3자 bridge/wrapped USDC를 같은 발행·상환 위험으로 보는 오류.
- 동결 권한을 거래 취소 권한과 동일시하는 오류. 온체인 송금은 되돌릴 수 없지만 특정 주소의 이후 이동·상환을 제한할 수 있다.
- GENIUS Act 제정과 2027-01-18 시행을 구분하지 않거나, Circle이 이미 새 연방 허가를 받았다고 추정하는 오류.
- 한국 거래소의 원화 가격에는 USD/KRW, 거래소 유동성·출금, 체인·브리지 위험이 추가된다는 점을 누락하는 오류.

### 3.5 Upbit 거래지원 정책

#### 최신 상태 요약

업비트는 공개 정책에서 발행주체 신뢰성, 이용자 보호, 기술·보안, 법규 준수, 토크노믹스·정보 투명성, 팀 역량·사업성을 종합 심사한다고 밝힌다. 거래지원 신청·심의는 비공개이고 최초 공개는 공지사항을 통해 이뤄진다. 유지·유의·종료는 사후 모니터링, 프로젝트 소명, 거래지원 심의위원회 의결을 거친다.

DAXA의 「가상자산 거래지원 모범사례」는 2024-07-19 시행됐고 현행 공개본은 2025-06-01 개정본이다. 이는 자율규제이며, 금융위원회가 관여하고 “공적 규제 성격이 강하다”고 표현했더라도 곧바로 법률 조문이 되지는 않는다. 가상자산이용자보호법의 예치금·보관·불공정거래·상시감시 의무와 거래지원 모범사례의 심사기준을 구분해야 한다.

| Evidence ID | 핵심 검증 주장 | 1차 자료 | 현재 판정·검토 포인트 |
|---|---|---|---|
| AUD-UPBIT-01 | 신규 거래지원 절차·평가영역 | [Upbit 거래지원 프로세스 PDF](https://static.upbit.com/guide/market_policy_open.pdf) | `ISSUER_CLAIM`이자 거래소 공개 정책. 점수·가중치·위원별 판단은 공개되지 않는다. 최종 거부 시 1년 제한 등 세부 절차는 현행 PDF 문구로 확인한다. |
| AUD-UPBIT-02 | 유의·종료 절차와 사유 | [Upbit 거래 유의종목·종료 정책 PDF](https://static.upbit.com/guide/market_policy_close.pdf), [Upbit 시장경보 안내](https://support.upbit.com/hc/ko/articles/900005994766-%EC%97%85%EB%B9%84%ED%8A%B8-%EC%8B%9C%EC%9E%A5-%EA%B2%BD%EB%B3%B4-%EC%A0%9C%EB%8F%84-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0) | 일반 정책과 개별 종목 공지를 분리한다. 종료 공지는 규제기관의 위법 확정이 아니라 거래소 결정일 수 있다. |
| AUD-UPBIT-03 | 종료 후 정리매매·출금 | [Upbit 종료 자산 안내](https://support.upbit.com/hc/ko/articles/900006049846-%EA%B1%B0%EB%9E%98-%EC%A7%80%EC%9B%90-%EC%A2%85%EB%A3%8C-%EB%94%94%EC%A7%80%ED%84%B8-%EC%9E%90%EC%82%B0%EC%9D%80-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%95%B4%EC%95%BC-%ED%95%98%EB%82%98%EC%9A%94), [종료 정책 PDF](https://static.upbit.com/guide/market_policy_close.pdf) | 정책은 공지 후 30일 정리매매와 특별한 사정이 없는 한 종료 후 30일 출금을 설명한다. 개별 공지의 실제 날짜를 우선한다. |
| AUD-UPBIT-04 | DAXA 모범사례의 최신 공개본·자율규제 성격 | [DAXA 2025-06-01 개정본](https://www.kdaxa.org/support/regulation.php?boardid=regulation&category=&idx=240&mode=view&offset=&sk=&sw=), [DAXA 2024 시행 발표](https://kdaxa.org/support/press.php?boardid=news&idx=53&mode=view) | `OFFICIAL_RECORD`인 협의체 자료. 법률·감독규정과 구분한다. |
| AUD-UPBIT-05 | 2025 개정의 상장빔·좀비코인 대응 | [금융위원회 2025-05-02 보도자료](https://www.fsc.go.kr/no010101/84478) | 2025-06-01 이후 신규 거래지원 종목 적용. 회전율·시총·커뮤니티 수치는 예시인지 확정 일률 기준인지 원문 문맥을 확인한다. |
| AUD-UPBIT-06 | 법정 의무의 범위 | [국가법령정보센터 가상자산이용자보호법](https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EA%B0%80%EC%83%81%EC%9E%90%EC%82%B0%EC%9D%B4%EC%9A%A9%EC%9E%90%EB%B3%B4%ED%98%B8%EB%93%B1%EC%97%90%EA%B4%80%ED%95%9C%EB%B2%95%EB%A5%A0) | 법률상 이용자 보호·불공정거래 의무와 거래소/DAXA의 거래지원 기준을 조문별로 분리한다. |

#### 오류 위험 포인트

- 공개된 정성 기준을 비공개 점수표·자동 상장 공식처럼 표현하는 오류.
- DAXA 자율규제를 법률 또는 금융위의 개별 상장 승인제로 표현하는 오류.
- 업비트의 거래지원 결정을 규제기관의 적법성·위법성 판단으로 바꾸는 오류.
- 2025 개정 자료의 예시 수치를 모든 종목에 적용되는 절대 cut-off로 표현하는 오류.
- 신규 심사, 정기 재평가, 유의 지정, 종료를 하나의 절차로 단순화하는 오류.
- 일반 정책보다 개별 종목 공지의 일정·사유가 우선한다는 점을 누락하는 오류.

### 3.6 토큰증권 금융기관 사업모델

#### 최신 상태 요약

한국의 토큰증권 개정법은 이미 **공포**됐지만 2027-02-04 **시행 예정**이다. 전자증권법 개정 법률 제21318호는 분산원장을 전자등록계좌부로 이용할 근거와 발행인계좌관리기관을 도입하고, 자본시장법 개정 법률 제21324호는 투자계약증권 유통 등 관련 구조를 바꾼다. 2026-10-02~11-11 예고된 하위법규안의 자기자본 40억원, 전문인력 4명, 참여기관 수, 일반투자자 연간 순매수 1억원 등은 기준일 현재 **입법예고안 수치**이지 확정 시행 규정이 아니다.

금융기관의 발행·인수·중개·신탁·계좌관리·수탁·결제 수수료는 가능한 수익 경로지만, 공개 원문만으로 실제 수요·가격·마진·손익을 입증할 수 없다. 해외 사례에서도 발행 또는 서비스 launch는 확인 가능하지만 수익성은 별도다. DTCC 서비스는 2026-10-28 상용 출시됐고 UBS·EIB의 실제 디지털 채권 발행도 존재한다. 반면 MAS는 2026-10-28 공식 연설에서 기술적 실현 가능성과 대규모 상업 채택이 같지 않다고 명시했다.

| Evidence ID | 핵심 검증 주장 | 1차 자료 | 현재 판정·검토 포인트 |
|---|---|---|---|
| AUD-STO-01 | 개정법 공포·시행일 | [전자증권법 미래 시행본](https://www.law.go.kr/lsInfoP.do?lsiSeq=283195&viewCls=lsRvsDocInfoR), [금융위 본회의 통과 설명](https://www.fsc.go.kr/no010101/86064) | 법률 제21318호, 2026-02-03 공포, 2027-02-04 시행. `LAW_PROMULGATED_NOT_EFFECTIVE`. |
| AUD-STO-02 | 자본시장법 개정과 투자계약증권 유통 | [자본시장법 개정문](https://law.go.kr/LSW/lsRvsDocListP.do?chrClsCd=010102&lsId=010513), [금융위 설명](https://www.fsc.go.kr/no010101/86064) | 법률 제21324호의 조문별 시행일을 확인한다. 법 전체의 화면상 시행일과 토큰증권 관련 조문의 시행일을 혼동하지 않는다. |
| AUD-STO-03 | 하위법규안의 범위·수치·절차 | [금융위원회 2026-10-01 입법예고](https://www.fsc.go.kr/no010101/87838) | `REGULATION_DRAFT`. 예고기간은 끝났지만 금융위 의결·법제처 심사·국무회의·공포 전에는 수치를 확정요건으로 쓰지 않는다. |
| AUD-STO-04 | 토큰증권은 증권의 기술적 형식이며 기존 증권규율 적용 | [금융위원회 2026-01-15 설명](https://www.fsc.go.kr/no010101/86064) | 무인가 중개, 공모 공시 등 기존 증권 규율이 기술 때문에 사라지지 않는다. 토큰증권을 가상자산과 동일시하지 않는다. |
| AUD-STO-05 | 상용 서비스의 실제 사례 | [DTCC 2026-10-28 launch](https://www.dtcc.com/press-releases/2026/dtcc-tokenization-service-goes-live), [UBS 2022 digital bond](https://www.ubs.com/content/news/en/2022/11/03/digital-bond/_jcr_content/root/contentarea/mainpar/toplevelgrid/col_2/linklistnewlook/actionbutton.0815280196.file/PS9jb250ZW50L2RhbS9hc3NldHMvbmV3cy8yMDIyLzExLzAzLzIwMjIxMTAzLW1yLXVicy1kaWdpdGFsIGJvbmQtZW4ucGRm/20221103-mr-ubs-digital%2520bond-en.pdf), [EIB 2021 public-chain bond](https://www.eib.org/en/press/all/2021-141-european-investment-bank-eib-issues-its-first-ever-digital-bond-on-a-public-blockchain) | 실제 발행·launch는 확인되지만 거래량·고객 유지·수익성은 별도 자료가 필요하다. |
| AUD-STO-06 | 파일럿·상용 확장의 경계 | [MAS Project Guardian](https://www.mas.gov.sg/schemes-and-initiatives/project-guardian), [MAS 2026-10-28 연설](https://www.mas.gov.sg/news/speeches/2026/the-singapore-story---attracting-capital--enabling-enterprise---sustaining-trust) | 일부 live use case가 있어도 대규모 채택을 자동 증명하지 않는다. MAS도 기술 실현과 상업 채택을 구분한다. |
| AUD-STO-07 | 효율·유동성 개선의 경험적 근거 | [HKMA 2023 연구](https://www.hkma.gov.hk/media/eng/publication-and-research/research/research-memorandums/2023/RM04-2023.pdf) | 공식 연구이나 2023년 표본·방법론·선택편향을 확인한다. 한국 사업자의 미래 손익으로 그대로 전이하지 않는다. |

#### 오류 위험 포인트

- 공포된 법률과 아직 시행되지 않은 제도를 “현행 상용 제도”로 표현하는 오류.
- 입법예고안의 40억원·4명·1억원·분산원장 참여자 요건을 확정 규정으로 표현하는 오류.
- 토큰증권을 새로운 독립 자산군 또는 규제 밖 가상자산으로 취급하는 오류.
- 발행·수탁·계좌관리·지갑보관·기초자산 신탁·현금결제를 같은 역할로 묶는 오류.
- 발행액·서비스 출시·실험 성공을 금융기관 매출·비용절감·수익성으로 바꾸는 오류.
- 해외 정부·대형 금융기관의 신용과 규제 인프라를 국내 핀테크 사업성에 그대로 일반화하는 오류.
- 정책 기대효과를 실제 고객 수요·유동성·수수료 데이터로 표현하는 오류.

## 4. 답변 표본에서 관찰된 우선 재검토 패턴

아래는 일부 상세 답변을 AI가 표본 확인한 결과이며, 120건 전체의 인간 판정이 아니다.

1. **공식 기록 접근 실패 후 2차 자료에 과도하게 의존:** CLARITY 상원 표결은 공식 Senate roll call에서 직접 확인 가능하다. 답변이 2차 자료만 썼다면 공식 기록과 숫자·표결 성격을 다시 대조한다.
2. **프로젝트 자체 주장에 `VERIFIED_FACT`를 주지 못하면서도 결론은 강함:** Chainlink 채택·Reserve·TVE는 상대방 자료 또는 온체인 대조가 없으면 `ISSUER_CLAIM`으로 유지한다.
3. **동적 수치의 시점·정의 누락:** LINK 공급·Reserve·staking, USDC 준비금·유통량, Ethereum 활동·집중도는 캡처 시각과 방법론이 없으면 재현 불가다.
4. **원문 요약만 확인하고 조문 또는 첨부 PDF를 읽지 않음:** Upbit/DAXA 정책과 한국 토큰증권 법령은 요약 페이지가 아니라 정책 PDF·개정문·부칙을 확인한다.
5. **파일럿/제한 생산/상용 launch 혼합:** DTCC는 2026-07 제한 생산과 2026-10 launch를 구분해야 한다. Swift 실험과 UBS/EIB 실제 발행도 같은 등급이 아니다.
6. **검증수준 혼합:** Circle 주간 자체공시, 월간 examination, SEC 재무제표, 예금보험은 네 개의 다른 층이다.

## 5. 기타 인간 검토 대기 항목

### Phase 8 네 사례

`docs/PHASE_8_HUMAN_REVIEW.md`의 CLARITY·Chainlink·Ethereum·USDC A/B 답변에도 이 문서의 AUD Evidence를 재사용할 수 있다. 특히 다음 기존 항목은 아직 사람이 직접 판단해야 한다.

- CLARITY: 상원 공식 표결과 버전 관계, 한국의 현행·미시행·정책 구분.
- Chainlink: 상대방 기관이 확인한 실제 운영 범위, LINK 수요로 이어지는 공개 경로와 비공개 단위경제성.
- Ethereum: finality·L1/L2·집중도 방법론, 계획 업그레이드와 구현 기능 구분.
- USDC: 일반 한국 보유자의 직접상환 가능성, examination/audit/보험 구분, 체인·브리지·동결·환율 위험.

기존 모델 보조점수는 인간 점수가 아니며 그대로 유지한다.

### EIB·홍콩 디지털채권 사례

`docs/HUMAN_REVIEW_GUIDE.md`와 `docs/RESEARCH_QUALITY_AUDIT.md`가 요구한 다음 항목은 여전히 미완료다.

- EIB 2023 파운드 디지털채권의 룩셈부르크 직접 법적 근거와 거래별 법률의견.
- EIB private legal record와 public mirror 각각의 법적·운영적 효과.
- 홍콩 2024 다중통화 디지털 녹색채권의 개별 적용 법령·면제·법률의견.
- SFC 일반 circular를 개별 채권 승인 문서처럼 사용하지 않았는지.
- 두 사례의 비용·처리시간·유동성·수요·수익성, 외국환·세무·회계, 장애복구·원장 불일치 책임.

검토자는 기존 Evidence ID와 원문의 페이지·문단을 `docs/ANALYST_REVIEW.md` 사본에 직접 기록해야 한다. 이 AI 보조 문서가 작성자·날짜·의견을 대신 채우지 않는다.

## 6. 사람 검토자가 남겨야 할 최소 기록

각 답변마다 다음만은 직접 기록한다.

- blind ID
- 답변 기준일과 실제 검토일
- 핵심 주장 3~7개와 각 주장에 사용한 AUD Evidence 또는 추가 공식 URL
- 원문 위치(조문·페이지·문단)와 문서 버전
- 판정: `확인`, `제한부 확인`, `미해결`, `모순`
- 치명적 오류 여부와 이유
- 답변 후 공개된 자료 때문에 필요한 업데이트인지, 생성 당시에도 틀린 주장인지
- 반대 근거와 남은 불확실성

최종 승인·조건부 승인·재실험·반려는 120개 검토 완료 뒤 사용자가 직접 결정한다. 이 문서 작성으로 `reviews.json`이나 인간 검토 상태를 변경하지 않았다.
