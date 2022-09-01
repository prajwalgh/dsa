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


    def is_balance(self,root):
        def dfs1(root):
            if root is None: return [True, 0]

            left, right = dfs1(root.left), dfs1(root.right)
            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return (balance, 1 + max(left[1], right[1]))

        return dfs1(root)[0]
    def invert(self,node):

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

#top view of tree
def topview(root):
     q=[(root,0)]
     freq={}
     while len(q)!=0:
            for i in q:
                if i[1] not in freq:
                    i[0]:i[1]
                else:
                    pass
            temp=q.pop()
            dis=temp[1]
            q.append((temp[0].left,dis-1))
            q.append((temp[0].right,dis+1))

