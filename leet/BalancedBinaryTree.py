class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    lheight = height(node.left)
    rheight = height(node.right)

    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


def is_balanced(node):
    if node is None:
        return True
    if abs(height(node.left) - height(node.right)) < 2:
        return is_balanced(node.left) and is_balanced(node.right)
    else:
        return False


if __name__ == '__main__':
    # [1,2,2,3,null,null,3,4,null,null,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = None
    root.right.left = None
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right.right.right = TreeNode(4)

    # [2,1,4,null,null,3,5,null,null,null,6]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)

    print(height(root))
    print(is_balanced(root))
