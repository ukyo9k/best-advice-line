#!/usr/bin/env python3
"""Write one sentence -- the best advice I ever got -- to entry.txt.

The line below is a single sentence (at most 200 characters) about the
best advice the writer ever received: the night before his first job,
his father told him to take the work nobody else wants. The program
writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to
/output/entry.txt), reads the file back, and verifies the round-trip is
byte-identical, with no trailing newline.
"""

import os
import sys

LINE = (
    "The night before my first job, my father said, "
    "'Take the job nobody wants -- that's the one "
    "they'll remember you for.'"
)

MAX_CHARS = 200
TERMINATORS = ".!?"


def _fail(message):
    raise ValueError(message)


def validate(line):
    """Guard the line before it is written; every check must pass."""
    if not isinstance(line, str) or not line:
        _fail("line is empty")
    if line.strip() == "":
        _fail("line must not be only whitespace")
    if line != line.strip():
        _fail("line has leading or trailing whitespace")
    if any(ch in line for ch in "\n\r\t"):
        _fail("line must be a single line with no control characters")
    if any(ord(ch) < 0x20 for ch in line):
        _fail("line contains a control character")
    if len(line) > MAX_CHARS:
        _fail("line is %d characters, over the %d limit" % (len(line), MAX_CHARS))
    if "  " in line:
        _fail("line contains a double space")
    # Exactly one sentence: one terminator, and it must end the line
    # (allowing a closing quote after it).
    core = line.rstrip("'\"")
    ends = [ch for ch in core if ch in TERMINATORS]
    if len(ends) != 1 or not core.endswith(ends[0]):
        _fail("line must be exactly one sentence ending in . ! or ?")
    if core.endswith(("..", "!!", "??", "?!")):
        _fail("line must not end with repeated punctuation")
    # It must be advice someone actually gave: a speaker and a quote.
    if "said" not in line or "'" not in line:
        _fail("line must quote the advice someone gave")


def main():
    validate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    with open(path, "rb") as fh:
        stored = fh.read()
    if stored != data:
        _fail("round-trip mismatch: file differs from the line")
    if stored.endswith(b"\n"):
        _fail("file must not end with a trailing newline")
    if stored.decode("utf-8") != LINE:
        _fail("file is not valid UTF-8 matching the line")

    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
