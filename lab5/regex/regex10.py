import re

text = input("Enter: ")
camelTo_snake = re.sub(r"([A-Z])", lambda match: "_" + match.group(0).lower(), text)
print(camelTo_snake)