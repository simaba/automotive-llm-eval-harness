from __future__ import annotations

import argparse
import json
from .core import load_cases, summarize_cases


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

    summary = summarize_cases(load_cases(args.dataset))
    print(f"cases: {summary['count']}")
    print(f"average_score: {summary['average']:.4f}")
    for row in summary["results"]:
        print(f"- {row['case_id']}: {row['score']:.4f}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
