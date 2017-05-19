from collections import defaultdict
from collections import deque


def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    dic = {i: set() for i in xrange(numCourses)}
    neighbors = defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neighbors[j].add(i)
    order_queue = deque(i for i in dic if not dic[i])
    count, res = 0, []
    while len(order_queue) != 0:
        node = order_queue.popleft()
        res.append(node)
        count += 1
        for i in neighbors[node]:
            dic[i].remove(node)
            if not dic[i]:
                order_queue.append(i)
    return res if count == numCourses else []


def findOrder1(numCourses, prerequisites):
    dic = {i: set() for i in xrange(numCourses)}
    neighbors = defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neighbors[j].add(i)
    order_stack = [i for i in dic if not dic[i]]
    count, res = 0, []
    while order_stack:
        node = order_stack.pop()
        res.append(node)
        count += 1
        for i in neighbors[node]:
            dic[i].remove(node)
            if not dic[i]:
                order_stack.append(i)
    return res if count == numCourses else []


if __name__ == '__main__':
    print findOrder(2, [[1, 0]])
    print findOrder1(2, [[1, 0]])

    print findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print findOrder1(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
