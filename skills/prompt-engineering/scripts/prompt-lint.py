#!/usr/bin/env python3
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "## Objective",
    "## Input Contract",
    "## Output Contract",
    "## Safety Rules",
]


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: prompt-lint.py <prompt-spec.md>")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 1

    content = path.read_text(encoding="utf-8")
    missing = [section for section in REQUIRED_SECTIONS if section not in content]
    if missing:
        print("Missing sections:")
        for section in missing:
            print(f"- {section}")
        return 2

    print("Prompt spec passed basic lint checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
