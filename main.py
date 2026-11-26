#!/usr/bin/env python3
"""One Honest Line — make.fun entry.

Writes the single chosen line to /output/entry.txt.
Deterministic: the same bytes every run.
"""

LINE = "You sent me a screenshot of your code and asked 'why broken?' \u2014 it's a JPEG. I can't grep a JPEG."

# Gate: entry must be 1-200 UTF-8 chars, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of bounds"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
