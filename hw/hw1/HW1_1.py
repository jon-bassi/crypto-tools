__author__ = 'jon-bassi'

import sys
import IndexOfCoincidence
import Vignere
import ChiSquaredStatistic


if len(sys.argv) != 2:
    print 'error executing IndexOfCoincidence.py\nusage: python HW1_1.py [text]'
    sys.exit(0)

# find ic of different periods, target is > 0.06
# cipher text is hogvkiougtbtwlittwkopovsvebsvkiougtbtwlittwkjbd
# vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmumshwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluysdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt

text = sys.argv[1].lower()
IndexOfCoincidence.list_all_ic(text)
keyLength = int(raw_input('key length: '))

periodicList = [''] * keyLength
for idx in range(len(text)):
    periodicList[idx % keyLength] += text[idx]

key = ''
for string in periodicList:
    key += ChiSquaredStatistic.list_all_cs(string)
print ('key: %s\ndecrypted text: %s' % (key, Vignere.decrypt(text, key)))
