import re

text = input("Enter: ")
pattern = re.search(r"ab*", text)
print(pattern)