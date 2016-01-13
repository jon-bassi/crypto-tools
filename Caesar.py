__author__ = 'jon-bassi'

#test
import sys

ALPHABET='abcdefghijklmnopqrstuvwxyz'

text = sys.argv[1].lower()
operation = sys.argv[2]

if operation == 'decrypt':
    for key in range(len(ALPHABET)):
        decrypted = ''
        for letter in text:
            if letter in ALPHABET:
                num = ALPHABET.find(letter)
                num = num + key

                if num >= len(ALPHABET):
                    num = num - len(ALPHABET)
                decrypted += ALPHABET[num]

            else:
                decrypted += letter
        print('key %2s: %s' % (key,decrypted))

else:
    operation = int(operation)
    encrypted = ''
    for letter in text:
        if letter in ALPHABET:
            num = ALPHABET.find(letter)
            num = num + operation

            if num >= len(ALPHABET):
                num = num - len(ALPHABET)
            encrypted = encrypted + ALPHABET[num]
        else:
            encrypted = encrypted + letter
    print encrypted
