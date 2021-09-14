# Module 2 Assignment #2
# Thomas Gill
# 8/24/2021
# Weight on Other Planets
# For this I think I will play with the dictionary functionality and see how that works since we spoke about it in class

# Define and create the dictionary of the multipliers
body_multipliers = {
    "Sun": 27.01,
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1,     # (defined)
    "Moon": 0.166,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.06,
}
# Get user data
name = input("Please enter the name you go by:")
weight = float(input("Please enter your weight:"))
print("Thank you.")

# Do the calculations and show the weights
print("Hello,",name)
for x,y in body_multipliers.items():                  # I hope using a for loop is ok even if we haven't covered it,
    print("Your weight on",x,"is",y*weight,"lbs.")    #  I really wanted to see how it would work with a dictionary.
                                                      #  I used https://www.w3schools.com/python/python_dictionaries_loop.asp
                                                      #  to show me how to loop through it correctly.

