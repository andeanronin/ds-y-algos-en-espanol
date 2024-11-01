# Find all numbers that disappeared in array

"""
Given an array nums of n integers, where nums[i] is in the range [1, n]  
return an array of all the integers in the range [1, n] that do not appear in nums. 

Example:
    - input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
    - output: 5, 6
    - range: [1, 8]


Make a sorted list of the numbers in the given range, all_nums = [1, 2, 3, 4, 5, 6, 7, 8]
- Set nums = set(nums)
- Sort set = sort(set) 
Iterate over nums, get value i, iterate over list of range, remove the value from list of range
Whatever numbers are left in all_nums are the missing ones.  
"""

nums = [4, 3, 2, 7, 8, 2, 3, 1] # size = 8


def solution(inputnums):
    comparison_list = list(range(1, len(inputnums) + 1))

    print('comparison list: ', comparison_list)
    set_nums = set(inputnums)
    print('set of nums: ', set_nums)
    
    for i in set_nums:
        comparison_list.remove(i)
    
    print('missing values: ', comparison_list)

solution(nums)
    

def solution_two(nums):
    full_set = set(range(1, len(nums) + 1))

    set_nums = set(nums)

    missing_values = full_set - set_nums

    return missing_values

print(solution_two(nums))



    

    

    



