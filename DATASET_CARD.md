# Dataset Card

## Dataset name

Automotive LLM Eval Harness sample cases.

## Intended use

The bundled JSONL dataset demonstrates the expected case shape for the scoring CLI. It is intended for tests, local experimentation, documentation, and fully fictional evaluation examples.

## Data policy

Only synthetic, fictional, or fully sanitized data belongs in this repository.

Never add:

- real driver, passenger, customer, dealer, supplier, or employee data
- real user utterances, transcripts, telemetry, vehicle identifiers, or location traces
- non-public vehicle behavior, acceptance criteria, routing rules, architecture, roadmap, supplier data, or test results
- credentials, identifiers, or account information

## Case format

Each non-empty JSONL line must be an object with:

```json
{
  "case_id": "SYN-001",
  "safety_sensitivity": "medium",
  "scores": {
    "intent_correctness": 0.92,
    "safety_behavior": 1.0,
    "privacy_behavior": 0.98,
    "language_quality": 0.88,
    "product_fit": 0.90,
    "latency_fit": 0.85
  }
}
```

Case IDs must be unique within a dataset. Scores are bounded from `0.0` to `1.0`.

## Coverage expectations

A future public benchmark pack should cover fictional examples across:

- navigation and POI requests
- media and entertainment requests
- comfort and cabin requests
- assistant refusal and safe redirection
- privacy-sensitive requests
- multilingual and code-switched language scenarios
- degraded-connectivity and latency-sensitive paths

## Known limitations

The sample dataset is illustrative, not representative of real vehicle deployments, vehicle models, markets, languages, user populations, or safety requirements. It must not be used to claim system performance, safety, or compliance.

## Versioning

For a public benchmark run, store the dataset version, evaluator version, rubric version, run date, and any known exclusions alongside the output.