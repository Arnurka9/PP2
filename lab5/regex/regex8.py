import re

text = input("Enter: ")
splitAllWords = re.split(r"(?<!^)(?=[A-Z])",text)
print(splitAllWords)

# (?<!^) - not the beginning
# (?=pattern) - след элемент паттерн 