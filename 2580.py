sudoku = []
sudoku_row_used = [[False for i in range(9)] for j in range(9)]
sudoku_column_used = [[False for i in range(9)] for j in range(9)]
sudoku_square_used = [[False for i in range(9)] for j in range(9)]

for i in range(9):
    row = [int(t) for t in input().split()]
    sudoku.append(row)
    for idx,j in enumerate(row):
        if j > 0:
            sudoku_row_used[i][j-1] = True
            sudoku_column_used[idx][j-1]=True
            sudoku_square_used[(i//3)*3+idx//3][j-1] = True

def check(row,col,value):
    # row check
    if sudoku_row_used[row][value] == True:
        return False
    # col check
    if sudoku_column_used[col][value] == True:
        return False
    if sudoku_square_used[(row//3)*3+col//3][value] == True:
        return False
    return True

def go(row_idx,col_idx):
    global sudoku
    global sudoku_row_used
    global sudoku_column_used
    global sudoku_square_used
    next_row_idx = row_idx if col_idx <8 else row_idx+1
    next_col_idx = col_idx+1 if col_idx <8 else 0
    if row_idx == 9:
        for row in sudoku:
            print(*row)
        exit()

    number  = sudoku[row_idx][col_idx]
    if number == 0:
        for i in range(9):
            if check(row_idx,col_idx,i):
                sudoku[row_idx][col_idx]= i+1
                sudoku_row_used[row_idx][i] = True
                sudoku_column_used[col_idx][i] = True
                sudoku_square_used[(row_idx//3)*3+col_idx//3][i] = True
                go(next_row_idx,next_col_idx)
                sudoku[row_idx][col_idx]= 0
                sudoku_row_used[row_idx][i] = False
                sudoku_column_used[col_idx][i] = False
                sudoku_square_used[(row_idx//3)*3+col_idx//3][i] = False

    else :
        go(next_row_idx,next_col_idx)

go(0,0)