def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    for row in A:
        for idx in range(int(len(row)/2)):
            temp = row[idx]
            row[idx] = row[-1-idx]
            row[-1 - idx] = temp
        for idx in range(len(row)):
            if row[idx] == 0:
                row[idx] = 1
            elif row[idx] == 1:
                row[idx] = 0
    return A


if __name__ == '__main__':
    imatrix = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(flipAndInvertImage(imatrix))
