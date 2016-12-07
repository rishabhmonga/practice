class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(root, level, res):
    if root:
        if len(res) < level + 1: res.append([])
        if level % 2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)
        preorder(root.left, level + 1, res)
        preorder(root.right, level + 1, res)


def zigzagLevelOrder(root):
    res = []
    preorder(root, 0, res)
    return res


if __name__ == '__main__':
    # [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(zigzagLevelOrder(root))
