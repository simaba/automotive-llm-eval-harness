# Contributing

## Principles

1. Be precise.
2. Prefer reusable templates over one-off prose.
3. Keep prompts and agent instructions observable and testable.
4. Add examples for every new skill or command.
5. Avoid vendor lock-in unless the repo clearly requires a specific harness.

## File conventions

- Agents: `agents/<name>.md`
- Skills: `skills/<skill-name>/SKILL.md`
- Commands: `commands/<command>.md`
- Rules: `rules/common/*.md`
- Templates: `templates/**/*.md`
- Tests: `tests/**`

## Review checklist

- Does the change improve clarity or repeatability?
- Is the output auditable?
- Are assumptions explicit?
- Are sample inputs and outputs included?
- If code exists, are tests updated?
