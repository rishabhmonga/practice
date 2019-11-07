from queue import Queue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def displayTree(root):
    if not root:
        return

    displayTree(root.left)
    print(root.val, end=' ')
    displayTree(root.right)


def printLevelOrder2Queue(root):
    orderQueue = Queue()
    auxQueue = Queue()
    orderQueue.put(root)
    while not orderQueue.empty():
        current = orderQueue.get()
        print(current.val, end=" ")
        if current.left is not None:
            auxQueue.put(current.left)
        if current.right is not None:
            auxQueue.put(current.right)
        if orderQueue.empty():
            while not auxQueue.empty():
                orderQueue.put(auxQueue.get())
            print()


def flipTree(root):
    orderQueue = []
    auxQueue = []
    orderQueue.append(root)
    while len(orderQueue) != 0:
        current = orderQueue.pop()
        print(current.val, end=" ")
        if current.right is not None:
            auxQueue.append(current.right)
        if current.left is not None:
            auxQueue.append(current.left)
        if len(orderQueue) == 0:
            while len(auxQueue) != 0:
                orderQueue.append(auxQueue.pop())
            print()


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    printLevelOrder2Queue(root)

    print()

    flipTree(root)
