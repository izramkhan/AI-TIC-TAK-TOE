import random

board = [' ' for _ in range(9)]

def check_winner(player):

    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(board[a] == board[b] == board[c] == player
                for a, b, c in win_combos)

def is_draw():
    return ' ' not in board

def win_or_block():
    empty_cells = [i for i in range(9) if board[i] == ' ']

    # 1. Try to WIN
    for cell in empty_cells:
        board[cell] = 'O'
        if check_winner('O'):
            return
        board[cell] = ' '

    # 2. Try to BLOCK
    for cell in empty_cells:
        board[cell] = 'X'
        if check_winner('X'):
            board[cell] = 'O'
            return
        board[cell] = ' '

    # 3. Otherwise RANDOM
    board[random.choice(empty_cells)] = 'O'
