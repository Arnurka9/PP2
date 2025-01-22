
#ex1 change list item

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#ex2 change a range of item value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#ex3 if use put more items than your range then these items just will insert to list
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#ex4 here we replaced "banana" and "cherry" to "watermelon"
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#ex5 insert (work only when we give index and value)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

