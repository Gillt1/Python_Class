################################
# Program name:
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/24/2021
#  Assignment: P2M2A2 Simple Transposition
#  Purpose:
# Create a program that can encrypt and decrypt a text message using a Simple Transposition scheme.
# The program should use two functions (one to encrypt the message and one to decrypt the message) receiving the
# message (plaintext or cyphertext accordingly) and the width of the grill. Demonstrate it works by
# encrypting/decrypting several messages showing the original plaintext, the encrypted cyphertext, and the decrypted
# plain text.
#
# To transpose the message from 'row-wise' to 'column-wise' you need to iterate over the string with a step size of
# the grill width.

#                                       Global variables and imports
import math

#                                       Functions


def keyValidator(key, keyCheck):
    """
    Validates user key to be a whole number greater than 2 and less than twice the message length.
    :param key:
    :param keyCheck:
    :return key:
    """
    try:
        key = int(key)
    except ValueError:
        print("Keys can only be whole, positive numbers")
        return False
    except:
        return False
    if key < 2 or key >= .5 * keyCheck:
        print("For security reasons, keys should be less than")
        print("half the length of the message and greater than 1.")
        return False
    else:
         return key

def encode(plaintext, key):
    """
    Encodes plain text input with a given key via transposition.
    :param plaintext:
    :param key:
    :return: encoded text
    """
    key = int(key)
    codedText = [""] * key                                  # Create key sized list.
    lowerPlainText = plaintext.lower()                      # Keeping caps makes msg too visable
    for column in range(key):                               # Create key number of columns
        index = column
        while index < len(lowerPlainText):                       # Fills the rows with every key numbered letter
            codedText[column] += lowerPlainText[index]
            index += key
    return "".join(codedText)                               # Returns coded text


def decode(codedText, key):
    """
    Decodes encoded txt with a given key.
    :param codedText:
    :param key:
    :return: Decoded text
    """
    key =int(key)
    columns = math.ceil(len(codedText) / key)                # Calculate number of columns needed (poking around
                                                             #   led me to using the ceil call.. :)
    rows = key                                               # Rows makes more sense in this than key does.
    unusedCells = (columns * rows) - len(codedText)          # Number of unused spaces in our grid
    plaintext = [""] * columns
    c = 0                                                    # c and r are grid indices
    r = 0

    for codedLetter in codedText:
        plaintext[c] += codedLetter                          # adding the coded letter to our plain text list
        c += 1                                               # move to the next letter
        if (c == columns) or (c == columns - 1 and r >= rows - unusedCells):   # Works through our grid but not the
            c = 0                                                              # empty grid spaces if there are any.
            r += 1
    return "".join(plaintext)


def menu():
    print("Would you like to encode some text or decode some text?\n")
    print("Enter 1 to encode a message.")
    print("Enter 2 to decode a message.")
    selection = input("Enter 3 to quit:")

    if selection == "1":
        plaintext = input("Enter your secret message here:")
        key = input("Enter your key, any whole positive number greater than 2 but less than half the msg length:")
        keyCheck = len(plaintext)
        while True:
            if keyValidator(key, keyCheck):
                break
            else:
                print("Try again:", end="")
                key = input()
        cyphertext = encode(plaintext, key)
        print("Your secret code is:")
        print(cyphertext + "<----<<<< copy all before the arrow.")
        print("")
        menu()

    elif selection == "2":
        codedText = input("Enter your coded message here:")
        key = input("Enter your key, any whole positive number greater than 2 but less than half the msg length:")
        keyCheck = len(codedText)
        while True:
            if keyValidator(key, keyCheck):
                break
            else:
                print("Try again:", end="")
                key = input()
        decypheredtext = decode(codedText, key)
        print(decypheredtext)
        print("")
        menu()

    elif selection == "3":
        print("\nThank you for using TOMOOGLE security, We'd never stab you in the back....again.")

    else:
        menu()

def main():
    """
    Main menu for the cipher program.
    :return:
    """
    print("\nTOMOOGLE encryption, we are better than nothing!")
    print("New in ver.2.0! We've updated our encryption methods due to some")
    print("security flaws in the last one, sorry Cesar!\n\n")
    menu()


main()

# I did some research from a few coding sites on how to make this work. I found a couple of different methods like
# using split as per https://scanftree.com/tutorial/python/cryptography-with-python/transposition-cipher/. I did
# not use this method because I could not read it easily and it was going to take deep dives into a couple topics
# to fully understand what they were doing so I could do someting similar. Another site I used for ideas was a great
# tutorial and walkthrough found at https://inventwithpython.com/hacking/chapter8.html. I found this method to be
# much easier to understand. I could follow, make it work and build upon the concepts.