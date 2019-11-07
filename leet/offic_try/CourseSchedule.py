def build_graph(graph, course, req):
    if course not in graph:
        if req is None:
            graph[course] = []
        else:
            graph[course] = [req]
    else:
        if graph[course] is None and req is not None:
            graph[course] = [req]
        elif req is not None:
            graph[course].append(req)

    return graph


def topsort(graph, visited):
    sorted_stack = []
    for course, prereq in graph.items():
        if course not in visited:
            visited.add(course)
            for c in prereq:
                sorted_stack.append(c)

    return sorted_stack


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if numCourses <= 1:
        return True

    graph = dict()
    for i in range(len(prerequisites)):
        graph = build_graph(graph, prerequisites[i][0], prerequisites[i][1])
        graph = build_graph(graph, prerequisites[i][1], None)
    print(graph.items())
    visited = set()
    sorted_stack = topsort(graph, visited)
    print('sorted stack : ', sorted_stack)
    return True if len(sorted_stack) == numCourses else False


if __name__ == '__main__':
    courses = [[1, 0]]
    print(canFinish(2, courses))
