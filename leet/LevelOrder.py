import Lib.queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def levelOrder(root):
        orderQueue = Lib.queue.Queue()
        auxQueue = Lib.queue.Queue()
        orderQueue.put(root)

        while not orderQueue.empty():
            current = orderQueue.get()
            print(current.val, end=' ')
            if current.left is not None:
                auxQueue.put(current.left)
            if current.right is not None:
                auxQueue.put(current.right)
            if orderQueue.empty():
                while not auxQueue.empty():
                    orderQueue.put(auxQueue.get())
                print()

# [3,9,20,null,null,15,7]
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    TreeNode.levelOrder(root)