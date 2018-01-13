class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_height(node):
    if node is None:
        return 0
    left_height = get_height(node.left)
    right_height = get_height(node.right)

    if left_height == -1 or right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def is_balanced(node):
    if not node:
        return True
    return get_height(node) != -1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(is_balanced(root))
    print(get_height(root))
