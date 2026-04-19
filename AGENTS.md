# Agent Instructions

Use this repo to evaluate LLM-powered automotive features with domain-aware criteria.

## Principles

1. Evaluate against user intent and product constraints, not generic helpfulness alone.
2. Treat safety-adjacent requests differently from benign information requests.
3. Separate policy failure from model misunderstanding.
4. Preserve traceability from case to score.
5. Prefer deterministic metrics where possible.

## Delegation

- `eval-designer` to define cases and rubrics
- `safety-refusal-reviewer` to inspect refusal behavior
- `latency-budget-reviewer` to assess route and latency fit
- `privacy-reviewer` to inspect PII handling
