################################
# Program name: MOD3 Distance Traveled.py
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/7/2021
#  Assignment: Module 3 - Assignment 3: Distance Traveled
#  Purpose: The distance a vehicle travels can be calculated as follows:
#
# distance = speed * time
#
# For example, if a train travels 40 miles per hour for 3 hours, the distance traveled is 120 miles.
#
# Write a program that asks the user for the speed of a vehicle (in miles per hour) and how many hours it has traveled.
# The program should then use a loop to display the distance the vehicle has traveled for each hour of that time period.
# Here is an example of the output:
#
# What is the speed of the vehicle in mph? 40
# How many hours has it traveled? 3
# Hour  Distance Traveled
# --------------------------------
#  1           40
#  2           80
#  3          120
# Input Validation: Do not accept a negative number for speed and do not accept any value less than 1 for time traveled.
#######################################################################################################################
# Any imports or global variables will go here:


#######################################################################       Function creations begin here:
# Speed validation.
def speedValidator(userInput):
    try:
        userInput = float(userInput)
    except:
        return False
    return userInput > 0

#Get the speed input
def getSpeed(prompt="First, please enter a vehicle speed in miles per hour (mph):"):
    while True:
        userInput = input(prompt)
        if speedValidator(userInput):
            return float(userInput)
        else:
            print("That's not a valid speed!")

# Duration validation
def hourValidator(userInput):
    try:
        userInput = float(userInput)
    except:
        return False
    return userInput >= 1

# Get the duration input
def getHours(prompt="Next, please enter duration in hours:"):
    while True:
        userInput = input(prompt)
        if hourValidator(userInput):
            return float(userInput)
        else:
            print("That's not a valid number of hours!")

# Output Function
def headerInfo():
    print("*****************************")
    print("Welcome to your new spiffy distance display!")
    print("You will give me a speed and duration and I will show you how much distance you cover each hour!")

#Calc and body printout
def calcs(speed, hours):
    count = 0
    totalDistance = 0
    while hours > count:
        count += 1
        totalDistance = speed + totalDistance
        print("#",count,"   ",round(totalDistance, 1),"miles")

def main():
    headerInfo()
    speed = getSpeed()
    hours = getHours()
    print("*************************\nHour    Distance Traveled\n*************************")
    calcs(speed,hours)
    print("*************************\nEnjoy your trip!")

main()