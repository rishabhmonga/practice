"""
Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation:
The grid is:
[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

Notes:

    1 < grid.length = grid[0].length <= 50.
    All heights grid[i][j] are in the range [0, 100].
    All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

"""


# class Solution:
# def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
# pass

def findMaxRow(grid):
    max_rows = []
    for i in grid:
        max_rows.append(max(i))
    return max_rows


def findMaxCol(grid):
    max_cols = []
    for j in range(len(grid[0])):
        maximum = 0
        for i in range(len(grid)):
            maximum = max(maximum, grid[i][j])
        max_cols.append(maximum)
    return max_cols


def maxIncreaseKeepingSkyline(grid):
    max_rows = findMaxRow(grid)
    max_cols = findMaxCol(grid)

    newGrid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            newGrid[i][j] = min(max_rows[i], max_cols[j])

    return newGrid


if __name__ == '__main__':
    grid = [[3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]]
    # print(findMaxRow(grid))
    # print(findMaxCol(grid))
    print(maxIncreaseKeepingSkyline(grid))

