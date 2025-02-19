import re

text = input("Enter: ")
snake_toCamel = re.sub(r"_([a-z])", lambda match: match.group(1).upper() ,text)
print(snake_toCamel)