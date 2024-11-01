"""
Given an array nums, for each nums[i] find out how many numbers in the array are smaller than it.

That is, for each nums[i] you have to count the number of j's such that j =! i and nums[j] < nums[i]

Return the answer in the array.

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Difficulty: Easy 
"""

# brute force solution. time complexity: O(n^2)  and space complexity = O(n)
def brute_solution(int_array):
    """
    Brute force Solution: 
        - initiate empty array
        - iterate over each item in the array with a for loop
            - initiate count variable = 0
        - inner for loop for each item in the arrray
            - if i is smaller than outer foor loop i 
            - count += 1 
            - append count to empty array
    """
    output = []
    for i in int_array:   # time complexity: O(n)
        count = 0
        for j in int_array: # time complexity: O(n)   
            if j < i:
                count += 1  
        output.append(count)  # O(1)
    return(output)               # net time complexity of nested for loop function: O(n^2) 
nums = [8,1,2,2,3]
test = brute_solution(nums)
print(test)

#  solution 2
def solution2(nums):
    """
    If we sort the array, and with enumerate get the indices and number pairs, then we know that the index also tells us the amount
    of numbers smaller than the number. 
        - the smallest number in the array will be at index 0, and 0 are the amount of numbers smaller than the smallest number. 
        - the largest number in the array will be at index X, and x will be the amount of numbers that are smaller than it.
    """
    nums = [8,1,2,2,3]

    temp = sorted(nums)
    d = {}
    for i, num in enumerate(temp):
        if num not in d:
            d[num] = i

    output = []
    for num in nums:
        output.append(d[num])
    return output

nums2 = [8,1,2,2,3]
test2 = brute_solution(nums2)
print(test2)