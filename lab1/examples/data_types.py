
"""
*Built-in Data Types

Python has the following data types built-in by default, in these categories:

?   - Text Type:	    str
?   -Numeric Types:	    int, float, complex
?   -Sequence Types:	list, tuple, range
?   -Mapping Type:	    dict
?   -Set Types:	        set, frozenset
?   -Boolean Type:	    bool
?   -Binary Types:	    bytes, bytearray, memoryview
?   -None Type:	        NoneType
"""

#!the second version is called: Specific Data Type

x = "text" #str
print(type(x))
#or
x = str("text") #str
print(type(x))




x = 5 #int
print(type(x))
#or
x = int(5) #int
print(type(x))




x = 5.0 #float
print(type(x))
#or
x = float(5.0) #float
print(type(x))





x = 5 + 1j #complex
print(type(x))
#or
x = complex(5 + 1j) #complex
print(type(x))



x = [1, "text", 4.0] #list
print(type(x))
#or
x = list((1, "text", 4.0)) #list
print(type(x))



x = (1, "text", 4.0) #tuple
print(type(x)) 
#or
x = tuple((1, "text", 4.0)) #tuple
print(type(x)) 




x = range(10) #range
print(type(x))



x = {"name": "Arnur", "age": 18} #dict
print(type(x))
#or
x = dict(name = "Arnur", age = 18) #dict
print(type(x))





x = {"image", "picture", "art"} #set
print(type(x))
#or
x = set(("image", "picture", "art")) #set
print(type(x))






x = frozenset({"image", "picture", "art"}) #frozenset
print(type(x))
#or
x = frozenset(("image", "picture", "art")) #frozenset
print(type(x))





x = True #bool
print(type(x))
#or
x = bool(10) #bool
print(type(x))




x = b"Person" #bytes
print(type(x))
#or 
x = bytes(6) #bytes
print(type(x))




x = bytearray(10) #bytearray
print(type(x))

x = memoryview(bytes(10)) #memoryview
print(type(x))

x = None #NoneType
print(type(x))

