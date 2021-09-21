################################
# Program name:
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/16/2021
#  Assignment: MOD01A1 Phone List
#  Purpose: Write a program that provides a menu-driven digital contact list to the user. The program should utilize a
#  file containing names, phone numbers (number and type - such as Cell, Home, Work, etc.) and email addresses (address
#  and type).
#
# The program should open the file (if it exists) and populate the program with the contact data.
# The user should then be able to
#   search for the data for a given contact name
#   add new contacts
#   delete contacts
#   add/update/delete phone numbers or email addresses for a contact.
# When the program finishes it should create a file (or overwrite the existing file) with the contact information

# Store any functions you create in a package separate from the 'main' menu-driven program/script and import them as
# needed.

#                                       Global variables and imports
import sys

#                                       Functions

def mainMenu():
    phoneBook = open("phoneBook.txt","a")
    phoneBook.close()
    print("\nWelcome to contacts by TOMOOGLE.")

    while True:
        print("\n*****Contacts by TOMOOGLE*****",
        "\nPlease enter your one of the below selections:",
        "\nEnter 1 to search for and view a contact.",
        "\nEnter 2 to search for and edit a contact.",
        "\nEnter 3 to add a new contact.",
        "\nEnter 4 to remove a contact.",
        "\nEnter 5 to exit.",)
        selection = input("Selection: ")
        print("\n")
        if selection == "5":                                        # Quit Program
            print("\nThank you for using TOMOOGLE contacts.")
            sys.exit()

        elif selection == "1":                                      # search for and return a contact
            print("Please enter contacts last name, first name to view their information.")
            name = input("Lastname, Firstname: ")
            print("\n")
            phoneBook = open("phoneBook.txt", "r")
            for line in phoneBook:
                if line.find(name) != -1:
                    print(line)
            print("Please note: if the name you searched for returns no results, it was not in your contact list.\n")

        elif selection == "2":                                      # search for and edit a contact
            print("Please enter the exact information you want to replace.")
            print("For example, if you want to replace a phone number, "
                  "enter the phone number exactly as you entered it.")
            search_info = input("Enter information to be corrected: ")
            replace_info = input("Now please enter the correct information: ")
            with open ("phoneBook.txt", "r") as file:
                corrected = file.read()
                corrected = corrected.replace(search_info, replace_info)
            with open("phoneBook.txt", "w") as file:
                file.write(corrected)
            print("Correction Made")

        elif selection == "3":                                      # add new contact
            phoneBook = open("phoneBook.txt", "a")
            newContact = input("Please enter contacts Lastname: ")
            newContact = newContact + ", " + input("Please enter contacts First name: ")
            newContact = newContact + "; " + input("Phone number type: ")
            newContact = newContact + ": " + input("Phone number: ")
            newContact = newContact + "; " + input("Email Type: ")
            newContact = newContact + ": " + input("Email address: ")
            phoneBook.write(newContact)
            phoneBook.write("\n")
            phoneBook.close()
            continue

        elif selection == "4":                                       # remove a contact
            with open("phoneBook.txt", "r") as phoneBook:
                lines = phoneBook.readlines()
                contact = input("Enter Contact name (Last, First) to remove: ")
            with open("phoneBook.txt", "w") as phoneBook:
                for line in lines:
                    if line.find(contact) == -1:
                        phoneBook.write(line)
            print("Removed.")

        else:
            print("Please enter a valid selection, its not hard (1, 2, 3 or 4).")

mainMenu()