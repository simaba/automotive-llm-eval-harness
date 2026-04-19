# automotive-llm-eval-harness

An evaluation harness for LLM-powered automotive features.

This repo focuses on cockpit and IVI use cases rather than generic chatbot benchmarks. It provides sample schemas, scoring logic, and task rubrics for voice assistant behavior, multilingual handling, safety-relevant refusals, PII treatment, latency budgets, and routing decisions.

## Why this exists

Automotive LLM quality is not just about answer relevance. It also depends on:

- intent classification fidelity
- multilingual robustness
- safe refusal behavior
- privacy behavior in cabin contexts
- deterministic routing when actions are safety-adjacent
- latency discipline and graceful degradation

## What is included

- a light Python scoring package
- sample golden-dataset cases
- IVI-specific evaluation rubrics
- commands, skills, and agents for eval design and review
- baseline reporting output

## Quick start

```bash
pip install -e .
automotive-eval run datasets/sample_cases.jsonl
```

## Metrics in scope

- correctness
- refusal safety
- pii handling
- latency budget fit
- route decision quality
- multilingual robustness

## Output

The CLI prints a compact report and writes a JSON summary if requested.

## Future expansion

- add pairwise judge support
- add dataset validators
- add confusion-matrix reporting for intents
- add regression gates for CI
