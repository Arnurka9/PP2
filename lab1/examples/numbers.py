#Python has 3 type of variable 

#1 int
#2 float
#3 complex


x = 1 #int
print(type(x))

x = 1.2 #float
print(type(x))

x = 1 + 2j #complex
print(type(x))



#* Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 12232131231231231432
print(x)

x = -123213123
print(x)

x = 0
print(x)



#* Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.0
print(x)

x = -23.232321312
print(x)

x = 1.22
print(x)


#* Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 20e20
print(x) #2e+21

x = 12E10
print(x) #120000000000.0

x = -99.2e100
print(x) # -9.92e+101




 
#* Complex numbers are written with a "j" as the imaginary part:

x = 3+3j
print(type(x))

x = 9j
print(type(x))

x = -8j
print(type(x))




#* We can convert from one type to another with int(), float(), complex()

int_num = 10
float_num = 10.99
complex_num = 1j

a = float(int_num)
print(a)

b = int(float_num)
print(b)

c = complex(int_num)
print(c)
c = complex(float_num)
print(c)

#! Note: You cannot convert complex numbers into another number type.




#* Random number

#we don't have any random() function, but we can call the random library and use the randrange() function there

import random 

print(random.randrange(1, 10))

#we set a range (1-9) for a random number and output it. Each time we will get a different number

