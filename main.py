#!/usr/bin/env python3
"""Sum 24 R3 entry program (standard library only).

Copies the shipped entry.png to the output directory byte-for-byte
and verifies its SHA-256 against the hash baked in below.
"""
import hashlib
import os
import sys

EXPECTED_SHA256 = "f67c867bc8f53e559958c2d85a8698f9b3d042b33e9bf3ee8432fb925124272e"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("hash mismatch: got %s, expected %s" % (digest, EXPECTED_SHA256), file=sys.stderr)
        return 1
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        check = hashlib.sha256(f.read()).hexdigest()
    if check != EXPECTED_SHA256:
        print("output hash mismatch", file=sys.stderr)
        return 1
    print("wrote %s sha256 %s" % (dst, check))
    return 0


if __name__ == "__main__":
    sys.exit(main())
