# Problem Link: https://leetcode.com/problems/design-linked-list/
# Pattern: Linked List
# Time Complexity: O(1) for addAtHead, O(1) for get (when index=0), 
#                  O(n) for get, addAtTail, addAtIndex (worst case)
# Space Complexity: O(n) — to store the linked list elements

class Node:
    """Node structure for singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val    # Value of the node
        self.next = next  # Pointer to the next node


class MyLinkedList:
    """Implementation of a singly linked list with basic operations."""

    def __init__(self):
        self.head = None  # Pointer to the first node in the list
        self.size = 0     # Number of elements in the list

    def get(self, index: int) -> int:
        """
        Retrieve the value at the given index.
        Returns -1 if index is invalid.
        """
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for _ in range(index):  # Traverse to the desired node
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Insert a new node at the beginning of the list.
        """
        new_node = Node(val, self.head)  # New node points to current head
        self.head = new_node             # Update head to new node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a new node at the end of the list.
        """
        if not self.head:
            self.addAtHead(val)  # If list is empty, add at head
        else:
            new_node = Node(val)
            cur = self.head
            while cur.next:      # Traverse to last node
                cur = cur.next
            cur.next = new_node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Insert a new node before the given index.
        If index == size, append at tail.
        If index < 0 or index > size, do nothing.
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        
        cur = self.head
        for _ in range(index - 1):  # Traverse to node before insertion point
            cur = cur.next
        new_node = Node(val, cur.next)
        cur.next = new_node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the node at the given index.
        If index is invalid, do nothing.
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next  # Remove head
        else:
            cur = self.head
            for _ in range(index - 1):  # Traverse to node before target
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1

if __name__ == "__main__":
    my_list = MyLinkedList()
    my_list.addAtHead(1)
    my_list.addAtTail(3)
    my_list.addAtIndex(1, 2)    # List becomes 1->2->3
    print(my_list.get(1))       # Output: 2
    my_list.deleteAtIndex(1)    # Now list is 1->3
    print(my_list.get(1))       # Output: 3


"""
Always keep track of head (start node) and size (optional but useful for validation).

Be careful when modifying pointers — wrong pointer assignments can break the list.

Common pitfalls:

Forgetting to handle empty list cases.

Forgetting to update size after operations.

Not handling index out of range cases.

Traversal is O(n) — optimize by storing tail pointer if many tail insertions are needed.

For index operations, always check boundaries before proceeding.
"""