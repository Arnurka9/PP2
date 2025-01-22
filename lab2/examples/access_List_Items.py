
#ex1 Access Items (by index)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


#ex2 using negarive index
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#ex3 we can output multiple elements as a separate list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


#ex4 if we need output many elements with begin then just not put in slace first element
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#ex5 we can output many elements using negative index too
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


#ex6 check for existence 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
