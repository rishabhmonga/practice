from leet import LevelOrder


class InvertTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def invertTree(root):
        if root is not None:
            return
        temp = root.right
        root.right = root.left
        root.left = temp

        InvertTree.invertTree(root.left)
        InvertTree.invertTree(root.right)

# [3,9,20,null,null,15,7]
root = LevelOrder.TreeNode(3)
root.left = LevelOrder.TreeNode(9)
root.right = LevelOrder.TreeNode(20)
root.left.left = None
root.left.right = None
root.right.left = LevelOrder.TreeNode(15)
root.right.right = LevelOrder.TreeNode(7)

LevelOrder.TreeNode.levelOrder(root)
InvertTree.invertTree(root)
print("\n")
LevelOrder.TreeNode.levelOrder(root)
