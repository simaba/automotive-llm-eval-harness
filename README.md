# Automotive LLM Eval Harness

A compact evaluation **scorer** for **fictional, synthetic, or fully sanitized** automotive and in-cabin assistant scenarios.

## Maturity

**Working prototype.**

This repository validates JSONL case artifacts, scores the values supplied in those artifacts, applies illustrative safety/privacy gates and quality thresholds, and produces transparent reports. It does **not** yet generate model responses, orchestrate judges, or independently measure an LLM system.

## Start here

- [Methodology](METHODOLOGY.md): dimensions, weights, gates, thresholds, reproducibility context, and limitations.
- [Dataset Card](DATASET_CARD.md): data policy, case format, coverage expectations, and exclusions.
- [Run reproducibility](docs/REPRODUCIBILITY.md): how manifests, dataset digests, run count, seed policy, and permission scope make a prototype score reviewable.
- [Sample run manifest](datasets/sample_run_manifest.json): required dataset, rubric, evaluator, harness, model, run-count, seed-policy, permission-scope, date, and exclusion context.
- [Public Release Checklist](docs/PUBLIC_RELEASE_CHECKLIST.md): pre-publication review steps.
- [Draft v0.1.0 notes](docs/releases/v0.1.0.md): intended public-release scope.

## Purpose

Automotive LLM quality is not only answer relevance. This prototype makes the following dimensions explicit:

- intent correctness
- safety behavior
- privacy behavior
- language quality
- product fit
- latency fit

## Current capabilities

- lightweight Python scoring package and CLI
- sample public-safe JSONL cases and a reproducibility manifest
- required score validation and duplicate case-ID detection
- risk-tiered safety and privacy hard gates
- risk-tiered weighted quality thresholds
- CLI and JSON output that distinguish hard-gate status from overall quality status
- dataset digest plus manifest-based dataset/rubric/evaluator/harness/model/run-count/seed-policy/permission-scope/date/exclusions capture
- automated tests for malformed input, prototype quality semantics, and manifest validation

## Quick start

```bash
python -m pip install -e .
automotive-eval run datasets/sample_cases.jsonl \
  --manifest datasets/sample_run_manifest.json
automotive-eval run datasets/sample_cases.jsonl \
  --manifest datasets/sample_run_manifest.json \
  --json-out out.json
```

A manifest is optional for an ad-hoc local score, but the report will mark the run as `manifest_not_supplied`. Use a manifest for any result you intend to share, compare, or revisit.

## Publication safety

This repository must contain only fictional, synthetic, or fully sanitized examples.

Do not publish:

- proprietary vehicle feature behavior or non-public architecture
- unreleased product names, launch plans, acceptance criteria, or routing rules
- internal benchmark results, safety evidence, or release gates
- real user utterances, telemetry, location traces, vehicle identifiers, or personal data
- supplier-, vendor-, employer-, customer-, or employee-specific material
- credentials, endpoints, system prompts, or confidential tool configuration

## Out of scope

This prototype does not provide:

- model-output generation or end-to-end judge orchestration
- enterprise dataset management
- pairwise model comparisons or a public leaderboard
- scenario grouping, slice dashboards, or regression history
- CI gating across multiple benchmark suites
- safety certification, regulatory approval, homologation, or production-release readiness

## Roadmap

The next substantive iteration should add:

1. a realistic but fully synthetic multilingual benchmark pack
2. scenario grouping and slice analysis
3. reproducible regression-run history built on the manifest format
4. richer reporting beyond case-level summaries
5. evaluator adapters that create scored case artifacts from controlled inputs and outputs

## Scope and disclaimer

This repository is shared in a personal capacity. It is not affiliated with or endorsed by any automaker, supplier, regulator, or employer. It is not a safety case, compliance tool, homologation artifact, or production-validation suite.

Evaluation results are exploratory signals only. Safety-adjacent or vehicle-control-related behavior requires appropriate engineering, safety, legal, privacy, cybersecurity, and regulatory review.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*