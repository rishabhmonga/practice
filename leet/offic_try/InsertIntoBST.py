# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, path=""):
        self.val = x
        self.left = None
        self.right = None
        self.path = path


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        pass


def insertNode(root: TreeNode, node: TreeNode):
    if root.val > node.val:
        if root.left is None:
            root.left = node
            return
        insertNode(root.left, node)
    if root.val < node.val:
        if root.right is None:
            root.right = node
            return
        insertNode(root.right, node)


def printTree(root, path, end='\n'):
    if root is None:
        return
    print(root.val, path, end=end)
    printTree(root.left, root.path + ' L', '\n')
    printTree(root.right, root.path + ' R', '\n')


def findVal(root, val, path=''):
    if root is None:
        return ""
    if root.val == val:
        return path + " " + root.path
    if root.val > val:
        return findVal(root.left, val, path + " " + root.path)
    elif root.val < val:
        return findVal(root.right, val, path + " " + root.path)


if __name__ == '__main__':
    root = TreeNode(4, 'root')
    root.left = TreeNode(2, 'L')
    root.left.left = TreeNode(1, 'L')
    root.left.right = TreeNode(3, 'R')
    root.right = TreeNode(5, 'R')
    root.right.right = TreeNode(8, 'R')

    # printTree(root, root.path)
    # print(findVal(root, 3))
    insertNode(root, TreeNode(10))
    print(findVal(root, 10))
