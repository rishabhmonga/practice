class SparseMat:
    def __init__(self, rows, cols):
        self.mat = dict()
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            self.mat[i] = dict()

    def getDimensions(self):
        return self.rows, self.cols


def matmul(A, B):
    result = SparseMat(len(A), len(B[0]))

    rows = result.getDimensions()[0]
    cols = result.getDimensions()[1]

    for i in range(rows):
        for k in range(len(A[0])):
            if A[i][k] != 0:
                for j in range(cols):
                    if j not in result.mat[i]:
                        result.mat[i][j] = A[i][k] * B[k][j]
                    else:
                        result.mat[i][j] += A[i][k] * B[k][j]
    return result


if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[1, 2],
         [3, 4],
         [5, 6]]

    output = matmul(A, B)

    print(output.getDimensions())

    print(output.mat)


