# http://www.extremesudoku.info/sudoku.html evil sudoku

from SudokuSquare import SudokuSquare

# sudoku = SudokuSquare("sudoku1.in")   # (Solved) Made by me
sudoku = SudokuSquare("sudoku2.in")   # (Solved) Hard Sudoku
# sudoku = SudokuSquare("sudoku3.in")   # Extreme Sudoku (Not solvable yet)
# sudoku = SudokuSquare("sudoku4.in")   # Evil Sudoku (Not solvable yet

sudoku.print()
sudoku.solve()
