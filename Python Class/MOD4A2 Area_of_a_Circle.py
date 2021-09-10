###############################
# Program name:MOD4assignment1_Falling_Distances.py
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/8/2021
#  Assignment: Module 4 - ASSIGNMENT 2: Area of a Circle
# Purpose:
# The following formula gives the distance between two points, (x1, y1) and (x2, y2) in the Cartesian plane:
#
# distance = sqrt((x2 -x1)^2 + (y2 - y1)^2)
#
# Given the center and a point on the circle, you can use this formula to find the radius of the circle.

# Write a program that prompts the user to enter the center and a point on the circle (two tuples containing an
# x and y value).
#
# The program should then output the circle’s radius, diameter, circumference, and area. Your program
# must have at least the following functions:
#
# calculateRadius: Receives the x-y coordinates of the center and point on the circle (as input by the user) and
# calculates the distance between the points. This value is returned as the radius of the circle.
#
# calculateArea: Receives the radius of a circle, calculates and returns the area of the circle.
#
# calculatePerimeter: Receives the radius of a circle, calculates and returns the perimeter of the circle.
#
# The output should clearly display the radius, area, and perimeter of the resulting circle.
#######################################################################################################################
# Any imports or global variables will go here:
import math

#######################################################################       Function creations begin here:

# Duration validation
def inputValidator(userInput):
    try:
        userInput = [float(i) for i in userInput]
    except:
        return False
    return userInput

# Conversion function
def conversion(points):
    points = [float(i) for i in points]
    points = tuple(points)
    return points

# Get the users input
def getInput(name):
    print("Please enter", name, "as x,y: ",end="")
    inputter = input()
    while True:
        userInput = inputter.split(",")
        if inputValidator(userInput):
            userInput = conversion(userInput)
            return userInput
        else:
            print("That's not a valid entry, please try again.")
            print("Please enter", name, "as x,y: ", end="")
            inputter = input()

# Header Function
def headerInfo():
    print("*****************************")
    print("This script will give you a circle’s radius, diameter, circumference, and area")
    print("after you enter the center and a point on the circle, how cool is that!?")

# Calc Radius distance = sqrt((x2 -x1)^2 + (y2 - y1)^2)
def calculateRadius(center, point):
    radius = math.sqrt((center[0]-point[0])**2+(center[1]-point[1]**2))
    return radius

# calculateArea = pi*r^2
def calculateArea(radius):
    area = math.pi*radius**2
    return area

# calculatePerimeter = 2*pi*r
def calculatePerimeter(radius):
    perimeter = 2*math.pi*radius
    return perimeter

def main():
    headerInfo()
    center = getInput("the circle center point")
    point = getInput("a point on the circle")
    print(center, point)
    radius = calculateRadius(center, point)
    area = calculateArea(radius)
    perimeter = calculatePerimeter(radius)
    print(radius, area, perimeter)
    print("****************************")

main()