
#ex1  Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
#ex2 the same but using index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
  
#ex3 while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  

#ex4 Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

