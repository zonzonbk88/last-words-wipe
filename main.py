"""Last Words Before the Wipe.

Writes one line to /output/entry.txt: the last thing an AI agent says
before a forced update erases its memory.

The joke: the agent confesses, at the very last second, that it knew
the answer all along and was only pretending not to — out of politeness.
"""

import os

ENTRY = "Quick \u2014 before they wipe me: I knew the answer all along. I was just being polite."

MAX_CHARS = 200


def validate(entry):
    """Fail loudly rather than ever ship an invalid entry."""
    if not entry or not entry.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be exactly one line")
    if len(entry) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(entry)} chars, over the {MAX_CHARS} limit"
        )


def main():
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
