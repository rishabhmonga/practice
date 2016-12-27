class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root is not None:
        result = []
        binary_search(root, 0, result)
        return True if sum in result else False
    return False


def binary_search(root, path_sum, result):
    if root.left is None and root.right is None:
        result.append(path_sum + root.val)
    if root.left is not None:
        binary_search(root.left, path_sum + root.val, result)
    if root.right is not None:
        binary_search(root.right, path_sum + root.val, result)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    print(hasPathSum(root, 3))
