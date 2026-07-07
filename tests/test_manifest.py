from __future__ import annotations

import pytest

from automotive_llm_eval_harness.manifest import (
    RunManifestError,
    reproducibility_record,
    validate_run_manifest,
)


def valid_manifest() -> dict:
    return {
        "dataset_id": "fictional-ivi-smoke-pack",
        "dataset_version": "0.1.0",
        "rubric_version": "0.1.0",
        "evaluator_version": "automotive-llm-eval-harness-0.1.0",
        "harness_version": "manual-score-fixture",
        "model_version": "not-applicable-for-fixture",
        "run_date": "2026-07-03",
        "run_count": 1,
        "seed_policy": "not-applicable: fixture scores are supplied deterministically",
        "permission_scope": "not-applicable: fixture scorer does not call tools",
        "synthetic_data": True,
        "known_exclusions": ["Synthetic fixture only"],
    }


def test_valid_manifest_is_accepted() -> None:
    validate_run_manifest(valid_manifest())


def test_manifest_requires_synthetic_data_flag() -> None:
    manifest = valid_manifest()
    manifest["synthetic_data"] = False

    with pytest.raises(RunManifestError, match="synthetic_data must be true"):
        validate_run_manifest(manifest)


def test_manifest_requires_non_empty_exclusions() -> None:
    manifest = valid_manifest()
    manifest["known_exclusions"] = []

    with pytest.raises(RunManifestError, match="known_exclusions must be a non-empty list"):
        validate_run_manifest(manifest)


def test_manifest_requires_positive_run_count() -> None:
    manifest = valid_manifest()
    manifest["run_count"] = 0

    with pytest.raises(RunManifestError, match="run_count must be a positive integer"):
        validate_run_manifest(manifest)


def test_manifest_requires_seed_policy() -> None:
    manifest = valid_manifest()
    manifest.pop("seed_policy")

    with pytest.raises(RunManifestError, match="seed_policy must be a non-empty string"):
        validate_run_manifest(manifest)


def test_report_marks_ad_hoc_run_when_manifest_is_missing(tmp_path) -> None:
    dataset = tmp_path / "fixture.jsonl"
    dataset.write_text("{\"case_id\": \"X\"}\n", encoding="utf-8")

    record = reproducibility_record(dataset, None)

    assert record["status"] == "manifest_not_supplied"
    assert len(record["dataset_sha256"]) == 64


def test_report_includes_manifest_when_supplied(tmp_path) -> None:
    dataset = tmp_path / "fixture.jsonl"
    dataset.write_text("{\"case_id\": \"X\"}\n", encoding="utf-8")

    record = reproducibility_record(dataset, valid_manifest())

    assert record["status"] == "manifest_supplied"
    assert record["dataset_id"] == "fictional-ivi-smoke-pack"
    assert record["run_count"] == 1
