"""ai-joke-03 entry: write one one-liner about AI coding agents.

Writes exactly one joke to <output dir>/entry.txt, with no trailing
newline. The output directory comes from MAKEFUN_OUTPUT_DIR, falling
back to /output. Standard library only, offline, deterministic:
both runs write the same bytes. The joke lands as a triple: an
agent fixes a race condition the only way it knows how, by
deleting the race, the condition, and finally the feature itself.
"""

import os
from pathlib import Path

JOKE = (
    "My agent fixed the race condition by removing the race, "
    "the condition, and the feature."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
