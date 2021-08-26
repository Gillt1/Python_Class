# Module 2 Assignment #1
# Thomas Gill
#8/24/2021
# Restaurant Bill:
#
# Write a Python script that informs a user of their total meal charges.
#
# Prompt the user for the amount of the meal (e.g. $32.95).
# Compute the tax on the restaurant bill. The tax should be 6.75 percent of the meal cost.
# Prompt the user for the tip amount (Suggesting a value equal to 18 percent of the total).
# Display the meal cost, tax amount, tip amount, and total bill on the screen.
#
# Name your script restaurant.py and submit it as an attachment to the assignment.

# Get the Meal Cost and calc tax
meal_cost = float(input("Please enter the cost of your meal:"))
tax = meal_cost * .0675

# I didnt like the way the script was not always showing the .00 so found a way to force it to.
formatted_meal_cost = '{0:.2f}'.format(meal_cost)
formatted_tax='{0:.2f}'.format(tax)

# Calc suggested tip and format
suggested_tip = (meal_cost+tax) * .18
formatted_sug_tip = '{0:.2f}'.format(suggested_tip)

# Get tip amount
print("The suggested tip of 18% comes to: $",formatted_sug_tip)
tip = float(input("Please enter your tip amount:"))

formatted_tip='{0:.2f}'.format(tip)

# Total cost calc
total_cost= meal_cost + tax + tip

# more formatting
formatted_total_cost = '{0:.2f}'.format(total_cost)    #originally I used round but that left odd looking prices

#I wanted to write this on one line.. Just because.
print("The itemized costs for your fabulous meal are: ","\nMeal Cost $",formatted_meal_cost,"\nTax $",formatted_tax,"\nTip $",formatted_tip,"\nTotal $",formatted_total_cost)
print("Thank you and come again!")