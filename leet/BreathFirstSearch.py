from collections import deque


class Graph:
    def __init__(self, x):
        self.val = x
        self.children = None


class BFS:
    visited = set()

    def bfs(self, source):
        bfs_queue = deque()
        bfs_queue.append(source)

        while len(bfs_queue) != 0:
            current = bfs_queue.popleft()
            print(current.val)
            if current.children != None:
                for node in current.children:
                    bfs_queue.append(node)


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

    bfs = BFS()
    bfs.bfs(root)
