# Problem: https://leetcode.com/problems/find-peak-element/
# Tags: Binary Search
# Approach: Binary Search Template II — move in direction of higher neighbor
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid  # Peak is at mid or to the left
            else:
                left = mid + 1  # Peak is to the right

        return left  # left == right is the peak index


# Example usage
if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement([1, 2, 3, 1]))          # Output: 2 (3 is a peak)
    print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5 or 1 (6 or 2 are peaks)
