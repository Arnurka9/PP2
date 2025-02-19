import re

text = input("Enter: ")
with_under = re.sub(r"(?<!^)([A-Z])", lambda match: " " + match.group(0), text)
print(with_under)
    

# (?<!^) - not the beginning