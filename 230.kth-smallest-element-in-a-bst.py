#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # method 3 no use of extra space
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

        # #method 2 do inorder it will give value in sorted order
        # ans=[]
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     ans.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return ans[k-1]
        # method 1 time o(n)+O(nlogn) for sorting and space O(n)
        # ans=[]
        # def dfs(root):
        #     if not root:
        #         return
        #     ans.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # print(ans)
        # ans.sort()
        # print(ans)
        # return ans[k-1]
# @lc code=end
