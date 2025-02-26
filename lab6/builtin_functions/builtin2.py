
text = input("Enter text: ")

upperLetters = sum(1 for char in text if char.isupper())
lowerLetters = sum(1 for char in text if char.islower())

print("Amount of upper letters:", upperLetters)
print("Amount of lower letters:", lowerLetters)