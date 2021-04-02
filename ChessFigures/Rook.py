from constants import *
from ChessFigures.Figure import *


class Rook(Figure):
    def __str__(self):
        if self.color == WHITE:
            return 'wR'
        return 'bR'

    def can_move(self, row, col):
        return True