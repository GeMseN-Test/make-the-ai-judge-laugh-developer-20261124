"""Make the AI Judge Laugh: Developer Excuses — entry program.

Writes one funny single-line excuse a developer gives when code breaks in
production to /output/entry.txt. Deterministic: the same line every run,
no input, no network, no randomness — the harness just runs this file.
"""

import os

# The excuse. Written for this bounty, in this session.
# Twist: the user did exactly what the ticket asked — the one path never
# tested. Sounds like a real developer defending themselves out loud, and it
# steers clear of the worn "works on my machine / tests passed / staging"
# excuses that flood this bounty.
LINE = (
    "In my defense, the code worked perfectly until a user did exactly "
    "what the ticket asked \u2014 the one path I never tested."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
