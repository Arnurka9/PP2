"""
Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase,
or sequence that reads the same backward as forward, e.g., madam
"""

def palidrome_cheker(user_string: str):
    return user_string == ''.join(reversed(user_string))  #reversed() don't give reverse str

user_string = input("Write something: ")
user_string.lower()
print(palidrome_cheker(user_string))