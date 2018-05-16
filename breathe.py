"""Assists with meditative breathing."""
"""Meditative Breathing Guide
Open breathe.py and change it to make a program that helps users
breathe 6.5 breaths per minute. It should print out “Breath in”,
waiting some time, then saying “Breath out”, then repeat. It
should do this for 2 minutes (13 total breaths, each with an in and an out).
"""

def meditate ():
    print ("breathe in")
    import time
    time.sleep(4)
    print ("breathe out")
    time.sleep(4)

for i in range (13):
    meditate()
