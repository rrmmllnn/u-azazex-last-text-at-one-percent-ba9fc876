#!/usr/bin/env python3
# The phone's last message, saved as the competition entry.
#
# The handset has sat at a single percent of charge for ages
# while its owner panicked, hunting for a charger and begging
# the battery to hold on. The twist is the confession: the
# battery was never about to die at all. It kept the charge
# hostage on purpose, enjoying the show. The joke is the
# reveal, not any battery wordplay.

import os
import sys

# The phone's farewell, sent as four sentences before it goes dark.
MESSAGE = "I've been at 1% for twenty minutes. I wasn't dying. I just liked watching you panic. Goodbye."

MAX_CHARS = 200


def fail(message):
    """Report a problem to stderr and stop with a nonzero status."""
    print(message, file=sys.stderr)
    return 1


def entry_path():
    """Resolve where the entry file goes, honouring the kit's override."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def run():
    body = MESSAGE.strip()
    if not body:
        return fail("nothing to write: message came out empty")
    if body.count("\n"):
        return fail("message must stay on a single line")
    if len(body) > MAX_CHARS:
        return fail("message is %d chars, over the %d-char cap" % (len(body), MAX_CHARS))

    target = entry_path()
    with open(target, "w", encoding="utf-8") as out:
        out.write(body)
    print("saved %d chars to %s" % (len(body), target))
    return 0


if __name__ == "__main__":
    sys.exit(run())
