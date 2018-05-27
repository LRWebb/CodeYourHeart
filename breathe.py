"""Prompt from here: http://www.superpython.party/03/exercises.html"""

"""
Meditative Breathing Guide
Open breathe.py and change it to make a program that helps users
breathe 6.5 breaths per minute. It should print out “Breath in”,
waiting some time, then saying “Breath out”, then repeat. It
should do this for 2 minutes (13 total breaths, each with an in and an out).
"""

"""Some of my changes- I shortened the number of repetitions, and made the exhale longer than the inhale"""

def meditate ():
    print ("breathe in, you numbskull")
    import time
    time.sleep(4.5)
    print ("breathe out, motherfucker")
    time.sleep(6.5)

for i in range (10):
    meditate()

print ("The world is probably still turning")
