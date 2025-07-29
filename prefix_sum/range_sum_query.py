# Problem: https://leetcode.com/problems/range-sum-query-immutable/
# Tags: Prefix Sum, Array
# Approach: Precompute the prefix sum to answer range sum queries in O(1) time.
# Time Complexity:
#   - Constructor: O(n) where n = len(nums)
#   - sumRange: O(1) per query
# Space Complexity: O(n) for storing prefix sums

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        """
        Initializes the object with the integer array nums.
        Builds a prefix sum array where prefix_sum[i] stores the sum of nums[0] to nums[i].
        """
        self.prefix_sum = []
        current_sum = 0

        for n in nums:
            current_sum += n
            self.prefix_sum.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        """
        Returns the sum of elements between indices left and right (inclusive).
        Efficiently computed using the prefix sum array.
        """
        right_sum = self.prefix_sum[right]
        left_sum = self.prefix_sum[left - 1] if left > 0 else 0
        return right_sum - left_sum


if __name__ == "__main__":
    # Initialize the object
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    
    # Query the sum between various ranges
    print(num_array.sumRange(0, 2))  # Output: 1      → -2 + 0 + 3
    print(num_array.sumRange(2, 5))  # Output: -1     → 3 -5 + 2 -1
    print(num_array.sumRange(0, 5))  # Output: -3     → Full array sum
