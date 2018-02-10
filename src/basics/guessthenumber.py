#!/usr/bin/python
"""
Make computer to choose a random number between 1 and 9 (inclusive) and ask user to make a guess,
and let user know if the guessed number is too high or too low or exact.
"""

import random

class GuessTheNumber():

    def __init__(self):
        """
        Constructor for GuessTheNumber
        """
        print("Initializing GuessTheNumber...")

    def computerChoice(self):
        """
        Counter chooses a random number between 1 and 9 (inclusive)
        :return: Random Number
        """
        return random.randint(1, 9)

    def userGuess(self):
        """
        Let user guess a number
        :return: Integer input from the user
        """
        return int(input("Guess what the computer choose from the range 1 to 9: "))

    def checkIfUserIsCorrect(self):
        """
        Checks if the guess made by user is too big, too less or exact
        :return: "you guessed a larger Number", "You guessed a smaller Number", "Exactly"
        """
        requestToContinue = ""
        correctGuess = 0
        totalTimesPlayed = 0

        while(requestToContinue.lower() != "no"):
            computerChoice = self.computerChoice()
            userGuess = self.userGuess()
            totalTimesPlayed += 1

            if (computerChoice > userGuess):
                print("You guessed a smaller Number...")
            elif (computerChoice < userGuess):
                print("You guessed a number greater than what computer choose...")
            else:
                print("Exactly!!! Computer choose %d" % computerChoice)
                correctGuess += 1

            requestToContinue = input("Do you want to continue? (Yes/No): ")

        print("You guessed correct %d times out of %d" % (correctGuess, totalTimesPlayed))