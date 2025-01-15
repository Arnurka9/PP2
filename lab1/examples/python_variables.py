#Python doesn't have command for declaring a variable
#A variable is created the moment you first assign a value to it.

a = 7
b = "I'm just a baby"
print(a)
print(b)


#* Casting
#if we want to specify the type of a variable, we can use type casting to create a variable with the type we need

a = str(1)
b = float(1)
c = int(1)


#* Check the type of variable

print(type(a)) #<class 'str'>
print(type(b)) #<class 'float'>
print(type(c)) #<class 'int'>

#we can check the type of variable with the command type()



#* Single or Double Quotes?

my_str = "Hello world"
#is the same as
str_is_mine = 'Hello world'

print(my_str == str_is_mine) #True


#* Case-Sensitive

letter = "a"
#isn't the same as 
letter2 = "A"

print(letter == letter2) #False