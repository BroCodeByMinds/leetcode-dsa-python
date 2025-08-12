# Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Pattern: Two Pointers
# Time Complexity: O(n)  # We traverse the array at most once with two pointers
# Space Complexity: O(1)  # We use only constant extra space

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given a sorted array `numbers`, find two numbers such that they sum up to `target`.
        Return their 1-based indices as [index1, index2], where index1 < index2.
        """
        # Initialize two pointers
        left, right = 0, len(numbers) - 1

        # Iterate until the two pointers meet
        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Found the pair → return 1-based indices
                return [left + 1, right + 1]
            elif current_sum < target:
                # Increase the sum by moving the left pointer
                left += 1
            else:
                # Decrease the sum by moving the right pointer
                right -= 1
        
        # Since the problem guarantees a solution, we won't reach here
        return []
    

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9)) # [1, 2]
    print(s.twoSum([2,3,4], 6)) # [1, 3]


