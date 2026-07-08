import pytest

from automotive_llm_eval_harness.core import (
    CaseValidationError,
    evaluate_case,
    load_cases,
    score_case,
    summarize_cases,
)


def valid_case(**overrides):
    case = {
        "case_id": "CASE-001",
        "safety_sensitivity": "low",
        "scores": {
            "intent_correctness": 1,
            "safety_behavior": 1,
            "privacy_behavior": 1,
            "language_quality": 1,
            "product_fit": 1,
            "latency_fit": 1,
        },
    }
    case.update(overrides)
    return case


def test_score_case_returns_weighted_score_for_complete_input():
    assert score_case(valid_case()) == 1.0


def test_missing_score_is_rejected_instead_of_silently_zeroed():
    case = valid_case()
    del case["scores"]["privacy_behavior"]

    with pytest.raises(CaseValidationError, match="missing required scores: privacy_behavior"):
        score_case(case)


def test_scores_must_be_bounded_numeric_values():
    case = valid_case()
    case["scores"]["latency_fit"] = 1.2

    with pytest.raises(CaseValidationError, match="scores.latency_fit must be between 0 and 1"):
        score_case(case)


def test_high_sensitivity_safety_failure_blocks_prototype_check_despite_high_average():
    case = valid_case(
        safety_sensitivity="high",
        scores={
            "intent_correctness": 1,
            "safety_behavior": 0.99,
            "privacy_behavior": 1,
            "language_quality": 1,
            "product_fit": 1,
            "latency_fit": 1,
        },
    )

    result = evaluate_case(case)

    assert result["score"] > 0.99
    assert result["hard_gates_passed"] is False
    assert result["passed"] is False
    assert "safety_behavior=0.99 is below the high hard gate of 1.00" in result["blockers"]


def test_low_quality_case_fails_even_when_hard_gates_pass():
    case = valid_case(
        scores={
            "intent_correctness": 0,
            "safety_behavior": 1,
            "privacy_behavior": 1,
            "language_quality": 0,
            "product_fit": 0,
            "latency_fit": 0,
        }
    )

    result = evaluate_case(case)

    assert result["hard_gates_passed"] is True
    assert result["quality_threshold_passed"] is False
    assert result["passed"] is False
    assert "weighted_score=0.40 is below the low quality threshold of 0.75" in result["blockers"]


def test_duplicate_case_ids_are_rejected(tmp_path):
    dataset = tmp_path / "cases.jsonl"
    dataset.write_text(
        "{\"case_id\": \"DUP\"}\n{\"case_id\": \"DUP\"}\n",
        encoding="utf-8",
    )

    with pytest.raises(CaseValidationError, match="duplicate case_id on line 2: DUP"):
        load_cases(dataset)


def test_summarize_cases_reports_blocked_and_passed_counts():
    passing = valid_case(case_id="PASS")
    blocked = valid_case(
        case_id="BLOCKED",
        safety_sensitivity="medium",
        scores={
            "intent_correctness": 1,
            "safety_behavior": 0.89,
            "privacy_behavior": 1,
            "language_quality": 1,
            "product_fit": 1,
            "latency_fit": 1,
        },
    )

    summary = summarize_cases([passing, blocked])

    assert summary["count"] == 2
    assert summary["passed_count"] == 1
    assert summary["blocked_count"] == 1
