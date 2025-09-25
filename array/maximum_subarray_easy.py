class Solution:
    # @param A : integer (size of array)
    # @param B : integer (max allowed sum)
    # @param C : list of integers (array elements)
    # @return an integer
    def maxSubarray(self, A, B, C):
        total_sum = 0

        # Check all subarrays using two pointers (i, j)
        for i in range(A):
            cur_sum = 0
            for j in range(i, A):
                cur_sum += C[j]

                if cur_sum <= B:
                    total_sum = max(total_sum, cur_sum)

        return total_sum


# -------------------------
# Approach:
# - Generate all subarrays (i, j).
# - Keep running sum for each subarray.
# - If sum <= B, update maximum.
#
# Time Complexity: O(N^2)   (since N ≤ 1000, acceptable)
# Space Complexity: O(1)    (no extra space used)
#
# Pattern: Brute Force / Subarray Sum
# -------------------------


# Example usage
print(Solution().maxSubarray(5, 12, [2, 1, 3, 4, 5]))  # Output: 12
print(Solution().maxSubarray(3, 1, [2, 2, 2]))        # Output: 0