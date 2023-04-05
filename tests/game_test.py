import unittest

import numpy as np

import logic_operations
from game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.game.init_pygame()
        self.game.init_logic_prm()

    # def tearDown(self):

    def test_click(self):
        self.game.click(1, 1)
        self.assertEqual(self.game.board[1, 1], 1)

    def test_enemy_turn(self):
        self.game.enemy_turn()
        xs, ys = np.where(self.game.board == 2)
        zeroes = list(zip(xs, ys))
        self.assertTrue(zeroes is not None)


class LogicOperationsTest(unittest.TestCase):

    def test_valid_move(self):
        board = np.zeros((2, 2))
        board[0, 0] = 1
        self.assertFalse(logic_operations.is_valid_move(0, 0, board))
        self.assertTrue(logic_operations.is_valid_move(1, 1, board))

    def test_col_row_to_xy(self):
        x, y = 160, 160
        self.assertTrue(logic_operations.col_row_to_xy(1, 1, 9), (x, y))

