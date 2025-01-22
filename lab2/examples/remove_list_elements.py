


#ex1 remove() 

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#ex2 remove() removed one banana not all

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) 


#ex3 pop()  using index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#ex4   remove last element
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


#ex5   The del keyword also removes the specified index

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#ex6   del can delete list

thislist = ["apple", "banana", "cherry"]
del thislist


#ex7  delete all element of list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

