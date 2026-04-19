# CLAUDE.md

## Overview

This repo provides a small, extensible evaluation framework for automotive LLM features.

## Layout

- `src/`: scoring and CLI
- `datasets/`: sample golden cases
- `rubrics/`: domain scoring dimensions
- `agents/`, `skills/`, `commands/`: harness-facing workflows
- `tests/`: package tests

## Quality rules

- Favor explicit rubric criteria over vague grading.
- Keep sample cases sanitized.
- Keep failure explanations actionable.
