# Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Tags: Hash Map, Counting
# Approach: Use a hash map to store element frequencies from nums1, then check and decrement while iterating nums2
# Time Complexity: o(n + m)
# Space Complexity: o(min(n, m))

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_map = {}
        result = []

        for n in nums1:
            count_map[n] = count_map.get(n, 0) + 1
        
        for n in nums2:
            if count_map.get(n, 0) > 0:
                result.append(n)
                count_map[n] -= 1
        
        return result

# Example Usage
if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersect(nums1, nums2))  # Output: [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersect(nums1, nums2))  # Output: [4, 9]
                

# Notes:
"""
Pattern:
    - Hash Map (Counting frequency of elements)
    - If arrays are sorted, could also use Two Pointers for optimization.

Approach:
    1. Build a frequency map for nums1.
    2. Iterate through nums2:
        * If element exists in map with positive count → add to result.
        * Decrease the count in the map.
"""