"""Prompt from here: http://www.superpython.party/03/exercises.html"""

"""
Snobby Greeting
Change greeting.py to have the following behavior:

Check if the given name has a “t” or “m” in it.
Print something very friendly if it does
Print “Oh. Hi.” if it doesn’t
Make sure you check for both upper- and lower-case letters
"""

name = input("What's your name, friend? ")

def snobbygreeting():
    if "t" in name:
        print(f"Hi there {name}!")
    if "T" in name:
        print(f"Hi there {name}!")
    if "m" in name:
        print(f"Hi there {name}!")
    if "M" in name:
        print(f"Hi there {name}!")
    else:
        print("Oh...... hi.")

snobbygreeting()
