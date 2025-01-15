
#* Specify a Variable Type

"""
Casting in python is therefore done using constructor functions:

*int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), 
*or a string literal (providing the string represents a whole number)

*float() - constructs a float number from an integer literal, a float literal or a string literal 
*(providing the string represents a float or an integer)

*str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""


#! int
x = int(1) #x will be 1
print(x)

x = int(2.99) #x will be 2
print(x)

x = int('3') #x will be 3
print(x)



#! float
x = float(1) #x will be 1.0
print(x)

x = float(2.12) #x will be 2.12
print(x)

x = float('2') #x will be 2.0
print(x)

x = float('2.12') #x will be 2.12
print(x)


#! str 
x = str(1) #x will be '1'
print(x)

x = str(9.2) #x will be '9.2'
print(x)

x = str("seven") #x will be "seven"
print(x)


