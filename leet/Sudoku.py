def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i in range(0, 9):
        row = []
        col = []
        cube = []
        for j in range(0, 9):
            if board[i][j] is not '.' and board[i][j] in row:
                return False
            if board[j][i] is not '.' and board[j][i] in col:
                return False
            rowIdx = int(3 * (i / 3))
            colIdx = int(3 * (i % 3))
            if board[rowIdx + int(j / 3)][colIdx + int(j % 3)] is not '.' and board[rowIdx + int(j / 3)][
                        colIdx + int(j % 3)] in cube:
                return False
    return True


#     for(int i = 0; i<9; i++){
#         HashSet<Character> rows = new HashSet<Character>();
#         HashSet<Character> columns = new HashSet<Character>();
#         HashSet<Character> cube = new HashSet<Character>();
#         for (int j = 0; j < 9;j++){
#             if(board[i][j]!='.' && !rows.add(board[i][j]))
#                 return false;
#             if(board[j][i]!='.' && !columns.add(board[j][i]))
#                 return false;
#             int RowIndex = 3*(i/3);
#             int ColIndex = 3*(i%3);
#             if(board[RowIndex + j/3][ColIndex + j%3]!='.' && !cube.add(board[RowIndex + j/3][ColIndex + j%3]))
#                 return false;
#         }
#     }
#     return true;


if __name__ == '__main__':
    board = [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
             "9........"]
    print(isValidSudoku(board))
