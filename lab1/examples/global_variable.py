
"""
*Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

x = "easy"

def myfn() :
    print("Python is " + x)

myfn()



#* Difference from Local and Global val

language = "js"

def myfun():
    language = "py"
    print("I love " + language)

myfun() # i love py

print("I love " + language) # I love js



#* the "global" keyword

num = 5

def my_func():
    global num
    num = 10
    
print("Please. Just a " + str(num) + " minutes")

my_func()

print("Please. Just a " + str(num) + " minutes")

#we use global to make a local variable global

