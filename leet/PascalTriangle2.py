def getRow(rowIndex):
    row = []
    soln = []
    for i in range(rowIndex+1):
        row.insert(0, 1)
        print("row : ", row)
        for j in range(1, len(row) - 1):
            row[j] = row[j] + row[j+1]
        soln.append(list(row))
    return soln[rowIndex]

print(getRow(2))
