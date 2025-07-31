# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Tags: Binary Search, Rotated Array
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in left half
                else:
                    left = mid + 1   # Target is in right half

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in right half
                else:
                    right = mid - 1  # Target is in left half

        return -1  # Target not found

    
# Example usage
if __name__ == "__main__":
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums, target))  # Output: 4
