# Problem: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Pattern: Two Pointers / Array In-place

# Time and Space Complexity
# Time Complexity: O(n) — single pass through the array
# Space Complexity: O(1) — in-place modification, no extra array used

# Approach (Optimal)
# Use a two-pointer technique:
# i points to the last unique element found. Start with i = 0.
# j scans the array from index 1 to the end.
# If nums[j] != nums[i], increment i and set nums[i] = nums[j].
# Finally, return i + 1 as the number of unique elements.

# Tips and Tricks
# Since the array is sorted, duplicates are consecutive → two-pointer technique is ideal.
# Do not worry about values beyond k — they can be anything.
# Always return the count i + 1, not the last index.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0  # pointer for last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # move unique element to the front

        return i + 1  # count of unique elements

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print("Number of unique elements:", k)
    print("Array after removing duplicates:", nums[:k])
