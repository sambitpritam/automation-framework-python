#!/usr/bin/python
"""
This is about list comprehension. Get the common from two list of different size
"""

import random

class ListComprehensionPartTwo():

    firstList = []
    secondList = []

    def __init__(self):
        """
        Constructor for ListComprehensionPartTwo
        """
        print("Initializing ListComprehensionPartTwo...")

    def generateRandomLists(self):
        """
        initialize two list with random values of different size
        :return: None
        """
        self.firstList = random.sample(range(100), 40)
        self.secondList = random.sample(range(100), 52)

    def getCommonElementsFromTheList(self):
        """
        get the common elements from two list of different size usig list comprehension
        :return:
        """
        return set(self.firstList).intersection(set(self.secondList))