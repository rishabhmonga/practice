class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 is None:
        return t2
    if t2 is not None:
        t1.val += t2.val
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t1.right, t2.right)
    return t1




def showTree(t1):
    from queue import Queue
    order_q = Queue()
    aux_q = Queue()
    order_q.put(t1)
    while not order_q.empty():
        curr_node = order_q.get()
        print(curr_node.val, end=' ')
        if curr_node.left is not None:
            aux_q.put(curr_node.left)
        if curr_node.right is not None:
            aux_q.put(curr_node.right)
        if order_q.empty():
            while not aux_q.empty():
                order_q.put(aux_q.get())
            print()


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    showTree(t1)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    print()

    showTree(t2)
    root = mergeTrees(t1, t2)

    print()

    showTree(root)

