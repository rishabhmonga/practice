class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findClosest(root, x):
    dfs_stack = [root]
    closest = 100000
    while len(dfs_stack) != 0:
        curr = dfs_stack.pop()
        if curr.val == x:
            return curr.val
        elif abs(x - curr.val) < abs(x - closest):
            closest = curr.val
        if curr.val > x:
            if curr.left is not None:
                dfs_stack.append(curr.left)
        else:
            if curr.right is not None:
                dfs_stack.append(curr.right)

    return closest


def printTree(root, end='\n'):
    if root is None:
        return
    print(root.val, end=end)
    printTree(root.left, ' ')
    printTree(root.right, '\n')


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(8)

    print(findClosest(root, 1.5))
