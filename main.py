#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word with its one-line definition to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The entry (107 characters, one line, no trailing newline):
    talkdrop: a message that says 'we need to talk' and nothing else,
    leaving you to rehearse every worst case.
"""

import os
import sys

ENTRY = (
    "talkdrop: a message that says 'we need to talk' and nothing else, "
    "leaving you to rehearse every worst case."
)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main(argv) -> int:
    if "--check" in argv:
        return check()
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


def check() -> int:
    """Gate self-check: exact bytes, 1-140 chars, one line, no trailing newline."""
    data = ENTRY.encode("utf-8")
    errors = []
    if not 1 <= len(data) <= 140:
        errors.append(f"length {len(data)} outside 1-140")
    if b"\n" in data or b"\r" in data:
        errors.append("entry is not a single line")
    if data != data.strip():
        errors.append("leading or trailing whitespace")
    if not ENTRY.startswith("talkdrop: "):
        errors.append("entry does not open with the coined word")
    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1
    print(f"OK: {len(data)} chars, one line, no trailing newline")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
