def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    result = 0
    for p in points:
        distances = {}
        for q in points:
            dx = p[0] - q[0]
            dy = p[1] - q[1]
            distances[dx * dx + dy * dy] = 1 + distances.get(dx * dx + dy * dy, 0)
        for k in distances:
            result += distances[k] * (distances[k] - 1)
    return result


if __name__ == '__main__':
    print numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
