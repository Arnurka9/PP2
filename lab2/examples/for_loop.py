# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


#ex 1 example of for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  

# ex2 Looping Through a String

for x in "banana":
  print(x)
  
  
# ex3 break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#ex4 the same situation but here we see consequences using break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#ex5 continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  
#ex6 range()  (range of numbers from #1number to #2number not inclusive, then you can add a step as a third argument)
for x in range(6):
  print(x)


#ex7 
for x in range(2, 6):
  print(x)
  
  
#ex8 
for x in range(2, 30, 3):
  print(x)
  
#ex9  else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
  
#ex10 else with break
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #this part of code doesn't work
  


#ex11  Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    

#ex12 pass
for x in [0, 1, 2]:
  pass

#pass does nothing
