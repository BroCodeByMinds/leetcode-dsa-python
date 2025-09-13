"""
Problem: Sum of All Even Numbers ≤ n
Pattern: Sum of Natural Numbers
Time Complexity: O(1) — Direct formula
Space Complexity: O(1) — Constant space

Given an integer n, return the sum of all even numbers less than or equal to n.

Approach:
---------
- Find the largest even number ≤ n (m).
- Number of terms (k) = m // 2.
- Use AP sum formula: S = (k/2) * (first_term + last_term).
- Here, first_term = 2, last_term = m.
"""
class Solution:
    def sum_of_evens(self, n: int) -> int:
        if n < 2:
            return 0
        m = n if n % 2 == 0 else n - 1
        k = m // 2
        return (k * (2 + m)) // 2


# --------------- Example Usage --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.sum_of_evens(10))   # Expected Output: 30
    print(sol.sum_of_evens(15))   # Expected Output: 56