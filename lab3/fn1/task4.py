"""
You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an 
agrument and returns only prime numbers from the list.
"""


def filter_prime(list_nums):
    
    prime_list = []
    
    for num in list_nums:
        is_prime = True
        
        if num > 1:
            for vari in range(2, int(num**0.5) + 1):
                if num % vari == 0:
                    is_prime = False
        else:
            is_prime = False
            
        if is_prime:
            prime_list.append(num)
    
    return prime_list




list_nums = list(map(int, input("Input some integers: ").split()))

print(filter_prime(list_nums))
