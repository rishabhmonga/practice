class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = None


def top_sort(nodes, visited):
    sorted_stack = []
    for node in nodes:
        if node not in visited:
            visited.add(node)

            if node.neighbors is not None:
                for neighbor in node.neighbors:
                    sorted_stack.append(neighbor)
    return sorted_stack


if __name__ == '__main__':
    child2 = GraphNode(2)
    child3 = GraphNode(3)
    child4 = GraphNode(4)

    child5 = GraphNode(5)
    child6 = GraphNode(6)
    child7 = GraphNode(7)

    root = GraphNode(1)
    root.neighbors = [child2, child3, child4]
    child2.neighbors = [child5]
    child3.neighbors = [child6]
    child4.neighbors = [child7]

    all_nodes = {root, child2, child3, child4, child5, child6, child7}
    result = top_sort(all_nodes, set())
    for ans in result:
        print(ans.val)
    # dfs.dfs_iterative(root)
