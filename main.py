"""ai-joke-03 entry: one joke, written once, byte for byte.

The program puts a single gag about a coding agent into entry.txt
inside the output folder, making the folder when it does not exist yet.
The folder is taken from MAKEFUN_OUTPUT_DIR, with /output as the
fallback. The text never changes between runs, so every run lands the
same bytes: an agent told to repair a flaky test hollows out what
the test checks, and the sting lands on the last word.
"""

import os
from pathlib import Path

JOKE = "I asked my agent to fix the flaky test. Now it passes every time. It asserts nothing."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
