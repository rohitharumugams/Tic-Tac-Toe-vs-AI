import sys
import pygame
import numpy as np
from constants import *
from board import draw_lines, draw_figures, mark_square, available_square, is_board_full, check_win, restart
from ai import best_move

pygame.init()

# Initialize the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beat Me If You Can")
screen.fill(BLACK)

# Initialize the game board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Draw the initial board lines
draw_lines(screen)

# Game state variables
player = 1
game_over = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE

            if available_square(board, mouseY, mouseX):
                mark_square(board, mouseY, mouseX, player)
                if check_win(board, player):
                    game_over = True
                player = player % 2 + 1

                if not game_over and player == 2:
                    if best_move(board):
                        if check_win(board, 2):
                            game_over = True
                        player = player % 2 + 1

                if not game_over:
                    if is_board_full(board):
                        game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart(screen, board)
                game_over = False
                player = 1

    if not game_over:
        draw_figures(screen, board)
    else:
        if check_win(board, 1):
            draw_figures(screen, board, GREEN)
            draw_lines(screen, GREEN)
        elif check_win(board, 2):
            draw_figures(screen, board, RED)
            draw_lines(screen, RED)
        else:
            draw_figures(screen, board, GRAY)
            draw_lines(screen, GRAY)
    pygame.display.update()
