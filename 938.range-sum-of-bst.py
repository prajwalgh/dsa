#
# @lc app=leetcode id=938 lang=python
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
         global ans
          ans = 0

           def dfs(root):
                if not root:
                    return
                if low <= root.val <= high:
                    global ans
                    ans += root.val
                dfs(root.left)
                dfs(root.right)
            dfs(root)
            return ans
# @lc code=end

