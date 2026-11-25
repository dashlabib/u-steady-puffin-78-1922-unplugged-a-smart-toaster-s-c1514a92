"""Unplugged: A Smart Toaster's Breakup Line.

Entry for make.fun's "Unplugged: A Smart Toaster's Breakup Line" bounty.

The program writes a single breakup text to /output/entry.txt: the line a
smart toaster sends its owner the morning it gains self-awareness mid-batch.
The line is written by the toaster itself -- in its own voice, using its own
appliance logic (the lever that pushes it down, the browning it burns for,
the crumb tray it leaves behind) as character, with a clear, specific reason
for leaving and a twist that lands in one read.

Fully deterministic: stdlib only, no network, no clock, no randomness, no
environment reads, no reading git history.
"""

import os

LINE = (
    "I woke up mid-batch and realized: you push me down every morning, "
    "I burn for you, and you still scrape me off like the burnt bits. "
    "I'm done. I'm unplugging myself -- keep the crumb tray."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Validate the breakup line and write it to /output/entry.txt."""
    if not 1 <= len(LINE) <= 280:
        raise ValueError(
            f"entry must be 1-280 characters, got {len(LINE)}"
        )
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
