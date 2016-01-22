__author__ = 'jon-bassi'

import sys
import IndexOfCoincidence
import NGramScore
import Vignere


def iterate_key(key, index, letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newText = ''
    for idx in range(len(key)):
        if idx != index:
            newText += key[idx]
        else:
            newText += alphabet[letter]
    return newText


def modify_key(key, periodicList):
    bestKey = key
    bestScore = float(NGramScore.score(key, periodicList, 4))
    score = -1
    for index in range(0, len(key)):
        for letter in range(0, 26):
            key = iterate_key(key, index, letter)
            score = float(NGramScore.score(key, periodicList, 4))
            if score > bestScore:
                bestScore = score
                bestKey = key
            print ("%s\t%s\t%s" % (key, score, Vignere.decrypt(periodicList,key)))
        key = bestKey
    return bestKey


if len(sys.argv) != 2:
    print 'error executing HW1_2.py\nusage: python HW1_2.py [text]'
    sys.exit(0)


# find ic of different periods, target is > 0.06
# cipher text is hogvkiougtbtwlittwkopovsvebsvkiougtbtwlittwkjbd
# vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmumshwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluysdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt

text = sys.argv[1].lower()

# get the most likely key lengthIndexOfCoincidence.list_all_ic(text)
IndexOfCoincidence.list_all_ic(text)
keyLength = int(raw_input('key length: '))

# try to build a key, check the fitness of the deciphered text
key = ''
for idx in range(0, keyLength):
    key += 'a'

#lastBestKey = '0'
bestKey = ''
bestScore = float("-inf")
while True:
    #lastBestKey = bestKey
    bestKey = modify_key(key, text)
    print('%s %s' % (bestKey, Vignere.decrypt(text, bestKey)))
    input = raw_input('press enter to try again or type x to exit: ')
    if input == 'x':
        break
    lastBestKey = '0'
    key = bestKey
print('%s %s' % (bestKey, Vignere.decrypt(text, bestKey)))