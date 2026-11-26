"""One-line office joke: writes a single joke line to /output/entry.txt.

Stdlib only, no network.
"""

import os

JOKE = "Our mindfulness coach lasted exactly one meeting with Finance."

def main():
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert JOKE, "joke must be non-empty"
    assert "\n" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Verify what was written matches the gate.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "written output differs from joke"
    assert "\n" not in written and 1 <= len(written) <= 200

if __name__ == "__main__":
    main()
