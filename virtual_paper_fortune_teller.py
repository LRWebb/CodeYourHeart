"""Prompt from here: http://www.superpython.party/03/exercises.html"""

"""
Virtual Paper Fortune Teller
Create a program that emulates the experience of a paper fortune teller (https://en.wikipedia.org/wiki/Paper_fortune_teller#Telling_fortunes). The program should:

Ask for a color chosen from 4 colors
Ask for a number chosen from a set of 4 numbers depending on which color was chosen
Repeat step 2 as long as you’d like
Finally, have the user choose from a set of 4 numbers and reveal a fortune related to that number

"""

import random
import time

fortunetellercolors = [red, yellow, blue, green]

fortunetellernumbers = [one, two, three, four]

def virtualfortuneteller ():
print ("What is the question you wish answered? ")
print ("What color? ")
print ("What number? ")
print ("Choose a number to reveal the answer: ")


virtualfortuneteller ()
