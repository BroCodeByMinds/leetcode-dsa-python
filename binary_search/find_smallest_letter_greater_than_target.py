# Problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Tags: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        Finds the smallest character in letters greater than target.
        Wraps around if no greater character exists.
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # Wrap-around if left points beyond last index
        return letters[left] if left < len(letters) else letters[0]


# Example usage
s = Solution()
print(s.nextGreatestLetter(["c","f","j"], "a"))  # "c"
print(s.nextGreatestLetter(["c","f","j"], "c"))  # "f"
print(s.nextGreatestLetter(["x","x","y","y"], "z"))  # "x"