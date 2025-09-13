"""
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/
Pattern: Linked List / Math (Carry Propagation)
Time Complexity: O(max(m, n)) — we traverse both lists once, where m and n are their lengths
Space Complexity: O(max(m, n)) — output list stores the sum digits, extra space only for result

Approach:
---------
We simulate digit-by-digit addition as in elementary math:
1. Initialize a dummy node to simplify result list handling.
2. Traverse both lists simultaneously:
   - Extract digit from each list (0 if one list is shorter).
   - Compute sum = val1 + val2 + carry.
   - Carry = sum // 10, digit = sum % 10.
   - Append digit as a new node to result list.
3. Move pointers forward in both lists.
4. After loop, if carry remains, add a final node.
5. Return dummy.next (head of result list).

This approach works even if lists are unequal in length.

Tips & Tricks:
--------------
- Always use a dummy node to simplify linked list construction.
- Be careful to update carry correctly after each addition.
- Remember to handle the case when a carry remains at the end (like adding 999 + 1).
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        left, right = l1, l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Traverse both lists
        while left or right:
            val1 = left.val if left else 0
            val2 = right.val if right else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if left:
                left = left.next
            if right:
                right = right.next

        # Handle leftover carry
        if carry > 0:
            curr.next = ListNode(carry)

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
    l1 = build_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_list([9, 9, 9, 9])
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # Output: [8, 9, 9, 9, 0, 0, 0, 1]