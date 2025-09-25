class Solution:
    # @param A : list of integers
    # @return a long
    def subarraySum(self, A):
        total_sum = 0
        n = len(A)

        # Each element A[i] contributes to (i+1) * (n-i) subarrays
        for i in range(n):
            count = (i + 1) * (n - i)
            total_sum += count * A[i]

        return total_sum


# -------------------------
# Approach:
# - Instead of generating all subarrays (O(N^2)),
#   observe that A[i] appears in several subarrays:
#   -> It can be chosen as the starting point in (i+1) ways
#   -> It can be chosen as the ending point in (n-i) ways
#   -> So, total contribution = (i+1) * (n-i) * A[i]
# - Sum contributions for all elements.
#
# Time Complexity: O(N)   (single loop over array)
# Space Complexity: O(1)  (only variables used)
#
# Pattern: Contribution Technique / Prefix Sum Optimization
# -------------------------


# Example usage
print(Solution().subarraySum([1, 2, 3]))   # Output: 20
print(Solution().subarraySum([2, 1, 3]))   # Output: 19