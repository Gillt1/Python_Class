################################
# Program name: Mod4 Lab ATM.py
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/9/2021
#  Assignment: Module 3 - Lab Assignment: ATM
#  Purpose: Create a functional ATM with Deposit, Withdraw, Check balance etc.

shoppinglist = set()

while True:
    choice = input("""Welcome to your enhanced Shopping list:\nEnter 1 to Add Item\nEnter 2 to Remove Item\nEnter 3 to see list or press Enter to finish: """)
    if choice == "":
        break
    elif choice == "1":
        item = input("What would you like to add?")
        shoppinglist.add(item)
    elif choice == "2":
        item = input("What would you like to remove?")
        shoppinglist.remove(item)
    elif choice == "3":
        print("Your Shopping List\n-----------------")
        for item in shoppinglist:
            print(item)
        print("-----------------")
    else:
        print("Please enter a valid choice.")


