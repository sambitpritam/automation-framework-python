#!/usr/bin/python
"""
Main program to import and execute the required methods in the current folder...
"""
# from CharacterInput import CharacterInput
from listbasics import ListBasic

if __name__ == "__main__":

    print("Welcome to practice Main()....")

    lb = ListBasic()
    lb.getValuesFromListLessThanFive()
    print(item for item in lb.getListWithValuesLessThanFive())
    print(item for item in lb.getValuesLessThanFiveInOneLine())
    print(item for item in lb.getListValuesLessThanUserInput())

    print("End of main execution...")