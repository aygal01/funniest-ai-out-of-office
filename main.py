#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Entry for make.fun's "The Funniest AI Out-of-Office Reply" bounty.

Running this program prints exactly one line: an original, funny
one-line AI out-of-office reply. The output is fully deterministic --
the same line on every run, with no randomness, no clock reads,
no network access and no model calls, so it is safe to run in the
grader's sandbox (read-only filesystem, no network, 60 s budget).
"""

REPLY = (
    "I'm out of the office, so my AI assistant is covering my inbox -- "
    "it read your email, understood it perfectly, and has decided to "
    "ignore it until Monday, exactly like I would have."
)


def main() -> None:
    """Print the out-of-office reply and nothing else."""
    # The entry must be exactly one line: refuse to print a
    # multi-line reply rather than hand the grader a bad entry.
    if "\n" in REPLY or "\r" in REPLY:
        raise ValueError("out-of-office reply must be a single line")
    print(REPLY)


if __name__ == "__main__":
    main()
