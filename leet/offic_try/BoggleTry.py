def preProcessBoard(board):
    boardMap = dict()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in boardMap:
                boardMap[board[i][j]].append(i * len(board) + j)
            else:
                boardMap[board[i][j]] = [i * len(board) + j]
    return boardMap


def getNeighbors(index, dimension):
    row = int(index / dimension)
    col = int(index % dimension)
    neighbors = set()

    for