import re

text = input("Enter: ")
pattern = re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", text) 
print(pattern)

#(?: ) - не брать, суть в том, что элементы выводятся по последнему слову
# и чтобы брать все целиком, нужно не брать последнее слово