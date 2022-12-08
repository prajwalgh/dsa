#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# my solution
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ans = []
        temp = head
        while head:
            ans.append(head.val)
            head = head.next
        print(ans)
        l = 0
        r = len(ans)-1
        i = 0
        while l <= r:
            if i % 2 == 0:
                temp.val = ans[l]
                temp = temp.next
                l += 1
            else:
                temp.val = ans[r]
                temp = temp.next
                r -= 1
            i += 1
        return temp
# populer solution


# @lc code=end
