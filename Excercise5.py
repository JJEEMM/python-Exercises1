__author__ = 'Justin'

"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class MyString:
    def __init__(self):
        self.my_str = ""

    def get_string(self):
        self.my_str = input("Enter a String: ")

    def print_string(self):
        print(self.my_str.upper())

strObj = MyString()
strObj.get_string()
strObj.print_string()

"""
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()
"""