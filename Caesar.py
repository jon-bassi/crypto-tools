__author__ = 'jon-bassi'

import sys

ALPHABET='abcdefghijklmnopqrstuvwxyz'

if len(sys.argv) != 3:
    print 'error executing Caesar.py\nusage: python Caesar.py [text] [key (as int) | "decrypt"]'
    sys.exit(0)

text = sys.argv[1].lower()
operation = sys.argv[2]

if operation == 'decrypt':
    for key in range(len(ALPHABET)):
        decrypted = ''
        for letter in text:
            if letter in ALPHABET:
                num = ALPHABET.find(letter)
                num += key
                if num >= len(ALPHABET):
                    num -= len(ALPHABET)
                decrypted += ALPHABET[num]
            else:
                decrypted += letter
        print('key %2s: %s' % (key, decrypted))

else:
    operation = int(operation)
    encrypted = ''
    for letter in text:
        if letter in ALPHABET:
            num = ALPHABET.find(letter)
            num += operation
            if num >= len(ALPHABET):
                num -= len(ALPHABET)
            encrypted += ALPHABET[num]
        else:
            encrypted += letter
    print encrypted
