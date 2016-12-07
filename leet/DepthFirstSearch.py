class Graph:
    def __init__(self, x):
        self.val = x
        self.children = None


class DFS:
    visited = set()

    def dfs_stack(self, root):
        if root not in self.visited:
            self.visited.add(root)
            print(root.val)
        if root.children is not None:
            for child in root.children:
                if child not in self.visited:
                    self.dfs_stack(child)

    def dfs_iterative(self, root):
        dfs_list = [root]
        while len(dfs_list) != 0:
            node = dfs_list.pop()
            # print(node.val)       #post-order
            if node not in self.visited:
                self.visited.add(node)
                print(node.val)
                if node.children is not None:
                    for child in node.children:
                        dfs_list.append(child)


if __name__ == '__main__':
    child2 = Graph(2)
    child3 = Graph(3)
    child4 = Graph(4)

    child5 = Graph(5)
    child6 = Graph(6)
    child7 = Graph(7)

    root = Graph(1)
    root.children = [child2, child3, child4]
    child2.children = [child5]
    child3.children = [child6]
    child4.children = [child7]

    dfs = DFS()
    dfs.dfs_stack(root)
    # dfs.dfs_iterative(root)