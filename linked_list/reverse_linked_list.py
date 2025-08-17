"""
Problem: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Pattern: Linked List
Time Complexity:
    Iterative: O(n)
    Recursive: O(n)
Space Complexity:
    Iterative: O(1)
    Recursive: O(n) - recursion stack

Given the head of a singly linked list, reverse the list and return the new head.

Approach:
---------
Two ways to solve:
1. Iterative:
   - Maintain three pointers: prev, current, next_node.
   - Reverse pointers one by one until the end.
2. Recursive (follow-up):
   - Recursively reverse the rest of the list, then fix the current node.

Return the new head after reversal.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution(object):

    # ----- Iterative method -----
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # store next node
            curr.next = prev       # reverse the pointer
            prev = curr
            curr = next_node       # move to next
        
        return prev

    # ----- Recursive method -----
    def reverseListRecursive(self, head):
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)
        
        # Fix the current node's pointer
        head.next.next = head
        head.next = None
        
        return new_head


# ------------------ Example Usage ------------------



def build_list(values):
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        node = ListNode(v)
        cur.next = node
        cur = node
    return head

def print_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)

if __name__ == "__main__":
    head = build_list([1,2,3,4,5])
    sol = Solution()
    # Iterative reverse
    new_head = sol.reverseList(head)
    print_list(new_head)  # [5, 4, 3, 2, 1]
    
    # Recursive reverse example
    head2 = build_list([1,2,3])
    new_head2 = sol.reverseListRecursive(head2)
    print_list(new_head2)  # [3, 2, 1]
