def is_safe(board, row, col, n):
    # 檢查同一列是否有皇后
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_queens(board, row, n):
    if row == n:
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_queens(board, row + 1, n)
            board[row] = -1  # 回溯

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def eight_queens(n):
    board = [-1] * n
    solve_queens(board, 0, n)

# 測試解八皇后問題
eight_queens(8)
