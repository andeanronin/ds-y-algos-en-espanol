
"""
Given an array nums containing n distinct numbers in the range [0, n] , return the only number in the range that is missing from the array.

Example 1:  
input: nums = [3, 0, 1]
output: 2
explanation: n = 3 since there are three numbers, the missing number in the range is 2 

Example 2: 
input: nums = [0, 1]
output: 2 
explanation: n = 2 since there are two numbers [0, 2] , so the missing nubmer is 2
"""


anArray = [0, 1, 5, 3, 2]


def missing_number(nums): 
    """
    time complexity of this solution is nlog(n) because sorting is slow (nlog(n)) in python
    """
    print('array length: ', len(nums))
    nums.sort()  # sorting in python is slow: nlog(n)

    for i, v in enumerate(nums):
        print(i, v)
        if (i != v):
            return v - 1 

        if v == len(nums) - 1:
            return v + 1 
        
def missing_number2(nums):
    """
    len = O(1)
    range takes O(1)
    sum  = O(n) -- if our list size doubles, we only have to do double the additions 
    1+ 
    """
    return sum(range(len(nums) + 1 )) - sum(nums)

