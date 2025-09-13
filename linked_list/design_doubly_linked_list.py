"""
Problem: Design Linked List
Link: https://leetcode.com/problems/design-linked-list/
Pattern: Linked List / Implementation
Time Complexity:
    - get(index): O(n) in worst case (traversing up to n nodes)
    - addAtHead, addAtTail: O(1) constant-time updates
    - addAtIndex, deleteAtIndex: O(n) in worst case (traversing to index)
Space Complexity: O(n) — storing n nodes in the linked list

Approach:
---------
We implement a doubly linked list with both head and tail pointers
for efficient insertions at both ends. Each node contains value,
prev, and next references.

Operations:
- get(index): Traverse from head until index is reached.
- addAtHead(val): Create a new node, update head pointers.
- addAtTail(val): Create a new node, update tail pointers.
- addAtIndex(index, val): Traverse to position, insert node by rewiring prev and next.
- deleteAtIndex(index): Traverse to index, unlink node and adjust neighbors.

Maintaining `size` helps in boundary validation quickly.
"""

class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        new_node = ListNode(val)
        if not self.head:  # empty list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = ListNode(val)
        if not self.tail:  # empty list
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        new_node = ListNode(val)
        prev_node = curr.prev

        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            if self.head == self.tail:  # only one node
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
            return
        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        prev_node = curr.prev
        next_node = curr.next

        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1


# ----------------- Example Usage -----------------
if __name__ == "__main__":
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
    print(myLinkedList.get(1))     # Output: 2
    myLinkedList.deleteAtIndex(1)  # linked list becomes 1->3
    print(myLinkedList.get(1))     # Output: 3
