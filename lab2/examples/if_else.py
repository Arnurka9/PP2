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



#* ex9 (and in if)
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  


#* ex10 (or in if)
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
  
#* ex11 (not if if)
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  

#* ex12 (nested if)
# nested - вложенный
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    
#* ex13 (pass in if-else)
a = 33
b = 200

if b > a:
  pass

# Usually pass we are using pass when you want to say: Here will be code soon
# Another way when we need some variable without extra variable

for i in range(5):
    if i % 2 == 0:
        pass
    else:
        print(f"Нечётное число: {i}")
