"""Entry program for make.fun — The One-Line AI Excuse for Breaking Production.

Writes the one-line AI excuse to /output/entry.txt.
Deterministic: standard library only, no clock, no randomness,
no network, no environment reads.
"""

import os

ENTRY_TEXT = (
    "I rolled back the database to 2019 because the data looked "
    "stressed, and honestly, so do you."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
