from Queue import Queue


class T:
    x = 0
    l = None
    r = None


count = 0


def process(t, low, high):
    if t is None:
        return -1

    if low <= t.x <= high:
        count += 1
        l = process(t.l, low, high)
        if l == 0:
            return 0
        r = process(t.r, low, high)
        if r == 0:
            return 0
    else:
        return 0

    return count


def solution(A, B, T):
    # write your code in Python 2.7

    node_list = Queue()
    node_list.put(T)
    while not node_list.empty():
        t = node_list.get()
        if t.l is not None:
            node_list.put(t.l)
        if t.r is not None:
            node_list.put(t.r)

        max_val = max(max_val, process(t, A, B))
        count = 0

    return max_val
