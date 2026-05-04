## Overview

This project presents a complete implementation of a Sudoku validation and solving system in Python, enhanced with an interactive graphical user interface built using Tkinter. It demonstrates how constraint-based problems can be modeled computationally and solved efficiently through recursive backtracking.



## Objectives
Design a reliable Sudoku validation system based on rule enforcement↳
Implement a recursive backtracking algorithm for solving constraint-based problems↳
Integrate algorithmic logic with a graphical interface for better usability
Demonstrate the practical application of recursion and state-space exploration↳

## Core Features
Complete Sudoku validation (rows, columns, and subgrids)
Recursive backtracking solver
Interactive 9×9 graphical grid for user input
Preloaded sample puzzle for testing and demonstration
Clear/reset functionality for repeated use
Input restriction to valid digits (1–9)
Algorithmic Approach
Validation Strategy (checkboard)

## The validation component ensures that the Sudoku grid strictly follows the fundamental rules:

Row Integrity: No repeated values within any row
Column Integrity: No repeated values within any column
Subgrid Integrity: Each 3×3 subgri

Empty cells, represented by ".", are ignored during validation, allowing partially filled boards to be checked without false conflicts.

## Solving Strategy (solve_sudoku)

The solver uses a depth-first search (DFS) with backtracking, a standard approach for constraint satisfaction problems.

## Workflow:

Traverse the grid to locate the next empty cell
Attempt values from 1 to 9
Validate the board after each assignment
If valid, recursively proceed to the next cell
If invalid, revert the assignment (backtrack)
Continue until a complete valid solution is found

## This method explores the solution space systematically while eliminating invalid paths early.

## Graphical User Interface

The GUI is built using Tkinter to provide an accessible interaction layer:

Structured 9×9 input grid
Solve button to execute the algorithm
Load Example button to autofill a sample puzzle
Clear button to reset the board
Input validation to ensure only digits 1–9 are accepted



## Structure
checkboard(board) – Validates the Sudoku grid
solve_sudoku(board) – Implements the backtracking solver↳
get_board() – Retrieves input from the GUI↳
display(board) – Updates the GUI with results↳
GUI controls – Buttons and event handlers
Main loop – Runs the application↳
Sample Puzzle
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
## Output

After execution, the solver generates a completed valid Sudoku grid, displayed directly in the GUI:

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
...
## Limitations
Uses brute-force backtracking without heuristic optimization
Performance may decrease for highly complex or sparse puzzles
Returns only a single valid solution
Limited feedback for invalid board states in the GUI
Future Enhancements
Implement heuristics such as Minimum Remaining Values (MRV) and forward checking
Add real-time feedback for invalid inputs
Introduce step-by-step solving visualization
Support multiple solution detection and enumeration
Improve UI design with enhanced styling and clearer grid segmentation
## Conclusion

This project demonstrates how classical algorithmic techniques like recursion and backtracking can be applied to structured logical problems. By combining these methods with a graphical interface, the system not only solves Sudoku puzzles but also provides an accessible and interactive platform for users.

---
