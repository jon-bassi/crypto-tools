__author__ = 'jon-bassi'

import sys
import math
import Vignere

# load files into memory - increase load time, decrease runtime
mono = 'english_monograms'
bi = 'english_bigrams'
tri = 'english_trigrams'
quad = 'english_quadgrams'

monograms = {}
mN = 0.0
for line in file(mono):
    key, score = line.split(' ')
    monograms[key.lower()] = float(score)
    mN += float(score)

bigrams = {}
bN = 0.0
for line in file(bi):
    key, score = line.split(' ')
    bigrams[key.lower()] = float(score)
    bN += float(score)

trigrams = {}
tN = 0.0
for line in file(tri):
    key, score = line.split(' ')
    trigrams[key.lower()] = float(score)
    tN += float(score)

quadgrams = {}
qN = 0.0
for line in file(quad):
    key, score = line.split(' ')
    quadgrams[key.lower()] = float(score)
    qN += float(score)


def calculate_log_score(text, option):
    '''
    calculates the log score of the undecrypted text, using mongram -> quadgram statistics
    :param text:
    :param option:
    :return:
    '''
    ngrams = {}
    ngrams_list = []
    n = 0
    if option == 1:
        print 'not supported yet'
        ngrams = monograms
        n = mN
        return
    elif option == 2:
        print 'not supported yet'
        ngrams = bigrams
        n = bN
        return
    elif option == 3:
        print 'not supported yet'
        ngrams = trigrams
        n = tN
        return
    elif option == 4:
        for start in range(0, len(text) - 3):
            ngrams_list.append(text[start:start + 4])
        ngrams = quadgrams
        n = qN
    else:
        print 'must chose a number between 1 and 4'
        return
    logScore = 0.0
    for ngram in ngrams_list:
        if ngram in ngrams:
            logScore += float(math.log10(ngrams[ngram] / n))
        else:
            logScore += float(math.log10(0.01 / n))
    return logScore


def iterate_key(key, index, letter):
    '''
    increment the given index of the key by one letter
    :param key:
    :param index:
    :param letter:
    :return:
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newText = ''
    for idx in range(len(key)):
        if idx != index:
            newText += key[idx]
        else:
            newText += alphabet[letter]
    return newText


def find_best_key(key, cipherText):
    '''
    finds the best scoring key by modifying the key one letter at a time and calculating the log score
    :param key:
    :param cipherText:
    :return:
    '''
    bestKey = key
    bestScore = float(calculate_log_score(Vignere.decrypt(cipherText, key), 4))
    score = -1
    for index in range(0, len(key)):
        for letter in range(0, 26):
            key = iterate_key(key, index, letter)
            score = float(calculate_log_score(Vignere.decrypt(cipherText, key), 4))
            if score > bestScore:
                bestScore = score
                bestKey = key
            print ("%s\t%s\t%s" % (key, score, Vignere.decrypt(cipherText,key)))
        key = bestKey
    return bestKey

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'error executing NGramScore.py\nusage: python NGramScore.py [text] [key size]'
        sys.exit(0)
    text = sys.argv[1]

    keySize = int(sys.argv[2])
    key = ''
    # could make this a random key
    for i in range(0, keySize):
        key += 'a'

    while True:
        bestKey = find_best_key(key, text)
        print('%s %s' % (bestKey, Vignere.decrypt(text, bestKey)))
        input = raw_input('press enter to try again or type x to exit: ')
        if input == 'x':
            break
        key = bestKey
