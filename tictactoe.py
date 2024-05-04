import math, random


def play():
    players = set('XO')
    board = [' '] * 9

    while not (user := input("Pick a player (XO): ").upper()) in players:
        print("Pick a valid player.")

    computer = other(user, players)
    player = random.choice(list(players))

    while not ((winner := check(players, board)) or filled(board)):
        display(board)
        if player == user:
            move = user_move(board)
            player_description = "You"
        else:
            move = computer_move(computer, board, players)
            player_description = "Computer"
        board[move] = player
        print(f"{player_description} made move at {move + 1}")

        player = other(player, players)

    display(board)
    if winner == user:
        print("You win.")
    elif winner == computer:
        print("You lose.")
    else:
        print("Tie.")


def other(player, players):
    return (players - set(player)).pop()


def display(board):
    for line in ('|'.join(item for item in row) for row in rows(board)):
        print(line)


def check(players, board):
    horizontal = next((player for player in players if check_horizontal(player, board)), None)
    vertical   = next((player for player in players if check_vertical(player, board)), None)
    diagonal   = next((player for player in players if check_diag1(player, board) or\
        check_diag2(player, board)), None)
    return horizontal or vertical or diagonal


def check_horizontal(player, board):
    return any(all(item == player for item in row) for row in rows(board))


def rows(board):
    return ((board[3 * i + j] for j in range(3)) for i in range(3))


def check_vertical(player, board):
    return any(all(item == player for item in col) for col in columns(board))


def columns(board):
    return ((board[3 * j + i] for j in range(3)) for i in range(3))


def check_diag1(player, board):
    return all(item == player for item in diag1(board))


def diag1(board):
    return (board[3 * i + i] for i in range(3))


def check_diag2(player, board):
    return all(item == player for item in diag2(board))


def diag2(board):
    return (board[2 * (i + 1)] for i in range(3))


def filled(board):
    return board.count(' ') == 0


def user_move(board):
    while True:
        try:
            move = int(input("Make a move (1-9): ")) - 1
            if not valid_move(move, board):
                raise ValueError
        except ValueError:
            print("Move is invalid.")
            continue
        else:
            break

    return move


def computer_move(computer, board, players):
    if free_cells(board) == 9:
        move = random.randrange(9)
    else:
        move = minimax(computer, computer, board, players)
        move = move[1]
    return move


def valid_move(move, board):
    return move in range(9) and board[move] == ' '


def minimax(player, maxplayer, board, players):
    if (result := check(players, board)) == maxplayer:
        return (1 * (free_cells(board) + 1), None)
    elif result == other(maxplayer, players):
        return (-1 * (free_cells(board) + 1), None)
    elif filled(board):
        return (0, None)
    if player == maxplayer:
        value = (-math.inf, None)
        for move in available_moves(board):
            score = try_move(move, player, maxplayer, board, players)
            if score[0] > value[0]:
                value = (score[0], move)
    else:
        value = (+math.inf, None)
        for move in available_moves(board):
            score = try_move(move, player, maxplayer, board, players)
            if score[0] < value[0]:
                value = (score[0], move)
    return value


def try_move(move, player, maxplayer, board, players):
    board[move] = player
    result = minimax(other(player, set('XO')), maxplayer, board, players)
    board[move] = ' '
    return result


def available_moves(board):
    return (move for move, cell in enumerate(board) if cell == ' ')


def free_cells(board):
    return board.count(' ')


play()
