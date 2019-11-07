from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]
"""


class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != '-':
                val, i = val + S[i], i + 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]



"""
def recoverFromPreorder(self, S):
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == '-':
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != '-':
                val, i = val + S[i], i + 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
"""

def displayTree(root, end='\n'):
    if root is None:
        return
    print(root.val, end=end)
    displayTree(root.left, ' ')
    displayTree(root.right, ' ')


if __name__ == '__main__':
    soln = Solution()
    root = soln.recoverFromPreorder('1-2--3--4-5--6--7')
    displayTree(root)


