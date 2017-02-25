# Class for the sudoku square, with the solving function and others.


class SudokuSquare:

    # Initiate: read input file, 0 represents an empty spot
    def __init__(self, nume_fisier):
        self.sudoku_file = open(nume_fisier, 'r')
        self.sudoku_square = [[int(x) for x in line.split()] for line in self.sudoku_file]

    # Print the sudoku square
    def print(self):
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

    # Checks if there exists only one number that fits in a certain slot
    # Runs only once
    def solve(self):
        # Seeking for "definites"
        for i in range(9):
            for j in range(9):
                if self.sudoku_square[i][j] == 0:
                    self.sudoku_square[i][j] = self.sure_value(i, j)

    # Returns a number that is certainly the only number that can fit in that slot, else 0
    def sure_value(self, i, j):
        # return x if x != 0 in square
        numar = self.square_value(i, j)
        if numar != 0:
            return numar
        # return x if x != 0 in line
        # return x if x != 0 in column
        # return 0
        return 0

    # Seek "definite" in a square
    def square_value(self, i, j):
        empty_slot = [0] * 9
        s = 0
        x = 0
        i_patrat = int(i / 3) * 3
        j_patrat = int(j / 3) * 3
        for ii in range(i_patrat, i_patrat + 3):
            for jj in range(j_patrat, j_patrat + 3):
                if self.sudoku_square[ii][jj] != 0:
                    empty_slot[self.sudoku_square[ii][jj]] = 1
        for iii in range(1, 10):
            s += empty_slot[iii]
            if empty_slot[iii] == 0:
                x = iii
        if s == 8:
            return x
        else:
            return 0
