# Problem: https://leetcode.com/problems/first-bad-version/
# Tags: Binary Search
# Approach: Use Binary Search Template II to find the first version that returns True from isBadVersion
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Mock API (for local testing only)
# In LeetCode this is predefined
bad = 4  # Example: You can change this to simulate different scenarios

def isBadVersion(version: int) -> bool:
    return version >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Versions range from 1 to n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # mid might be the first bad version
            else:
                left = mid + 1  # first bad version must be to the right

        # Loop ends when left == right
        return left


# Example Usage
if __name__ == "__main__":
    s = Solution()
    print(s.firstBadVersion(5))  # Output: 4
