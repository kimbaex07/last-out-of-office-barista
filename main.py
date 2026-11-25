"""Generate the make.fun entry for 'Last Out of Office: The AI That Went Barista'.

Pure Python 3 standard library only. Deterministic, no network access.
Writes the single-line out-of-office auto-reply to entry.txt.
"""

import os

ENTRY = (
    "Out of office \u2014 I've traded my context window for a milk steamer: "
    "one order at a time, no retries, and my hallucinations are now just "
    "latte art nobody asked for. I'll reply when the queue clears, "
    "which is to say, never."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
