
#in python we can 2 variants of write string. We can use '' or ""

my_str = "Hello world"
str_of_mine = 'Have a nice day'

print(str_of_mine)
print(my_str)



#* Quotes inside Quotes

print("His name is 'Tady'")
print('Her name is "Aknur"')

#we can use quotes inside quotes if one pair of quotes different from another



#* example with big string

my_text = """ I need more relax time.
But I can't relax. 
"""
print(my_text)



#* strings are arrays

my_str = "I love cars"

print(my_str[3])

#string is an array. We can access any symbol by index




#* Looping Through a String

my_str = "I love a pizza"

for l in my_str:
    print(l)

#the variable l goes through each character of the string and the print function prints each l
#переменная л проходит по каждому символу строки и функция принт выводит каждый л





#* Length of str

my_str = 'U so pretty'

print(len(my_str)) #11



#* Check String
# To check if a certain phrase or character is present in a string, we can use the keyword #! in

my_str = "I wanna be your vacuum cleaner"

print("wanna be your" in my_str) #True




#* Check with if

if "vacuum cleaner" in my_str:
    print("Yes, 'vacuum cleaner' is present.")




#* Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword #! not in.

my_str = "Venom"

print("love" not in my_str) #True



#* Check with if

if "Spidermen" not in my_str:
    print("Yes, 'Spidermen' isn't in my_str")

#equivalent situation