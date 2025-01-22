
#List 

# ex1 (example of list)
thislist = ["apple", "banana", "cherry"]
print(thislist)


# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.


#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.



# ex2 (the sheet may contain the same values)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)



# ex3 len() with list

thislist = ["apple", "banana", "cherry"]
print(len(thislist))



# ex4 any data type in list

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]



# ex5 list can consist of different data type
list1 = ["abc", 34, True, 40, "male"]



# ex6 type() for list

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'>


# ex7 list()

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


