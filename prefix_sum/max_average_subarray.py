# Problem: https://leetcode.com/problems/maximum-average-subarray-i/
# Tags: Prefix Sum, Array
# Approach: Use prefix sum array to compute window sums
# Time Complexity: O(n), Space: O(n)

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)

        max_avg = float('-inf')
        for i in range(k, len(prefix_sum)):
            total = prefix_sum[i] - prefix_sum[i - k]
            avg = total / k
            max_avg = max(max_avg, avg)

        return max_avg


# Example usage
if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(Solution().findMaxAverage(nums, k))  # Output: 12.75