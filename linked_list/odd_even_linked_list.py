"""
Problem: Odd Even Linked List
Link: https://leetcode.com/problems/odd-even-linked-list/
Pattern: Linked List / Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)

Group all nodes at odd indices together followed by the nodes at even indices.
(Indices are 1-based: first node is odd, second is even.)

Approach:
---------
Use two pointers:
- odd points to the current odd-indexed node
- even points to the current even-indexed node
We also store the head of the even list as even_head.
Iterate and rewire next pointers such that:
  odd.next = even.next
  even.next = odd.next
At the end connect the tail of odd list to even_head.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # save the start of even list for later

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


# ------------------ Example Usage ------------------

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        node = ListNode(v)
        cur.next = node
        cur = node
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == "__main__":
    # Example 1
    head = build_list([1,2,3,4,5])
    sol = Solution()
    new_head = sol.oddEvenList(head)
    print_list(new_head)  # Output: [1, 3, 5, 2, 4]

    # Example 2
    head2 = build_list([2,1,3,5,6,4,7])
    new_head2 = sol.oddEvenList(head2)
    print_list(new_head2)  # Output: [2, 3, 6, 7, 1, 5, 4]
