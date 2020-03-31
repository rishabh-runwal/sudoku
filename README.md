# Sudoku Generator and Solver
Sudoku is a logic-based,combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which has to be filled completely by the solver.
## Implementation
This is a fairly simple Sudoku solver written in Python employing a backtracking Algorithm to generate solutions.
##### Generation
Initially the Program develops a Sudoku grid and then asks the User to Enter a level of difficulty. According to the level of difficulty chosen, some numbers are removed from the grid and then presented to the user.
##### Solver
Upon solving the generated sudoku, the user can verify their solution with a one created by the program. 
Using a function Solver()
