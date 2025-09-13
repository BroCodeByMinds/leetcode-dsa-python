# Problem: Remove Element
# Link: https://leetcode.com/problems/remove-element/
# Pattern: Two Pointers / In-place Array Modification
# Time Complexity: O(n) — We iterate the array once
# Space Complexity: O(1) — No extra data structure used

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Problem: Remove Element
        Link: https://leetcode.com/problems/remove-element/
        Pattern: Two Pointers / In-place Array Modification
        Time Complexity: O(n) — Iterate array once
        Space Complexity: O(1) — In-place modification
        """

        k = 0  # write index to place next valid element

        # Traverse all elements
        for i in range(len(nums)):
            if nums[i] != val:
                # Keep only elements not equal to val
                nums[k] = nums[i]
                k += 1

        # k is the count of elements not equal to val
        return k


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    sol = Solution()

    nums1 = [3, 2, 2, 3]
    k1 = sol.removeElement(nums1, 3)
    print(k1, nums1[:k1])  # Expected: 2, [2, 2]

    nums2 = [0,1,2,2,3,0,4,2]
    k2 = sol.removeElement(nums2, 2)
    print(k2, nums2[:k2])  # Expected: 5, [0,1,3,0,4] (order may vary)
