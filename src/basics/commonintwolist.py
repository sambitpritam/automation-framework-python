#!/usr/bin/python
"""
Take 2 list and find the list of elements that are common in both the list
"""

import random

class CommonInTwoList():

    firstList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    secondList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def __init__(self):
        """
        constructor for CommonInTwoList
        """
        print("Initializing CommonInTwoList class...")

    def findCommonInTwoList(self):
        commonList = set(self.firstList).intersection(self.secondList)
        return commonList

    def generateTwoRandomList(self):
        self.firstList = random.sample(range(100), 21)
        self.secondList = random.sample(range(200), 43)