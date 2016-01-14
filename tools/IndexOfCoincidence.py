__author__ = 'jon-bassi'

import sys


def index_coincidence(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ic = 0.0
    n = len(text)
    for letter in alphabet:
        fi = 0
        for char in text:
            if char == letter:
                fi += 1
        ic += fi * (fi - 1)
    ic /= (n * (n - 1))

    return ic

if len(sys.argv) != 2:
    print 'error executing IndexOfCoincidence.py\nusage: python IndexOfCoincidence.py [text]'
    sys.exit(0)

print index_coincidence(sys.argv[1].lower())
