# K-DARI — Korean Digital Asset Research Intelligence

K-DARI is an Agent Skill that routes natural-language digital-asset questions to evidence-led research frameworks. It covers law and policy, coins and projects, networks, whitepapers, stablecoins, tokenised assets, exchange policies and business models. Korean context is added only when materially relevant.

It is not legal, tax, accounting or investment advice.

## Quick start

```bash
npx skills add junjunny/k-digital-asset-research-intelligence@k-digital-asset-research-intelligence
```

Then ask a supported agent a natural-language question. If the agent does not select the skill automatically, invoke its current identifier explicitly:

```text
Use $k-digital-asset-research-intelligence to explain the current status of the CLARITY Act using official sources.
```

Repository discovery and isolated Codex and Claude Code installation were checked with Skills CLI 1.9.0 on 21 November 2026. Installation does not by itself prove automatic activation. See the [current project status](docs/PROJECT_STATUS_2026-11.md) for separately reported verification states.

Existing users of `k-digital-asset-policy-intelligence` should follow the [K-DAPI to K-DARI migration guide](docs/MIGRATION_KDAPI_TO_KDARI.md) to avoid duplicate installations.

## What it does

- Routes 12 question types and requests missing identifiers
- Selects `QUICK`, `STANDARD`, or `DEEP_RESEARCH` depth
- Separates enacted law, future-effective law, draft rules, policy announcements and guidance
- Links major claims to Evidence IDs and verification states
- Compares HTML, text and PDF excerpts and records hashes
- Avoids forcing unrelated questions into a Korean regulatory comparison
- Replaces buy/sell conclusions with structure and risk checks

Example questions:

```text
Evaluate Ethereum as a network, including consensus, decentralisation, actual use and operational risks.
```

```text
How does USDC maintain its price, and what are its reserve, redemption and depegging risks?
```

See the [general user guide](docs/GENERAL_USER_GUIDE.md), [question routing](docs/QUESTION_ROUTING.md), and [evidence policy](references/evidence-policy.md).

## Validation limits

`CONTENT_VERIFIED` means that the fetched source and stored excerpt matched. It does not prove the full legal meaning, issuer claims, business legality or investment safety. The EIB and Hong Kong case studies remain research drafts pending relevant expert review.

Do not upload company-confidential material, personal data, private contracts, or API keys to an external AI service or a public repository. Follow your organisation's approved environment and data policy.

## Research status

Phase 9 generated all 120 Claude-cohort answers and completed a separate AI-assisted pre-review. Human blind review and relevant expert review remain pending. AI-assisted scores are not human approval, and no condition-level conclusion should be drawn before the review gate is completed.

## Local checks

```bash
python3 -m pip install -r requirements.txt
python3 scripts/route_question.py "What are tokenised securities?"
python3 scripts/validate_sources.py examples/tokenization-case-study/evidence.json
python3 scripts/validate_report.py examples/tokenization-case-study/report.json
python3 -m unittest discover -s tests -v
npx skills add . --list
```

Python 3.9 or later is required. PDF extraction uses `pypdf`.

## Licence

MIT. Historical experiment artifacts retain the earlier K-DAPI name and identifier for reproducibility.
