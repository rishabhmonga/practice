import Lib.queue


class Node:
    prev = None
    head = None

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_list(node):
    while node:
        print(node.val, end=' ')
        node = node.right


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




def tree_to_dll(root):
    if root is None:
        return None
    tree_to_dll(root.left)

    if Node.prev is None:
        Node.head = root
    else:
        root.left = Node.prev
        Node.prev.right = root

    Node.prev = root

    tree_to_dll(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    levelOrder(root)
    tree_to_dll(root)
    print()
    print_list(Node.head)
