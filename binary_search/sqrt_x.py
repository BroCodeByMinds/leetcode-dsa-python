# Problem: https://leetcode.com/problems/sqrtx/
# Tags: Binary Search
# Approach: Use binary search to find the integer square root
# Time Complexity: O(log x)
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        # For x = 0 or 1, the square root is the number itself
        if x < 2:
            return x

        # Initialize binary search bounds
        # We search in the range [1, x//2] because sqrt(x) is always <= x//2 for x >= 2
        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2       # Midpoint of current search space
            square = mid * mid              # Compute mid squared

            if square == x:
                return mid                  # Perfect square found
            elif square < x:
                left = mid + 1              # Move right since mid^2 is too small
            else:
                right = mid - 1             # Move left since mid^2 is too large

        # Loop ends when left > right
        # At this point, right is the largest value such that right^2 <= x
        return right


# Example Usage
if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(4))  # Output: 2, since sqrt(4) = 2
    print(s.mySqrt(8))  # Output: 2, since sqrt(8) ≈ 2.828, and we round down to 2
