import re

text = input("Enter: ")
pattern = re.findall(r"\b[A-Z][a-z]+\b",text)
print(pattern)