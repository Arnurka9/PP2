"""
Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
"""

def unique_element(list_nums):
    unique_list = []
    
    for num in list_nums:
        if num not in unique_list:
            unique_list.append(num)
    
    return unique_list


list_nums = list(map(int, input("Input some ints: ").split()))
print(unique_element(list_nums))
