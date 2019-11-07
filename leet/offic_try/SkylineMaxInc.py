def maxIncreaseKeepingSkyline(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    leftright = []
    for i in grid:
        leftright.append(max(i))

    topdown = []
    for i in range(len(grid[0])):
        maxht = 0
        for j in range(len(grid)):
            maxht = max(maxht, grid[j][i])
        topdown.append(maxht)
    print(topdown)
    print(leftright)



if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    maxIncreaseKeepingSkyline(grid)