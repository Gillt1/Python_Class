
#                                                Secret number guessing game

##secret_number = 777
##
##print(
##"""
##+================================+
##| Welcome to my game, muggle!    |
##| Enter an integer number        |
##| and guess what number I've     |
##| picked for you.                |
##| So, what is the secret number? |
##+================================+
##""")
##guess=int(input())
##
##while guess != secret_number:
##    
##    print("Ha ha! You're stuck in my loop!")
##    guess = int(input("Guess again",))
##    
##print("Well done, muggle! You are free now.")   


#                                                For Loops
##for i in range(10):
##    print("The value of i is currently", i)


##for i in range(2, 8):
##    print("The value of i is currently", i)

##for i in range(2, 8, 3):
##    print("The value of i is currently", i)


##import time
##
### Write a for loop that counts to five.
##    # Body of the loop - print the loop iteration number and the word "Mississippi".
##    # Body of the loop - use: time.sleep(1)
##
### Write a print function with the final message.
##for i in range (1, 6):
##    print(i,"Mississippi")
##    use: time.sleep(1)
##    
##print("Ready or not, here I come!")

#                                                            use of break
##largest_number = -99999999
##counter = 0
##
##while True:
##    number = int(input("Enter a number or type -1 to end program: "))
##    if number == -1:
##        break
##    counter += 1
##    if number > largest_number:
##        largest_number = number
##
##if counter != 0:
##    print("The largest number is", largest_number)
##else:
##    print("You haven't entered any number.")
##
##
##
###                                                           use of continue and counter:
##largest_number = -99999999
##counter = 0
##
##number = int(input("Enter a number or type -1 to end program: "))
##
##while number != -1:
##    if number == -1:
##        continue
##    counter += 1
##
##    if number > largest_number:
##        largest_number = number
##    number = int(input("Enter a number or type -1 to end program: "))
##
##if counter:                                                 #note that counter: is counter!=0:
##    print("The largest number is", largest_number)
##else:
##    print("You haven't entered any number.")


##secret="chupacabra"
##
##while True:
##    password=input()
##    if password==secret:
##        break
##
##print("You've successfully left the loop.")


#                                                                 vowel eater exercise
# Prompt the user to enter a word
# and assign it to the user_word variable.

##user_word=input("Type something stupid: ")
##user_word=user_word.upper()
##
##for letter in user_word:
##    # Complete the body of the for loop.
##    if letter == "A": continue
##    if letter == "E": continue
##    if letter == "I": continue
##    if letter == "O": continue
##    if letter == "U": continue
##    print(letter)


# Prompt the user to enter a word
# and assign it to the user_word variable.

##user_word=input("Type something stupid: ")
##user_word=user_word.upper()
##word_without_vowels=""                     #note the "" here and not ()
##
##for letter in user_word:
##   # Complete the body of the for loop.
##    if letter == "A": continue
##    if letter == "E": continue
##    if letter == "I": continue
##    if letter == "O": continue
##    if letter == "U": continue
##    word_without_vowels = word_without_vowels + letter
##
##print(word_without_vowels)




















