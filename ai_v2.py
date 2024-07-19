import numpy as np
import random
from board import check_win, is_board_full, mark_square
from constants import BOARD_ROWS, BOARD_COLS

def minimax(board, depth, is_maximizing):
    """Minimax algorithm to determine the best move for the AI."""
    if check_win(board, 2):
        return float('inf')
    elif check_win(board, 1):
        return float('-inf')
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 2
                    score = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    """Determines the best move for the AI and marks the board."""
    # Probability factor: 20% chance to make a blunder
    if random.random() < 0.2:
        blunder_move(board)
        return True
    
    best_score = -1000
    move = (-1, -1)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)

    if move != (-1, -1):
        mark_square(board, move[0], move[1], 2)
        return True
    return False

def blunder_move(board):
    """Makes a random move (blunder) for the AI."""
    available_moves = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if board[row][col] == 0]
    if available_moves:
        move = random.choice(available_moves)
        mark_square(board, move[0], move[1], 2)
