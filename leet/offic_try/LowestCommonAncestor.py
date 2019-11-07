class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def getLCA(root, node1, node2):
    if root is None:
        return
    if root.val == node1.val or root.val == node2.val:
        return root

    leftLCA = getLCA(root.left, node1, node2)
    rightLCA = getLCA(root.right, node1, node2)

    if leftLCA and rightLCA:
        return root

    return leftLCA if leftLCA is not None else rightLCA


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

    print(getLCA(root, root.right.right.right.right, root.left.left).val)
