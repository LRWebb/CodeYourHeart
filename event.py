"""Prompt from here: http://www.superpython.party/04/exercises.html """

"""
Guest List
Make a program event.py that asks the user for their name,
checks a list of names and either tells them “Welcome THEIR_NAME!”
or “Sorry, but you’re not on the guest list”.
"""

import random
import time

guestlist = ["Superman", "Superwoman", "Catwoman", "Batman", "dog", "neighbor"]

print ("Hiiiiiii good to see you one thing real quick we jsut need to check if you're on the guest list")
time.sleep(1)
name = input("Okay what is your name? ")
time.sleep(2)
print ("hmmmmmmmmmmmmmmmmmmmmmm")
time.sleep(2)
if name in guestlist:
    print (f"Welcome, {name}!!!!!")
else:
    print ("Sorry, but you’re not on the guest list")
