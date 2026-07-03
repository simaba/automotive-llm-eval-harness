"""Reproducibility metadata for transparent prototype scoring runs."""

from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Any


REQUIRED_TEXT_FIELDS = (
    "dataset_id",
    "dataset_version",
    "rubric_version",
    "evaluator_version",
    "harness_version",
    "model_version",
    "run_date",
)


class RunManifestError(ValueError):
    """Raised when a scoring-run manifest is incomplete or malformed."""


def _read_json(path: str | Path) -> dict[str, Any]:
    source = Path(path)
    try:
        payload = json.loads(source.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RunManifestError(f"could not read run manifest: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RunManifestError(f"invalid JSON run manifest: {exc.msg}") from exc
    if not isinstance(payload, dict):
        raise RunManifestError("run manifest must be a JSON object")
    return payload


def validate_run_manifest(payload: dict[str, Any]) -> None:
    """Validate the minimum context needed to interpret a prototype run."""
    for field in REQUIRED_TEXT_FIELDS:
        value = payload.get(field)
        if not isinstance(value, str) or not value.strip():
            raise RunManifestError(f"{field} must be a non-empty string")

    try:
        date.fromisoformat(payload["run_date"])
    except ValueError as exc:
        raise RunManifestError("run_date must use YYYY-MM-DD") from exc

    if payload.get("synthetic_data") is not True:
        raise RunManifestError("synthetic_data must be true for public prototype runs")

    exclusions = payload.get("known_exclusions")
    if not isinstance(exclusions, list) or not exclusions:
        raise RunManifestError("known_exclusions must be a non-empty list")
    if not all(isinstance(item, str) and item.strip() for item in exclusions):
        raise RunManifestError("known_exclusions must contain non-empty strings")


def load_run_manifest(path: str | Path) -> dict[str, Any]:
    """Load and validate a run manifest from JSON."""
    payload = _read_json(path)
    validate_run_manifest(payload)
    return payload


def dataset_sha256(path: str | Path) -> str:
    """Return a stable digest for the exact scored JSONL artifact."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def reproducibility_record(
    dataset_path: str | Path,
    manifest: dict[str, Any] | None,
) -> dict[str, Any]:
    """Build a reportable run-context record without inventing missing metadata."""
    path = Path(dataset_path)
    record: dict[str, Any] = {
        "dataset_file": path.name,
        "dataset_sha256": dataset_sha256(path),
    }
    if manifest is None:
        record.update(
            {
                "status": "manifest_not_supplied",
                "note": (
                    "Ad-hoc prototype score only. Supply --manifest to record dataset, rubric, "
                    "evaluator, harness, model, date, and exclusions."
                ),
            }
        )
        return record

    record.update({"status": "manifest_supplied", **manifest})
    return record
