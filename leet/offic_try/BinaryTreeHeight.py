class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def getHeight(root):
    if root is None:
        return 0

    lheight = getHeight(root.left)
    rheight = getHeight(root.right)

    return 1 + max(lheight, rheight)


if __name__ == '__main__':
    root = BinaryTree(4)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(1)
    root.left.right = BinaryTree(3)

    root.right = BinaryTree(6)
    root.right.left = BinaryTree(5)
    root.right.right = BinaryTree(7)
    root.right.right.right = BinaryTree(8)
    root.right.right.right.right = BinaryTree(9)
    root.right.right.right.right.right = BinaryTree(10)

    print(getHeight(root))
