"""Prompt from here: http://www.superpython.party/03/exercises.html"""

"""
Virtual Paper Fortune Teller
Create a program that emulates the experience of a paper fortune teller (https://en.wikipedia.org/wiki/Paper_fortune_teller#Telling_fortunes). The program should:

Ask for a color chosen from 4 colors
Ask for a number chosen from a set of 4 numbers depending on which color was chosen
Repeat step 2 as long as you’d like
Finally, have the user choose from a set of 4 numbers and reveal a fortune related to that number
"""

"""
Mostly works, but the selecting is not quite what a paper fortune teller would do. Need to look at selecting steps again.
"""

import random
import time

fortunetellercolors = ["Red", "Yellow", "Blue", "Green"]

fortunetellernumbers = ["One", "Two", "Three", "Four"]

fortunetelleranswers = [
"It is certain", \
"It is decidedly so", \
"Without a doubt", \
"Yes definitely", \
"You may rely on it", \
"As I see it yes", \
"Most likely", \
"Outlook good", \
"Yes", \
"Signs point to yes", \
"Reply hazy try again", \
"Ask again later", \
"Better not tell you now", \
"Cannot predict now", \
"Concentrate and ask again", \
"Don't count on it", \
"My reply is no", \
"My sources say no", \
"Outlook not so good", \
"Very doubtful"
]

def virtualfortuneteller ():
    print ("Welcome to the Virtual Fortune Teller!")
    time.sleep(2)
    question = input ("What is the question you wish answered? ")
    time.sleep(2)
    print (f"I see, you want to know {question} ... ")
    time.sleep(2)

    def firsthalf ():
        """Ask for a color chosen from 4 colors"""
        print ("What color? Your options are: ")
        print(*fortunetellercolors, sep = "\n")
        colorchoice = input ("So what'll it be? ")
        if colorchoice in fortunetellercolors:
            print ("Ah, excellent choice!! ");
        else:
            print(colorchoice);
            colorchoice = input("Hmmmm, that's not really one of the options. Pick from the list above ");
        """Ask for a number chosen from a set of 4 numbers depending on which color was chosen"""
        print ("What number? Your options are: ")
        print(*fortunetellernumbers, sep = "\n")
        numberchoice = input ("So what'll it be? ")
        if numberchoice in fortunetellernumbers:
            print ("Ah, excellent choice!! ");
        else:
            print(numberchoice);
            numberchoice = input("Hmmmm, that's not really one of the options. Pick from the list above ");
        """Repeat step 2 as long as you’d like"""

    firsthalf ()

    def checktocontinueorrepeat():
        playerreply = input("Would you like to repeat choosing colors and numbers or go ahead to the last step? Choose C for choosing or L to go to the last step ")
        if playerreply == "c" or playerreply == "C":
            firsthalf()
        elif playerreply == "l" or playerreply == "L":
            print ("Here we go! Final step coming up!")
            finalhalf ()
        else:
            print ("That's not C or L, try again please- ")
            checktocontinueorrepeat()

    checktocontinueorrepeat()

    def finalhalf ():
        """have the user choose from a set of 4 numbers and reveal a fortune related to that number"""
        print ("One last step! Choose a number to reveal the answer: ")
        print ("Your options are: ")
        print(*fortunetellernumbers, sep = "\n")
        time.sleep(2)
        numberchoice = input ("So what'll it be? ")
        print ("The answer is....")
        time.sleep(2)
        print (random.choice(fortunetelleranswers))

    finalhalf ()

virtualfortuneteller ()
