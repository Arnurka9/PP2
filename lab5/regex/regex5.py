import re 

text = input("Enter: ")
pattern = re.search(r"a.*b+\b",text)
print(pattern)