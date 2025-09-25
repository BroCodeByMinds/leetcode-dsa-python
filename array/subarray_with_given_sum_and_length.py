# Approach:
# - Use Sliding Window since subarray length B is fixed.
# - Compute the sum of the first B elements.
# - Slide the window across the array:
#     - Add the new element entering the window.
#     - Remove the old element leaving the window.
# - Check if at any point the sum equals C.
# - Return 1 if such subarray exists, otherwise 0.
#
# Time Complexity: O(N)  -> Each element processed once
# Space Complexity: O(1) -> Constant extra space


class Solution:
    # @param A : list of integers
    # @param B : integer (window length)
    # @param C : integer (target sum)
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)

        # Step 1: Calculate sum of first window
        window_sum = sum(A[:B])
        if window_sum == C:
            return 1

        # Step 2: Slide the window
        for i in range(B, n):
            window_sum += A[i] - A[i - B]  # add new, remove old
            if window_sum == C:
                return 1

        return 0


# Example usage:
if __name__ == "__main__":
    print(Solution().solve([4, 3, 2, 6, 1], 3, 11))  # Output: 1
    print(Solution().solve([4, 2, 2, 5, 1], 4, 6))   # Output: 0