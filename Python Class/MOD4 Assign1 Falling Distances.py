################################
# Program name:MOD4assignment1_Falling_Distances.py
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/8/2021
#  Assignment: Module 4 - ASSIGNMENT 1: Falling Distance
#  Purpose:
#
# When an object is falling because of gravity, the following formula can be used to determine the distance the object
# falls in a specific time period:
#
# d = 1/2 gt2
#
# The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the amount of time, in
# seconds, that the object has been falling.
#
# Write a function named fallingDistance that accepts an object’s falling time (in seconds) as an argument. The
# function should return the distance, in meters, that the object has fallen during that time interval. Write a program
# that demonstrates the function by prompting the user for the total time and calling the function in a loop that
# passes the time values in 5 second increments as the argument and displays the elapsed time and return value.
#
# The output should have a header identifying the column names and tabular formatted values (values displayed are to
# illustrate formatting only):
#
# Time	Distance
# 0	    0.0
# 5	    30.0
# 10	45.0
# 15	52.0
#######################################################################################################################
# Any imports or global variables will go here:


#######################################################################       Function creations begin here:
# Duration validation
def timeValidator(userInput):
    try:
        userInput = int(userInput)
    except:
        return False
    return userInput > 0

# Get the duration input
def getTime(prompt="Please the enter the time to fall in seconds:"):
    while True:
        userInput = input(prompt)
        if timeValidator(userInput):
            return float(userInput)
        else:
            print("That's not a valid number of seconds!")

# Header Function
def headerInfo():
    print("*****************************")
    print("Gravity sucks! No really, just enter a time below and I will demonstrate how far something will fall")
    print("every 5 seconds for the duration!")

#Calc and body printout
def fallingDistance(t):
    count = 0
    g = 9.8
    while t >= count:
        d = .5 * g * count**2
        print(count,"seconds\t",round(d, 1),"meters")
        count += 5

def main():
    headerInfo()
    t = getTime()
    print("****************************\nTime\t\t Distance Fallen\n****************************")
    fallingDistance(t)
    print("****************************")

main()