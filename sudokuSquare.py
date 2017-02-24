# Class for the sudoku square, with the solving function and others.


class SudokuSquare:
    sudoku_square = [[[0 for i in range(9)] for ii in range(9)] for iii in range(9)]
    possible_values = []
    # Initiate: read input file, 0 represents an empty spot
    def __init__(self, nume_fisier):
        self.sudoku_file = open(nume_fisier, 'r')
        self.sudoku_square = [[int(x) for x in line.split()] for line in self.sudoku_file]

    # Print the sudoku square
    def show(self):

        print('###################\n')
        for i1 in range(9):
            for j1 in range(9):
                print(self.sudoku_square[i1][j1], end=' ')
                if (j1 + 1) % 3 == 0:
                    print(' ', end='')
            if (i1 + 1) % 3 == 0:
                print()
            print()
        print('###################\n')
