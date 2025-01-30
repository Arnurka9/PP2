
"""
Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
"""

is_prime = lambda num: num>1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

user_list = list(map(int, input("Input some ints: ").split()))

prime_list = list(filter(is_prime, user_list))

print(prime_list)