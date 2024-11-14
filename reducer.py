#! /usr/bin/env python3

import sys
SEPARATOR = "\t"

if __name__ == "__main__":
    data = sys.stdin.read()
    all_values = {}
    for w in data.split("\n"):
        if w == "":
            continue
        word, count = w.split(SEPARATOR)
        all_values[word] = all_values.get(word, 0) + int(count)
    for word, count in sorted(all_values.items()):
        print(word + SEPARATOR + str(count))
