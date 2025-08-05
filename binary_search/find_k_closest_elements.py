# Problem: https://leetcode.com/problems/find-k-closest-elements/
# Tags: Binary Search, Two Pointers
# Time Complexity: O(log(n - k) + k)
# Space Complexity: O(1) + O(k) for output

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # We want to find the best starting index for a window of size k
        left = 0
        right = len(arr) - k  # last valid starting point for window of size k

        while left < right:
            mid = (left + right) // 2

            # Compare the distance between x and the edge elements of the window
            dist_left = x - arr[mid]
            dist_right = arr[mid + k] - x

            if dist_left > dist_right:
                # The right side of the window is closer to x, move window to the right
                left = mid + 1
            else:
                # The left side is closer (or equally close), move window to the left
                right = mid

        # Once left == right, we have found the best starting point
        return arr[left:left + k]


# Example Usage
s = Solution()
print(s.findClosestElements([1, 2, 3, 4, 5], k=4, x=3))    # Output: [1, 2, 3, 4]
print(s.findClosestElements([1, 1, 2, 3, 4, 5], k=4, x=-1)) # Output: [1, 1, 2, 3]

"""
Example to Remember

Input:
arr = [1, 2, 3, 4, 5], k = 4, x = 3

Valid windows of size 4:
- [1, 2, 3, 4]  (start at index 0)
- [2, 3, 4, 5]  (start at index 1)

Comparison:
- |1 - 3| = 2   (left edge of first window)
- |5 - 3| = 2   (right edge of second window)

Since distances are equal → prefer the smaller values → pick the first window → [1, 2, 3, 4]
"""
