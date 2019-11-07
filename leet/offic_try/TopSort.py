from functools import cmp_to_key
from queue import Queue


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    # function to add an edge to graph
    def addEdge(self, v):
        self.neighbors.append(v)


def top_sort(vertices, visited):
    """
    :param vertices: list
    :param visited: set
    :return: void
    """
    if vertices is None or len(vertices) == 0:
        return

    vertices.sort(key=lambda s: len(s.neighbors), reverse=True)

    order_queue = Queue()
    # order_queue = []
    for node in vertices:
        # order_queue.append(node)
        order_queue.put(node)
        # while len(order_queue) != 0:
        while not order_queue.empty():
            # current = order_queue.pop()
            current = order_queue.get()
            if current not in visited:
                visited.add(current)
                print(current.val)
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    # order_queue.append(neighbor)
                    order_queue.put(neighbor)


if __name__ == '__main__':
    g0 = GraphNode(0)
    g1 = GraphNode(1)
    g2 = GraphNode(2)
    g3 = GraphNode(3)
    g4 = GraphNode(4)
    g5 = GraphNode(5)

    g5.addEdge(g2)
    g5.addEdge(g0)
    g4.addEdge(g0)
    g4.addEdge(g1)
    g2.addEdge(g3)
    g3.addEdge(g1)

    vertices = [g5, g2, g0, g4, g1, g3]

    print("Following is a Topological Sort of the given graph")
    top_sort(vertices, set())
