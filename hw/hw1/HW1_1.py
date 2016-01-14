__author__ = 'jon-bassi'

import sys
import IndexOfCoincidence
#import Vignere


if len(sys.argv) != 2:
    print 'error executing IndexOfCoincidence.py\nusage: python HW1_1.py [text]'
    sys.exit(0)

# find ic of different periods, target is > 0.06
# cipher text is hogvkiougtbtwlittwkopovsvebsvkiouzwmalwbbslwacav
# vptnvffuntshtarptymjwzirappljmhhqvsubwlzzygvtyitarptyiougxiuydtgzhhvvmumshwkzgstfmekvmpkswdgbilvjljmglmjfqwioiivknulvvfemioiemojtywdsajtwmtcgluysdsumfbieugmvalvxkjduetukatymvkqzhvqvgvptytjwwldyeevquhlulwpkt

text = sys.argv[1].lower()
for i in range(2, len(text) / 2):
    avgIC = 0.0
    strList = []
    for letterIdx in range(len(text)):
        strList.append('')
        strList[letterIdx % i] += text[letterIdx]
    for string in strList:
        avgIC += IndexOfCoincidence.index_coincidence(string)
    avgIC /= i
    print ("Size: %2s  %s" % (i, avgIC))

