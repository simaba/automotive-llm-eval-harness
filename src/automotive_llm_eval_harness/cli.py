from __future__ import annotations

import argparse
import json

from .core import CaseValidationError, load_cases, summarize_cases


def main() -> int:
    parser = argparse.ArgumentParser(prog="automotive-eval")
    sub = parser.add_subparsers(dest="command")

    run = sub.add_parser("run")
    run.add_argument("dataset")
    run.add_argument("--json-out")

    args = parser.parse_args()
    if args.command != "run":
        parser.print_help()
        return 1

    try:
        summary = summarize_cases(load_cases(args.dataset))
    except (OSError, CaseValidationError) as exc:
        parser.error(str(exc))

    print(f"cases: {summary['count']}")
    print(f"average_score: {summary['average']:.4f}")
    print(f"passed: {summary['passed_count']}")
    print(f"blocked: {summary['blocked_count']}")
    for row in summary["results"]:
        status = "PASS" if row["passed"] else "BLOCKED"
        print(f"- {row['case_id']}: {row['score']:.4f} [{status}]")
        for blocker in row["blockers"]:
            print(f"  - {blocker}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as file:
            json.dump(summary, file, indent=2, ensure_ascii=False)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
