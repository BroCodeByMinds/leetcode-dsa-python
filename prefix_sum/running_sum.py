from typing import List

# Problem: https://leetcode.com/problems/subarray-sum-equals-k/
# Tags: Prefix Sum, Array
# Approach : Iterate through array and calculate the running sum 
#           Add the running sum to the current element in place

def runningSum(nums: List[int]):
    total = 0 # Initialize the running sum

    for index, num in enumerate(nums):
        nums[index] += total # Add the running sum to the current element 
        total += num # Update the running sum

    return nums