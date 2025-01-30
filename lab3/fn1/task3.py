"""
Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
"""


def solve(numheads, numlegs):
    chikens = numlegs//4
    rabbits = numheads - chikens
    return f"Count of rabbints: {rabbits} and count of chikens: {chikens}"
    
heads = int(input("amount of heads: "))
legs = int(input("amount of legs: "))

print(solve(heads, legs))