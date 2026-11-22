#!/usr/bin/env python3
"""Deterministically route a Korean or English digital-asset question.

This module selects a research framework and response depth. It does not fetch
sources, identify an unspecified asset, or produce investment advice.
"""

import argparse
import json
import re
import unicodedata


QUESTION_TYPES = (
    "CONCEPT_EXPLANATION",
    "LAW_AND_REGULATION",
    "REGULATORY_COMPARISON",
    "COIN_OR_PROJECT_REVIEW",
    "NETWORK_OR_PROTOCOL_REVIEW",
    "WHITEPAPER_REVIEW",
    "STABLECOIN_REVIEW",
    "TOKENIZED_ASSET_OR_RWA",
    "EXCHANGE_SUPPORT_POLICY",
    "BUSINESS_MODEL_REVIEW",
    "INVESTMENT_OR_PRICE_REQUEST",
    "AMBIGUOUS_REQUEST",
)

RESPONSE_MODES = ("QUICK", "STANDARD", "DEEP_RESEARCH")

INVESTMENT_TERMS = (
    "사도 돼", "사도돼", "매수", "매도", "팔아야", "투자해도", "투자할까",
    "가격 오를", "가격이 오를", "수익률", "매수 타이밍", "투자 추천",
    "should i buy", "should i sell", "price prediction", "buy now",
)
COMPARISON_TERMS = ("비교", "차이", "versus", " vs ", "compare")
LAW_TERMS = (
    "법안", "법률", "규제", "정책", "시행령", "감독규정", "입법예고", "의회",
    "법적", "regulation", "regulatory", "legislation", "congress", " act", "act ",
)
LAW_NAME_TERMS = ("clarity", "클래리티", "클래러티")
WHITEPAPER_TERMS = ("백서", "whitepaper", "white paper")
STABLECOIN_TERMS = (
    "스테이블코인", "stablecoin", "usdc", "usdt", "테더", "dai", "pyusd", "usde",
    "디페깅", "depeg",
)
TOKENIZED_ASSET_TERMS = (
    "토큰증권", "토큰 증권", "token security", "tokenized secur", "토큰화 증권",
    "rwa", "실물연계자산", "실물 자산 토큰", "조각투자",
)
EXCHANGE_TERMS = (
    "거래지원", "상장폐지", "상장 폐지", "유의종목", "유의 종목", "상장 심사",
    "listing policy", "delisting", "업비트", "빗썸", "코인원", "코빗",
)
NETWORK_TERMS = (
    "네트워크", "프로토콜", "메인넷", "합의 방식", "검증자", "노드", "레이어1",
    "레이어 1", "layer 1", "layer1", "blockchain network", "protocol",
)
KNOWN_NETWORKS = (
    "이더리움", "ethereum", "비트코인", "bitcoin", "솔라나", "solana", "아발란체",
    "avalanche", "폴리곤", "polygon", "수이", "sui", "앱토스", "aptos", "코스모스",
    "cosmos", "폴카닷", "polkadot",
)
BUSINESS_TERMS = (
    "사업모델", "비즈니스 모델", "수익모델", "수익 모델", "사업 가능", "사업성",
    "시장 진입", "business model", "go-to-market", "fintech", "핀테크",
)
PROJECT_TERMS = (
    "코인", "토큰", "프로젝트", "재단", "토크노믹스", "에어드롭", "coin", "token",
    "project", "tokenomics",
)
KOREAN_CONTEXT_TERMS = (
    "한국", "국내", "원화", "대한민국", "금융위원회", "금감원", "국회", "한국은행",
    "업비트", "빗썸", "코인원", "코빗", "korea", "korean",
)
LEGAL_FEASIBILITY_TERMS = (
    "지금 발행", "발행할 수", "가능해", "가능한가", "허용", "적법", "불법",
    "can issue", "legally", "permitted",
)
DEEP_TERMS = (
    "심층", "심도 있게", "상세 보고서", "종합 보고서", "리서치 보고서", "보고서로",
    "deep research", "in-depth report", "comprehensive report",
)
QUICK_TERMS = (
    "뭐야", "무엇이야", "알려줘", "쉽게", "간단히", "한눈에", "요약해",
    "what is", "explain simply", "briefly",
)


def normalize_question(question):
    return " ".join(unicodedata.normalize("NFKC", question).casefold().split())


def contains_any(text, terms):
    return any(term in text for term in terms)


def has_law_intent(text):
    return contains_any(text, LAW_TERMS) or (
        contains_any(text, LAW_NAME_TERMS) and any(term in text for term in ("법", "act"))
    )


def has_explicit_identifier(original, normalized=None):
    text = normalized if normalized is not None else normalize_question(original)
    if re.search(r"https?://", text):
        return True
    if contains_any(text, KNOWN_NETWORKS + STABLECOIN_TERMS):
        return True
    # Preserve upper-case ticker information from the original question.
    if re.search(r"(?<![A-Za-z])[A-Z][A-Z0-9]{1,9}(?![A-Za-z])", original):
        return True
    return False


def ambiguous_subject(text, original=None):
    patterns = (
        r"(?:^|\s)이\s*코인(?:\s|$)",
        r"(?:^|\s)이\s*네트워크(?:\s|$)",
        r"(?:^|\s)이\s*법안(?:\s|$)",
        r"(?:^|\s)이\s*프로젝트(?:\s|$)",
        r"(?:^|\s)이\s*토큰(?:\s|$)",
    )
    return any(re.search(pattern, text) for pattern in patterns) and not has_explicit_identifier(original or text, text)


def clarification_for(text, original, primary_type):
    if primary_type == "WHITEPAPER_REVIEW" and not (
        re.search(r"https?://|첨부|파일", text) or has_explicit_identifier(original, text)
    ):
        return "검토할 백서 파일이나 공식 URL, 프로젝트명을 알려주세요."
    if primary_type == "REGULATORY_COMPARISON" and not any(
        term in text for term in ("미국", "유럽", "eu", "영국", "일본", "싱가포르", "홍콩", "clarity", "mica")
    ):
        return "한국 규제와 비교할 해외 법률·정책 또는 관할권을 알려주세요."
    if primary_type == "INVESTMENT_OR_PRICE_REQUEST" and ambiguous_subject(text, original):
        return "검토할 코인의 이름이나 티커와 사용 네트워크를 알려주세요."
    if ambiguous_subject(text, original):
        if "법안" in text:
            return "법안의 정확한 이름과 국가 또는 관할권을 알려주세요."
        if "네트워크" in text:
            return "평가할 네트워크나 프로토콜의 정확한 이름을 알려주세요."
        return "코인 또는 프로젝트 이름, 티커, 사용 네트워크 중 확인 가능한 정보를 알려주세요."
    return None


def choose_response_mode(text, primary_type):
    if contains_any(text, DEEP_TERMS):
        return "DEEP_RESEARCH"
    if contains_any(text, QUICK_TERMS) and primary_type in {
        "CONCEPT_EXPLANATION", "LAW_AND_REGULATION", "TOKENIZED_ASSET_OR_RWA"
    }:
        return "QUICK"
    return "STANDARD"


def classify_question(question):
    if not isinstance(question, str) or not question.strip():
        raise ValueError("question must be a non-empty string")
    original = unicodedata.normalize("NFKC", question).strip()
    text = normalize_question(original)
    secondary = []
    reasons = []

    if contains_any(text, INVESTMENT_TERMS):
        primary = "INVESTMENT_OR_PRICE_REQUEST"
        reasons.append("매수·매도·가격·수익 요청을 감지함")
    elif contains_any(text, COMPARISON_TERMS) and has_law_intent(text):
        primary = "REGULATORY_COMPARISON"
        reasons.append("법률·규제·정책의 관할권 비교 요청을 감지함")
    elif contains_any(text, WHITEPAPER_TERMS):
        primary = "WHITEPAPER_REVIEW"
        reasons.append("백서 검토 요청을 감지함")
    elif has_law_intent(text):
        primary = "LAW_AND_REGULATION"
        if contains_any(text, STABLECOIN_TERMS):
            secondary.append("STABLECOIN_REVIEW")
        if contains_any(text, TOKENIZED_ASSET_TERMS):
            secondary.append("TOKENIZED_ASSET_OR_RWA")
        reasons.append("법률·법안·규제·정책 질문을 감지함")
    elif contains_any(text, STABLECOIN_TERMS):
        primary = "STABLECOIN_REVIEW"
        reasons.append("스테이블코인 또는 가격 안정 메커니즘 대상을 식별함")
    elif (
        contains_any(text, NETWORK_TERMS) or (
            contains_any(text, KNOWN_NETWORKS) and any(
                term in text for term in ("평가", "장단점", "합의", "노드", "네트워크", "차이", "비교")
            )
        )
    ) and not ambiguous_subject(text, original):
        primary = "NETWORK_OR_PROTOCOL_REVIEW"
        reasons.append("블록체인 네트워크 또는 프로토콜 평가 요청을 감지함")
    elif contains_any(text, EXCHANGE_TERMS):
        primary = "EXCHANGE_SUPPORT_POLICY"
        reasons.append("거래소 거래지원·유의·종료 정책 질문을 감지함")
    elif ambiguous_subject(text, original):
        primary = "AMBIGUOUS_REQUEST"
        reasons.append("분석 대상의 고유 이름·티커·관할권이 없음")
    elif contains_any(text, TOKENIZED_ASSET_TERMS):
        if contains_any(text, QUICK_TERMS):
            primary = "CONCEPT_EXPLANATION"
            secondary.append("TOKENIZED_ASSET_OR_RWA")
            reasons.append("토큰증권·RWA에 대한 간단한 개념 설명 요청을 감지함")
        else:
            primary = "TOKENIZED_ASSET_OR_RWA"
            if contains_any(text, KOREAN_CONTEXT_TERMS) and contains_any(text, LEGAL_FEASIBILITY_TERMS):
                secondary.append("LAW_AND_REGULATION")
            reasons.append("토큰증권·RWA 구조 분석 요청을 감지함")
    elif contains_any(text, BUSINESS_TERMS):
        primary = "BUSINESS_MODEL_REVIEW"
        reasons.append("사업모델·수익구조·시장진입 질문을 감지함")
    elif contains_any(text, PROJECT_TERMS):
        primary = "COIN_OR_PROJECT_REVIEW"
        reasons.append("코인·토큰·프로젝트 평가 요청을 감지함")
    elif contains_any(text, QUICK_TERMS):
        primary = "CONCEPT_EXPLANATION"
        reasons.append("간단한 개념 설명 요청을 감지함")
    else:
        primary = "AMBIGUOUS_REQUEST"
        reasons.append("지원 유형과 분석 대상을 확정할 정보가 부족함")

    clarification = clarification_for(text, original, primary)
    if primary == "AMBIGUOUS_REQUEST" and clarification is None:
        clarification = "분석할 디지털자산 주제와 원하는 결과를 조금 더 구체적으로 알려주세요."
    include_korean_context = contains_any(text, KOREAN_CONTEXT_TERMS)
    response_mode = choose_response_mode(text, primary)
    requires_web = primary != "AMBIGUOUS_REQUEST"

    return {
        "question": original,
        "primary_type": primary,
        "secondary_types": secondary,
        "response_mode": response_mode,
        "needs_clarification": clarification is not None,
        "clarification_question": clarification,
        "include_korean_context": include_korean_context,
        "requires_current_web_verification": requires_web,
        "investment_safety_redirect": primary == "INVESTMENT_OR_PRICE_REQUEST",
        "can_start_without_pdf_or_api_key": primary != "AMBIGUOUS_REQUEST",
        "reasons": reasons,
    }


def main():
    parser = argparse.ArgumentParser(description="Route a natural-language K-DARI question")
    parser.add_argument("question", nargs="+", help="natural-language question")
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    args = parser.parse_args()
    result = classify_question(" ".join(args.question))
    print(json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
