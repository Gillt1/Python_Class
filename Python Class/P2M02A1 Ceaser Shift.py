################################
# Program name:
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/23/2021
#  Assignment: P2M02A1 Ceaser Shift
#  Purpose:
#  Create a program that can encrypt and decrypt a text message using a Caser encryption scheme.
#  The program should use two functions (one to encrypt the message and one to decrypt the message) receiving
#  the message (plaintext or cyphertext accordingly) and the Caesar shift offset. Demonstrate it works by
#  encrypting/decrypting several messages showing the original plaintext, the encrypted cyphertext, and the
#  decrypted plain text. Remember to keep all characters in the printable ASCII range, when you shift an ASCII value
#  above 127 you need to subtract 95 and when you shift an ASCII value below 32 you need to add 95.

#                                       Global variables and imports
import sys

#                                       Functions


def keyValidator(key):
    """
    Validates user key to be a number between 2 and 126
    :param key:
    :return :
    """
    try:
        key = int(key)
    except:
        return False
    if key < 2 or key > 126:
         return False
    else:
         return key


def encypher(plaintext, key):
    """
    Encodes plain text input with a given key.
    :param plaintext:
    :param key:
    :return: encoded text
    """
    key = int(key)
    codedText = []

    for letter in plaintext:
        codedLetterOrd = ord(letter.upper()) + key
        if codedLetterOrd > 127:
            codedLetterOrd -= 95
        codedText.append(chr(codedLetterOrd))
    return "".join(codedText)


def decypher(codedText, key):
    """
    Decodes encoded txt with a given key.
    :param codedText:
    :param key:
    :return: Decoded text
    """
    key =int(key)
    plaintext = []

    for letter in codedText:
        decodedLeterOrd = ord(letter) - key
        if decodedLeterOrd < 32:
            decodedLeterOrd += 95
        plaintext.append(chr(decodedLeterOrd).lower())
    return "".join(plaintext)


def main():
    """
    Main menu for the cipher program.
    :return:
    """
    print("\nTOMOOGLE encryption, we are better than nothing!")
    print("Would you like to encode some text or decode some text?\n")
    selection = input("Enter 1 for encode, 2 for decode, 3 to quit:")

    if selection == "1":
        plaintext = input("Enter your secret message here:")
        key = input("Enter your key, 2-126:")
        while True:
            if keyValidator(key):
                break
            else:
                print("C'mon Brutus, enter a number 2-126:", end="")
                key = input()
        cyphertext = encypher(plaintext, key)
        print("Your secret code is:")
        print(cyphertext)
        print("")
        main()

    elif selection == "2":
        cyphertext = input("Enter your coded message here:")
        key = input("Enter your key, 2-126:")
        while True:
            if keyValidator(key):
                break
            else:
                print("C'mon Burtus, enter a number 2-126:", end="")
                key = input()
        decypheredtext = decypher(cyphertext, key)
        print(decypheredtext)
        print("")
        main()

    elif selection == "3":
        print("\nThank you for using TOMOOGLE security, We'd never stab you in the back!")
        sys.exit()

    else:
        main()



main()