def countBattleships(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                continue
            if row > 0 and board[row - 1][col] == 'X':
                continue
            if col > 0 and board[row][col - 1] == 'X':
                continue
            count += 1
    return count


if __name__ == '__main__':
    # board = ["X..X", "...X", "...X"]
    board = ["XXX"]
    print(countBattleships(board))
