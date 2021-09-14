################################
# Program name: Mod4 Lab ATM.py
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/9/2021
#  Assignment: Module 3 - Lab Assignment: ATM
#  Purpose: Create a functional ATM with Deposit, Withdraw, Check balance etc.

import sys

checkingAcc = {
    "Account Number" : 8675309,
    "Balance" : 420.69,
    "Type" : "Checking",
}
savingsAcc = {
    "Account Number" : 5318008,
    "Balance" : 69420.00,
    "Type" : "Savings",
}
# Balance validation.
def amountValidator(userInput, depWithdraw, balance):
    try:
        userInput = float(userInput)
    except:
        print("*" * 70)
        print("Invalid entry, think about what you want to do while I take you back to main menu.")
        print("*" * 70)
        mainMenu()
    if depWithdraw == "dep" and userInput > 0:
        return userInput
    elif depWithdraw == "wd" and userInput > 0 and userInput <= balance:
        return userInput
    else:
        print("*" * 70)
        print("Invalid entry, think about what you want to do while I take you back to main menu.")
        print("*" * 70)
        mainMenu()

def subMenu():
    while True:
        type = input("""Checking or Savings?
        Press 1 for Checking
        Press 2 for Savings
        Press 3 to return: """)
        if type == "1" or type == "2":
            print ()
            return type
            break
        if type == "3":
            mainMenu()
            break
        else:
            print("Please enter a valid selection, its not rocket science (1,2 or 3): ")

# def depositWithdraw(selection, type):
#     if type == "1":
def mainMenu():
    while True:
        selection = input("""\t\t*****Welcome to Bank of Tom!*****
        Please enter your one of the below selections:
        Enter 1 to check your balance.
        Enter 2 to make a deposit.
        Enter 3 to make a withdrawal.
        Enter 4 to exit.
        Selection: """)
        if selection == "4":        # Quit Program
            print("Thank you for banking with BoT, your information is safe with me...ugh.. Us!")
            sys.exit()
        elif selection == "1":      # Balance Check
            type = subMenu()        # Checking 1, Savings 2
            if type == "1":
                print("Your account balance is $",checkingAcc["Balance"])
            if type == "2":
                print("Your account balance is $",savingsAcc["Balance"])
        elif selection == "2":      # Deposits
            type = subMenu()        # Checking 1, Savings 2
            if type == "1":
                amount = input("How much would you like to give me, I mean deposit today?:")
                amount = amountValidator(amount, "dep", checkingAcc["Balance"])
                checkingAcc["Balance"] += amount
                print("Your account balance is now $",checkingAcc["Balance"])
            if type == "2":
                amount = input("How much would you like to give me, I mean deposit today?:")
                amount = amountValidator(amount, "dep", savingsAcc["Balance"])
                savingsAcc["Balance"] += amount
                print("Your account balance is now $",savingsAcc["Balance"])
        elif selection == "3":      # Withdrawals
            type = subMenu()        # Checking 1, Savings 2
            if type == "1":
                amount = input("Are you sure you want to do this? Ok, fine. How much?:")
                amount = amountValidator(amount, "wd", checkingAcc["Balance"])
                checkingAcc["Balance"] -= amount
                print("Your account balance is now $", checkingAcc["Balance"])
            if type == "2":
                amount = input("Are you sure you want to do this? Ok, fine. How much?:")
                amount = amountValidator(amount, "wd", savingsAcc["Balance"])
                savingsAcc["Balance"] -= amount
                print("Your account balance is now $", savingsAcc["Balance"])
        else:
            print("Please enter a valid selection, its not hard (1, 2, 3 or 4).")

mainMenu()
