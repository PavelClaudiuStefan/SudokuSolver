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

    # Solves sudoku aquare
    def solve(self):
        while not self.completed():
            self.solve_once()
            self.print()

    # Checks if there exists only one number that fits in a certain slot
    def solve_once(self):
        # Empty spots will have a list with all the possible solutions
        for i in range(9):
            for j in range(9):
                if self.sudoku_square[i][j] == 0:
                    self.sudoku_square[i][j] = self.value(i, j)

    def value(self, i, j):
        # Check to see if there is a value that is found only here and not in any other list from the square
        numar = self.check_in_square(i, j)
        if numar != 0:
            return numar
        # Check to see if there is a value that is found only here and not in any other list from the line
        numar = self.check_in_line(i, j)
        if numar != 0:
            return numar
        # Check to see if there is a value that is found only here and not in any other list from the column
        numar = self.check_in_column(i, j)
        if numar != 0:
            return numar
        return 0

    def check_in_square(self, i, j):
        lista_principala = []
        lista_secundara = []
        for x in range(1, 10):
            if not self.in_square(x, i, j) and not self.in_line(x, i) and not self.in_column(x, j):
                # Appends a possible solution
                lista_principala.append(x)
        i_s = int(i / 3) * 3
        j_s = int(j / 3) * 3
        for ii in range(i_s, i_s + 3):
            for jj in range(j_s, j_s + 3):
                if self.sudoku_square[ii][jj] == 0 and (ii != i or jj != j):
                    for x in range(1, 10):
                        if not self.in_square(x, ii, jj) and not self.in_line(x, ii) and not self.in_column(x, jj):
                            # Appends a possible solution
                            lista_secundara.append(x)
        if len(lista_principala) == 1:
            return lista_principala[0]
        else:
            for x in lista_principala:
                if x not in lista_secundara:
                    return x
        return 0

    def check_in_line(self, i, j):
        lista_principala = []
        lista_secundara = []
        for x in range(1, 10):
            if not self.in_square(x, i, j) and not self.in_line(x, i) and not self.in_column(x, j):
                lista_principala.append(x)
        for ii in range(9):
            if self.sudoku_square[i][ii] == 0 and ii != j:
                for x in range(1, 10):
                    if not self.in_square(x, i, ii) and not self.in_line(x, i) and not self.in_column(x, ii):
                        lista_secundara.append(x)
        if len(lista_principala) == 1:
            return lista_principala[0]
        else:
            for x in lista_principala:
                if x not in lista_secundara:
                    return x
        return 0

    def check_in_column(self, i, j):
        lista_principala = []
        lista_secundara = []
        for x in range(1, 10):
            if not self.in_square(x, i, j) and not self.in_line(x, i) and not self.in_column(x, j):
                lista_principala.append(x)
        for jj in range(9):
            if self.sudoku_square[jj][j] == 0 and jj != i:
                for x in range(1, 10):
                    if not self.in_square(x, jj, j) and not self.in_line(x, jj) and not self.in_column(x, j):
                        lista_secundara.append(x)
        if len(lista_principala) == 1:
            return lista_principala[0]
        else:
            for x in lista_principala:
                if x not in lista_secundara:
                    return x
        return 0

    def in_square(self, nr, i, j):
        i_s = int(i / 3) * 3
        j_s = int(j / 3) * 3
        for ii in range(i_s, i_s + 3):
            for jj in range(j_s, j_s + 3):
                if nr == self.sudoku_square[ii][jj]:
                    return True
        return False

    def in_line(self, nr, i):
        for ii in range(9):
            if nr == self.sudoku_square[i][ii]:
                return True
        return False

    def in_column(self, nr, j):
        for jj in range(9):
            if nr == self.sudoku_square[jj][j]:
                return True
        return False

    # Function returns true if square is completely filled
    def completed(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku_square[i][j] == 0:
                    return False
        return True
