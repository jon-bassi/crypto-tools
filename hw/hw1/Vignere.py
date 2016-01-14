__author__ = 'jon-bassi'

import sys

# Vignere Cipher encrypt and decrypt tools


def encrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # alphabet is first letter in vignere alphabet
    # difference between letter and alphabet is the new letter
    encrypted = ''
    for letter in range(len(text)):
        shiftamt = alphabet.find(text[letter]) + alphabet.find(key[letter % len(key)])
        if shiftamt > 25:
            shiftamt -= 26
        encrypted += alphabet[shiftamt]
    return encrypted


def decrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    for letter in range(len(text)):
        shiftamt = alphabet.find(text[letter]) - alphabet.find(key[letter % len(key)])
        if shiftamt < 0:
            shiftamt += 26
        decrypted += alphabet[shiftamt]
    return decrypted

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print 'error executing Vignere.py\nusage: python Vignere.py [text] [key] ["decrypt" (optional)]'
        sys.exit(0)

    if len(sys.argv) < 4:
        print encrypt(sys.argv[1].lower(), sys.argv[2].lower())
    else:
        print decrypt(sys.argv[1].lower(), sys.argv[2].lower())
