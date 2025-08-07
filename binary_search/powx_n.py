# Problem: https://leetcode.com/problems/powx-n/
# Tags: Math, Binary Exponentiation
# Time Complexity: O(log n)
# Space Complexity: O(log n) due to recursion stack

class Solution(object):
    def myPow(self, x, n):
        """
        Calculates x raised to the power n (x^n) using fast exponentiation.
        :type x: float
        :type n: int
        :rtype: float
        """

        def fast_pow(base, exponent):
            # Base case: any number raised to power 0 is 1
            if exponent == 0:
                return 1

            # Recursive call to compute half power
            half = fast_pow(base, exponent // 2)

            # If exponent is even, result is half * half
            if exponent % 2 == 0:
                return half * half
            else:
                # If exponent is odd, multiply extra base once
                return half * half * base

        # If exponent is negative, invert the base and use positive exponent
        if n < 0:
            x = 1 / x
            n = -n

        # Compute power using helper function
        return fast_pow(x, n)

# Instantiate the solution class
sol = Solution()

# Example 1
x1, n1 = 2.00000, 10
print(f"{x1}^{n1} = {sol.myPow(x1, n1)}")  # Expected Output: 1024.00000

# Example 2
x2, n2 = 2.10000, 3
print(f"{x2}^{n2} = {sol.myPow(x2, n2)}")  # Expected Output: 9.26100

# Example 3
x3, n3 = 2.00000, -2
print(f"{x3}^{n3} = {sol.myPow(x3, n3)}")  # Expected Output: 0.25000
