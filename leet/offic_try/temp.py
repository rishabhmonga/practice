if __name__ == '__main__':
    grid = [[3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]]

    print(list(map(max, grid)))
    print(list(map(max, *grid)))
