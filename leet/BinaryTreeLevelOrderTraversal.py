class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_traverse(root):
    if root is None:
        return None
    from collections import deque
    order_queue = deque()
    order_queue.append(root)
    while len(order_queue) != 0:
        curr = order_queue.popleft()
        print(curr.val, end="")
        if curr.left is not None:
            order_queue.append(curr.left)
        if curr.right is not None:
            order_queue.append(curr.right)


def level_order_two_queues(root):
    if root is None:
        return []
    from collections import deque
    order_queue = deque()
    aux_queue = deque()
    order_queue.append(root)
    tree = list()
    level = list()
    while len(order_queue) != 0:
        current = order_queue.popleft()
        level.append(current)
        if current.left is not None:
            aux_queue.append(current.left)
        if current.right is not None:
            aux_queue.append(current.right)
        if len(order_queue) == 0:
            while len(aux_queue) != 0:
                order_queue.append(aux_queue.popleft())
            tree.append(level)
            level = list()
    return tree


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)

    # [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)


    # level_traverse(root)
    tree = level_order_two_queues(root)
    for lvl in tree:
        # for node in lvl:
        #     print(node.val, end='')
        # print()
        for l in lvl:
            print(l.val, end=' ')
        print()

