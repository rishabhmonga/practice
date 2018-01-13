# 0 0 0 1
# 1 0 1 0
# 1 1 1 0
# 0 0 0 0

# 1 1
# (0, 0)

visited_cells = set()


def get_cell_count(board, idx, idy):
    cell_count = 1
    if 0 <= idx < len(board) and 0 <= idy < len(board) and (idx, idy) not in visited_cells:
        visited_cells.add((idx, idy))
        if board[idx][idy] == 1:
            cell_count += get_cell_count(board, idx - 1, idy) + get_cell_count(board, idx, idy - 1) + get_cell_count(board, idx + 1, idy) + get_cell_count(board, idx, idy + 1)
    return cell_count


print(get_cell_count([[1, 1], [1, 1]], 0, 0))