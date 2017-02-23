# Class for the sudoku square, with the solving function and others.


class SudokuSquare:

    def __init__(self, nume_fisier):
        self.sudoku_file = open(nume_fisier, "r")
        self.sudoku_square = [[int(x) for x in line.split()] for line in self.sudoku_file]
