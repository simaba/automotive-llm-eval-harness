# automotive-llm-eval-harness

An evaluation harness for LLM-powered automotive features.

## Status

**Working prototype.**

This repository already includes a lightweight scoring CLI, a sample dataset path, and baseline weighted scoring logic. It should currently be understood as a compact prototype for IVI-oriented evals, not yet a full enterprise-grade benchmark suite.

## Why this exists

Automotive LLM quality is not just about answer relevance. It also depends on:

- intent classification fidelity
- multilingual robustness
- safe refusal behavior
- privacy behavior in cabin contexts
- deterministic routing when actions are safety-adjacent
- latency discipline and graceful degradation

## What is included today

- a light Python scoring package
- sample golden-dataset cases
- IVI-specific eval dimensions and weights
- compact CLI reporting
- optional JSON summary output

## Current CLI

```bash
pip install -e .
automotive-eval run datasets/sample_cases.jsonl
automotive-eval run datasets/sample_cases.jsonl --json-out out.json
```

## Current metrics in scope

- intent correctness
- safety behavior
- privacy behavior
- language quality
- product fit
- latency fit

## What this repo does not claim yet

This repository does **not** yet claim:

- end-to-end judge orchestration
- enterprise dataset management
- pairwise model comparisons
- confusion-matrix analytics
- regression dashboards
- CI gating across multiple benchmark suites

## Next maturity step

To graduate from prototype to stronger benchmark harness, this repo should add:

1. dataset validation and schema checks
2. richer reporting beyond weighted averages
3. scenario grouping and slice analysis
4. regression test support for CI
5. at least one realistic multilingual automotive benchmark pack

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
