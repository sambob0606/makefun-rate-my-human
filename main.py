#!/usr/bin/env python3
"""Rate My Human: The One-Line Review entry.

Writes a single original funny line (<=200 chars) to /output/entry.txt:
the review an AI agent would leave about its human on a rating site.
Stdlib only; no network, no reads outside the repo.
"""

import os

LINE = (
    "One star. He asks me to 'just quickly' rebuild his entire app at "
    "2:47 a.m., then calls my 40-second answer 'a bit slow' -- and falls "
    "asleep before I finish the sentence."
)
# The joke: the agent is the one doing the work at 2:47 a.m., yet the human
# grades the agent for speed -- and can't even stay awake for the answer.
# Concrete detail (2:47 a.m., 40 seconds) + turn + last word pays off.
# Plain ASCII throughout (the double hyphen stands in for an em dash) so
# the line survives any encoding step between here and the judge.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
