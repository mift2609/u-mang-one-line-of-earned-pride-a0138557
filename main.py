"""One Line of Earned Pride — make.fun entry "Front Row".

A single quiet, earned moment of pride: after eleven years of night
shifts, a mother finally watches her daughter graduate — and lets
herself sit in the front row.

Running this script writes the line to /output/entry.txt (deterministic,
standard library only, no randomness, no network).
"""

import os

LINE = (
    "After eleven years of night shifts, she finally watched her "
    "daughter graduate, and for once she let herself sit in the "
    "front row."
)


def main() -> None:
    assert "\n" not in LINE, "entry line must be a single line"
    assert 1 <= len(LINE) <= 240, "entry line must be 1-240 characters"
    assert LINE.endswith("."), "entry line should end with a full stop"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "entry.txt content mismatch"

    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
