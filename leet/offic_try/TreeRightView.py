from queue import Queue


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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


def printRightView(root):
    orderQueue = Queue()
    auxQueue = Queue()
    orderQueue.put(root)
    while not orderQueue.empty():
        current = orderQueue.get()
        if current.left is not None:
            auxQueue.put(current.left)
        if current.right is not None:
            auxQueue.put(current.right)
        if orderQueue.empty():
            while not auxQueue.empty():
                orderQueue.put(auxQueue.get())
            print(current.val)


def printLevelOrder(root):
    orderQueue = Queue()
    orderQueue.put(root)
    while not orderQueue.empty():
        current = orderQueue.get()
        print(current.val, end=" ")
        if current.left is not None:
            orderQueue.put(current.left)
        if current.right is not None:
            orderQueue.put(current.right)

def printSpiral(root):
    count = 0
    orderQueue = Queue()
    auxStack = list()
    orderQueue.put(root)
    while not orderQueue.empty():
        current = orderQueue.get()
        print(current.val, end=" ")
        if current.left is not None:
            auxStack.append(current.left)
        if current.right is not None:
            auxStack.append(current.right)
        if orderQueue.empty():
            while len(auxStack) != 0:
                orderQueue.put(auxStack.pop())
            print()


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    root.right.left.left = BinaryTree(8)

    # printLevelOrder(root)
    #
    # print('\n')
    #
    printLevelOrder2Queue(root)

    print('\n')

    # printRightView(root)

    printSpiral(root)
