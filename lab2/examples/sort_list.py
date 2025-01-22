
#ex1 Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)



#ex2 numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


#ex3 reverse Alphanumerically (reverse = True:) in sort  
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


#ex4 reverse numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#ex5 Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#ex6 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


#ex7 Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#ex8 reverse 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


