__author__ = 'jon-bassi'

import math
import Vignere

# load files
mono = 'english_monograms'
bi = 'english_bigrams'
tri = 'english_trigrams'
quad = 'english_quadgrams'


def calculate_log_score(text, option):
    ngrams = {}
    ngrams_list = []
    if option == 1:
        print 'not supported yet'
        return
    elif option == 2:
        print 'not supported yet'
        return
    elif option == 3:
        print 'not supported yet'
        return
    elif option == 4:
        for line in file(quad):
            key, score = line.split(' ')
            ngrams[key.lower()] = float(score)
        for start in range(0, len(text) - 3):
            ngrams_list.append(text[start:start + 4])
    else:
        print 'must chose a number between 1 and 4'
        return
    logScore = 0.0
    n = 0
    for key in ngrams:
        n += float(ngrams[key])
    for ngram in ngrams_list:
        if ngram in ngrams:
            logScore += float(math.log10(ngrams[ngram] / n))
        else:
            logScore += float(math.log10(0.01 / n))
    return logScore


def score(key, cipherText, option):
    decipheredText = Vignere.decrypt(cipherText, key)
    return calculate_log_score(decipheredText, option)
