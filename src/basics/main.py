#!/usr/bin/python
"""
Main program to import and execute the required methods in the current folder...
"""
# from CharacterInput import CharacterInput
from listbasics import ListBasic
from commonintwolist import CommonInTwoList
from isstringpalindrome import IsStringPalindrome
from listcomprihension import ListComprihension
from rockpaperscissor import RockPaperScissor
from guessthenumber import GuessTheNumber
from listcomprehensionparttwo import ListComprehensionPartTwo

if __name__ == "__main__":
    print("Welcome to practice Main()....")

    listComprehensionPartTwo = ListComprehensionPartTwo()
    listComprehensionPartTwo.generateRandomLists()
    print(list(listComprehensionPartTwo.getCommonElementsFromTheList()))

    print("End of main execution...")
