def numberOfLines(widths, S):
    """
    :type widths: List[int]
    :type S: str
    :rtype: List[int]
    """
    res, cur = 1, 0
    for i in S:
        width = widths[ord(i) - ord('a')]
        res += 1 if cur + width > 100 else 0
        cur = width if cur + width > 100 else cur + width
    return [res, cur]


if __name__ == '__main__':
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "bbbcccdddaaa"
    print(numberOfLines(widths, S))
