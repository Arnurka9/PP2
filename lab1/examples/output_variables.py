
#*Output Variables
#The print() function in Python is commonly used to display the values of variables.

boy = "Sigmaboy"
print(boy)




#* output multiple variables
#we can output several values ​​at once in python separated by commas

sister1 = "Amanda"
sister2 = "Linda"
sister3 = "Rose"
print(sister1, sister2, sister3)

#Note: and it's convenient that the values ​​come out immediately with a space



#* We can use + for output multiple variables
print(sister1 + sister2 + sister3)

#Note: but here without space between variables, so we must add their on one's own


#Note: but for numbers + is opperator of sum
x = 55
y = 45
print(x+y)



#! if we try + with str and int. We will get an error

x = 55
my_str = "Hello world"
# print(my_str + x)

#! it's a mistake

#* so we need use , if we need to separate different types of varibles in one output

print(x, my_str) #55 Hello world
