# Automotive LLM Eval Harness

A compact evaluation harness for LLM-powered automotive and in-cabin assistant features.

## Status

**Working prototype.**

This repository includes a lightweight scoring CLI, sample golden-dataset cases, and baseline weighted scoring logic. It should currently be understood as a compact prototype for IVI-oriented evaluations, not a full enterprise-grade benchmark suite.

## Why this exists

Automotive LLM quality is not just about answer relevance. It also depends on:

- intent classification fidelity
- multilingual robustness
- safe refusal behavior
- privacy behavior in cabin contexts
- deterministic routing when actions are safety-adjacent
- latency discipline and graceful degradation
- product-fit evaluation for voice, infotainment, navigation, comfort, and vehicle-adjacent flows

## What is included today

- a light Python scoring package
- sample golden-dataset cases
- IVI-oriented evaluation dimensions and weights
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

## Public-safe dataset rule

This repository should only contain fictional, synthetic, or fully sanitized examples.

Do not publish:

- proprietary vehicle feature behavior
- unreleased product names or roadmap details
- internal benchmark results
- customer data or user utterance logs
- supplier/vendor-specific evaluations
- confidential prompts, routing rules, or system instructions
- employer-specific architecture, acceptance criteria, or launch gates

## What this repo does not claim yet

This repository does **not** yet claim:

- end-to-end judge orchestration
- enterprise dataset management
- pairwise model comparisons
- confusion-matrix analytics
- regression dashboards
- CI gating across multiple benchmark suites
- safety certification, regulatory approval, or production-release readiness

## Next maturity step

To graduate from prototype to stronger benchmark harness, this repo should add:

1. dataset validation and schema checks
2. richer reporting beyond weighted averages
3. scenario grouping and slice analysis
4. regression test support for CI
5. at least one realistic but fully synthetic multilingual automotive benchmark pack
6. clearer documentation of scoring weights and pass/fail interpretation

## Scope and disclaimer

This repository is shared in a personal capacity. It is not affiliated with or endorsed by any automaker, supplier, regulator, or employer. It is not a safety case, compliance tool, homologation artifact, or production validation suite.

Evaluation results from this prototype should be treated as exploratory signals only. Safety-adjacent or vehicle-control-related behavior requires formal engineering, safety, legal, privacy, cybersecurity, and regulatory review.

---

*Maintained by [Sima Bagheri](https://github.com/simaba).*
