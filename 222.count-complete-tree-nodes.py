#
# @lc app=leetcode id=222 lang=python
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        global count
        count = 0

        def dfs(root):
            if root:
                global count
                count += 1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return count


# @lc code=end
