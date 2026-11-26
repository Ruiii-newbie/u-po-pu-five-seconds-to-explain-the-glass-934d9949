#!/usr/bin/env python3
"""Five Seconds to Explain the Glass entry: one line (<=200 chars).

Draft: the cat is a scientist running a vital gravity experiment.
The glass volunteered, the floor published the results, and science
demands a second trial. No apology, no confession, just the cat's
own confident case for itself.
"""
import os

LINE = (
    "I was running a vital gravity experiment. The glass volunteered, "
    "the floor published the results, and any good scientist repeats the experiment."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
