"""
Problem: Sum of Squares of First n Natural Numbers
Pattern: Sum of Natural Numbers
Time Complexity: O(1) — Direct formula
Space Complexity: O(1) — Constant space

Given an integer n, return the sum of squares of first n natural numbers.

Approach:
---------
- Use the formula: S = n(n+1)(2n+1) / 6
- This avoids looping and gives an O(1) solution.
"""
class Solution:
    def sum_of_squares(self, n: int) -> int:
        if n <= 0:
            return 0
        return (n * (n + 1) * (2 * n + 1)) // 6


# --------------- Example Usage --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.sum_of_squares(5))   # Expected Output: 55
    print(sol.sum_of_squares(10))  # Expected Output: 385