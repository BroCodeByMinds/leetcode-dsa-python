"""
Problem: Print All Prime Numbers ≤ n
Pattern: Factors & Prime
Time Complexity: O(n√n) — Check primality for each number up to n.
Space Complexity: O(1) — Only storing primes list.

Given an integer n, return all prime numbers less than or equal to n.

Approach:
---------
- Define a helper function is_prime(x) that checks divisibility up to √x.
- Iterate from 2 to n.
- Collect all numbers that are prime into a list.
- Return the list.
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

    def all_prime_numbers(self, num: int):
        primes = []
        for i in range(2, num + 1):
            if self.is_prime(i):
                primes.append(i)
        return primes


# --------------- Example Usage --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.all_prime_numbers(100))
    # Expected Output: [2, 3, 5, 7, 11, 13, ..., 97]
