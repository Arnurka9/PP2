s = input("Enter string: ")

print(s.lower() == "".join(reversed(s.lower())))