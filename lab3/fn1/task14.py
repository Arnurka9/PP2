"""
Create a python file and import some of the functions from the above 13 tasks and try to use them.
"""

from task1 import to_ounces #float
from task2 import to_centigrade #float
from task5 import all_permutations #str
from task12 import histogram #list


print(to_ounces(float(input("input grams: "))))
print()

print(to_centigrade(float(input("input fahrenheit: "))))
print()

all_permutations(input("write word/words: "))
print()

histogram(list(map(int, input("input some ints: ").split())))
