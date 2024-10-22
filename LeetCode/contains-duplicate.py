# contains dupulicate

"""
Given an interger array nums, return true if any value appears at least twice in the array.

Return false if every value is distinct.

Example: 
- nums = [1, 2, 1 , 4]  (return true) 
- nums = [2, 5 , 8 , 9] (return false) 

"""

myArray = [1, 1 , 5, 9] 


def containsDuplicate(nums):
    if len(nums) == len(set(nums)):
        return True
    else:
        return False 

print(containsDuplicate(myArray))