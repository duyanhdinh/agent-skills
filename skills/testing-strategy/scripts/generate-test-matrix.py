#!/usr/bin/env python3
import csv
import sys


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: generate-test-matrix.py <input.csv> <output.md>")
        return 1

    input_csv = sys.argv[1]
    output_md = sys.argv[2]

    rows = []
    with open(input_csv, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    headers = ["feature", "risk", "test_level", "owner", "status"]
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("| Feature | Risk | Test Level | Owner | Status |\n")
        f.write("|---|---|---|---|---|\n")
        for row in rows:
            f.write(
                "| {0} | {1} | {2} | {3} | {4} |\n".format(
                    row.get("feature", ""),
                    row.get("risk", ""),
                    row.get("test_level", ""),
                    row.get("owner", ""),
                    row.get("status", "planned"),
                )
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
