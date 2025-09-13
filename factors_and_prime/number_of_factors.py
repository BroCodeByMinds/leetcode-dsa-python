
"""
Problem: Count the Number of Factors
Pattern: Factors & Prime
Time Complexity: O(√n) — We only check divisors up to sqrt(n).
Space Complexity: O(1) — Constant space.

Given a number n, return the count of its factors (divisors).
A factor is a number that divides n exactly without leaving a remainder.

Approach:
---------
- Initialize count = 0
- Iterate i from 1 to √n
    - If i divides n:
        - If i == n // i (perfect square), count += 1
        - Else count += 2 (i and n//i are distinct factors)
- Return count
"""
class Solution:
    def find_factors(self, num: int) -> int:
        count = 0
        if not num:
            return count

        i = 1
        while i * i <= num:
            if num % i == 0:
                if i == num // i:   # perfect square
                    count += 1
                else:
                    count += 2
            i += 1
        return count


# --------------- Example Usage --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.find_factors(36))  # Expected Output: 9
