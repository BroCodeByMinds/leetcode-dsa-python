# Problem: https://leetcode.com/problems/binary-search/
# Tags: Binary Search
# Approach: Iterative binary search on sorted array
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Identify the mid by dividing the sum of left and right

            if nums[mid] == target:    # If the mid value is the target, return its index
                return mid
            elif nums[mid] < target:   # If target is greater, search right half
                left = mid + 1
            else:                      # If target is smaller, search left half
                right = mid - 1

        return -1  # If target does not exist, return -1


# Example Usage
if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))  # Output: 4


# Notes:
"""
What binary search does?
    Binary search works on sorted arrays. It repeatedly:
        * Picks the middle element
        * Compares it to the target
        * Discards half of the space each time

Linear search: O(n)
    Start from the first element and go one by one — worst case visits every element.

Binary search: O(log n)
    Jump to the middle → decide to go left or right → repeat. Much faster.

Why base 2?
    We use base-2 logarithm (log₂) because binary search halves the problem space each step.

What is a logarithm?
    A logarithm is the inverse of exponentiation.

    Example:
        2^Z = 8  →  log₂(8) = Z  →  Z = 3

    So, a logarithm answers:
        "To what power must I raise 2 to get this number?"
"""
