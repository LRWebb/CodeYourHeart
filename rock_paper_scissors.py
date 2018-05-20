"""Prompt from here: http://www.superpython.party/03/exercises.html"""

"""
Rock, Paper, Scissors
Create a rock, paper, scissors program that evaluates two moves given as input and prints out which move
would win. You can reference the rules of rock, paper, scissors here: https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors
Ruls:
Rock beats Scissors
Scissors beat Paper
Paper beats Rock
Ties are possible
"""

def rockpaperscissors ():
    print ("Welcome to Rock Paper Scissors! This is NOT best out of three- this is best out of ONE- HERE WE GO!")

    playerOnethrow = input("Ready Player One- what is your throw, Rock (r), Paper (p), or Scissors (s)? ")
    playerOnethrow = playerOnethrow.lower();
    while (playerOnethrow != "r" and playerOnethrow != "p" and playerOnethrow != "s"):
    	print(playerOnethrow);
    	playerOnethrow = input("That choice is not valid. Enter your choice (r/p/s): ");
    	playerOnethrow = playerOnethrow.lower();

    playerTwothrow = input("Ready Player Two- what is your throw, Rock (r), Paper (p), or Scissors (s)? ")
    playerTwothrow = playerTwothrow.lower();
    while (playerTwothrow != "r" and playerTwothrow != "p" and playerTwothrow != "s"):
    	print(playerTwothrow);
    	playerTwothrow = input("That choice is not valid. Enter your choice (r/p/s): ");
    	playerTwothrow = playerTwothrow.lower();

    print (f'The challenge is: {playerOnethrow} vs {playerTwothrow}')

    if playerOnethrow == playerTwothrow:
        print("It's a draw! Ya'll both win")

    elif playerOnethrow == 'r' and playerTwothrow == 's':
        print("Player One wins!!!")
    elif playerOnethrow == 'r' and playerTwothrow == 'p':
        print("Player Two wins!!!")

    elif playerOnethrow == 'p' and playerTwothrow == 'r':
        print("Player One wins!!!")
    elif playerOnethrow == 'p' and playerTwothrow == 's':
        print("Player Two wins!!!")

    elif playerOnethrow == 's' and playerTwothrow == 'p':
        print("Player One wins!!!")
    elif playerOnethrow == 's' and playerTwothrow == 'r':
        print("Player Two wins!!!")
    playagain()

def playagain():
    choice = input("Would you like to play again? Choose y or n ")
    if choice == "y" or choice == "yes" or choice == "Yes" or choice == "Y":
        rockpaperscissors()
    elif choice == "n" or choice == "no" or choice == "No" or choice == "n":
        print ("Okay, thanks for playing!")
        quit ()
    else:
        print ("That's not y or n, try again please- ")
        playagain()

rockpaperscissors()
