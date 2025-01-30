"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""

def has_33(nums):
    has_two3 = False
    
    for i in range(0, len(nums)-1):
        if nums[i] == nums[i+1] and nums[i] == 3:
            has_two3 = True
        
    return has_two3
            
     
            

nums = list(map(int, input("Input some ints with 3: ").split()))
print(has_33(nums))