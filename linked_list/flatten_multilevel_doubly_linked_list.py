"""
Problem: Flatten a Multilevel Doubly Linked List
Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
Pattern: Linked List / DFS

Time Complexity: O(n) — each node is visited once
Space Complexity: O(n) — stack stores nodes in worst case
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Dummy node to simplify connections
        dummy = Node(0, None, head, None)
        prev = dummy
        stack = [head]

        while stack:
            curr = stack.pop()

            # Connect prev and curr
            prev.next = curr
            curr.prev = prev

            # Push next to stack (process later)
            if curr.next:
                stack.append(curr.next)

            # Push child to stack (process first)
            if curr.child:
                stack.append(curr.child)
                curr.child = None  # IMPORTANT: reset child pointer

            prev = curr

        # Detach dummy node
        real_head = dummy.next
        real_head.prev = None
        return real_head


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    # Example: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    #                |
    #                7 -> 8 -> 9 -> 10
    #                     |
    #                     11 -> 12
    n1 = Node(1); n2 = Node(2); n3 = Node(3); n4 = Node(4)
    n5 = Node(5); n6 = Node(6); n7 = Node(7); n8 = Node(8)
    n9 = Node(9); n10 = Node(10); n11 = Node(11); n12 = Node(12)

    n1.next = n2; n2.prev = n1
    n2.next = n3; n3.prev = n2
    n3.next = n4; n4.prev = n3
    n4.next = n5; n5.prev = n4
    n5.next = n6; n6.prev = n5

    n3.child = n7
    n7.next = n8; n8.prev = n7
    n8.next = n9; n9.prev = n8
    n9.next = n10; n10.prev = n9
    n8.child = n11
    n11.next = n12; n12.prev = n11

    sol = Solution()
    flat = sol.flatten(n1)

    # Print flattened list
    res = []
    while flat:
        res.append(flat.val)
        flat = flat.next
    print(res)  # Expected: [1,2,3,7,8,11,12,9,10,4,5,6]
