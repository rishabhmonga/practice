from collections import deque


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root):
    order_queue = deque()
    order_queue.append(root)
    while order_queue:
        curr = order_queue.popleft()
        print(curr.val, end=' ')
        if curr.left:
            order_queue.append(curr.left)
        if curr.right:
            order_queue.append(curr.right)


def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    return max(lheight, rheight) + 1


def left_leaf(root):
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    level_order(root)
    print()
    print(left_leaf(root))
