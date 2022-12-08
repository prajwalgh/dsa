#
# @lc app=leetcode id=872 lang=python
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, ans):
            if not root:
                return
            if not root.left and not root.right:
                ans.append(root.val)
            dfs(root.left, ans)
            dfs(root.right, ans)
        leaf1 = []
        leaf2 = []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        if leaf1 == leaf2:
            return 1
        else:
            return 0
# @lc code=end
