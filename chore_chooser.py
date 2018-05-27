"""Prompt from here: http://www.superpython.party/04/exercises.html """

"""
Chore Chooser
Make a program chore_chooser.py that does the following:

Create two lists do_now and do_later, along with a list of chores
Assign each item in the list of chores to do_now or do_later at random
Print each list in a nice, human-readable way
"""

"""
Mostly works, but I think the code is randomly deleting variables from the chores list,
not deleting the one that was used. Need to look at pop again.
"""

import random
import time
from random import shuffle

do_now = []
do_later = []
chores = ["sweep", "vaccume", "dishes", "laundry"]

print ("Welcome to the chore chooser!!!")
time.sleep(2)
print ("Just a moment while I take all the chores and shuffle them, then we'll see what's on for today!")
time.sleep(1.5)
print ("shuffling... \n .... ")
time.sleep(1)
shuffle(chores)
choresshuffled = chores

for chore in choresshuffled:
    do_now.append(chore)
    choresshuffled.remove(chore)
    for chore in choresshuffled:
        do_later.append(chore)
        choresshuffled.remove(chore)

print ("  ")
print ("Do Now: ")
print (*do_now, sep = "\n")
print ("  ")
print ("Do Later: ")
print (*do_later, sep = "\n")
print (" ")
print ("Well there you have it! Go do some things!  ")
