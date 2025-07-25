from typing import List

# https://leetcode.com/problems/find-pivot-index/
def pivotIndex(nums: List):
    total = sum(nums)
    left_sum = 0

    for index, num in range(len(nums):
        right_sum = total - left_sum - num

        if right_sum == left_sum:
            return index
        
        left_sum += num
    
    return -1 