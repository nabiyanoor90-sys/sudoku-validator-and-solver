import tkinter as tk

# ---------- VALIDATOR ----------
def checkboard(board):
    for row in board:
        nums = [x for x in row if x != "."]
        if len(nums) != len(set(nums)):
            return False

    for col in range(9):
        nums = []
        for row in range(9):
            if board[row][col] != ".":
                nums.append(board[row][col])
        if len(nums) != len(set(nums)):
            return False

    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            nums = []
            for i in range(3):
                for j in range(3):
                    val = board[br+i][bc+j]
                    if val != ".":
                        nums.append(val)
            if len(nums) != len(set(nums)):
                return False

    return True


# ---------- SOLVER ----------
def solve_sudoku(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                for num in range(1, 10):
                    board[r][c] = str(num)

                    if checkboard(board):
                        if solve_sudoku(board):
                            return True

                    board[r][c] = "."
                return False
    return True


# ---------- GUI ----------
root = tk.Tk()
root.title("Sudoku Solver")

cells = []

# grid
for i in range(9):
    row = []
    for j in range(9):
        e = tk.Entry(root, width=3, font=("Arial", 18), justify='center')
        e.grid(row=i, column=j, padx=2, pady=2)
        row.append(e)
    cells.append(row)


# get board
def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = cells[i][j].get()
            if val == "":
                row.append(".")
            else:
                row.append(val)
        board.append(row)
    return board


# display board
def display(board):
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            cells[i][j].insert(0, board[i][j])


# example board
def load_example():
    example = [
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
    display(example)


# solve
def solve():
    board = get_board()

    if solve_sudoku(board):
        display(board)
    else:
        print("No solution")


# clear board
def clear():
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)


# buttons
tk.Button(root, text="Load Example", command=load_example).grid(row=9, column=0, columnspan=3)
tk.Button(root, text="Solve", command=solve).grid(row=9, column=3, columnspan=3)
tk.Button(root, text="Clear", command=clear).grid(row=9, column=6, columnspan=3)

root.mainloop()
