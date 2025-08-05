# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Tags: Binary Search
# Approach: Modified binary search to locate pivot/minimum element
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid is greater than right, the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # The minimum is in the left half (including mid)
                right = mid

        return nums[left]


# Example Usage
if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))       # Output: 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2])) # Output: 0
    print(s.findMin([11, 13, 15, 17]))     # Output: 11