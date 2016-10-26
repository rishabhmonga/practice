def computeArea(A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    x = 0
    y = 0
    if min(G, C) > max(E, A):
        x = (min(G, C) - max(E, A))
    if min(D, H) > max(B, F):
        y = (min(D, H) - max(B, F))
    return (D - B) * (C - A) + (G - E) * (H - F) - x * y

if __name__ == '__main__':
    print(computeArea(-2, -2, 2, 2, -2, -2, 2, 2))
