#!/usr/bin/python
"""
Take Input from user
@param: name
@param: age

Print how far is the user from reaching 100 years

Additional:
- Ask user for another input, and print the above output that many times
- same message in separate lines
"""

class CharacterInput():
    username = None
    age = 0
    
    def __init__(self):
        """
        Constructor for CharacterInput...
        """
        print('Intializing CharacterInput class...')
        
    def getUserDetails(self):
        """
        Getting user information
        Name
        Age
        """
        self.username = input("Enter your Name: ")
        self.age = input("Enter your Age: ")
    
    def calculateAgeFromHundred(self):
        return (100 - int(self.age))
    
    def printSolution(self):
        if self.calculateAgeFromHundred() > 0:
            print("Wait up Buddy, you still have %d years left to reach 100" % self.calculateAgeFromHundred())
        else:
            print("Wow!! You have already reached 100... GO and celebrate now...")
            
    def printSolutionMultipleTimes(self):
        printCount = input("How many times do you want to print the above message: ")
        counter = 0
        while counter < int(printCount):
            self.printSolution();
            counter = counter + 1
            