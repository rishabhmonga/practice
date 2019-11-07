from collections import deque


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
"""


def printTreeInorder(root):
    if root is None:
        return
    orderStack = []
    curr = root
    done = 0

    while not done:
        if curr is not None:
            orderStack.append(curr)
            curr = curr.left
        elif len(orderStack) != 0:
            curr = orderStack.pop()
            print(curr.val)
            curr = curr.right
        else:
            done = 1


"""
    1) If right subtree of node is not NULL, then succ lies in right subtree. Do following.
        Go to right subtree and return the node with minimum key value in right subtree.
    2) If right sbtree of node is NULL, then start from root and us search like technique. Do following.
        Travel down the tree, if a node’s data is greater than root’s data then go right side, otherwise go to left side.
"""


def getMinKeyInSubTree(root):
    if root is not None:
        if root.left is not None:
            return getMinKeyInSubTree(root.left)
        else:
            return root


def findNode(root, x):
    if root is None:
        return
    if root.val == x:
        return root
    elif root.val > x:
        return findNode(root.left, x)
    else:
        return findNode(root.right, x)


def getInOrderSuccessor(root, x):
    if root is None or x is None:
        return
    if x.right is not None:
        return getMinKeyInSubTree(x.right).val
    succ = None
    while root is not None:
        if x.val < root.val:
            succ = root
            root = root.left
        elif x.val > root.val:
            root = root.right
        else:
            break
    return succ.val if succ is not None else False


def findSuccessor(root, x):
    node = findNode(root, x)
    return getInOrderSuccessor(root, node)


if __name__ == '__main__':
    root = BinaryTree(4)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(1)
    root.left.right = BinaryTree(3)

    root.right = BinaryTree(6)
    root.right.left = BinaryTree(5)
    root.right.right = BinaryTree(7)

    print(findSuccessor(root, 1))
    print(findSuccessor(root, 2))
    print(findSuccessor(root, 3))
    print(findSuccessor(root, 4))
    print(findSuccessor(root, 5))
    print(findSuccessor(root, 6))
    print(findSuccessor(root, 7))

    print(root.val, getMinKeyInSubTree(root).val)
    print(root.left.val, getMinKeyInSubTree(root.left).val)
    print(root.right.val, getMinKeyInSubTree(root.right).val)
    print(root.right.val, getMinKeyInSubTree(root.right).val)
    print(root.left.right.val, getMinKeyInSubTree(root.left.right).val)
    print(root.right.left.val, getMinKeyInSubTree(root.right.left).val)
    print(root.right.right.val, getMinKeyInSubTree(root.right.right).val)
