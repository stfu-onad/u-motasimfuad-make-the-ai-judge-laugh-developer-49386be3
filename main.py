#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one original funny single-line excuse a developer gives when
code breaks in production to /output/entry.txt.
"""

EXCUSE = (
    "It worked on my machine, so I shipped my machine to production. "
    "Please sign for the fan noise."
)


import os


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars"
    assert "\n" not in text, "excuse must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
