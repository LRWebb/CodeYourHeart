"""Prompt from here: http://www.superpython.party/04/exercises.html """

"""
FIRST ITERATION OF PROMPT
Lazy Chef Sandwich Generator
You’ve just opened a restaurant but you’re too lazy to come up with a sandwich menu. Make a program to do it instead!

Create a program lazy_chef.py that does the following:

Create a list of options for each element of the sandwich (proteins, spreads, bread, etc.).
Print one random item from each of the sandwich elements lists when the program is run.
Example usage:

$ python3.6 lazy_chef.py
olives
mustard
beef
white bread
"""

import random
import time

protein = ["Chicken", "Steak", "Tuna", "Roast beef", "Egg"]
bread = ["rye", "white", "honey wheat", "potato", "challah"]
spreads = ["mustard", "good mustard", "mayonaise", "tahini", "ranch dressing"]
greenstuff = ["avocado", "lettuce", "spinach leaves", "tomato", "micro greens"]

print ("Welcome to the lazy chef sandwich maker!")
time.sleep(1)
print ("We're gonna help you make a sandwich with a minimum of decision making, so you can protect your cognitive load and get some food as the same time!")
print ("Okay here we go!")
time.sleep(1)
print ("Your sandwich today is: ")
time.sleep(2)
print ((random.choice(protein)) + " on " + (random.choice(bread)) + " with " + (random.choice(spreads)) + " and of course, " + (random.choice(greenstuff)))


"""
SECOND PROMPT
Better Lazy Chef
Expand your lazy chef program to do the following:

Choose a name at random from a name of sandwiches and assign your random sandwich ingredients to that name. Your menu should not include two sandwiches with the same name.
Print out your menu items in a nice, human-readable way.
Hint
If you didn’t make a lazy chef program previously, you can use these lists to start with:

proteins = ["ham", "turkey", "beef", "tofu"]
condiments = ["mustard", "mayo", "hummus"]
veggies = ["tomato", "lettuce", "onion", "sprouts"]
breads = ["white bread", "wheat bread", "pita bread", "sourdough"]
"""
