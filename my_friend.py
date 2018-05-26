"""Prompt from here: http://www.superpython.party/04/exercises.html """
"""Flower source: http://chris.com/ascii/index.php?art=plants/flowers """

"""
Virtual Friend
Create a program my_friend.py that does the following:

Asks how you are
Compares the input to a list of good emotions, and a list of bad emotions, then prints an appropriate response depending on which list contains the input
Prints “I truly don’t know what that is like.” if the input isn’t in either list
Chooses a random response if the input “How are you” is received (with any capitalization)
Example usage:

$ python3.6 my_friend.py
How are you? Good
Oh, that's great!

$ python3.6 my_friend.py
How are you? Horrible
I'm sorry to hear that

$ python3.6 my_Friend.py
How are you? Pickles
I truly don't know what that is like.

$ python3.6 my_friend.py
How are you? How are you?
I like beans.
"""

import random
import time

positiveemotions = ["good", "great", "awesome", "fantastic", "wonderful"]
negativeemotions = ["a bit down", "sad", "mad", "frustrated"]
congratsresponse = ["That's awesome!!!!", "I'm so glad to hear that!!!", "Wonderful to hear!!!!", "That is so wonderful!!!"]
condolenceresponse = ["I'm sorry o hear that", "I hope things turn around for you soon!", "That dosen't sound good", "That's tough but I believe in you!"]
virtualfriendreponseback = ["I'm make of 0s and 1s", "I like electricity", "I am functioning, I suppose you would say that is good!", "As long as I have electricity I'm happy!"]

def HowAreYou ():
    print ("  (\o/)_______________________________________________________(\o/)")
    print ("  (/|\)                                                       (/|\)")
    print ("    |            {o}{o}{o}                                      |")
    print ("    |             |  |  |                                       |")
    print ("    |            \|/\|/\|/          ~Friend time~               |")
    print ("    |           [~~~~~~~~~]                                     |")
    print ("    |            |~~~~~~~|                                      |")
    print ("    |            |_______|                                      |")
    print ("  (\o/)_______________________________________________________(\o/)")
    print ("  (/|\)                                                       (/|\)")
    print ("  ")
    print ("  ")
    print ("Welcome to Virtual Friend! I want to hear how you're doing! ")
    time.sleep(1)
    print ("Before we get to the question, here are some choices to consider: ")
    print (*negativeemotions, sep = "\n")
    time.sleep(2)
    print (*positiveemotions, sep = "\n")
    time.sleep(2)

    emotion = input("So, how are you, my friend? ")
    emotion = emotion.lower ()
    print (f"ah, {emotion} ..... ")
    time.sleep(1)

    if emotion in positiveemotions:
        print (random.choice(congratsresponse))
    elif emotion in negativeemotions:
        print (random.choice(condolenceresponse))
    elif emotion == "How are you":
        print (random.choice(virtualfriendreponseback))
    else:
        print ("I truly don’t know what that is like.")

    time.sleep(1)
    print ("Take care, my friend. I believe in you!!!!!!!!!!!!!!!!")



HowAreYou ()
