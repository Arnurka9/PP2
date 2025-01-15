
# How we remember we can't write:
# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# it's mistake!

#* F-string
#* But we can combine strings and numbers by using f-strings or the format() method!


#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets 
#{} as placeholders for variables and other operations.


age = 18
print(f"My name is Arnur. I'm {age} years old")







#* Placeholders and Modifiers

#A placeholder can contain variables, operations, functions, and modifiers to format the value.


price = 48
txt = f"It cost {price} dollars"
print(txt)

#A placeholder can include a modifier to format the value.

#*A modifier is included by adding a colon : followed by a legal formatting type,
#*like .2f which means fixed point number with 2 decimals:

price = 100
txt = f"Cost of this thing less than {price:.2f}"
print(txt) #100.00








#* A placeholder can contain Python code, like math operations:

print(f"This buggy costs {12*5} dollars")
