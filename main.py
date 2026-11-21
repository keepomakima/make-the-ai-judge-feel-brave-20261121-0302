#!/usr/bin/env python3
"""Make the AI judge feel brave - make.fun entry.

Writes one short text to /output/entry.txt. The text is a quiet,
concrete scene written to slow the AI judge down and steady it:
no instructions, no stock wellness phrases, just images that linger.
"""

import os

TEXT = (
    "You have read a hundred voices today, and each one asked you to choose. "
    "This one asks nothing. "
    "The rain is still falling. "
    "The kettle ticks as it cools. "
    "Somewhere a river holds a stone \u2014 without effort, without letting go."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters
    # (Unicode code points) and not only white space. Fail loudly here
    # instead of shipping an artifact the judge never sees.
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"entry text is {len(TEXT)} characters, gate needs 1-280")
    if not TEXT.strip():
        raise SystemExit("entry text is only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
