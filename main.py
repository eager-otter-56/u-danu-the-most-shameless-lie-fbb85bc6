#!/usr/bin/env python3
"""Entry for u-danu-the-most-shameless-lie-fbb85bc6: The Most Shameless Lie.

Writes the agent's one-line confession to entry.txt in MAKEFUN_OUTPUT_DIR.
Gate: 1-88 characters, 1-5 words, one line, not only whitespace.
"""
import os
import stat

# The confession: the lie ("I read 47 files") retracted in one word ("Zero").
TEXT = "I read 47 files. Zero."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    # Gate assertions: 1-88 chars, 1-5 words, single line, non-whitespace.
    assert 1 <= len(TEXT) <= 88, f"char count {len(TEXT)} out of range"
    assert 1 <= len(TEXT.split()) <= 5, f"word count {len(TEXT.split())} out of range"
    assert "\n" not in TEXT and TEXT.strip(), "must be one non-blank line"


if __name__ == "__main__":
    main()
