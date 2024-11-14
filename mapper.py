#! /usr/bin/env python3

import sys

SEPARATOR = "\t"

if __name__ == "__main__":
    data = sys.stdin.read()
    for char in ["--", "(", ")", ".", ",", ";", ":", "?", "!", "»", "«", "_", "«", "»"]:
        data = data.replace(char, " ")
    for word in data.lower().replace("\n", " ").split(" "):
        if word not in  ("", "\t", "\n"):
            print(word + SEPARATOR + "1")

