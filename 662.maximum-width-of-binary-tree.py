#
# @lc app=leetcode id=662 lang=python
#
# [662] Maximum Width of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def levl(root):
            q = [(root, 0)]
            ans = 0
            while len(q) != 0:
                len1 = len(q)
                start = q[0][1]
                end = q[-1][1]
                ans = max(ans, end - start + 1)
                for i in range(len1):
                    node, index = q.pop(0)
                    if node.left:
                        q.append((node.left, index * 2 + 1))
                    if node.right:
                        q.append((node.right, index * 2 + 2))
            return ans

        return levl(root)


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def level(root):
            if not root:
                return 0

            queue = [(root, 0)]
            ans = 0

            while queue:
                size = len(queue)
                start = queue[0][1]
                end = queue[-1][1]
                ans = max(ans, end - start + 1)

                for i in range(size):
                    node, index = queue.pop(0)
                    if node.left:
                        queue.append((node.left, index * 2 + 1))
                    if node.right:
                        queue.append((node.right, index * 2 + 2))

            return ans

        return level(root)


# @lc code=end
