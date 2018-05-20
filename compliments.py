""" Prompt from here: http://www.superpython.party/03/exercises.html """

"""
Edit compliments.py so it prints out a random compliment from the variable compliments.
"""

import random

# hint: look at the random module in the Python documentation

compliments = [
    "You look very nice today.",
    "You're better than sliced ham.",
    "I've always thought you were super!",
    "You look like magic!",
    "You're doing amazing, sweetie",
    "You care about people and it shows- thank you :)",
    "You are doing incredible! Keep it up!"
]

print (random.choice(compliments))
