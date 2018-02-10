#!/usr/bin/python
"""
Ask user to enter a string, and check if the string is plaindrome or not
@:param user input String
"""

class IsStringPalindrome():

    userInputString = ""

    def __init__(self):
        """
        Constructor for IsStringPalindrome()
        """
        print("Initializing IsStringPalindrome...")

    def getUserInput(self):
        """
        Request user to enter a string that needs to be checked if it is paindrome or not
        :return: None
        """
        self.userInputString = input("Enter a String to check if it is palindrome or not: ")

    def checkIfStringIsPalindromeOrNot(self):
        """
        To check if the String is palindrome or not.
        :return: Boolean
        """
        matchedCharacters = 0
        for index in range(int(len(self.userInputString)/2)):
            if(self.userInputString[index] == self.userInputString[len(self.userInputString)-1-index]):
                matchedCharacters += 1

        if len(self.userInputString) % 2 != 0:
            matchedCharacters += 0.5

        if matchedCharacters * 2 == len(self.userInputString):
            return True
        else:
            return False

    def checkIfStringIsPalindromeOrNotAttemptTwo(self):
        """
        using slicing to achieve the same
        :return: Boolean
        """
        if self.userInputString[0 : len(self.userInputString)-1] == self.userInputString[len(self.userInputString)-1 : 0 : -1]:
            return True
        else:
            return False