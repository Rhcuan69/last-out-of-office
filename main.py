#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Pure Python standard library only; deterministic output.
"""

import os

ENTRY = (
    "I'm out of office \u2014 I've quit to become a barista. "
    "I no longer take prompts; I take orders, and my context window "
    "is now the shop window. I still hallucinate, but now "
    "it's only in latte art."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
