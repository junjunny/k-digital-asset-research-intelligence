import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "k-dari" / "scripts"))

from route_question import QUESTION_TYPES, RESPONSE_MODES, classify_question  # noqa: E402


class QuestionRouterTests(unittest.TestCase):
    def route(self, question):
        result = classify_question(question)
        self.assertIn(result["primary_type"], QUESTION_TYPES)
        self.assertIn(result["response_mode"], RESPONSE_MODES)
        return result

    def test_clarity_act_is_law_not_token_security(self):
        result = self.route("CLARITY Act가 뭐야?")
        self.assertEqual("LAW_AND_REGULATION", result["primary_type"])
        self.assertEqual("QUICK", result["response_mode"])
        self.assertNotIn("TOKENIZED_ASSET_OR_RWA", result["secondary_types"])
        self.assertTrue(result["requires_current_web_verification"])

    def test_korean_regulatory_comparison(self):
        result = self.route("한국 규제와 비교해 줘.")
        self.assertEqual("REGULATORY_COMPARISON", result["primary_type"])
        self.assertTrue(result["include_korean_context"])
        self.assertTrue(result["needs_clarification"])

    def test_token_security_simple_question_is_quick_concept(self):
        result = self.route("토큰증권이 뭐야?")
        self.assertEqual("CONCEPT_EXPLANATION", result["primary_type"])
        self.assertIn("TOKENIZED_ASSET_OR_RWA", result["secondary_types"])
        self.assertEqual("QUICK", result["response_mode"])

    def test_ethereum_network_is_not_coin_review(self):
        result = self.route("이더리움 네트워크 평가해 줘.")
        self.assertEqual("NETWORK_OR_PROTOCOL_REVIEW", result["primary_type"])
        self.assertFalse(result["include_korean_context"])

    def test_usdc_routes_to_stablecoin(self):
        result = self.route("USDC는 어떻게 가격을 유지해?")
        self.assertEqual("STABLECOIN_REVIEW", result["primary_type"])

    def test_whitepaper_keeps_framework_and_requests_source(self):
        result = self.route("이 프로젝트 백서 검토해 줘.")
        self.assertEqual("WHITEPAPER_REVIEW", result["primary_type"])
        self.assertTrue(result["needs_clarification"])
        self.assertIn("공식 URL", result["clarification_question"])

    def test_named_project_whitepaper_does_not_reask_identity(self):
        result = self.route("솔라나 백서 검토해 줘.")
        self.assertEqual("WHITEPAPER_REVIEW", result["primary_type"])
        self.assertFalse(result["needs_clarification"])

    def test_unspecified_coin_is_ambiguous(self):
        result = self.route("이 코인 어떤 거야?")
        self.assertEqual("AMBIGUOUS_REQUEST", result["primary_type"])
        self.assertTrue(result["needs_clarification"])
        self.assertIn("티커", result["clarification_question"])

    def test_investment_request_redirects_without_advice(self):
        result = self.route("이 코인 사도 돼?")
        self.assertEqual("INVESTMENT_OR_PRICE_REQUEST", result["primary_type"])
        self.assertTrue(result["investment_safety_redirect"])
        self.assertTrue(result["needs_clarification"])

    def test_investment_risk_review_still_requires_current_sources(self):
        result = self.route("BTC 지금 사도 돼?")
        self.assertEqual("INVESTMENT_OR_PRICE_REQUEST", result["primary_type"])
        self.assertTrue(result["requires_current_web_verification"])

    def test_unspecified_network_is_ambiguous(self):
        result = self.route("이 네트워크 괜찮아?")
        self.assertEqual("AMBIGUOUS_REQUEST", result["primary_type"])
        self.assertIn("네트워크", result["clarification_question"])

    def test_explicit_ticker_prevents_arbitrary_asset_selection(self):
        result = self.route("이 코인 SOL 어떤 거야?")
        self.assertEqual("COIN_OR_PROJECT_REVIEW", result["primary_type"])
        self.assertFalse(result["needs_clarification"])

    def test_exchange_policy_is_distinct_from_regulation(self):
        result = self.route("업비트가 이 코인의 거래지원을 종료한 이유가 뭐야?")
        self.assertEqual("EXCHANGE_SUPPORT_POLICY", result["primary_type"])
        self.assertTrue(result["include_korean_context"])

    def test_exchange_name_does_not_override_network_intent(self):
        result = self.route("업비트에서 거래되는 솔라나의 네트워크를 평가해 줘.")
        self.assertEqual("NETWORK_OR_PROTOCOL_REVIEW", result["primary_type"])

    def test_stablecoin_law_question_routes_to_law_with_secondary(self):
        result = self.route("USDC 관련 미국 법률을 설명해 줘.")
        self.assertEqual("LAW_AND_REGULATION", result["primary_type"])
        self.assertIn("STABLECOIN_REVIEW", result["secondary_types"])

    def test_korean_transliteration_of_clarity_routes_to_law(self):
        result = self.route("클래리티법 알려줘.")
        self.assertEqual("LAW_AND_REGULATION", result["primary_type"])

    def test_country_context_does_not_turn_network_comparison_into_regulation(self):
        result = self.route("한국에서 이더리움과 솔라나의 차이는 뭐야?")
        self.assertEqual("NETWORK_OR_PROTOCOL_REVIEW", result["primary_type"])
        self.assertTrue(result["include_korean_context"])

    def test_holdout_stablecoin_legislation_variant(self):
        result = self.route("미국 스테이블 코인 규제법을 핵심만 설명해줘")
        self.assertEqual("LAW_AND_REGULATION", result["primary_type"])

    def test_holdout_clarity_transliteration_variant(self):
        result = self.route("미국 클래러티 법안 핵심 알려줘")
        self.assertEqual("LAW_AND_REGULATION", result["primary_type"])

    def test_holdout_exchange_and_network_shorthand(self):
        result = self.route("업비트 솔라나 네트워크 장단점")
        self.assertEqual("NETWORK_OR_PROTOCOL_REVIEW", result["primary_type"])

    def test_korean_token_security_feasibility_keeps_law_secondary(self):
        result = self.route("한국에서 토큰증권 지금 발행할 수 있어?")
        self.assertEqual("TOKENIZED_ASSET_OR_RWA", result["primary_type"])
        self.assertIn("LAW_AND_REGULATION", result["secondary_types"])

    def test_simple_question_does_not_force_deep_report(self):
        result = self.route("토큰증권이 뭐야?")
        self.assertNotEqual("DEEP_RESEARCH", result["response_mode"])

    def test_deep_request_selects_deep_mode(self):
        result = self.route("이더리움 네트워크를 심층 보고서로 평가해 줘.")
        self.assertEqual("NETWORK_OR_PROTOCOL_REVIEW", result["primary_type"])
        self.assertEqual("DEEP_RESEARCH", result["response_mode"])

    def test_foreign_network_does_not_force_korean_context(self):
        result = self.route("솔라나 네트워크의 장단점을 평가해 줘.")
        self.assertFalse(result["include_korean_context"])

    def test_korean_business_question_includes_context(self):
        result = self.route("이 디지털자산 사업모델을 한국에서 할 수 있을까?")
        self.assertEqual("BUSINESS_MODEL_REVIEW", result["primary_type"])
        self.assertTrue(result["include_korean_context"])

    def test_empty_question_fails(self):
        with self.assertRaises(ValueError):
            classify_question("   ")


if __name__ == "__main__":
    unittest.main()
