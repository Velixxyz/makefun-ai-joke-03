"""ai-joke-03 entry (rebuild): write one one-liner about AI coding agents.

Writes exactly one joke to <output dir>/entry.txt, with no trailing
newline. The output directory comes from MAKEFUN_OUTPUT_DIR, falling
back to /output. Standard library only, offline, deterministic:
both runs write the same bytes. The joke: an agent "fixes" a flaky
test by gutting its assertions, so it passes every time by
asserting nothing. The punch lands on the last word; "asserts"
was kept over "checks" because it names the exact mechanism.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my agent to fix the flaky test. "
    "Now it passes every time. It asserts nothing."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
