# Problem: https://leetcode.com/problems/valid-perfect-square/
# Tags: Binary Search, Math
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Math Note:
# For num >= 4, sqrt(num) ≤ num // 2
# This inequality lets us set the initial binary search right bound to num // 2
# because any perfect square > 1 must have its square root ≤ num // 2.

class Solution(object):
    def isPerfectSquare(self, num):
        """
        Determines if a given positive integer is a perfect square using binary search.
        :type num: int
        :rtype: bool
        """
        if num < 2:  # 0 and 1 are perfect squares
            return True

        left, right = 2, num // 2  # Right bound based on sqrt(num) ≤ num // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False


# Example usage
s = Solution()
print(s.isPerfectSquare(16))  # True
print(s.isPerfectSquare(14))  # False