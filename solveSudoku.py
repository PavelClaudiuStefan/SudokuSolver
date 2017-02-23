# Solve Sudoku


class SudokuGame:

    sudoku_square = [[[0 for i in range(9)] for ii in range(9)] for iii in range(9)]

    # Read the numbers from a file
    def __init__(self, nume_fisier):
        self.sudoku_file = open(nume_fisier, "r")
        self.sudoku_square = [[int(x) for x in line.split()] for line in self.sudoku_file]

    # Print the sudoku square
    def print_sudoku_square(self):
        print()
        for i1 in range(9):
            for j1 in range(9):
                print(self.sudoku_square[i1][j1], end=' ')
                if (j1 + 1) % 3 == 0:
                    print('  ', end='')
            if (i1 + 1) % 3 == 0:
                print()
            print()

    # Solution_map 1
    # Temporar
    def find_solutions(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku_square[i][j] == 0:
                    # print("m[{}][{}] = {}".format(i, j, self.sudoku_square[i][j]))
                    for x in range(1, 10):
                        x = x
                    # valid = valid_square(x, i, j) and valid_line(x, i, j) and valid_column(x, i, j)


    # Check if the number is valid in this small square
    def valid_square(self, x, i, j):
        # Ma gandeasc la un dictionar de liste
        # Exemple: 0: [0, 2], 1: [0, 2], ..., 8: [6, 8]


    # Check if the number is valid in this line

    # Check if the number is valid in this column

sudo = SudokuGame("sudoku1.in")
sudo.print_sudoku_square()
sudo.find_solutions()
