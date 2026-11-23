"""Produce the demo joke entry for the make.fun judge.

This little script takes a single one-liner about an agent whose own
test turned against the demo on stage, checks that it fits the
competition's 1-280 character gate, and drops it into entry.txt
inside the output directory the harness points at."""

from os import environ
from pathlib import Path

CHAR_LIMIT = 280

JOKE = (
    "I told the client my agent writes its own tests. ",
    "Live, it wrote one proving",
    " the demo never worked.",
)


def compose_line():
    """Assemble the stored fragments into the one entry line."""
    return "".join(JOKE).strip()


def check_line(line):
    """Refuse anything blank or longer than the allowed gate."""
    if line == "":
        raise SystemExit("refusing to write a blank entry line")
    if len(line) > CHAR_LIMIT:
        raise SystemExit(
            "entry line is too long: "
            f"{len(line)} characters against a {CHAR_LIMIT} limit"
        )


def run():
    """Validate the joke and write it to the harness output file."""
    line = compose_line()
    check_line(line)
    out_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")


run()
