class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)

        # Step 1: Build prefix sums
        prefix = [0] * (B + 1)
        for i in range(1, B + 1):
            prefix[i] = prefix[i - 1] + A[i - 1]

        # Step 2: Build suffix sums
        suffix = [0] * (B + 1)
        for i in range(1, B + 1):
            suffix[i] = suffix[i - 1] + A[n - i]

        # Step 3: Try all combinations of front + back picks
        max_sum = float("-inf")
        for k in range(B + 1):
            max_sum = max(max_sum, prefix[k] + suffix[B - k])

        return max_sum


# -------------------------
# Approach:
# - Precompute prefix sums for first B elements
# - Precompute suffix sums for last B elements
# - Try all combinations of taking k elements from front and (B-k) from back
# - Answer is maximum among these combinations
#
# Time Complexity: O(B)   (build prefix, build suffix, iterate k)
# Space Complexity: O(B)  (store prefix and suffix arrays)
#
# Pattern: Prefix Sum + Two Pointers (front/back picking)
# -------------------------


# Example usage
print(Solution().solve([-2, 1, -4, 5, 3], 2))   # Output: 8
print(Solution().solve([1, 2, 3, 4, 5], 3))     # Output: 12