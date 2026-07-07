# Prototype Run Reproducibility

A score from this repository is interpretable only alongside the exact case artifact and the context in which its supplied scores were produced.

## Required manifest fields

| Field | Why it is recorded |
|---|---|
| `dataset_id`, `dataset_version` | Identifies the scenario collection |
| `rubric_version` | Identifies the scoring definitions and interpretation |
| `evaluator_version` | Identifies the manual or automated evaluator process |
| `harness_version`, `model_version` | Identifies the scorer and any upstream model context |
| `run_date`, `run_count`, `seed_policy` | Distinguishes one-off from repeated runs and records determinism assumptions |
| `permission_scope` | Records whether tools, external calls, or permissions affected the evaluated output |
| `synthetic_data`, `known_exclusions` | Keeps the public artifact scope and blind spots visible |

The CLI also records a SHA-256 digest for the exact dataset file.

## Interpretation limits

A matching manifest and digest make a prototype score reviewable and repeatable. They do not establish model validity, independence of evaluators, benchmark coverage, safety sufficiency, production readiness, or release approval.

For this prototype's bundled fixture, the supplied scores are deterministic test values. `model_version` and `permission_scope` therefore use explicit `not-applicable` values rather than implying a live-model or tool-execution claim.
