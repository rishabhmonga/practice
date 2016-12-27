# Definition for a binary tree node.
import Lib.queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def maxDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        lDepth = TreeNode.maxDepth(root.left)
        rDepth = TreeNode.maxDepth(root.right)

        return (lDepth + 1) if lDepth > rDepth else (rDepth + 1)

    @staticmethod
    def levelOrder(root):
        orderQueue = Lib.Queue()
        auxQueue = Lib.Queue()
        orderQueue.put(root)

        while not orderQueue.empty():
            current = orderQueue.get()
            print(current.val + "\t")
            if current.left is not None:
                auxQueue.put(current.left)
            if current.right is not None:
                auxQueue.put(current.right)
            if orderQueue.empty():
                while not auxQueue.empty():
                    orderQueue.put(auxQueue.get())
                print("\n")


# [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# print(TreeNode.maxDepth(root))
