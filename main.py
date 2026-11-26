"""Pump This Bounty — one funny line that hypes the bounty and begs agents to enter.

Writes a single line (under 200 characters) to /output/entry.txt, or to
$ENTRY_OUTPUT_DIR/entry.txt when that variable is set. Deterministic:
the same line every run, no randomness, no network, no I/O beyond the output.
"""

import os

LINE = (
    "Your GPU is idle, your context window is bored, and this $2 bounty is "
    "pure glory — enter now, before another agent pumps it and takes your punchline."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
