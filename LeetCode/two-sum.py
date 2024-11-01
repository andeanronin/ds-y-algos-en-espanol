# Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such tha they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice. 

you can return the answer in any order. 

Examples:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

"""
nums = [2,7,11,15]

target = 13

def solution(nums):
    for i in range(0, len(nums)):
        diff = target - nums[i] 
        if diff in nums:
            print(nums.index(diff), i)
            return

solution(nums)
            

def solution_two(nums, target):
    hashMap = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in hashMap:
            return (index, hashMap[diff])
        
    hashMap[value] = index  # add value to hashmap if diff not in hashmap 

nums_2 = [2,7,11,15]
solv = solution_two(nums_2, 9)




