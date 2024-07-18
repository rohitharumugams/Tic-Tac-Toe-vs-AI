import pygame
import numpy as np
from constants import *

def draw_lines(screen, color=WHITE):
    """Draws the lines on the game board."""
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

def draw_figures(screen, board, color=WHITE):
    """Draws the figures (X and O) on the board."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20), (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), CROSS_WIDTH)
                pygame.draw.line(screen, color, (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + 20), (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), CROSS_WIDTH)

def mark_square(board, row, col, player):
    """Marks the square on the board with the player's symbol."""
    board[row][col] = player

def available_square(board, row, col):
    """Checks if a square on the board is available."""
    return board[row][col] == 0

def is_board_full(board):
    """Checks if the board is full."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(board, player):
    """Checks if the given player has won."""
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

    return False

def restart(screen, board):
    """Restarts the game by resetting the board and redrawing the lines."""
    screen.fill(BLACK)
    draw_lines(screen)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
