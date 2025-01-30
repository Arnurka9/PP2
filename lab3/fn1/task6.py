"""
Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
"""

def reverse_text(user_text: str):
    words = user_text.split()
    words.reverse()
    user_text = ' '.join(words)
    return user_text

user_text = input("Write something: ")
print(reverse_text(user_text))
