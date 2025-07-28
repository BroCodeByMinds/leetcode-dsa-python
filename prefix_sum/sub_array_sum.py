from collections import defaultdict
from typing import List


# Problem: https://leetcode.com/problems/subarray-sum-equals-k/
# Tags: Array, Prefix Sum, Hashing
# Approach: 
#       - Maintain running prefix sum
#       - Use a hash map to store how many times each prefix sum has occured
#       - Check if (prefix_sum - k) exist in the hash map
#       - If does exist, it means a subarray with sum k ends at the current index

def subArraySum(nums: List[int], k:int):
    prefix_sum = 0      # Running sum of elements
    count = 0           # Count the valid sub arrays

    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1        # Base Case : sum == 0 has occured once

    for index, num in enumerate(nums):
        prefix_sum += num

        # Check if there's a prefix sum that would make a subarray sum to k
        diff = prefix_sum - k
        if diff in prefix_counts:
            count += prefix_counts[diff]
        
        # Update the count of the current prefix sum
        prefix_counts[prefix_sum] += 1

    
    return count


# Example usage
print(subArraySum([1, 2, 3, 3, 2, 3], 3))