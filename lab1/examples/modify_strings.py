
#* Upper Case

# upper() - converts characters to uppercase

my_str = "Hello World"
print(my_str.upper()) 



#* Lower Case

# lower() - converts characters to lowercase

my_str = "HELLO WORLD"
print(my_str.lower())




#* Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

#! The strip() method removes any whitespace from the beginning or the end:

my_str = "   hello world   "
print(my_str.strip())




#* Replace String
# The replace() method replaces a string with another string:

my_str = "Your Welcome"
print(my_str.replace("o", "i")) #Yiur Welcime

#this method replace all letters to another



#* Split String
# The split() method returns a list where the text between the specified separator becomes the list items.


my_str = "Banana,Potato,Apple,Cucumber,Orange,Pear"
print(my_str.split(","))

#['Banana', 'Potato', 'Apple', 'Cucumber', 'Orange', 'Pear']

#the argument of the split function is the separator by which the function will divide the text into sheet elements


