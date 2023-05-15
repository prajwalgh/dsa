#  1721. Swapping Nodes in a Linked List
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        for i in range(k - 1):
            start = start.next
        # print(start.val)
        end = head
        fast = start
        i = 0
        while fast.next:
            end = end.next
            fast = fast.next
        # print(end.val,fast.val)
        # # print(i,i-k)
        # for i in range((i-k)):
        #     end=end.next
        # print(end.val)
        temp = end.val
        end.val = start.val
        start.val = temp
        return head


# following code is faster than above dont know how but
# above code have less loop but takes more time this may be
# because of computation inside for loops
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        for i in range(k - 1):
            start = start.next
        # print(start.val)
        end = slow = head
        i = 0
        while slow:
            i += 1
            slow = slow.next
        # print(i,i-k)
        for i in range((i - k)):
            end = end.next
        # print(end.val)
        temp = end.val
        end.val = start.val
        start.val = temp
        return head
