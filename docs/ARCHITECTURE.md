# Architecture

```text
Natural-language question
              ↓
 skills/k-dari/scripts/route_question.py
      + skills/k-dari/SKILL.md
  type + depth + clarification
  + Korean-context decision
              ↓
 type framework + official sources
              ↓
  Evidence records → Findings → Report
              ↓           ↓         ↓
 validate_sources   cross-links   KO report + EN summary
              └──── validate_report ────┘
```

규칙 기반 라우터는 연구 방법론을 선택할 뿐 답변이나 사실을 생성하지 않는다. 에이전트의 의미 판단, 공식자료 리서치, 결정적인 구조 검증을 분리한다. 스키마는 교환 계약이고 Python 스크립트는 외부 패키지 없이 핵심 불변조건을 검사한다. URL live check는 네트워크 제한과 공식 사이트의 자동 접근 차단 때문에 선택 기능이다.

