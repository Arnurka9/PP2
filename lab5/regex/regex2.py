import re 

text = input("Enter: ")
pattern = re.search(r'ab{2,3}', text)
print(pattern)