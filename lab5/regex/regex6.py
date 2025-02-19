import re

text = input("Enter: ")
replaceToColon = re.sub(r"[ ,.]", ":" , text)
print(replaceToColon)
