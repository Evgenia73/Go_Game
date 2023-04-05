import itertools
import sys
import pygame
import numpy as np
from pygame import gfxdraw

from ai import AI
import logic_operations
from constants import *


class Game:
    def __init__(self):
        self.size = 9
        self.ai = AI
        self.board = np.zeros((self.size, self.size))

    def start(self):
        pygame.init()
        self.init_pygame()
        self.init_logic_prm()
        self.clear_screen()
        while True:
            self.update()

    def init_logic_prm(self):
        self.black_turn = True
        self.game_on = True
        self.start_points, self.end_points = logic_operations.make_grid(
            self.size)

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_WIDTH),
                                              pygame.RESIZABLE)

    def clear_screen(self):
        self.screen.fill(BOARD_BROWN)
        for start_point, end_point in zip(self.start_points, self.end_points):
            pygame.draw.line(self.screen, BLACK, start_point, end_point)

        guide_dots = [3, self.size // 2, self.size - 4]
        for col, row in itertools.product(guide_dots, guide_dots):
            x, y = logic_operations.col_row_to_xy(col, row, self.size)
            gfxdraw.aacircle(self.screen, x, y, DOT_RADIUS, BLACK)
            gfxdraw.filled_circle(self.screen, x, y, DOT_RADIUS, BLACK)

        pygame.display.flip()

    def click(self, col, row):
        self.board[col, row] = 1 if self.black_turn else 2
        self.black_turn = not self.black_turn
        self.draw()

    def draw(self):
        self.clear_screen()
        for col, row in zip(*np.where(self.board == 1)):
            x, y = logic_operations.col_row_to_xy(col, row, self.size)
            gfxdraw.aacircle(self.screen, x, y, STONE_RADIUS, BLACK)
            gfxdraw.filled_circle(self.screen, x, y, STONE_RADIUS, BLACK)
        for col, row in zip(*np.where(self.board == 2)):
            x, y = logic_operations.col_row_to_xy(col, row, self.size)
            gfxdraw.aacircle(self.screen, x, y, STONE_RADIUS, WHITE)
            gfxdraw.filled_circle(self.screen, x, y, STONE_RADIUS, WHITE)
        pygame.display.flip()

    def enemy_turn(self):
        if not self.black_turn:
            x, y = self.ai.move(self.board)
            self.click(x, y)

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                col, row = logic_operations.xy_to_col_row(x, y, self.size)
                if logic_operations.is_valid_move(col, row, self.board):
                    self.click(col, row)
                    self.enemy_turn()
            if event.type == pygame.QUIT:
                sys.exit()
