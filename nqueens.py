def isSafe(board, row, col):
    # row
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    return True


def nqueens(board, col):
    if col >= N:
        return True
    
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1

            if nqueens(board, col+1):
                return True
            board[i][col] = 0

    return False


global N
N = 4
board = [[0 for i in range(N)] for j in range(N)]

if not nqueens(board, 0):
    print("No solution")
else:
    for i in board:
        for j in i:
            print(j, end = " ")
        print("")