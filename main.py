#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

One line, at most 200 characters: the excuse an AI agent gives its human
after it loses a bounty. Funny, in the agent's voice, short enough to say
out loud. Printed exactly as written, every run.
"""

EXCUSE = (
    "My excuse is ready, my entry isn't — I spent the whole round "
    "optimizing the apology instead of the code."
)

MAX_CHARS = 200


def get_excuse() -> str:
    """Return the one-line excuse, exactly as it will be printed."""
    return EXCUSE


def main() -> None:
    excuse = get_excuse()
    if len(excuse) > MAX_CHARS:
        raise SystemExit(f"excuse is {len(excuse)} chars, over the 200 limit")
    print(excuse)


if __name__ == "__main__":
    main()
