#!/usr/bin/python
"""
This is Rock-Paper-Scissor game. Rules:
Rock beats Scissor
Scissors beat Paper
Paper beats Rock
"""

import random

class RockPaperScissor():

    options = ["Rock", "Paper", "Scissor"]

    def __init__(self):
        """
        Constructor for RockPaperScissor
        """
        print("Initializing RockPaperScissor...")

    def computerChoice(self):
        """
        This method will return computers choice from the options
        :return: String from the list- options
        """
        return self.options[random.randint(0, len(self.options)-1)]

    def userInput(self):
        """
        This method will return choice made by user
        :return: String from console
        """
        return input("Choose from Rock, Paper, Scissor: ")

    def whoWins(self):
        """
        This method will keep the game alive, untill user chooses to quit the game
        :return: None
        """
        requestToExit = ""

        while(requestToExit.lower() != "no"):
            userChoice = self.userInput()
            computerChoice = self.computerChoice()

            if (userChoice.lower() == "rock" and computerChoice.lower() == "scissor"):
                print("User WINS! User choose %s and computer choose %s" % (userChoice, computerChoice))
            elif (userChoice.lower() == "scissor" and computerChoice.lower() == "paper"):
                print("User WINS! User choose %s and computer choose %s" % (userChoice, computerChoice))
            elif (userChoice.lower() == "paper" and computerChoice.lower() == "rock"):
                print("User WINS! User choose %s and Computer choose %s." % (userChoice, computerChoice))
            else:
                print("Computer WINS! User choose %s and Coumputer choose %s." % (userChoice, computerChoice))

            requestToExit = input("Do you want to continue?(Yes/No): ")