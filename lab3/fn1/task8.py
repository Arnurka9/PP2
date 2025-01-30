"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
"""


def has007(nums):
    givenlist = [0, 0, 7]
    index = 0

    for num in nums:
        if num == givenlist[index]:
            index += 1
        elif num == 0:
            index = 2 #позволяет выйти из ситуации 0000007 (поидее тут ничего не происходит)
        elif num == 7: 
            index = 0
        
        if index == len(givenlist):
            return True
    
    return False


nums = list(map(int, input("Input some ints include 0 and 7: ").split()))
print(has007(nums))


