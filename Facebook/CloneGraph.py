class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = list()


class Graph:

    @staticmethod
    def clone_graph(source):
        q = []
        map = {source:source.val}

        while len(q) is not 0:
            top = q[-1]
            clonedNode = map[top]

            if top.neighbors is not None:
                nodes = top.neighbors
                for node in nodes:
                    curr_node = map[node]
                    if curr_node is None:
                        q.append(node)
                        curr_node = GraphNode(node.val)
                        map[node] = curr_node
                    clonedNode.neighbors.append(curr_node)
        return map[source]

    @staticmethod
    def print_graph(source):
        dfs_list = [source]
        visited = set()
        while len(dfs_list) != 0:
            node = dfs_list.popleft()
            if node not in visited:
                visited.add(node)
                print node.val
                if node.neighbors is not None:
                    for neighbor in neighbors:
                        dfs_list.append(neighbor)

if __name__ == '__main__':
    
