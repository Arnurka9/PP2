"""
Write a function that accepts string from user and print all permutations of that string.
"""


import itertools

def all_permutations(user_string: str):
    for p in itertools.permutations(user_string):
        print(''.join(p))


if __name__ == "__main__":
    user_string = input("input text: ")
    all_permutations(user_string)