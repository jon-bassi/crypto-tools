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


def decrypt_all(text):
    """
    displays all decryptions
    :param text:
    :return:
    """
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


def decrypt(text, key):
    """
    displays single decryption
    :param text:
    :param key:
    :return:
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    for letter in text:
        if letter in alphabet:
            num = alphabet.find(letter)
            num -= key
            if num < 0:
                num += len(alphabet)
            decrypted += alphabet[num]
        else:
            decrypted += letter
    return decrypted


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'error executing Caesar.py\nusage: python Caesar.py [text] [key (as int) | "decrypt"]'
        sys.exit(0)
    operation = sys.argv[2]

    if operation == 'decrypt':
        decrypt_all(sys.argv[1].lower())

    else:
        operation = int(operation)
        print encrypt(sys.argv[1].lower(), operation)
