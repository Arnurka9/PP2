
#! Touples

#ex1 unchangeble collection 
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#ex2 In tuple elements can be repeated
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#ex3 len() for tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#! NOT a tuple 
thistuple = ("apple")
print(type(thistuple))

#ex4 correct version how create tuple
thistuple = ("apple",)
print(type(thistuple))

#ex5 checking type
thistuple = ("apple",)
print(type(thistuple))

#ex6 any type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#ex7 different types in one tuple
tuple1 = ("abc", 34, True, 40, "male")


#ex8 another way create tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#? Accsess Tuple Items

#ex9 access Tuple Items (also like list by index)
thistuple = ("apple", "banana", "cherry") 
print(thistuple[1])

#ex10 Negative index
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#ex11 slice 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#ex12  from begin to 4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#ex13   from 2 to end
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#ex14  slice with negative index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#ex15  checking existence
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


#? Update Tuples

#ex16  if we need to change a item/items  
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#ex17  if we need to add element
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#ex18  sum of two toples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y #here we create new tuple

print(thistuple)


#ex19 remove items 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#ex20 del tuple 
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


#? Unpacking a Tuple

#ex21 (nothing has been done yet)
fruits = ("apple", "banana", "cherry")

#ex22 Unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#ex23 Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#ex24 it works so that there are enough elements for everyone
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#? Loop Through a Tuple

#ex25  for loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#ex26  for loop through a tuple with another way
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
#ex27 with while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#? Join Tuples

#ex28   sum of two tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#ex29   multiplication of tuple  
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



#tuple has 2 methods 
#index()
#count()
