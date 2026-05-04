#validator
def checkboard(board):
#checking rows
 for row in board:
    num=[x for x in row if x!="."]
    if len(num)!=len(set(num)):
        return False
#checking columns
 for column in range(9):
    num=[]
    for row in range(9):
        if board[row][column]!=".":
            num.append(board[row][column])
    if len(num)!=len(set(num)):
                return False
#checking each box
 for boxrow in range(0,9,3):
    for boxcol in range(0,9,3):
        num=[]
        for i in range(3):
            for j in range(3):
                v=board[boxrow+i][boxcol+j]
                if v!=".":
                    num.append(v)
        if len(num)!=len(set(num)):
            return False
 return True
#solver
def solver(board):
    for row in range(9):
        for column in range(9):
            if board[row][column]==".":
                for num in range(1,10):
                 board[row][column]=str(num)
                 if checkboard(board):
                     if solver(board):
                        return True
                 board[row][column]="."
                return False
    return True
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
if checkboard(board):
    print("BOARD IS VALID")
else:
    print("BOARD IS NOT VALID")
result=solver(board)
for row in board:
    print(row)