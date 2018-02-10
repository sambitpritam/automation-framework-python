#!/usr/bin/python
"""
List Comprihension, take a list and get a list of all values that are even in a sinlge line of code
"""

import random

class ListComprihension():

    randomList = []

    def __init__(self):
        """
        Constructor for ListComprihension
        """
        print("Initializing ListComprihension...")

    def generateRandomList(self):
        """
        Generates a random list within a given range for the given length
        :return: None
        """
        self.randomList = random.sample(range(400), 213)

    def getListOfEvenNumbers(self):
        """
        Get the list of all even numbers from the list
        :return: List of even numbers
        """
        evenNumberList = (eachNumber for eachNumber in self.randomList if eachNumber % 2 == 0)
        return evenNumberList