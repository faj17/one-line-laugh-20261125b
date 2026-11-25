#!/usr/bin/env python3
"""One Line, One Laugh entry.

Writes one funny line to /output/entry.txt (1-200 characters, UTF-8,
not only whitespace). Standard library only, no network, no input.

The line is built from three fragments: the setup (the therapist
prescribes closure), the turn (closure taken literally as closing
browser tabs), and the punch (the payoff is absolutely nothing).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "My therapist said I need closure, so"
TURN = "I closed all 47 browser tabs"
PUNCH = "and felt absolutely nothing."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, turn: str, punch: str) -> str:
    """Join the three fragments into one funny line."""
    return f"{setup} {turn} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, a single line, UTF-8-encodable, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, TURN, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
