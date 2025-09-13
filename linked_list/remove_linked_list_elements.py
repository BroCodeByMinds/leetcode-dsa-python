"""
Problem: Remove Linked List Elements
Link: https://leetcode.com/problems/remove-linked-list-elements/
Pattern: Linked List / Two Pointers
Time Complexity: O(n) — traverse once
Space Complexity: O(1) — constant extra space

Given the head of a linked list and an integer val, remove all nodes of the list that have Node.val == val, and return the new head.

Approach:
---------
Use a dummy node before head to simplify removal of nodes (including the head).
Maintain two pointers: prev and curr.
If curr.val == val → we skip that node by doing prev.next = curr.next.
Else → we keep the node and move prev forward.
Always move curr forward in each iteration.
Finally return dummy.next as the new head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                # Skip this node
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next


# ----------------- Example Usage -----------------

def build_list(values):
    head = ListNode(values[0]) if values else None
    curr = head
    for val in values[1:]:
        node = ListNode(val)
        curr.next = node
        curr = node
    return head

def print_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)

if __name__ == "__main__":
    head = build_list([1,2,6,3,4,5,6])
    sol = Solution()
    new_head = sol.removeElements(head, 6)
    print_list(new_head)  # Output: [1, 2, 3, 4, 5]
