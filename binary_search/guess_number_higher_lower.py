# Problem: https://leetcode.com/problems/guess-number-higher-or-lower/
# Tags: Binary Search
# Approach: Use binary search between 1 and n
# Time Complexity: O(log n)
# Space Complexity: O(1)

# NOTE: In a real LeetCode submission, guess() is predefined.
# For local testing, we simulate it below.

# Simulated pick value for testing
pick = 6

def guess(num: int) -> int:
    """
    Mock implementation of the guess API:
    - returns 0 if num is correct
    - returns -1 if num is too high
    - returns 1 if num is too low
    """
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid  # Correct guess
            elif result < 0:
                right = mid - 1  # Guess is too high
            else:
                left = mid + 1   # Guess is too low

        return -1  # Should never happen if pick ∈ [1, n]


# Example Usage
if __name__ == "__main__":
    s = Solution()
    print(s.guessNumber(10))  # Output: 6