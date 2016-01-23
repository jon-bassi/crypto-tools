__author__ = 'jon-bassi'

import sys
import IndexOfCoincidence
import NGramScore
import Vignere


if len(sys.argv) != 2:
    print 'error executing HW1_2.py\nusage: python HW1_2.py [text]'
    sys.exit(0)

text = sys.argv[1].lower()

# find most likely key length
IndexOfCoincidence.list_all_ic(text)
keyLength = int(raw_input('key length: '))

# build a key of all a's of length specified above
key = ''
for idx in range(0, keyLength):
    key += 'a'

bestKey = ''
bestScore = float("-inf")
while True:
    '''
    find the best key by changing every character as described in source material
    e.g. aaaaa -> baaaa -> caaaa -> ... -> zzzzz, retaining the best character for each index in the key
    '''
    bestKey = NGramScore.find_best_key(key, text)
    print('%s %s' % (bestKey, Vignere.decrypt(text, bestKey)))
    input = raw_input('press enter to try again or type x to exit: ')
    if input == 'x':
        break
    lastBestKey = '0'
    key = bestKey
print('%s %s' % (bestKey, Vignere.decrypt(text, bestKey)))