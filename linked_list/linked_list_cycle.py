"""
Problem: Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/
Pattern: Linked List / Floyd’s Tortoise
Time Complexity: O(n) — Each pointer moves at most n steps
Space Complexity: O(1) — Constant extra space

Given the head of a linked list, determine if the linked list has a cycle.

Approach:
---------
We use Floyd’s Cycle Detection Algorithm:
1. Use two pointers — slow and fast.
2. Slow moves 1 step, fast moves 2 steps.
3. If there is a cycle, slow and fast will eventually meet.
4. If fast reaches None (end of list), then there is no cycle.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

# Helper ListNode definition for demonstration
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # Traverse the list with two pointers
        while fast and fast.next:
            slow = slow.next         # Move 1 step
            fast = fast.next.next    # Move 2 steps

            if slow == fast:         # If pointers meet, cycle exists
                return True

        return False  # No cycle detected


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    # Example 1: head = [3,2,0,-4], pos = 1
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # Creates cycle

    sol = Solution()
    print(sol.hasCycle(n1))  # Expected Output: True

    # Example 2: head = [1], pos = -1 (no cycle)
    n1 = ListNode(1)
    print(sol.hasCycle(n1))  # Expected Output: False
