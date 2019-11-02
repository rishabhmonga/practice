'''
Boggle
    - Given a string and a 2D char array, check whether the word can be constructed in the board
    - words can be constructed by a combination of adjacent cells (vertically or horizontally neighboring cells)
    - same cell cannot be used twice
Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


def preProcessBoard(board):
    sz = len(board)
    boardMap = {}
    for i in range(sz):
        for j in range(sz):
            if board[i][j] in boardMap:
                boardMap[board[i][j]].append(i * sz + j)
            else:
                boardMap[board[i][j]] = [i * sz + j]
    return boardMap


def getNeighbors(index, sz):
    row = int(index / sz)
    col = int(index % sz)
    neigs = set()
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < sz and 0 <= j < sz and not (i == row and j == col):
                neigs.add(i * sz + j)
    return neigs


def isOnBoard(boardMap, word, oldPos, posList):
    if len(word) == 0:
        return True
    if word[0] not in boardMap:
        return False
    else:
        if oldPos is None:
            for pos in boardMap[word[0]]:
                posList.add(pos)
                if isOnBoard(boardMap, word[1:], pos, posList):
                    return True
                else:
                    posList.remove(pos)
        else:
            for pos in boardMap[word[0]]:
                if pos in getNeighbors(oldPos, 4) and pos not in posList:
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
