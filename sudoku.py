def read(filename):
    try:
        file = open(filename, encoding='utf8')
        puzzle = list(int(item) for item in ' '.join(file.read().rstrip(',').splitlines()).split(','))
    except (ValueError, OSError):
        return None
    else:
        return puzzle
    finally:
        if 'file' in locals():
            file.close()


def solve(puzzle):
    print("Initial sudoku: ")
    display(puzzle)
    if find_solution(puzzle):
        print("Solved sudoku: ")
        display(puzzle)
    else:
        print("There is no solution.")


def find_solution(puzzle):
    if filled(puzzle):
        return True
    index = find_empty(puzzle)
    for guess in range(1, 10):
        if valid(guess, index, puzzle):
            puzzle[index] = guess
            if find_solution(puzzle):
                return True
        puzzle[index] = 0
    else:
        return False



def filled(puzzle):
    return puzzle.count(0) == 0


def find_empty(puzzle):
    return puzzle.index(0)


def valid(guess, index, puzzle):
    valid_row = check_row(guess, index, puzzle)
    valid_column = check_column(guess, index, puzzle)
    valid_square = check_square(guess, index, puzzle)
    return all((valid_row, valid_column, valid_square))


def check_row(guess, index, puzzle):
    return all(cell != guess for cell in row(index, puzzle))


def row(index, puzzle):
    return (puzzle[9 * (index // 9) + column] for column in range(9))


def check_column(guess, index, puzzle):
    return all(cell != guess for cell in column(index, puzzle))


def column(index, puzzle):
    return (puzzle[9 * row + (index % 9)] for row in range(9))


def check_square(guess, index, puzzle):
    return all(cell != guess for cell in square(index, puzzle))


def square(index, puzzle):
    row_value = index // 9
    column_value = index % 9
    square = 3 * (row_value // 3) + (column_value // 3)
    return (puzzle[square_pos(square) + 9 * row + column] for row in range(3) for column in range(3))


def square_pos(square):
    return 18 * (square // 3) + 3 * square


def display(puzzle):
    for row in range(9):
        if row % 3 == 0:
            print('+-------' * 3 + '+')
        for column in range(9):
            if column % 3 == 0:
                print(' |', end='')
            if puzzle[9 * row + column] == 0:
                print(' |', end='')
            else:
                print(str(puzzle[9 * row + column]) + '|', end='')
        print()
    print('+-------' * 3 + '+')


if puzzle := read('sudoku.txt'):
    solve(puzzle)
else:
    print("Invalid input file.")
