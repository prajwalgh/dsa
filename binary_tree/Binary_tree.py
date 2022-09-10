print(13 * "*", "binary_tree", 13 * "*")


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    def CreateNode(self, data):
        return Node(data)

    def InserNode(self, node, data):
        if node is None:
            return self.CreateNode(data)
        if data < node.data:
            node.left = self.InserNode(node.left, data)
        else:
            node.right = self.InserNode(node.right, data)
        return node

    def Traverse_Inorder(self, root):
        # print("inorder Traverse")
        # node is root node
        if root is not None:
            self.Traverse_Inorder(root.left)
            print(root.data, end=" ")
            self.Traverse_Inorder(root.right)

    def preOrder(self, root):
        # print("per order Traverse")
        if root is not None:
            print(root.data, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        # print("post order Traverse")
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end=" ")

    def height_of_tree(self, root):
        if root is None:
            return -1
        else:
            return max(self.height_of_tree(root.left), self.height_of_tree(root.right)) + 1

    def dfs(self, root):
        if root is None:
            return 0
        else:
            return max(self.dfs(root.left), self.dfs(root.right)) + 1

    def iterative_dfs(self, root):
        stack = [[root, 1]]
        result = 0
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result

    def level_treverse(self, root):
        # level traversal is BFS
        q = [root]
        while len(q) != 0:
            root = q.pop(0)
            print(root.data, end=" ")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)

    def is_balance(self, root):
        def dfs1(root):
            if root is None:
                return [True, 0]

            left, right = dfs1(root.left), dfs1(root.right)
            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return (balance, 1 + max(left[1], right[1]))

        return dfs1(root)[0]

    def invert(self, node):

        if (node == None):
            return
        else:

            temp = node

            # recursive calls
            self.invert(node.left)
            self.invert(node.right)

            # swap the pointers in this node
            temp = node.left
            node.left = node.right
            node.right = temp


tree = Tree()
a = tree.CreateNode(5)
# print(a.data)
# print(a.right)
# print(a.left)
tree.InserNode(a, 2)
tree.InserNode(a, 10)
tree.InserNode(a, 7)
tree.InserNode(a, 15)
tree.InserNode(a, 12)
tree.InserNode(a, 20)
tree.InserNode(a, 30)
tree.InserNode(a, 6)
tree.InserNode(a, 8)

tree.Traverse_Inorder(a)
print("\n")
tree.preOrder(a)
print("\n")
tree.postOrder(a)
print("\n")
print("height of tree is :", tree.height_of_tree(a), "\n")
print("level order traversal is:")
tree.level_treverse(a)
print("\n")
print("iterative dfs is for finding debt of tree ", tree.iterative_dfs(a))
print(" recursive dfs is for finding debt of tree ", tree.dfs(a))
tree.level_treverse(a)

print(tree.is_balance(a))
tree.level_treverse(a)
print("\n")

print("reverse . ..................")
tree.level_treverse(a)
print("\n")

tree.invert(a)
tree.level_treverse(a)
print("\n")


# Python program to construct tree using inorder and
# preorder traversals

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""Recursive function to construct binary of size len from
Inorder traversal in[] and Preorder traversal pre[]. Initial values
of inStrt and inEnd should be 0 and len -1. The function doesn't
do any error checking for cases where inorder and preorder
do not form a tree """


def buildTree(inOrder, preOrder, inStrt, inEnd):
    if (inStrt > inEnd):
        return None

    # Pick current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    # If this node has no children then return
    if inStrt == inEnd:
        return tNode

    # Else find the index of this node in Inorder traversal
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)

    # Using index in Inorder Traversal, construct left
    # and right subtrees
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

    return tNode


# UTILITY FUNCTIONS
# Function to find index of value in arr[start...end]
# The function assumes that value is present in inOrder[]

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def printInorder(node):
    if node is None:
        return

    # first recur on left child
    printInorder(node.left)

    # then print the data of node
    print(node.data, end=' ')

    # now recur on right child
    printInorder(node.right)


# Driver program to test above function
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)
print("\n")

# Let us test the build tree by printing Inorder traversal
print("Inorder traversal of the constructed tree is")
printInorder(root)

# top view of tree


def topview(root):
    q = [(root, 0)]
    freq = {}
    while len(q) != 0:
        for i in q:
            if i[1] not in freq:
                i[0]: i[1]
            else:
                pass
        temp = q.pop()
        dis = temp[1]
        q.append((temp[0].left, dis-1))
        q.append((temp[0].right, dis+1))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = []
        ans = []
        q.append(root)
        while q:
            lenth = len(q)
            temp = []
            for i in range(lenth):
                root = q.pop(0)
                if root:
                    temp.append(root.val)
                    q.append(root.left)
                    q.append(root.right)
            if temp:
                ans.append(sum(temp)/len(temp))
        return ans


# 429. N-ary Tree Level Order Traversal

# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value(See examples).
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        ans = []
        q = []
        q.append(root)
        while q:
            length = len(q)
            temp = []
            for i in range(length):
                root = q.pop(0)
                if root:
                    temp.append(root.val)
                    for x in root.children:
                        q.append(x)
            if temp:
                ans.append(temp)
        return ans


# 589. N-ary Tree Preorder Traversal
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value(See examples)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        ans = []

        def pre(root):
            if not root:
                return ans
            ans.append(root.val)
            for x in root.children:
                pre(x)
        pre(root)
        return ans


# 814. Binary Tree Pruning

# Given the root of a binary tree, return the same tree where every subtree(of the given tree) not containing a 1 has been removed.

# # Definition for a binary tree node.
# A subtree of a node node is node plus every node that is a descendant of node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        if not root:
            return None
        if self.pruneTree(root.left) is None:
            root.left = None
        if self.pruneTree(root.right) is None:
            root.right = None
        if root.val != 1 and root.left is None and root.right is None:
            root = None
        return root


# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]

class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        curr = dummy = None
        while head:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
        return curr
