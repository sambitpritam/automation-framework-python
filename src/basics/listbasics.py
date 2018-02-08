"""
Given a list of integers, find all the elements that are less than 5.
- get an input from the user and get all numbers less than the input number
- write the entire code in 1 line
"""

class ListBasic():

    initialList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    def __init__(self):
        """
        Constructor for the ListBasic() class
        """
        print("Initializing class ListBasic()")

    def getValuesFromListLessThanFive(self):
        for listItem in self.initialList:
            if listItem < 5:
                print(listItem)

    def getListWithValuesLessThanFive(self):
        valuesLessThanFiveList = []

        for listItem in self.initialList:
            if listItem < 5:
                valuesLessThanFiveList.append(listItem)

        return valuesLessThanFiveList

    def getValuesLessThanFiveInOneLine(self):
        valuesLessThanFiveList = []

        valuesLessThanFiveList.append(listItem for listItem in self.initialList if listItem < 5)

        return valuesLessThanFiveList

    def getListValuesLessThanUserInput(self):
        userInput = int(input("Enter a number to get the list with values lesser than: "))
        valuesLesserThanUserValue = []

        valuesLesserThanUserValue.append(listItem for listItem in self.initialList if listItem < userInput)

        return valuesLesserThanUserValue
