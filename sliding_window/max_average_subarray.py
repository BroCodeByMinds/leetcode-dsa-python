# Problem: https://leetcode.com/problems/maximum-average-subarray-i/
# Tags: Sliding Window, Array
# Approach: Fixed-size sliding window to track max sum
# Time Complexity: O(n), Space: O(1)

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate sum up to given index k => [1, 12, -5, -6, 50, 3]
        # window_sum = 1 + 12 + (-5) + (-6) ==> 2 (i.e from index 0 -> 3)
        window_sum = sum(nums[:k])
        max_total = window_sum

        # Start iteration from the given k and find the total sum of next window (i.e from index 1 -> 4)
        for i in range(k, len(nums)):
            # Add the element of current index and subtract the element from beginning index
            # Next window_sum = nums[4] - nums[4- 4] ==> 2 + 50 - 1 =>   51
            window_sum += nums[i] - nums[i-k]
            
            if window_sum > max_total:
                max_total = window_sum
        
        return max_total / 4
    
# Example usage
if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(Solution().findMaxAverage(nums, k)) 