#!/usr/bin/env python3
import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    if len(text) < 8:
        print(text + "Z" * (8 - len(text)))
    else:
        print(text)


if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        else:
            enlarge(param)
