

#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.


# ex1 (example of while loop)
i = 1
while i < 6:
  print(i)
  i += 1
  

#ex2 break (if we need to stop loop immediately we can use break statement)
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  

#ex3 continue (if we need to pass some iterations we can use continue)
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  


#ex4 else statement (if we need to do something after loop we can use else construction)
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


