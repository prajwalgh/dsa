#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = [0]
        ans = []
        while l1.next and l2.next:
            x = l1.val + l2.val + carry[0]
            carry[0] = 0
            if x > 10:
                carry[0] = x // 10
                x = x % 10
            ans.append(x)
            l1 = l1.next
            l2 = l2.next
        while not l1.next and l2.next:
            ans.append(l2.val)
            l2 = l2.next

        while not l2.next and l1.next:
            ans.append(l1.val)
            l1 = l.next
        return ans


# @lc code=end
