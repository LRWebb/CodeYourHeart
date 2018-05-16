""" Guess the Number
Write a program number_guesser.py that does the following:

Sets a random secret number from 1-14
Prompts input for a guess of what the number is
Prints a success message if the guess is correct and the program ends
If the number is incorrect, print a message indicating if the number is higher or lower
Prints “Out of tries!” after the third incorrct guess
"""

import random

random_number = random.randint(2, 999)

print ("I've picked a number between 1 and 1000- can you guess it?")
print ("What is your guess? Enter an integer between 1 and 1000 and let's see if you're right!")

input

if input = random_number
    print ("You're right! Good job!!")
    else print ("Hm, not quite- you can try again though- ")
