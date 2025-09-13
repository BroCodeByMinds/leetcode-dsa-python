"""
Problem: Check if a Number is Prime
Pattern: Factors & Prime
Time Complexity: O(√n) — We only check divisors up to sqrt(n).
Space Complexity: O(1) — Constant space.

Given an integer n, return True if it is a prime number, otherwise False.

Approach:
---------
- Prime numbers are greater than 1 and divisible only by 1 and themselves.
- Handle edge cases: n <= 1 is not prime.
- Iterate from 2 to √n:
    - If any i divides n, return False.
- Otherwise, return True.
"""
class Solution:
    def is_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True


# --------------- Example Usage --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.is_prime(7))   # Expected Output: True
    print(sol.is_prime(10))  # Expected Output: False