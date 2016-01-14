__author__ = 'jon-bassi'

import sys


def encrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for letter in text:
        if letter in alphabet:
            num = alphabet.find(letter)
            num += key
            if num >= len(alphabet):
                num -= len(alphabet)
            encrypted += alphabet[num]
        else:
            encrypted += letter
    return encrypted


def decrypt(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(len(alphabet)):
        decrypted = ''
        for letter in text:
            if letter in alphabet:
                num = alphabet.find(letter)
                num += key
                if num >= len(alphabet):
                    num -= len(alphabet)
                decrypted += alphabet[num]
            else:
                decrypted += letter
        print('key %2s: %s' % (key, decrypted))


if len(sys.argv) != 3:
    print 'error executing Caesar.py\nusage: python Caesar.py [text] [key (as int) | "decrypt"]'
    sys.exit(0)
operation = sys.argv[2]

if operation == 'decrypt':
    decrypt(sys.argv[1].lower())

else:
    operation = int(operation)
    print encrypt(sys.argv[1].lower(), operation)
