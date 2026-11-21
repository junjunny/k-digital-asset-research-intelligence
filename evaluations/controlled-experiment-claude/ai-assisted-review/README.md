# AI 보조 사전검토 데이터

이 폴더는 120개 블라인드 답변을 공식 원문과 대조한 **AI 보조 사전검토**만 저장한다.

- `reviews.json`: R001~R120의 점수, 핵심 주장 검증 수, 공식 근거 URL, 오류·누락 메모
- 상태는 모두 `NEEDS_HUMAN_VERIFICATION`이다.
- `human-review/reviews.json`과 revision history에는 어떠한 값도 복사하지 않는다.
- 이 결과는 인간 평가·전문가 검토·승인·서명 또는 실제 검토일을 대신하지 않는다.
- 실험 조건은 노출하지 않고 blind ID를 유지한다.

재생성:

```bash
python3 scripts/build_ai_assisted_review.py
```
