class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
public List<String> binaryTreePaths(TreeNode root) {
    List<String> answer = new ArrayList<String>();
    if (root != null) searchBT(root, "", answer);
    return answer;
}
private void searchBT(TreeNode root, String path, List<String> answer) {
    if (root.left == null && root.right == null) answer.add(path + root.val);
    if (root.left != null) searchBT(root.left, path + root.val + "->", answer);
    if (root.right != null) searchBT(root.right, path + root.val + "->", answer);
}
"""


def searchBinaryTree(root, path, result):
    if root.left is None and root.right is None:
        result.append(path + str(root.val))
    if root.left is not None:
        searchBinaryTree(root.left, path + str(root.val) + '->', result)
    if root.right is not None:
        searchBinaryTree(root.right, path + str(root.val) + '->', result)


def binaryTreePath(root):
    result = []
    if root is not None:
        searchBinaryTree(root, "", result)
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(binaryTreePath(root))
