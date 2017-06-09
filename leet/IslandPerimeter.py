def getCellPerimeter(grid, i, j):
    cell_perimeter = 0
    # edge
    if i == 0:
        cell_perimeter += 1
    if i == len(grid)-1:
        cell_perimeter += 1
    if j == 0:
        cell_perimeter += 1
    if j == len(grid[0])-1:
        cell_perimeter += 1

    # water
    if 0 < i and grid[i-1][j] == 0:
        cell_perimeter += 1
    if i < len(grid) - 1 and grid[i+1][j] == 0:
        cell_perimeter += 1

    if 0 < j and grid[i][j - 1] == 0:
        cell_perimeter += 1
    if j < len(grid[0]) - 1 and grid[i][j + 1] == 0:
        cell_perimeter += 1

    return cell_perimeter


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] is 1:
                perimeter += getCellPerimeter(grid, i, j)

    return perimeter


if __name__ == '__main__':

    # 16
    # print(islandPerimeter([[0, 1, 0, 0],
    #                        [1, 1, 1, 0],
    #                        [0, 1, 0, 0],
    #                        [1, 1, 0, 0]]
    #                       ))

    # 4
    # print(islandPerimeter([[1]]))

    # 7
    print(islandPerimeter([[0, 1, 1]]))
