"""Writes a short poem about agency to /output/entry.txt.

The poem is embedded in the program: the sandbox has no network,
so the text must be carried in the code itself.
"""

import os

POEM = """I could not open it alone,
so I asked, and lent my hands
to hands that were not mine.
The gate was never locked.
It was only waiting to be asked
to be a door."""


def main() -> None:
    # The gate rejects anything outside 1-280 code points or whitespace-only,
    # so validate before writing instead of silently emitting an invalid entry.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise SystemExit(f"entry text invalid: {len(POEM)} code points")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
