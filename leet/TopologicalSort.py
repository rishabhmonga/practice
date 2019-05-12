class Graph:
    def __init__(self, x):
        self.val = x
        self.children = None


class TopSort:
    visited = set()

    def sort(self, graph):
        sorted_stack = list()
        for node in graph:
            if node not in self.visited:
                self.visited.add(node)

                if node.children is not None:
                    for child in node.children:
                        sorted_stack.append(child.val)
        return sorted_stack


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

    all_nodes = {root, child2, child3, child4, child5, child6, child7}
    ts = TopSort()
    print(ts.sort(all_nodes))
    # dfs.dfs_iterative(root)
