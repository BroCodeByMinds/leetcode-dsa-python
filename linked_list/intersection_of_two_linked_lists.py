"""
Problem: Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Pattern: Linked List / Two Pointers
Time Complexity: O(m + n) — Traverse both lists once (at most twice)
Space Complexity: O(1) — Constant space

Given the heads of two singly linked lists, return the node at which they intersect.
Return None if the two linked lists have no intersection.

Approach:
---------
Use two pointers (nodeA and nodeB). Traverse both lists:
- Move both pointers one step at a time.
- When a pointer reaches the end of one list, redirect it to the head of the other list.
- If the lists intersect, the pointers will meet at the intersection node after at most m + n steps.
- If they don’t intersect, both pointers will eventually become None at the same time.

This aligns both pointers regardless of list lengths.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        nodeA, nodeB = headA, headB
        
        # Traverse both lists; switch heads when you reach the end.
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        
        return nodeA  # Intersection node or None


# --------------- Example Usage --------------------
if __name__ == "__main__":
    # Construct example intersecting lists: A: 4 -> 1 -> 8 -> 4 -> 5
    #                                      B:       5 -> 6 -> 1 \
    # both intersect at node with value = 8
    # Nodes after 8 are shared references between both lists.

    # Common part
    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)
    c1.next = c2
    c2.next = c3

    # List A
    a1 = ListNode(4)
    a2 = ListNode(1)
    a1.next = a2
    a2.next = c1

    # List B
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    b1.next = b2
    b2.next = b3
    b3.next = c1

    sol = Solution()
    intersection = sol.getIntersectionNode(a1, b1)
    if intersection:
        print("Intersection at value:", intersection.val)
    else:
        print("No intersection")

    # Expected Output: Intersection at value: 8
