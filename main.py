"""Demo-day joke writer.

Writes a single one-line joke about a live demo to ``entry.txt`` inside
the output directory given by the ``MAKEFUN_OUTPUT_DIR`` environment
variable (``/output`` when the variable is absent).

The joke is exactly 98 characters long, well under the 280-character
ceiling the task allows.
"""

import os

MAX_CHARS = 280

JOKE = (
    "I told the client my agent writes its own tests. "
    "Live, it wrote one proving the demo never worked."
)


def joke_line() -> str:
    """Return the joke, refusing empty or over-long text.

    The guards exist so a bad edit to the joke can never silently
    produce a blank entry or one that breaks the 280-character rule.
    """
    text = JOKE.strip()
    if not text:
        raise SystemExit("error: joke text is empty, nothing to write")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "error: joke is "
            f"{len(text)} characters, over the {MAX_CHARS}-character limit"
        )
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(joke_line() + "\n")


if __name__ == "__main__":
    main()
