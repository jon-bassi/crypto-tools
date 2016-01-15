__author__ = 'jon-bassi'

import sys


def index_coincidence(text):
    """
    finds the index of coincidence for a given string
    :param text:
    :return ic:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ic = 0.0
    n = len(text)
    if n == 0 or n == 1:
        return 0
    for letter in alphabet:
        fi = 0
        for char in text:
            if char == letter:
                fi += 1
        ic += fi * (fi - 1)
    ic /= (n * (n - 1))
    return ic


def list_all_ic(text):
    """
    lists all indicies of coincidence for a encrypted string
    :param text:
    :return None:
    """
    for i in range(2, len(text) / 2):
        avgIC = 0.0
        strList = []
        for letterIdx in range(len(text)):
            strList.append('')
            strList[letterIdx % i] += text[letterIdx]
        for string in strList:
            avgIC += index_coincidence(string)
        avgIC /= i
        print ("Size: %2s  %s" % (i, avgIC))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'error executing IndexOfCoincidence.py\nusage: python IndexOfCoincidence.py [text]'
        sys.exit(0)

    print index_coincidence(sys.argv[1].lower())
