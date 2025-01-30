
"""
Define a class which has at least two methods: getString: to get a string from console input printString: 
to print the string in upper case.
"""

class StrangeStringClass:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input("Write string: ")
    
    def to_upperCase(self):
        print(self.string.upper())


user_string1 = StrangeStringClass
user_string1.getString()
user_string1.to_upperCase()

print(user_string1)
