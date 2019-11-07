class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def getMidNode(nodes):
    return int((len(nodes) - 1) / 2)


def buildBST(nodes):
    if nodes is None or len(nodes) < 1:
        return None

    mid = getMidNode(nodes)
    root = BSTNode(nodes[mid])
    root.left = buildBST(nodes[:mid])
    root.right = buildBST(nodes[mid + 1:])
    return root


if __name__ == '__main__':
    nodes = sorted([10, 5, 15, 3, 7, 18])
    print(nodes)
    root = buildBST(nodes)
    print(root.val)
