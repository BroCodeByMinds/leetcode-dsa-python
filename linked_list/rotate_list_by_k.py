# Problem: Rotate List
# Link: https://leetcode.com/problems/rotate-list/
# Pattern: Linked List
# Time Complexity: O(n) — One full traversal to calculate length, another to find new head
# Space Complexity: O(1) — Only pointers are used, no extra data structures

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length and tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make it circular
        tail.next = head

        # Step 3: Normalize k
        k = k % length
        steps_to_new_tail = length - k - 1

        # Step 4: Find new tail
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Step 5: Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    # Input: head = [1,2,3,4,5], k = 2
    # Expected Output: [4,5,1,2,3]
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    sol = Solution()
    rotated = sol.rotateRight(n1, 2)

    # Print rotated list
    curr = rotated
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    # Expected: 4 -> 5 -> 1 -> 2 -> 3
