
# ex1  append()  add to end (need one argument value)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# ex2 insert()   add to anywhere (need two argument index, value)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#ex3 extend()   to append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#ex4 The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)