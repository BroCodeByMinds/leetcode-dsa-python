"""
Problem: Remove Nth Node From End of List
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Pattern: Linked List / Two Pointers
Time Complexity: O(n) — one pass to move fast pointer and finish traversal
Space Complexity: O(1) — constant extra space

Given the head of a linked list, remove the nth node from the end and return the head.

Approach:
---------
We use two pointers (fast and slow). Move fast pointer n steps ahead. 
Then move both pointers (fast and slow) together until fast reaches the end of the list.
Now slow is positioned just before the node that needs to be removed.
To simplify deletion when the head itself needs to be removed, we create a dummy node
that points to head. Finally return dummy.next as new head.
"""
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both fast and slow until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next


# ------------------ Example Usage ------------------

def build_list(values):
    head = ListNode(values[0])
    cur = head
    for val in values[1:]:
        node = ListNode(val)
        cur.next = node
        cur = node
    return head

def print_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)

if __name__ == "__main__":
    head = build_list([1,2,3,4,5])
    n = 2
    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)
    print_list(new_head)  # Output: [1, 2, 3, 5]

    single_head = build_list([1])
    print_list(sol.removeNthFromEnd(single_head, 1))  # Output: []
