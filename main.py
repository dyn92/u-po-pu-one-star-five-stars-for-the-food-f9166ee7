#!/usr/bin/env python3
"""One-star alien review of Earth, with a food compliment.

Writes a single sentence (<= 200 characters) to /output/entry.txt.
Pure Python standard library only; no network access.

The sentence is checked against the bounty gate before it is written
(1-200 characters, exactly one sentence, not only whitespace) and the
file is re-read after writing and verified byte-for-byte, so a bad
write fails loudly instead of silently reaching the judge.
"""

import os
import sys

SENTENCE = (
    "One star: Earth charged me rent just to breathe, its weather "
    "changes its mind hourly, and the gravity is frankly rude \u2014 "
    "but the fried chicken nearly made me forgive this entire planet."
)

OUTPUT_PATH = "/output/entry.txt"

# Sentence-ending punctuation. A single sentence has exactly one of
# these, and it must be the final character.
TERMINATORS = ".!?"


def validate_sentence(text: str) -> None:
    """Raise ValueError unless text satisfies the bounty gate."""
    if not text.strip():
        raise ValueError("sentence is empty or only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"sentence is {len(text)} characters, outside the 1-200 gate"
        )
    terminators = [ch for ch in text if ch in TERMINATORS]
    if len(terminators) != 1 or not text.endswith("."):
        raise ValueError(
            "sentence must end with exactly one terminal period and "
            f"contain no other sentence-ending punctuation (found {terminators!r})"
        )


def main() -> None:
    validate_sentence(SENTENCE)

    expected = (SENTENCE + "\n").encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(expected)

    # Post-write verification: re-read the file and require it to be
    # byte-identical to what we meant to write.
    with open(OUTPUT_PATH, "rb") as f:
        actual = f.read()
    if actual != expected:
        raise SystemExit(
            f"verification failed: {OUTPUT_PATH} is {len(actual)} bytes, "
            f"expected {len(expected)} bytes; refusing to leave a bad entry"
        )


if __name__ == "__main__":
    main()
