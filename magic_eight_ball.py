"""Prompt from here: http://www.superpython.party/03/exercises.html"""

"""
Magic 8 Ball
Make a program magic_eight_ball.py that takes a yes or no question
and gives a yes, no, or maybe response at random.

"""

import random
import time

magiceightballanswers = [
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

def magiceightball ():
    print('  __  __          _____ _____ _____    ___  ')
    print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
    print(' | \  / |  /  \ | |  __  | || |      | (_) |')
    print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
    print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
    print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
    print('')
    print('')
    print('')
    print ("You've picked up a magic eight ball! The true answer to any question will be revealed! Just a moment....")
    time.sleep(2.5)
    question = input("What do you wish to know? ")
    time.sleep(2.5)
    print ("Ah, I see")
    time.sleep(2.5)
    print (f"So your question is {question}")
    time.sleep(2.5)
    print ("That is something to think about")
    time.sleep(2.5)
    print ("The answer is....")
    time.sleep(2.5)
    print (random.choice(magiceightballanswers))
    time.sleep(2.5)
    playagain()

def playagain():
    playerreply = input("The end. Do you wish to ask another question? Choose Y or N ")
    if playerreply == "y" or playerreply == "yes" or playerreply == "Yes" or playerreply == "Y":
        magiceightball()
    elif playerreply == "n" or playerreply == "no" or playerreply == "No" or playerreply == "n":
        print ("The end the end! Live your life!")
        quit ()
    else:
        print ("That's not Y or N, try again please- ")
        playagain()

magiceightball ()
