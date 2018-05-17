"""Prompt from here: http://www.superpython.party/03/exercises.html"""

"""
Guess the Number
Write a program number_guesser.py that does the following:

Sets a random secret number from 1-14
Prompts input for a guess of what the number is
Prints a success message if the guess is correct and the program ends
If the number is incorrect, print a message indicating if the number is higher or lower
Prints “Out of tries!” after the third incorrct guess
"""

import random

random_number = random.randint(1, 14)

print ("I've picked a number between 1 and 14- can you guess it?")
guess = float(input("What is your guess? Enter an integer between 1 and 14 and let's see if you're right! "))

if guess == random_number:
    print ("You're right! Good job!!")
else:
    if guess > random_number:
        print ("Hm, not quite, the number is actually lower than that!- you can try again- ")
        guess = float(input("What is your second guess? You have three tries total. Enter an integer between 1 and 14 and let's see if you're right! "))
    else:
        print ("Hm, not quite, the number is actually higher than that!- you can try again- ")
        guess = float(input("What is your second guess? You have three tries total. Enter an integer between 1 and 14 and let's see if you're right! "))
if guess == random_number:
    print ("You're right! Good job!!")
else:
    if guess > random_number:
        print ("Hm, not quite, the number is actually lower than that!- you can try again- ")
        guess = float(input("What is your third and final guess? You have three tries total. Enter an integer between 1 and 14 and let's see if you're right! "))
    else:
        print ("Hm, not quite, the number is actually higher than that!- you can try again- ")
        guess = float(input("What is your third and final guess? You have three tries total. Enter an integer between 1 and 14 and let's see if you're right! "))
if guess == random_number:
    print ("You're right! Good job!!")
else:
    print ("Out of tries! " + str(guess) + " is not a match and that's your third and final guess- better luck next time!")
