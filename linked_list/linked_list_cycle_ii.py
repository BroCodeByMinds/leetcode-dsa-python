"""
Problem: Linked List Cycle II
Link: https://leetcode.com/problems/linked-list-cycle-ii/
Pattern: Linked List / Floyd’s Tortoise and Hare
Time Complexity: O(n) — Each pointer at most goes through the list once
Space Complexity: O(1) — No extra data structure used

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return None.

Approach:
---------
1. First detect if a cycle exists using two pointers (slow and fast).
   - slow moves 1 step each time
   - fast moves 2 steps
   - If they meet => cycle exists
2. Once they meet inside the cycle, move slow back to head
   - Now move both slow and fast one step at a time
   - They will meet exactly at the start of the cycle
"""

from typing import Optional

# Helper ListNode for testing inside this file
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Phase 1: Detect cycle using slow-fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # cycle detected
                break
        else:
            return None  # no cycle at all

        # Phase 2: Find the start node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # start of cycle node

# ------------------ Example Usage ------------------



if __name__ == "__main__":
    # Create a cycle list: 3 -> 2 -> 0 -> -4 -> back to 2
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle here

    sol = Solution()
    start_cycle = sol.detectCycle(n1)
    print("Cycle starts at node value:", start_cycle.val if start_cycle else None)
    # Expected: 2
