
#* Slicing

"""
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""

my_str = "Hello world"
print(my_str[1:5]) #ello

#we cut from 2 symbols (since the array is counted from 0) to 4 fourth



#* Slice From the Start
#By leaving out the start index, the range will start at the first character:

my_str = "Jojo is the best anime"
print(my_str[:5]) #Jojo




#* Slice To the End
#By leaving out the end index, the range will go to the end:

my_str = "This is for my safety"
print(my_str[3:]) #s is for my safety



#* Slice From the Start To the End

my_str = "uiauiauia"
print(my_str[:]) #uiauiauia



#* Negative Indexing
#Use negative indexes to start the slice from the end of the string:

my_str = "Have a nice day"
print(my_str[-5:-2]) #e d

