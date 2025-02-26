import math

list_of_ints = list(map(int , input("Enter ints: ").split()))
product = math.prod(list_of_ints)
print("Result of product:", product)
