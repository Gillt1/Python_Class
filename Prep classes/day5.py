#                                                    Block pyramid wall

##blocks = int(input("Enter the number of blocks: "))
##height = 0
##
##while blocks >= 0:
##
##    if blocks >= height + 1:
##        height += 1
##        blocks = blocks - height
##        
##    else: break
##
##
##print("The height of the pyramid:", height)

####################################################################################################################################

#                                                   Collatz hypothesis
##  In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven)
##  which can be described in the following way:
##
##  1. take any non-negative and non-zero integer number and name it c0;
##  2. if it's even, evaluate a new c0 as c0 ÷ 2;
##  3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
##  4. if c0 ≠ 1, skip to point 2.
##
##  The hypothesis says that regardless of the initial value of c0, it will always go to 1.
##
##  Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number
##  (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll
##   even find the one which would disprove the hypothesis.
##
##
##  Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1.
##  We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
##
##  Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.
##
##

##step = 0
##c0 = int(input("Enter any non-negative and non-zero number: "))
####
##
##while c0 != 1:
##    if c0 % 2 == 0:
##        c0 = c0/2
##        step += 1
##        print(int(c0))
##    else :
##        c0 = 3*c0+1
##        step += 1
##        print (int(c0))
##
##print("steps: ", step)
        
####################################################################################################################################
#
#                                                     Summary snippits

#Exercise 1

#Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

for i in range(0, 11):
    if i % 2 != 0:
        print(i)

# Exercise 2

#Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
      
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

#Exercise 3

#Create a program with a for loop and a break statement. The program should iterate over characters in an email address,
# exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Exercise 4

# Create a program with a for loop and a continue statement. The program should iterate over a string of digits,
#  replace each 0 with x, and print the modified string to the screen. Use the skeleton below:

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")


    
