#!/usr/bin/env python3
import csv
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: score_eval_results.py <results.csv>")
        return 1

    path = sys.argv[1]
    total = 0
    passed = 0
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if row.get("pass", "").strip().lower() in {"1", "true", "yes", "pass"}:
                passed += 1

    if total == 0:
        print("No rows found.")
        return 2

    rate = passed / total
    print(f"Passed: {passed}/{total} ({rate:.2%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
