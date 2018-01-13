class TreeNode:
    stack = []

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def start(curr):
        while curr is not None:
            TreeNode.stack.append(curr)
            curr = curr.left


def get_successor():
    if len(TreeNode.stack) == 0:
        return None
    curr = TreeNode.stack.pop()
    if curr.right is not None:
        TreeNode.stack.append(curr.right)
        if curr.right.left is not None:
            TreeNode.start(curr.right.left)
    return curr.value


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    TreeNode.start(root)

    print(get_successor())
    print(get_successor())
    print(get_successor())
    print(get_successor())
    print(get_successor())
    print(get_successor())
    print(get_successor())
