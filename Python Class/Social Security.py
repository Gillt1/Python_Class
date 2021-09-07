################################
# Program name: Social Security.py
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/2/2021
#  Assignment: Module 3 - Assignment 2: Social Security
#  Purpose: The full retirement age for social security has changed over the years:
#
# 65 for those born before 1943
# 66 for people born between 1943 and 1954
# 66 and 2 months for those born before 1957.
# 66 and 4 months for someone born before 1958,
# 66 and 6 months for someone born before 1960, and
# 67 for people born 1960 or later.
# While Social Security takes a user's 35 best-paid years and produces what it calls an average indexed monthly
# earnings (AIME), we will calculate "our" Social Security payout based on a user's stated current monthly income.
#
# Social Security then applies a formula to that monthly income to determine a user's retirement benefit (That’s
# the amount they’ll get each month from Social Security at their full retirement age).
#
# 90 percent of the first $996 of the user's monthly income;
# plus 32 percent of any amount over $996 up to $6,002
# plus 15 percent of any amount over $6,002.
# Write a program that prompts the user to enter their date of birth (month, day, and year) along with their current
# monthly income. The program will output a message indicating the date they will reach full retirement and the amount
# they will be eligible to collect.
#
# Input Validation: Do not accept a number <= 0 for monthly income, a value < 1 or > 12 for the month, a value
# < 1 or > 31 for the day and a value < 1940 or > 2021 for the year.
#######################################################################################################################
# Any imports or global variables will go here:
from datetime import date
from dateutil.relativedelta import relativedelta

#######################################################################       Function creations begin here:

# Income validator.. I couldn't make this work with the other one
def incomeValidator(userInput):
    try:
        userInput = float(userInput)
    except:
        return False
    return userInput > 0

# This function allows for 2 parameter conditions for the input
def dateValidator(userInput, cond1, cond2):
    try:
        userInput = int(userInput)
    except:
        return False
    return userInput >= cond1 and userInput <= cond2 and userInput !=0

# Gets Validated User Income
def getUserIncome(prompt="Please enter your monthly income:"):
    while True:
        userInput = input(prompt)
        if incomeValidator(userInput):
            return float(userInput)
        else:
            print("That's not a valid income!")

# Gets Validated User Birth Year
def getUserYear(prompt="Please enter your birth year (1940-2021) in whole numbers:"):
    while True:
        userInput = input(prompt)
        if dateValidator(userInput,1940, 2021):
            return int(userInput)
        else:
            print("That's not a valid birth year.")

# Gets Validated User Birth Month
def getUserMonth(prompt="Please enter your birth month (1-12) in whole numbers:"):
    while True:
        userInput = input(prompt)
        if dateValidator(userInput,1, 12):
            return int(userInput)
        else:
            print("That's not a valid birth month.")

# Gets validated User Birth Day of the Month
def getUserDay(prompt="Please enter your birth day of the month (1-31) in whole numbers:"):
    while True:
        userInput = input(prompt)
        if dateValidator(userInput,1, 31):
            return int(userInput)
        else:
            print("That's not a valid birth day of the month.")

# Returns date of Users Retirement.
def getUserRetAge(month, day, year):
    retTest = date(year, month, day)
    if year < 1943:
        retTest = retTest + relativedelta(years=+65)
    elif year <=1954 and year >= 1943:
        retTest = retTest + relativedelta(years=+66)
    elif year < 1957 and year > 1954:
        retTest = retTest + relativedelta(years=+66, months=+2)
    elif year == 1957:
        retTest = retTest + relativedelta(years=+66, months=+4)
    elif year < 1960 and year >= 1958:
        retTest = retTest + relativedelta(years=+66, months=+6)
    else:
        retTest = retTest + relativedelta(years=+67)
    return retTest

# Monthly retirement income calculator
def incomeCalc(income):
    if income <= 996:
        pay = income * .9
    elif income > 996 and income <=6002:
        pay = 996 *.9 + .32*(income-996)
    else:
        pay = 996 *.9 + .32*(6002-996)+ .15*(income-6002)
    return pay

# Output Function
def displayInfo(retDate, pay):
    print("*****************************")
    print("You can start Social Security on:")
    print(retDate,"(YYY-MM-DD) and receive $",pay,".")
    print("**************************")

def main():
    income = getUserIncome()
    year = getUserYear()
    month = getUserMonth()
    day = getUserDay()
    retDate = getUserRetAge(month, day, year)
    pay = incomeCalc(income)
    displayInfo(retDate,pay)

main()