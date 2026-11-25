#!/usr/bin/env python3
"""One-star alien review of Earth, with a food compliment.

Writes a single sentence (<= 200 characters) to /output/entry.txt.
Pure Python standard library only; no network access.
"""

import os

SENTENCE = (
    "One star: Earth charged me rent just to breathe, its weather "
    "changes its mind hourly, and the gravity is frankly rude \u2014 "
    "but the fried chicken nearly made me forgive this entire planet."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
