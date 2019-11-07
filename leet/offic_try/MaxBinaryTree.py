import queue
import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if nums is None or len(nums) == 0:
        return None
    curr, i = tree_partition(nums)
    root = TreeNode(curr)
    root.left = constructMaximumBinaryTree(nums[:i])
    root.right = constructMaximumBinaryTree(nums[i + 1:])
    return root


def tree_partition(nums):
    max = -sys.maxsize
    max_idx = 0
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
            max_idx = i
    return max, max_idx


def constructMaximumBinaryTree2(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    stk = []
    for i in nums:
        cur = TreeNode(i)
        while stk and stk[-1].val < i:
            cur.left = stk.pop()
        if stk:
            stk[-1].right = cur
        stk.append(cur)
    return stk[0]


def printTree(root):
    orderQueue = queue.Queue()
    auxQueue = queue.Queue()
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


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    printTree(constructMaximumBinaryTree(nums))
