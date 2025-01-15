
#* Escape Character

"""
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
"""


#? \"
my_text = "I call my dog as \"Princess\" "
print(my_text)

#? \'
my_text = 'I call my dog as \'Destroyer\' '
print(my_text)


#? \\ - Backslash
my_text = " \\a "
print(my_text) #\a


#? \n - new line

my_text = "I don't have a brain. \n But I have a plan"
print(my_text)


#? r - carriage return

my_text = "Hello\rWorld"
print(my_text) 

#\r as if writing over the left symbols it writes right and left because of this it gradually disappears



#? \t - tab

my_text = "Hello\tWorld"
print(my_text) #Hello   World
#with tab


#? \b - backspace 

my_text = "Hello World\b"
print(my_text) #Hello Worl without last letter



#? \f - form feed

my_text = "Hello\fworld"
print(my_text) 

#this escape character use often text files. So we don't see change.



#? \ooo - Octal value (from 000 to 377)

my_text = "\101"
print(my_text) #A

# Octal performance


#? xhh - hex value 

my_text = "\x41"
print(my_text) #A

my_text = "\x48\x65\x6c\x6c\x6f"
print(my_text) #Hello

# Hex performance