# Phase 2 — Evidence & Regulatory Engine

## 구현

- `evidence`, `finding`, `report` JSON Schema
- 표준 라이브러리 기반 `validate_sources.py`, `validate_report.py`
- 선택형 live URL check
- 법적 상태: 현행, 공포 후 시행 전, 법안, 의결 후 미공포, 입법예고, 정책 발표, 지침, 폐지
- 주장 등급: 사실, 근거 있는 추론, 미검증, 검토 필요

## 검출 대상

- 필수 메타데이터·날짜·URL 누락
- 중복 Evidence ID와 존재하지 않는 참조
- 미래 시행일을 현행으로 표시
- 정책 자료만으로 “현행법” 주장
- 입법예고로 확정·시행 중인 의무를 주장

자동 검증은 원문의 법적 해석이나 인용문 의미까지 보증하지 않는다. 이는 수동 검토 영역이다.

