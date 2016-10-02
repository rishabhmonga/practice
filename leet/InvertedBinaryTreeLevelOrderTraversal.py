class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        from collections import deque
        orderedQueue = deque()
        auxQueue = deque()
        orderedQueue.append(root)
        inverseStack = list()
        levelList = list()
        while len(orderedQueue) is not 0:
            current = orderedQueue.popleft()
            levelList.append(current.val)
            if current.left is not None:
                auxQueue.append(current.left)
            if current.right is not None:
                auxQueue.append(current.right)
            if len(orderedQueue) is 0:
                while len(auxQueue) is not 0:
                    orderedQueue.append(auxQueue.popleft())
                inverseStack.append(levelList)
                levelList = list()
        result = list()
        while len(inverseStack) is not 0:
            result.append(inverseStack.pop())
        return result


soln = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(soln.levelOrderBottom(root))
