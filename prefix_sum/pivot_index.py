from typing import List

# Problem: https://leetcode.com/problems/find-pivot-index/
# Tags: Prefix Sum, Array
# Approach: Track left sum; derive right sum from total sum

def pivotIndex(nums: List[int]) -> int:
    total = sum(nums)  # Total sum of array
    left_sum = 0        # Sum of elements to the left of current index

    for index, num in enumerate(nums):
        # Right sum = total sum - left sum - current number
        right_sum = total - left_sum - num

        # If left and right sums are equal, return index
        if left_sum == right_sum:
            return index

        # Move current number to left_sum for next iteration
        left_sum += num

    # If no pivot index found, return -1
    return -1