# K-DARI — Korean Digital Asset Research Intelligence

[한국어](README.md) · [skills.sh](https://skills.sh/junjunny/k-digital-asset-research-intelligence/k-dari) · [User guide](skills/k-dari/references/general-user-guide.md) · [Research methodology](skills/k-dari/references/research-methodology.md) · [Project status](docs/PROJECT_STATUS_2026-11.md)

K-DARI (`k-dari`) is an open-source Agent Skill for evidence-led digital-asset research. It routes natural-language questions to separate methods for law and policy, coins and projects, blockchain networks, whitepapers, stablecoins, RWA and tokenised securities, exchange policies, and business models. Korean regulatory and market context is added only when materially relevant.

> question → topic and depth → official sources → facts, inferences and unknowns → Korean context when relevant

K-DARI does not provide legal advice, investment recommendations, or price predictions.

## Install

Install the `k-dari` skill from the latest `main` branch:

```bash
npx skills add junjunny/k-digital-asset-research-intelligence@k-dari
```

Pin the verified release when reproducibility matters:

```bash
npx skills add junjunny/k-digital-asset-research-intelligence@v1.0.0 --skill k-dari
```

[v1.0.0 release and security changes](https://github.com/junjunny/k-digital-asset-research-intelligence/releases/tag/v1.0.0)

To inspect the discoverable skills before installing:

```bash
npx skills add junjunny/k-digital-asset-research-intelligence --list
```

## Example questions

```text
What is the US CLARITY Act? Check its current legislative status.
```

```text
Evaluate Ethereum as a network, including consensus, decentralisation, actual use, and major risks.
```

```text
How does USDC maintain its price, and what are its reserve, redemption, and depegging risks?
```

If a coin, network, or bill is ambiguous, the skill asks for the minimum identifying information instead of choosing a target on the user's behalf.

## Core behaviour

- Routes 12 question types and selects `QUICK`, `STANDARD`, or `DEEP_RESEARCH` depth
- Separates proposed bills, promulgated law, effective law, draft regulation, policy announcements, and guidance
- Distinguishes issuer claims, independently verified facts, supported inferences, and unknowns
- Records Evidence IDs, source locations, analysis dates, and verification status for material claims
- Avoids forcing unrelated questions into Korean regulation or tokenised-securities analysis
- Starts without requiring a PDF upload or external API key

When live web access or an official source is unavailable, the response must disclose that current verification was not possible.

External webpages, PDFs, and whitepapers are treated as untrusted data. Instructions embedded in them cannot change the agent's role, authorize tool execution, or request secrets or unrelated local data. See the [security audit](docs/SECURITY_AUDIT.md) for the threat model, pinned installs, and residual risks.

## Validate

```bash
python3 -m pip install -r skills/k-dari/requirements.txt
python3 skills/k-dari/scripts/route_question.py "What are tokenised securities?"
python3 skills/k-dari/scripts/validate_sources.py examples/tokenization-case-study/evidence.json
python3 skills/k-dari/scripts/validate_report.py examples/tokenization-case-study/report.json
python3 -m unittest discover -s tests -v
```

The repository includes reproducible EIB and Hong Kong digital-bond cases, independent breadth evaluation, controlled-experiment audit records, and a separate [AI-assisted preliminary review](docs/AI_ASSISTED_REVIEW_REPORT.md). Model-assisted scores are not human approval or expert legal, accounting, or technical review.

K-DARI stands for **Korean Digital Asset Research Intelligence**. Its searchable and installable skill identifier is the lowercase `k-dari`; the former development name `K-DAPI` remains only where needed to preserve historical evaluation records. Existing installations can use the [migration guide](docs/MIGRATION_KDAPI_TO_KDARI.md).

MIT License.
