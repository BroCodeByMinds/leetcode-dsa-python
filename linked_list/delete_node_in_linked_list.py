"""
Problem: Delete Node in a Linked List
Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
Pattern: Linked List / In-place update
Time Complexity: O(1)
Space Complexity: O(1)

You are given only the node to delete (not the head). 
Since you do not have access to the previous node, you cannot bypass the node directly.
Instead:
1. Copy the value of the next node into the current node.
2. Point current node's next to next.next
This effectively removes the next node from the list and replaces current node's value.

Note: Guaranteed that node to delete is not the last node of the list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: None
        """
        node.val = node.next.val           # Copy next node's value
        node.next = node.next.next         # Skip next node

# Example Usage
# build: 4 -> 5 -> 1 -> 9
# delete node with value 5

node4 = ListNode(9)
node3 = ListNode(1, node4)
node2 = ListNode(5, node3)
node1 = ListNode(4, node2)

def print_list_node(node: ListNode):    
    result = []
    curr = node
    while curr:
        result.append(curr.val)
        curr = curr.next
    
    return result
    
print("befire deletion", print_list_node(node1))

Solution().deleteNode(node2)

print("After deletion", print_list_node(node1))


# Now list becomes: 4 -> 1 -> 9