__author__ = 'jon-bassi'

import sys
import math
import Caesar

def chi_squared(text):
    """
    determines chi-squared statistic of a given string of text
    :param text:
    :return chiSquared:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # expected occurrence of every standard english letter
    expectedCount = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
                     0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
                     0.02758, 0.00978, 0.02361, 0.00150, 0.01974, 0.00074]

    actualCount = [0.0] * 26

    for letter in text:
        idx = alphabet.find(letter)
        actualCount[idx] += 1
    chiSquared = 0.0
    for i in range(0, 25):
        expectedCount[i] *= len(text)
        chiSquared += (math.pow((actualCount[i] - expectedCount[i]), 2)) / expectedCount[i]
    return chiSquared


def list_all_cs(text):
    """
    lists chi-squared statistic for all caesar shifts of the text, returns the user's choice of key to proceed with
    :param text:
    :return key:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(0, 26):
        decrypted = Caesar.decrypt(text, i)
        print ('key %2s  %s %10.4f' % (i, decrypted, chi_squared(decrypted)))
    return alphabet[int(raw_input('key choice: '))]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'error executing ChiSquaredStatistic.py\nusage: python ChiSquaredStatistic.py [text]'
        sys.exit(0)
    print chi_squared(sys.argv[1].lower())
