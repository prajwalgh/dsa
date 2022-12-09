#
# @lc app=leetcode id=1026 lang=python
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, curmin, curmax):
            if root == None:
                return abs(curmax-curmin)
            curmax = max(root.val, curmax)
            curmin = min(root.val, curmin)
            l = helper(root.left, curmin, curmax)
            r = helper(root.right, curmin, curmax)
            return max(l, r)
        if not root:
            return 0
        return helper(root, root.val, root.val)
# @lc code=end
