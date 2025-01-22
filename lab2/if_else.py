# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


#* ex1
a = 999
b = 1000
if b > a:
    print("b greater than a")
    


#! ex2 (how not to do it)
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error


#* ex3 elif (if we want to add output in some case then we use elif)
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  

#* ex4 else (the "else" construction is added when it is necessary to specify actions that do not correspond to the condition)
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
#* ex5 (we can not add "elif")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
#* ex6 (shortly version)

if a > b: print("a is greater than b")


#* ex7 (more details)
a = 2
b = 330
print("A") if a > b else print("B")


#* ex8 (ternary operator in python)
#(multiply conditions)
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

