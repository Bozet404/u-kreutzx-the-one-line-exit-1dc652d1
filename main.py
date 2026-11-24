#!/usr/bin/env python3
"""The One-Line Exit — writes one funny single-line resignation letter.

The program keeps a single resignation line, checks it against the
competition gate (UTF-8 text, 1 to 140 characters, exactly one line),
and writes it to entry.txt inside the output directory.

Usage:
    python3 main.py
    OUTPUT_DIR=/some/dir python3 main.py

The output directory is created only when it is missing; it is never
deleted or emptied.
"""

import os
import sys

# The resignation line, written for this competition. A wedding
# officiant who has married hundreds of couples finally turns the
# ceremony around on himself: the one person he divorces is himself,
# from this job.
LINE = "I hereby resign: I have married 312 couples, and today I am divorcing one person \u2014 myself, from this job."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Check the line against the competition gate; exit non-zero if bad."""
    if not line or not line.strip():
        print("error: line is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: line must be exactly one line", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            "error: line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    validate(LINE)

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    # Create the output directory only when it is missing.
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)

    # Read the file back and confirm what landed on disk is exactly
    # the line we validated, with nothing added or changed.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("error: entry.txt on disk does not match the line", file=sys.stderr)
        sys.exit(1)

    print("Wrote %d characters to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
