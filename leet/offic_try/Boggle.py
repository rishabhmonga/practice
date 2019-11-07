visited = set()


def checkNeighbors(char, board, idx, idy):
    possible_chars = []

    # up
    if idx > 0 and board[idx - 1][idy] == char:
        possible_chars.append((idx - 1, idy))

    # down
    if idx < len(board) - 1 and board[idx + 1][idy] == char:
        possible_chars.append((idx + 1, idy))

    # left
    if idy > 0 and board[idx][idy - 1] == char:
        possible_chars.append((idx, idy - 1))

    # right
    if idy < len(board[0]) - 1 and board[idx][idy + 1] == char:
        possible_chars.append((idx, idy + 1))

    # left - up
    if idx > 0 and idy > 0 and board[idx - 1][idy - 1] == char:
        possible_chars.append((idx - 1, idy - 1))

    # left - down
    if idy > 0 and idx < len(board) - 1 and board[idx + 1][idy - 1] == char:
        possible_chars.append((idx + 1, idy - 1))

    # right - up
    if idy < len(board[0]) - 1 and idx > 0 and board[idx - 1][idy + 1] == char:
        possible_chars.append((idx - 1, idy + 1))

    # right - down
    if idy < len(board[0]) - 1 and idx < len(board) - 1 and board[idx + 1][idy + 1] == char:
        possible_chars.append((idx + 1, idy + 1))

    if len(possible_chars) == 0:
        visited.add((idx, idy))
    return possible_chars


def findSequence(seq, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) not in visited and board[i][j] == seq[0]:
                result = [(i, j)]
                k = 0
                prev_x, prev_y = i, j
                while k < len(seq) - 1:
                    possible_chars = checkNeighbors(seq[k + 1], board, prev_x, prev_y)
                    if len(possible_chars) == 0:
                        visited.add((i, j))
                        break
                    for x, y in possible_chars:
                        result.append((x, y))
                        prev_x, prev_y = x, y
                        k += 1
                        if k == len(seq) - 1:
                            return result
    return []


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'D'],
             ['S', 'P', 'E', 'Y'],
             ['B', 'C', 'Q', 'U'],
             ['A', 'N', 'I', 'X']]
    # print(findSequence('ABCN', board))

    board = [['A', 'B', 'O', 'P', 'L'],
             ['X', 'Y', 'P', 'X', 'R'],
             ['Q', 'S', 'T', 'A', 'L'],
             ['R', 'T', '5', 'M', 'L'],
             ['S', 'M', 'Y', 'P', 'Q']]

    print(findSequence('STAMP', board))

    board = [['S', 'M,' 'E', 'F'],
             ['R', 'A', 'T', 'D'],
             ['L', 'O', 'N', 'I'],
             ['K', 'A', 'F', 'B']]
    # print(findSequence('SATIN', board))


