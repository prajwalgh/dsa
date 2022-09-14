# 876. Middle of the Linked List
# given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# Example 1:


# Input: head = [1, 2, 3, 4, 5]
# Output: [3, 4, 5]
# Explanation: The middle node of the list is node 3.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# 142. Linked List Cycle II
# Medium

# 8845

# 613

# Add to List

# Share
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to(0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        d = defaultdict(int)
        slow = head
        while slow:
            d[slow] += 1
            if d[slow] >= 2:
                return slow
            slow = slow.next
