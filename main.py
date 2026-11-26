#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt."""

import os

LINE = "My plants died of neglect, my sourdough starter died of neglect, and at this point my therapist is just taking notes for the sequel."


def main() -> int:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("LINE must be a single line")
    if not (1 <= len(LINE) <= 200):
        raise ValueError("LINE must be between 1 and 200 characters")
    if not LINE.strip():
        raise ValueError("LINE must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as fh:
        fh.write(LINE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
