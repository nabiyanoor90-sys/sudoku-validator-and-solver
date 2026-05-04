# Sudoku Solver & Validator (Python)

## Introduction

This project is a simple and effective Sudoku Solver and Validator implemented in Python. It performs two main tasks:

1. Validates whether a given Sudoku board follows the rules.
2. Solves the Sudoku puzzle using a backtracking algorithm.

The implementation is lightweight, uses no external libraries, and demonstrates core problem-solving techniques such as recursion and constraint checking.

---

## How It Works

### 1. Board Validation (`checkboard`)

The `checkboard` function ensures the Sudoku board is valid by checking three conditions:

* Rows: Each row must contain unique digits (1–9).
* Columns: Each column must contain unique digits.
* 3×3 Subgrids: Each 3×3 box must also contain unique digits.

Empty cells are represented by `"."` and are ignored during validation.

---

### 2. Sudoku Solver (`solver`)

The solver uses a backtracking approach:

1. Traverse the board to find an empty cell (`"."`).
2. Try placing numbers from 1 to 9.
3. After placing a number:

   * Validate the board using `checkboard`.
   * Recursively attempt to solve the rest of the board.
4. If a number leads to a dead end:

   * Reset the cell (`"."`) and try the next number.
5. Continue until:

   * The board is completely filled (solution found), or
   * All possibilities are exhausted (no solution).

---

## Code Structure

```
├── checkboard(board)   # Validates rows, columns, and 3x3 grids
├── solver(board)       # Solves the Sudoku using recursion
└── main execution      # Defines board, validates, solves, prints result
```

---

## Example Board

The following Sudoku puzzle is used as input:

```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

---

## Sample Output

First, the program checks if the board is valid:

```
BOARD IS VALID
```

Then, it prints the solved Sudoku:

```
['5', '3', '4', '6', '7', '8', '9', '1', '2']
['6', '7', '2', '1', '9', '5', '3', '4', '8']
['1', '9', '8', '3', '4', '2', '5', '6', '7']
['8', '5', '9', '7', '6', '1', '4', '2', '3']
['4', '2', '6', '8', '5', '3', '7', '9', '1']
['7', '1', '3', '9', '2', '4', '8', '5', '6']
['9', '6', '1', '5', '3', '7', '2', '8', '4']
['2', '8', '7', '4', '1', '9', '6', '3', '5']
['3', '4', '5', '2', '8', '6', '1', '7', '9']
```

---

## Limitations

* No Graphical User Interface (GUI): The program runs entirely in the console.
* Performance Constraints: Backtracking can be slow for highly complex or nearly empty boards.
* No Optimization Heuristics: Techniques like constraint propagation or MRV are not implemented.
* Static Input: The board is hardcoded; no file input or user input interface is provided.
* Single Solution Assumption: The solver stops after finding the first valid solution.

---

## Key Concepts Demonstrated

* Recursion
* Backtracking
* Constraint validation
* Grid-based problem solving

---

## Conclusion

This project is a solid starting point for understanding how Sudoku solvers work. It demonstrates the use of recursion and systematic search to solve constraint-based problems in a clear and straightforward way.

---
