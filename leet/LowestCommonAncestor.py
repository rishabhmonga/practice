# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        if leftLCA is not None and rightLCA is not None:
            return root
        return leftLCA if leftLCA is not None else rightLCA


soln = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(soln.lowestCommonAncestor(root, TreeNode(4), TreeNode(6)).val)
print(soln.lowestCommonAncestor(root, TreeNode(4), TreeNode(5)).val)
print(soln.lowestCommonAncestor(root, TreeNode(3), TreeNode(4)).val)
print(soln.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val)
