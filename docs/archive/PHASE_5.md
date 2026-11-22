# Phase 5 — Quality Hardening & Real-world Research Validation

기준일: 2026-11-16

## 완료 범위

### Evidence Verification

- HTML·텍스트·PDF 원문 추출
- 응답 코드, 콘텐츠 유형, 최종 URL, 조회시각 기록
- 문서·정규화 추출문 SHA-256 기록
- `relevant_excerpt` 원문 포함 여부 대조
- `URL_REACHABLE`, `CONTENT_VERIFIED`, `CONTENT_MISMATCH`, `ACCESS_RESTRICTED`, `MANUAL_REVIEW_REQUIRED` 구분
- Evidence v1→v2 마이그레이션. 마이그레이션만으로 검증 완료 처리하지 않음
- 수동 첨부 지원 및 진위 미확인 경고
- 외부 문서의 지시문 탐지·비실행

### Regulatory Validation

- 정규화된 `claim_type`과 Evidence `legal_status` 호환성 검사
- `analysis_date` 기준 시행 전·시행 중 판정
- 조문·부칙·경과규정용 `provisions`와 `provision_refs`
- 관할권 혼동, 365일 초과 상태 확인, 사용자 제공 법률 주장의 공식 근거 부재 차단
- `VERIFIED_FACT`에 `CONTENT_VERIFIED` 원문 요구

### Independent Research

홍콩 정부의 2024년 다중통화 디지털 녹색채권을 새 사례로 조사했다. HKMA 거래 발표, 홍콩 SFC PDF 지침, 2026년 HKMA 정책 발표와 한국 공식 자료를 독립적으로 조회했다. 국문 보고서, 영문 요약, Evidence v2, research log를 생성했다.

## 자동화하지 않은 판단

- 인용문의 법률적 해석과 전체 문맥
- 계약·법률의견서 비공개 내용
- 개별 사업의 인가·세무·회계·외국환 적법성
- 스캔 PDF OCR 및 복잡한 표·각주 의미
- 실제 비용 절감·수요·수익성

이 항목은 완료로 주장하지 않고 보고서 한계와 `NEEDS_REVIEW`로 남긴다.

