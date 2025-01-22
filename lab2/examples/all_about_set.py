
#! SETS

#ex1 usial set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#ex2 set has only unique items and set is unordered, unchangeable, unindexed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#ex3 True == 1, so 1 was removed, because set meet True firstly than 1
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#ex4  the same
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#ex5 len of set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#ex6 set also can include different type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#ex7 even in one set 
set1 = {"abc", 34, True, 40, "male"}

#ex8 checking type
myset = {"apple", "banana", "cherry"}
print(type(myset))

#ex9 another way create a set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



#? Access Set Items




#ex10  output all items using for
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#ex11 check existence of item
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#ex12 check absense of item
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)



#? Add Set Items

#! Set items are unchangeable, but you can remove items and add new items.



#ex13 adding element to a set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#ex14 add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#ex15 add another collection
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


#? Remove Set Items


#ex16 remove items 
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#ex17  method without error 
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#ex18  random item will be removed 
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#ex19  will delete all items inside set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#ex20 delete set 
thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset)


#? Loop sets

#ex21 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


#? Join Sets


#ex22  united both set in one
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#ex23  bitwise or 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#ex24  union() can unite many sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#ex25  and we can use many bitwise or
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)


#ex26  union() can unite different types  
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


#ex27  when you need to save the original set use update, and if you need a completely new one use union
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)




#ex28 ONLY the duplicates

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#ex29  bitwise and
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

#ex30  update with intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#ex31 show difference from each other
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

#ex32 only difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#ex33  the same as difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

#ex34 update + difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#ex35  all difference but i can just use update() or union()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#ex36 the same as symmetric_difference 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

#ex37 symmetric_difference + update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)