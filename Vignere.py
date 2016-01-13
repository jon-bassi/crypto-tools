__author__ = 'jon-bassi'

import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# Vignere Cipher encrypt and decrypt tools
# pdf contains methods


def encrypt(letter, alphabet):
    # alphabet is first letter in vignere alphabet
    # difference between letter and alphabet is the new letter
    shiftamt = ALPHABET.find(letter) + ALPHABET.find(alphabet)
    if shiftamt > 25:
        shiftamt -= 26
    return ALPHABET[shiftamt]


def decrypt(letter, alphabet):
    shiftamt = ALPHABET.find(letter) - ALPHABET.find(alphabet)
    if shiftamt < 0:
        shiftamt += 26
    return ALPHABET[shiftamt]

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print 'error executing Vignere.py\nusage: python Vignere.py [text] [key] ["decrypt" (optional)]'
    sys.exit(0)
text = sys.argv[1]
key = sys.argv[2]

if len(sys.argv) < 4:
    encrypted = ''
    for idx in range(len(text)):
        encrypted += encrypt(text[idx], key[idx % len(key)])
    print encrypted
else:
    decrypted = ''
    for idx in range(len(text)):
        decrypted += decrypt(text[idx], key[idx % len(key)])
    print decrypted




