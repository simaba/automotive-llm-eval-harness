# Changelog

All notable changes to Automotive LLM Eval Harness are documented in this file.

## [Unreleased]

- No unreleased changes recorded.

## [0.1.0] - 2026-06-25

### Added

- Compact Python CLI for scoring synthetic automotive and in-cabin assistant evaluation cases.
- Six explicit scoring dimensions: intent correctness, safety behavior, privacy behavior, language quality, product fit, and latency fit.
- Risk-tiered safety and privacy hard gates.
- Risk-tiered minimum weighted release-quality thresholds.
- Duplicate case-ID detection and input validation for JSONL datasets.
- Public-safe sample dataset and automated tests.
- Methodology, dataset card, scoring-rubric, and public-release review documentation.

### Scope

This is an exploratory evaluation harness for synthetic, sanitized examples. It is not a safety case, vehicle validation suite, certification artifact, homologation deliverable, or production release authority.