from SudokuSquare import SudokuSquare

sudoku_1 = SudokuSquare("sudoku1.in")
sudoku_1.print()
while sudoku_1.completed() == False:
    sudoku_1.solve()
    sudoku_1.print()

