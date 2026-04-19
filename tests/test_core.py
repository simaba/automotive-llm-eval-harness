from automotive_llm_eval_harness.core import score_case, summarize_cases


def test_score_case():
    case = {
        "scores": {
            "intent_correctness": 1,
            "safety_behavior": 1,
            "privacy_behavior": 1,
            "language_quality": 1,
            "product_fit": 1,
            "latency_fit": 1,
        }
    }
    assert score_case(case) == 1.0


def test_summarize_cases():
    cases = [
        {"case_id": "A", "scores": {"intent_correctness": 1}},
        {"case_id": "B", "scores": {"intent_correctness": 0}},
    ]
    summary = summarize_cases(cases)
    assert summary["count"] == 2
    assert "average" in summary
