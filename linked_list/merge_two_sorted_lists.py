# Problem:
# Merge Two Sorted Lists – https://leetcode.com/problems/merge-two-sorted-lists/
# Given two sorted linked lists, merge them into one sorted linked list and return it.

# Pattern:
# Linked List, Two Pointers

# Time Complexity:
# O(m + n), where m and n are the lengths of the two lists.
# Reason: Each node from both lists is visited exactly once.

# Space Complexity:
# O(1) (excluding output list).
# Reason: No extra data structures are used, we just rearrange pointers.

# Approach:
# 1. Use a dummy node to simplify handling of the head pointer.
# 2. Maintain a `tail` pointer to build the merged list.
# 3. Traverse both lists while both have elements:
#    - Attach the smaller node to `tail.next`.
#    - Move the pointer forward in the chosen list.
# 4. Once one list is exhausted, append the remaining nodes of the other list.
# 5. Return `dummy.next` as the head of the merged list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)   # Dummy node to simplify list merging
        tail = dummy
        left = list1
        right = list2

        # Merge nodes while both lists have elements
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        # Append the remaining part of the non-empty list
        if left:
            tail.next = left
        else:
            tail.next = right

        return dummy.next


# Example Usage / Test Case
def build_linked_list(values):
    """Helper to build linked list from Python list"""
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    """Helper to print linked list as Python list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Input lists
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

# Merge
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

# Output
print(print_linked_list(merged_head))  # Expected: [1, 1, 2, 3, 4, 4]
