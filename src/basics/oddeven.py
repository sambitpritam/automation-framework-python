"""
Get input from a user and check if the number is odd or even
@Params: number

Additional:
- Check if the number is divisible by 4 then print an appropriate message
- Get 2 numbers from user num1 and num2, check if num1 is divisible by num2
"""

class OddEven():

    oddEven = 0
    firstNumber = 0
    secondNumber = 0

    def __init__(self):
        """
        constructor for OddEven class
        """
        print("Initializing OddEven()...")

    def getInputFromUser(self):
        self.oddEven = int(input("Enter a number to check if the number is odd or even: "))

    def checkIfNumberIsEvenOrOdd(self):

        if (self.oddEven % 2 == 0):
            return "The number %d is even..." % self.oddEven
        else:
            return "The number %d is odd.." % self.oddEven

    def checkDivisibilityByFour(self):

        if (self.oddEven % 4 == 0):
            return "The number %d is divisible by 4..." % self.oddEven
        else:
            return "The number %d is not divisible by 4..." % self.oddEven

    def checkDivisibilityOfTwoNumbers(self):
        self.firstNumber = int(input("Enter a number to check the divisibility of: "))
        self.secondNumber = int(input("Enter a number with which you would like to check the divisibility of the previous number: "))

        if (self.firstNumber % self.secondNumber == 0):
            return "Number %d is divisible by %d" % (self.firstNumber, self.secondNumber)
        else:
            return "Number %d is not divisible by %d" % (self.firstNumber, self.secondNumber)