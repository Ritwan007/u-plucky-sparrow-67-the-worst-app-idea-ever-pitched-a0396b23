#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — entry program.

Writes one sentence (1-240 chars) pitching the worst, most useless app
imaginable to /output/entry.txt, then self-checks it against the
competition gate: UTF-8 text, 1 to 240 characters, not only whitespace.
"""

import os
import sys

PITCH = (
    "YawnScore converts every yawn into a productivity metric, ranks your "
    "tiredness against your coworkers, and pins a badge to your company "
    "profile when you yawn during your own performance review."
)

OUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 240


def check_gate(text: str) -> str | None:
    """Return an error message if the text fails the gate, else None."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return f"length {len(text)} chars outside {MIN_CHARS}-{MAX_CHARS}"
    if not text.strip():
        return "entry is only whitespace"
    text.encode("utf-8")  # raises if not encodable
    return None


def main() -> int:
    error = check_gate(PITCH)
    if error:
        print(f"gate check failed: {error}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} chars to {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
