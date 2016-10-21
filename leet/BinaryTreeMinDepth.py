class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_height_for_each_path(root, path_ht, ht_list):
    if root.left is None and root.right is None:
        ht_list.append(path_ht + 1)
    if root.left is not None:
        get_height_for_each_path(root.left, path_ht + 1, ht_list)
    if root.right is not None:
        get_height_for_each_path(root.right, path_ht + 1, ht_list)


def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    ht_list = []
    get_height_for_each_path(root, 0, ht_list)
    return min(ht_list)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(minDepth(root))
