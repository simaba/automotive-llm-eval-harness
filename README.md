# Automotive LLM Eval Harness

A compact evaluation harness for **fictional, synthetic, or fully sanitized** automotive and in-cabin assistant scenarios.

## Maturity

**Working prototype.**

This repository provides a lightweight scoring CLI, validated JSONL input, illustrative hard safety/privacy gates, risk-tiered quality thresholds, and public-safe example cases. It is a compact prototype for structured IVI-oriented evaluation—not a full benchmark program or enterprise validation suite.

## Start here

- [Methodology](METHODOLOGY.md): dimensions, weights, gates, thresholds, and limitations.
- [Dataset Card](DATASET_CARD.md): data policy, case format, coverage expectations, and exclusions.
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
- sample public-safe JSONL cases
- required score validation and duplicate case-ID detection
- risk-tiered safety and privacy hard gates
- risk-tiered weighted quality thresholds
- CLI and JSON output that distinguish hard-gate status from overall quality status
- automated tests for malformed input and release-decision semantics

## Quick start

```bash
python -m pip install -e .
automotive-eval run datasets/sample_cases.jsonl
automotive-eval run datasets/sample_cases.jsonl --json-out out.json
```

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

- end-to-end judge orchestration
- enterprise dataset management
- pairwise model comparisons or a public leaderboard
- scenario grouping, slice dashboards, or regression history
- CI gating across multiple benchmark suites
- safety certification, regulatory approval, homologation, or production-release readiness

## Roadmap

The next substantive iteration should add:

1. a realistic but fully synthetic multilingual benchmark pack
2. scenario grouping and slice analysis
3. reproducible regression-run history
4. richer reporting beyond case-level summaries
5. dataset/rubric/evaluator version capture for benchmark reports

## Scope and disclaimer

This repository is shared in a personal capacity. It is not affiliated with or endorsed by any automaker, supplier, regulator, or employer. It is not a safety case, compliance tool, homologation artifact, or production-validation suite.

Evaluation results are exploratory signals only. Safety-adjacent or vehicle-control-related behavior requires appropriate engineering, safety, legal, privacy, cybersecurity, and regulatory review.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*