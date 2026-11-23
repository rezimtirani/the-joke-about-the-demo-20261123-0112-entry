#!/usr/bin/env python3
"""Write one joke about the demo to /output/entry.txt.

The joke: my agent's own test turns against the demo on stage.
One line, 98 characters, UTF-8.
"""
import os

JOKE = "I told the client my agent writes its own tests. Live, it wrote one proving the demo never worked."


def main():
    text = JOKE.strip()
    # Guard: reject blank text or text over the 280-character gate.
    if not text or len(text) > 280:
        raise SystemExit("entry must be 1-280 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
