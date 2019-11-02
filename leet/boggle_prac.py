def preProcessBoard(board):
    dimension = len(board)
    boardMap = dict()

    for i in range(dimension):
        for j in range(dimension):
            if board[i][j] in boardMap:
                boardMap[board[i][j]].append(i * dimension + j)
            else:
                boardMap[board[i][j]] = [i * dimension + j]
    return boardMap


def getNeighbors(index, dimension):
    row = int(index / dimension)
    col = int(index % dimension)
    neighbors = set()
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i <= dimension and 0 <= j <= dimension and not (i == row and j == col):
                neighbors.add(i * dimension + j)
    return neighbors


dimension = 4


def isOnBoard(boardMap, word, oldPos, posList):
    if len(word) == 0:
        return True
    if word[0] not in boardMap:
        return False
    else:
        if oldPos is None:
            for pos in boardMap[word[0]]:
                posList.add((pos))
                if isOnBoard(boardMap, word[1:], pos, posList):
                    return True
                else:
                    posList.remove(pos)
        else:
            for pos in boardMap[word[0]]:
                if pos in getNeighbors(oldPos, dimension) and pos not in posList:
                    posList.add(pos)
                    if isOnBoard(boardMap, word[1:], pos, posList):
                        return True
                    else:
                        posList.remove(pos)
    return False



if __name__ == '__main__':
    board = [['s', 'm', 'e', 'f'],
             ['r', 'a', 't', 'd'],
             ['l', 'o', 'n', 'i'],
             ['k', 'a', 'f', 'b']]
    boardMap = preProcessBoard(board)
    print(boardMap)
    print(isOnBoard(boardMap, 'afna', None, set()))
