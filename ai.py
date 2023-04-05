from random import randrange

import numpy as np


class AI:

    @staticmethod
    def move(board):
        xs, ys = np.where(board == 0)
        zeroes = list(zip(xs, ys))
        index = randrange(0, len(zeroes))
        x, y = zeroes[index]
        return x, y
