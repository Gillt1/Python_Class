################################
# Program name: Triangles.py
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/1/2021
#  Assignment: Module 3 - Assignment 1: Triangles
#  Purpose: A triangle has three sides where the sum of the length of any (every) two of the sides must exceed
#  the other side.
#  In a right triangle, the square of the length of the longest side is equal to the sum of the squares of the
#  lengths of the other two sides.
#  In an isosceles triangle the length of any two of the sides must be equal.
#  In an equilateral triangle the length of all three sides must be equal.
#
# Write a program that prompts the user to enter the lengths of three sides of a triangle. The program will
# output a message indicating:
# #
# 1. whether or not the lengths form a triangle and, if so,
# 2. whether or not the triangle is
#   a. a right triangle,
#   b. an isosceles triangle, and/or
#   c. an equilateral triangle.
# Input Validation: Do not accept a number <= 0 for any side.
########################################

#First we need to load the math library and define a global var for our validator function
import math
toBeChecked = 0

#Validator Function, takes user input and checks to see if its a positive number and returns the input as an int.

def Validator(toBeChecked):
    isValid = False

    while isValid == False:
        try:
            if (int(toBeChecked) !=0 and toBeChecked.isnumeric() == True):     #var.isnumeric() will rtrn false if its a string or negative
                isValid = True
                break
            else:
                toBeChecked = input("Please enter a positive number and try again:")
        except ValueError:
            toBeChecked = input("Please enter a positive number and try again:")
    return (int(toBeChecked))

# Is it a triangle function
def triCheck(sideA, sideB, sideC):
    if (sideA + sideB <= sideC) or (sideB + sideC <= sideA) or (sideA + sideC <= sideB):
        print("Sorry but this is not a Triangle.")
    else:
        triType(sideA, sideB, sideC)


#Triangle type function, the sort is to always get the pythagorean theorem to work right.

def triType(sideA, sideB, sideC):
    sides = [sideA, sideB, sideC]
    sides_sorted = sorted(sides)
    if math.sqrt(sides_sorted[0]**2 + sides_sorted[1]**2) == sides_sorted[2]:
        print("Nice! You have a Right Triangle!")
    elif sideA == sideB and sideB == sideC:
        print("Awsome, this is an equilateral Triangle!")
    elif sideA == sideB or sideB == sideC or sideA == sideC:
        print("Cool, this is an isosceles Triangle!")
    else:
        print("Huh, this is a triangle, just not a special type.")

def main():
    name = input("Hey there, whats your name?")
    print("Thanks",name,"now lets see what kind of Triangle you have!")
    sideA = Validator(input("First I'm going to need the length of the first side:"))
    sideB = Validator(input("Now, lets get the length of that second side:"))
    sideC = Validator(input("Ok, One more side left, give it to me please:"))
    triCheck(sideA, sideB, sideC)

main()



