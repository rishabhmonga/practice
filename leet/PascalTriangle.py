def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    result = list()
    row = list()
    for i in range(numRows):
        row.insert(0, 1)
        for j in range(1, len(row)-1):
            row[j] = row[j] + row[j+1]
        result.append(list(row))
    return result


print(generate(5))

