"""Prompt from here: http://www.superpython.party/03/exercises1.html"""

"""
Write a program cheerleader.py that does the following:
Stores your name in a variable
Stores a compliment in a variable
Prints the compliment with your name 25 times.
"""

name = input("What's your name, eh? ")
compliment = "you're awesome and other people think that too!!!"

print(f'{name} {compliment}\n'*25)
