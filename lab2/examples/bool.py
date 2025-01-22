
#* Boolean

# ex1 You can evaluate any expression in Python, and get one of two answers, True or False.

print(10 > 9)
print(10 == 9)
print(10 < 9)




# ex2 When you run a condition in an if statement, Python returns True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



# ex3 convert   any val -> bool()

print(bool("Hello"))
print(bool(15))


# ex4 the same example with variable 

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# ex5   true val 
"""
Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])



#ex6    false val

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})



#ex7 (One more value, or object in this case, evaluates to False, and that is 
# if you have an object that is made from a class with a __len__ function that returns 0 or False:)

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



#ex8 Functions can Return a Boolean

def myFunction() :
  return True

print(myFunction())



#ex9  you can execute code based on the Boolean
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
  
  
#ex10  Python also has many built-in functions that return a boolean value, 
# like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))

