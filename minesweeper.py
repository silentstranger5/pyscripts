import itertools, random, sys


def play(size):
    dim_size = size
    num_bombs = size
    board = [' '] * (dim_size ** 2)
    plant_bombs(board, dim_size, num_bombs)

    while not filled(board):
        print("Game board: ")
        display(visible(board), dim_size)
        move = get_move(board, dim_size)
        if dig(move, board, dim_size):
            continue
        else:
            print("Game over.")
            break
    else:
        print("You win.")

    print("Game board: ")
    display(board, dim_size)


def filled(board):
    return board.count(' ') == 0


def visible(board):
    return [item if item != '*' else ' ' for item in board]


def plant_bombs(board, dim_size, num_bombs):
    for i in range(num_bombs):
        board[random.randrange(dim_size ** 2)] = '*'


def display(board, dim_size):
    print("--|" + '|'.join(str(i) for i in range(1, dim_size + 1)))
    for row, i in zip(rows(board, dim_size), range(1, dim_size + 1)):
        print(f"{i:2}|" + '|'.join(item for item in row))


def get_move(board, dim_size):
    while True:
        try:
            row, col = input(f"Type a move (row col 1-{dim_size}): ").split()
            row = int(row) - 1
            col = int(col) - 1
            move = dim_size * row + col
            if any(val not in range(dim_size) for val in (row, col)) or\
                board[move].isdigit():
                raise ValueError
        except ValueError:
            print("Invalid move.")
            continue
        else:
            return move


def rows(board, dim_size):
    return ((board[dim_size * i + j] for j in range(dim_size)) for i in range(dim_size))


def dig(move, board, dim_size):
    if (result := board[move] == ' '):
        value = get_neighbours(move, board, dim_size)
        board[move] = str(value)
        if value == 0:
            for cell in get_matrix(move, board, dim_size):
                dig(cell, board, dim_size)
    return result


def get_neighbours(move, board, dim_size):
    return sum(1 for item in filter(is_bomb, (board[cell] for cell in get_matrix(move, board, dim_size))))


def is_bomb(cell):
    return cell == '*'


def get_matrix(move, board, dim_size):
    row = int(move / dim_size)
    col = move % dim_size
    low_row = row if row == 0 else row - 1
    high_row = row + 1 if row == dim_size - 1 else row + 2
    row_range = range(low_row, high_row)
    low_col = col if col == 0 else col - 1
    high_col = col + 1 if col == dim_size - 1 else col + 2
    col_range = range(low_col, high_col)
    return (row * dim_size + col for col in col_range for row in row_range)


if len(sys.argv) == 2:
    try:
        size = int(sys.argv[1])
        if not 4 < size < 16:
            raise ValueError
    except ValueError:
        exit("Usage: python minesweeper.py size")
else:
    size = 5

play(size)
