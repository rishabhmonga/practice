class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        dfs_stack = [root]
        total = 0
        while len(dfs_stack) != 0:
            curr = dfs_stack.pop()
            if R >= curr.val >= L:
                total += curr.val
            if curr.right:
                dfs_stack.append(curr.right)
            if curr.left:
                dfs_stack.append(curr.left)
            print(curr.val)

        return total


def printTree(root, end='\n'):
    if root is None:
        return
    print(root.val, end=end)
    printTree(root.left, ' ')
    printTree(root.right, ' ')


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)

    # printTree(root)
    # print()
    soln = Solution()
    print(soln.rangeSumBST(root, 1, 2))