__author__ = 'jon-bassi'

import math
import Vignere

# load files into memory
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


def score(key, cipherText, option):
    decipheredText = Vignere.decrypt(cipherText, key)
    return calculate_log_score(decipheredText, option)
